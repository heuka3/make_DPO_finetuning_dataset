import openai
from dotenv import load_dotenv
import os

load_dotenv()
# 환경변수에서 OpenAI API 키 가져오기
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI API 키 설정 (환경변수 또는 직접 입력)
openai.api_key = OPENAI_API_KEY  # 환경변수에서 가져옴

# problem_1.md 파일에서 문제 형식 추출
with open("problems/problem_1.md", "r", encoding="utf-8") as f:
    problem_1_format = f.read()
# problem_2.md 파일에서 문제 형식 추출
with open("problems/problem_2.md", "r", encoding="utf-8") as f:
    problem_2_format = f.read()
# problem_3.md 파일에서 문제 형식 추출
with open("problems/problem_3.md", "r", encoding="utf-8") as f:
    problem_3_format = f.read()
# problem_4.md 파일에서 문제 형식 추출
with open("problems/problem_4.md", "r", encoding="utf-8") as f:
    problem_4_format = f.read()
# problem_5.md 파일에서 문제 형식 추출
with open("problems/problem_5.md", "r", encoding="utf-8") as f:
    problem_5_format = f.read()
# problem_6.md 파일에서 문제 형식 추출
with open("problems/problem_6.md", "r", encoding="utf-8") as f:
    problem_6_format = f.read()


# 프롬프트 생성: 기존 문제보다 약간 더 어려운 파일 입출력 문제 생성 요청
prompt = f"""

아래의 마크다운 문제 예시 형식의 내용이 아닌 형식만 맞춰서, 파이썬 파일 입출력에 관한,
입력 파일에 임의의 파이썬 코드(여러 개의 함수를 포함한)가 주어지고 해당 코드에서 전역 변수와 각 함수 내부에서 사용하는 변수를 구분하여 출력하는 문제를 만들어야 해.
새 문제는 기존 문제보다 더 어려워야 하며, 문제의 난이도는 중급 수준이어야 해. 
문제, 입력/출력 형식, 테스트 케이스, 그리고 파이썬 코드 정답까지 모두 포함해줘. 
문제는 반드시 영어 단어가 아닌 숫자, 특수문자, 또는 줄바꿈 등 추가적인 조건이 포함되어야 해.

예시 형식:
{problem_1_format}

{problem_2_format}

{problem_3_format}

{problem_4_format}

{problem_5_format}

{problem_6_format}

주의 사항: 
절대 다른 말을 뱉지 말고 위 형식에 맞춰서만 대답해줘.
예시로 주어진 파일의 내용을 절대 참고하지 말고 형식만 맞춰서 대답해.
새 문제는 기존의 문제와 절대 같아서는 안 돼.
"""

# OpenAI API 호출
response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "너는 파이썬 파일 입출력 문제를 만드는 AI야."},
        {"role": "user", "content": prompt}
    ],
    temperature=0.7,
    max_tokens=1200
)

# 응답에서 마크다운 문제 추출
problem_8_md = response.choices[0].message.content

# problem_2.md 파일로 저장
with open("problems/problem_8.md", "w", encoding="utf-8") as f:
    f.write(problem_8_md)