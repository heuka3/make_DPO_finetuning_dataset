import openai
from dotenv import load_dotenv
import os
from tqdm import tqdm
import logging

logging.basicConfig(level=logging.INFO)

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

with open("questions/question_format.md", "r", encoding="utf-8") as f:
    question_format = f.read()

# 문제 파일 반복 (problem_1.md ~ problem_8.md)
for problem_idx in range(1, 9):
    problem_md_path = f"problems/problem_{problem_idx}.md"
    questions_dir = f"questions/problem_{problem_idx}"
    os.makedirs(questions_dir, exist_ok=True)

    # 문제 파일 읽기
    with open(problem_md_path, "r", encoding="utf-8") as f:
        problem_md = f.read()

    existing_questions = []
    for j in range(1, 21):
        question_path = f"{questions_dir}/question_{j}.md"
        if os.path.exists(question_path):
            with open(question_path, "r", encoding="utf-8") as f:
                existing_questions.append(f.read())

    for i in tqdm(range(1, 21), desc=f"problem_{problem_idx} 질문 생성중"):
        question_path = f"{questions_dir}/question_{i}.md"
        # 파일이 비어있거나 존재해도 무조건 새로 작성
        prompt = f"""
아래는 파이썬 파일 입출력 문제와 질문 마크다운 형식 예시야.

문제:
{problem_md}

질문-마크다운-형식:
{question_format}

이미 만들어진 질문들:
{''.join(existing_questions)}

조금 멍청한 학생들이 위 문제를 푼다면 어떤 이유로 에러가 나서 어떤 질문을 던질 수 있을까? 
문제의 문제 설명을 자세히 읽고,
멍청한 학생들이 겪게 될 디버깅 에러나 휴먼 에러에 뭐가 있을지 틀리는 이유를 생각해서

- 그에 해당하는 멍청하게 짠 코드
- 그 코드에서 발생하는 에러
- 각 테스트 케이스에 대해 잘못 출력한 사례
- 이에 대해 뭐가 문제인지 물어보는 학생의 질문

이 4가지를 구분해서 생각하고 위 질문-마크다운-형식에 맞춰서 새로운 질문을 만들어줘.
반드시 이미 만들어진 질문들과 겹치지 않는 새로운 유형의 질문이어야 해.
질문은 실제 학생이 실수할 만한 다양한 유형으로 20개 만들어야 해.
지금은 {i}번째 질문을 만들어줘. 이미 만들어진 질문들을 참고해서 이미 만들어진 질문과 겹치지 않도록 해.
절대 다른 말을 하지 말고, 반드시 위 질문 마크다운 형식에 맞춰서만 대답해. 
절대 추가 설명을 넣지마. 
"""

        try:
            response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "너는 파이썬 파일 입출력 문제에 대한 학생 질문을 만드는 AI야."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=700
            )

            if not response.choices:
                logging.warning(f"problem_{problem_idx} - {i}번째 질문 생성 실패: 응답이 비어 있음.")
                continue

            question_md = response.choices[0].message.content.strip()

            with open(question_path, "w", encoding="utf-8") as f:
                f.write(question_md)

            existing_questions.append(question_md)

        except Exception as e:
            logging.error(f"problem_{problem_idx} - {i}번째 질문 생성 중 에러 발생: {e}")