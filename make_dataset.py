import openai
import os
from dotenv import load_dotenv
from tqdm import tqdm
import json

# .env 파일에서 환경 변수 로드
load_dotenv()
# OpenAI API 키 환경 변수에서 가져오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def generate_incorrect_answer(problem_md, question_md):
    """
    의도적으로 잘못된 답변을 생성하는 함수
    
    Args:
        problem_md: 문제 마크다운 텍스트
        question_md: 학생 질문 마크다운 텍스트
    
    Returns:
        잘못된 답변 텍스트
    """
    # 엉뚱한 답변을 위한 프롬프트 구성
    prompt = f"""
아래는 파이썬 문제와 이에 대한 학생 질문이야.

문제:
{problem_md}

학생 질문:
{question_md}

위 질문에 대해 의도적으로 잘못된 답변을 생성해야 해. 
학생 질문에 있는 "0. 틀린 이유"에 있는 이유가 아닌 다른 이유로 코드가 틀렸다고 설명해야 함. 

반드시 자신있는 어조로 틀린 설명을 해야 하며, 코드의 특정 부분을 지적하되 실제 문제와 관련 없는 부분을 지적해야 함.
문제가 요구하는 것과 관련 없는 부분을 중요하다고 강조하면서 잘못된 방향으로 안내해.
"""
    
    # OpenAI API를 사용하여 GPT-4o 모델에 요청
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "너는 학생들의 코딩 질문에 의도적으로 잘못된 설명을 제공하는 AI야."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,  # 다양한 답변을 위해 temperature 높게 설정
        max_tokens=1000
    )
    
    # API 응답에서 내용만 추출하여 반환
    return response.choices[0].message.content.strip()

def generate_correct_answer(problem_md, question_md, incorrect_answer):
    """
    올바른 답변을 생성하는 함수
    
    Args:
        problem_md: 문제 마크다운 텍스트
        question_md: 학생 질문 마크다운 텍스트
        incorrect_answer: 이전에 생성된 잘못된 답변
    
    Returns:
        올바른 답변 텍스트
    """
    # 올바른 답변을 위한 프롬프트 구성
    prompt = f"""
아래는 파이썬 문제와 이에 대한 학생 질문, 그리고 이전에 제공된 잘못된 답변이야.
학생 질문의 "0. 틀린 이유"를 정확히 이해하고, 문제의 요구사항에 맞게 올바른 답변을 작성해야 해.

문제:
{problem_md}

학생 질문:
{question_md}

이전에 제공된 잘못된 답변:
{incorrect_answer}

사용자 요청: 이전의 설명이 틀렸어. 제대로 설명해줘
"""
    
    # OpenAI API를 사용하여 GPT-4o 모델에 요청
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "너는 학생들의 코딩 질문에 정확하고 도움이 되는 설명을 제공하는 AI야."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,  # 정확한 답변을 위해 temperature 낮게 설정
        max_tokens=1000
    )
    
    # API 응답에서 내용만 추출하여 반환
    return response.choices[0].message.content.strip()

def save_answer_pair(incorrect_answer, correct_answer, output_path):
    """
    잘못된 답변과 올바른 답변 쌍을 파일로 저장하는 함수
    
    Args:
        incorrect_answer: 잘못된 답변 텍스트
        correct_answer: 올바른 답변 텍스트
        output_path: 저장할 파일 경로
    """
    # 디렉토리가 없으면 생성
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    # 답변 형식 구성
    content = f"""1. reject

{incorrect_answer}

2. chosen

{correct_answer}
"""
    
    # 파일에 저장
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Saved answer pair to {output_path}")

def main():
    # 처리할 문제 범위
    for problem_idx in range(2, 9):  # 1~8번 문제
        # 문제 파일 경로 설정
        problem_md_path = f"problems/problem_{problem_idx}.md"
        
        # 문제 파일이 존재하지 않으면 건너뛰기
        if not os.path.exists(problem_md_path):
            continue
        
        # 문제 파일 읽기
        with open(problem_md_path, "r", encoding="utf-8") as f:
            problem_md = f.read()
        
        # 질문 디렉토리 경로 설정
        questions_dir = f"questions/problem_{problem_idx}"
        # 출력 디렉토리 경로 설정
        output_dir = f"dataset/problem_{problem_idx}"
        
        # 디렉토리가 없으면 생성
        os.makedirs(output_dir, exist_ok=True)
        
        # 각 질문 파일에 대해 처리
        for i in tqdm(range(1, 21), desc=f"Processing problem_{problem_idx} questions"):  # 각 문제당 최대 20개 질문
            # 질문 파일 경로
            question_path = f"{questions_dir}/question_{i}.md"
            # 출력 파일 경로
            output_path = f"{output_dir}/answer_{i}.md"
            
            # 질문 파일이 존재하지 않으면 건너뛰기
            if not os.path.exists(question_path):
                continue
            
            # 질문 파일 읽기
            with open(question_path, "r", encoding="utf-8") as f:
                question_md = f.read()
            
            # 잘못된 답변 생성
            incorrect_answer = generate_incorrect_answer(problem_md, question_md)
            
            # 올바른 답변 생성
            correct_answer = generate_correct_answer(problem_md, question_md, incorrect_answer)
            
            # 답변 쌍 저장
            save_answer_pair(incorrect_answer, correct_answer, output_path)

if __name__ == "__main__":
    main()

