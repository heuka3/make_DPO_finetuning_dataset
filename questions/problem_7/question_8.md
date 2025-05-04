0. 틀린 이유

writelines()는 리스트의 각 문자열을 파일에 쓸 때 자동으로 줄바꿈을 추가하지 않기 때문에, 각 줄 끝에 '\n'을 수동으로 추가해야 한다.

1. 질문

왜 output.txt에 모든 줄이 붙어서 출력되나요? writelines()를 사용했는데도 줄바꿈이 안 되는 이유가 뭘까요?

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()
    keywords = set(lines[0].strip().lower().split())
    text_lines = lines[1:]

matched_lines = set()

for line in text_lines:
    lower_line = line.strip().lower()
    if any(keyword in lower_line for keyword in keywords):
        matched_lines.add(line.strip())

with open('output.txt', 'w') as outfile:
    outfile.writelines(matched_lines)
```

3. 에러 메시지

```
(없음)
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
This is an apple.Bananas are great!I love orange juice.
```

- 테스트 케이스 2

```
The quick brown fox jumps over the lazy dog.Cats are independent animals.Dogs are loyal.
```

- 테스트 케이스 3

```
I love to code in Python.AI is the future.Machine learning is a subset of AI.
```