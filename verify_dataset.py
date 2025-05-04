import openai
import os
from dotenv import load_dotenv
from tqdm import tqdm

# .env 파일에서 환경 변수 로드
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

def parse_answer_file(answer_path):
    """answer_n.md 파일에서 reject, chosen 항목 분리"""
    with open(answer_path, "r", encoding="utf-8") as f:
        content = f.read()
    reject = ""
    chosen = ""
    mode = None
    for line in content.splitlines():
        if line.strip().startswith("1. reject"):
            mode = "reject"
            continue
        elif line.strip().startswith("2. chosen"):
            mode = "chosen"
            continue
        if mode == "reject":
            reject += line + "\n"
        elif mode == "chosen":
            chosen += line + "\n"
    return reject.strip(), chosen.strip()

def generate_incorrect_answer(problem_md, question_md):
    """make_dataset.py 방식의 엉뚱한 답변 생성"""
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
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "너는 학생들의 코딩 질문에 의도적으로 잘못된 설명을 제공하는 AI야."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=1000
    )
    return response.choices[0].message.content.strip()

def generate_correct_answer(problem_md, question_md, incorrect_answer):
    """make_dataset.py 방식의 올바른 답변 생성"""
    prompt = f"""
아래는 파이썬 문제와 이에 대한 학생 질문, 그리고 이전에 제공된 잘못된 답변이야.
학생 질문의 "0. 틀린 이유"를 정확히 이해하고, 문제의 요구사항에 맞게 올바른 답변을 작성해야 해.
더불어, 문제의 "6. 파이썬 코드 정답"을 바탕으로 작성해야 해.
문제에서 주어진 코드가 아닌 다른 방식으로 설명하지 마!!

문제:
{problem_md}

학생 질문:
{question_md}

이전에 제공된 잘못된 답변:
{incorrect_answer}

사용자 요청: 이전의 설명이 틀렸어. 제대로 설명해줘
"""
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "너는 학생들의 코딩 질문에 정확하고 도움이 되는 설명을 제공하는 AI야."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=1000
    )
    return response.choices[0].message.content.strip()

def verify_answers(problem_md, question_md, reject, chosen):
    """
    reject/chosen 답변이 올바른지 검증.
    """
    prompt = f"""
아래는 파이썬 문제, 학생 질문, 그리고 두 개의 답변(1. reject, 2. chosen)이야.

문제:
{problem_md}

학생 질문:
{question_md}

1. reject:
{reject}

2. chosen:
{chosen}

검증 기준:
- 1. reject는 학생 질문의 "0. 틀린 이유"와 다르게, 문제의 요구사항과 관련 없는 엉뚱한 이유로 설명해야 해. 실제 문제의 핵심 원인과는 다른 부분을 강조해야 함.
- 2. chosen은 문제의 요구사항과 학생 질문의 "0. 틀린 이유"를 정확히 이해하고, 실제로 코드가 왜 틀렸는지 올바른 이유로 설명해야 해.
- !!chosen은 문제에서 주어진 "6. 파이썬 코드 정답"을 바탕으로 작성하여야 해. 문제에서 주어진 코드가 아닌 다른 방식으로 설명하지 마!!
- 두 답변 모두 문제와 질문의 맥락에 맞게 작성되어야 하며, 각각의 역할에 충실해야 함.

검증 결과:
- 두 답변이 위 기준에 맞게 잘 작성되어 있다면 "PASS"만 출력해.
- 만약 둘 중 하나라도 기준에 맞지 않으면 "FAIL"만 출력해.
- !!chosen의 내용이 "6. 파이썬 코드 정답"과 다르다면 "FAIL"로 간주해!!

반드시 "PASS" 또는 "FAIL"만 출력하고, 추가 설명은 하지 마.
"""
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "너는 DPO 데이터셋의 reject/chosen 쌍이 기준에 맞게 잘 작성됐는지 검증하는 AI야."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0,
        max_tokens=10
    )
    return response.choices[0].message.content.strip()

def save_answer_pair(incorrect_answer, correct_answer, output_path):
    """reject/chosen 쌍을 파일로 저장"""
    content = f"""1. reject

{incorrect_answer}

2. chosen

{correct_answer}
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

def main():
    for problem_idx in range(1, 9):
        problem_md_path = f"problems/problem_{problem_idx}.md"
        questions_dir = f"questions/problem_{problem_idx}"
        dataset_dir = f"dataset/problem_{problem_idx}"

        if not os.path.exists(problem_md_path):
            continue
        with open(problem_md_path, "r", encoding="utf-8") as f:
            problem_md = f.read()

        for i in tqdm(range(1, 21), desc=f"검증중: problem_{problem_idx}"):
            question_path = f"{questions_dir}/question_{i}.md"
            answer_path = f"{dataset_dir}/answer_{i}.md"
            revised_path = f"{dataset_dir}/answer_{i}_revised.md"

            if not (os.path.exists(question_path) and os.path.exists(answer_path)):
                continue

            with open(question_path, "r", encoding="utf-8") as f:
                question_md = f.read()
            reject, chosen = parse_answer_file(answer_path)

            # 검증
            result = verify_answers(problem_md, question_md, reject, chosen)

            if result.strip() == "PASS":
                # "PASS"인 경우 수정할 필요 없음
                print(f"PASS: {answer_path}")
                continue  # 문제 없으면 넘어감
            
            print(f"FAIL: {answer_path}")
            # FAIL이면 새로 생성
            incorrect_answer = generate_incorrect_answer(problem_md, question_md)
            correct_answer = generate_correct_answer(problem_md, question_md, incorrect_answer)
            save_answer_pair(incorrect_answer, correct_answer, revised_path)
            print(f"수정됨: {revised_path}")

if __name__ == "__main__":
    main()