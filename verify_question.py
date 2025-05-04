import openai
from dotenv import load_dotenv  # .env 파일에서 환경 변수 로드하기 위한 모듈
import os
from tqdm import tqdm  # 진행 상황을 표시하기 위한 진행 막대 모듈

# .env 파일에서 환경 변수 로드
load_dotenv()
# OpenAI API 키 환경 변수에서 가져오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

# question_format.md 파일을 읽어서 변수에 저장
with open("questions/question_format.md", "r", encoding="utf-8") as f:
    question_format = f.read()

def verify_and_revise(problem_md, question_md):
    """
    문제와 학생 질문 마크다운을 검증하고 필요시 수정하는 함수
    
    Args:
        problem_md: 문제 마크다운 텍스트
        question_md: 학생 질문 마크다운 텍스트
    
    Returns:
        수정된 마크다운 또는 원본 마크다운(수정이 필요없을 경우)
    """
    # GPT-4o에 전달할 프롬프트 구성
    prompt = f"""
아래는 파이썬 파일 입출력 문제와 이에 대한 학생 질문 마크다운 예시야.

문제 마크다운:
{problem_md}

학생 질문 마크다운:
{question_md}

질문-마크다운-형식:
{question_format}

검증 기준:
1. 먼저 문제의 1~4번 항목(과제 문제, 문제 설명, 입력 형식, 출력 형식)을 면밀히 분석하고 이해해야 함

2. "0. 틀린 이유" 항목이 정말 문제에서 요구하는 내용에 대해 틀린 이유인지 확인:
   - "0. 틀린 이유"가 문제 내용과 불일치하거나 부정확한 경우 수정
   - 학생의 코드가 제시된 문제 요구사항에 비추어 실제로 "0. 틀린 이유"에 명시된 이유로 틀렸는지 확인
   
3. "0. 틀린 이유"와 "1. 질문"에 제시된 내용이 "2. 잘못된 코드", "3. 에러 메시지", "4. 테스트 케이스에 대해 학생의 코드가 출력한 오답" 항목과 일관성이 있는지 검증:
   - "2. 잘못된 코드"가 실제로 "0. 틀린 이유"에 설명된 방식대로 틀렸는지
   - "3. 에러 메시지"가 "2. 잘못된 코드"에서 발생할 수 있는 실제 에러와 일치하는지
   - "4. 테스트 케이스에 대해 학생의 코드가 출력한 오답"이 "2. 잘못된 코드"를 실행했을 때 나올 수 있는 실제 결과와 일치하는지

4. 문제가 발견되면 다음과 같이 수정:
   - 문제 내용에 맞게 "0. 틀린 이유" 수정 (틀린 이유가 문제 요구사항에 비추어 부정확한 경우)
   - 수정된 "0. 틀린 이유"와 "1. 질문"에 맞게 "2~4" 항목도 일관성 있게 수정
   - 모든 수정은 문제에서 제시한 요구사항과 일치해야 함

수정이 필요 없다면 기존 마크다운을 그대로 반환하되, 수정이 필요하면 전체 마크다운을 다시 작성해 반환해. 
반드시 마크다운 전체만 반환하고, 추가 설명은 절대 하지 마. 
절대 ```markdown 이런 형식으로 마크다운을 감싸지 말고, 그냥 마크다운만 반환해. 질문-마크다운-형식에 맞춰서만 대답해.
절대 다른 말을 하지 말고, 반드시 위 질문 마크다운 형식에 맞춰서만 대답해.
'0. 틀린 이유'로 대답을 시작해.
"""
    # OpenAI API를 사용하여 GPT-4o 모델에 요청
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "너는 파이썬 문제와 학생 질문을 비교 분석하여, 학생 코드의 틀린 이유가 문제 내용에 적합한지, 그리고 제시된 코드/에러/오답이 틀린 이유와 일관성 있는지 검증하고 필요시 수정하는 AI야."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0,  # 일관된 결과를 위해 temperature 0 설정
        max_tokens=1000  # 응답 길이 제한
    )
    # API 응답에서 내용만 추출하여 반환
    return response.choices[0].message.content.strip()

# 1~8번 문제 각각에 대해 처리
for problem_idx in range(2, 9):
    # 문제 파일 경로 설정
    problem_md_path = f"problems/problem_{problem_idx}.md"
    # 질문 디렉토리 경로 설정
    questions_dir = f"questions/problem_{problem_idx}"
    
    # 문제 파일 읽기
    with open(problem_md_path, "r", encoding="utf-8") as f:
        problem_md = f.read()

    # 해당 문제에 대한 총 20개 질문 각각 처리
    for i in tqdm(range(1, 21), desc=f"problem_{problem_idx} 질문 검증중"):
        # 원본 질문 파일 경로
        question_path = f"{questions_dir}/question_{i}.md"
        # 수정된 질문을 저장할 파일 경로
        revised_path = f"{questions_dir}/question_{i}_revised.md"
        
        # 파일이 존재하지 않으면 건너뛰기
        if not os.path.exists(question_path):
            continue
        
        # 질문 파일 읽기
        with open(question_path, "r", encoding="utf-8") as f:
            question_md = f.read()

        # 질문 검증 및 필요시 수정
        revised_md = verify_and_revise(problem_md, question_md)

        # 기존 파일과 다르면(수정된 경우) 수정본 저장
        if revised_md.strip() != question_md.strip():
            with open(revised_path, "w", encoding="utf-8") as f:
                f.write(revised_md)