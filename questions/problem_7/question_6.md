0. 틀린 이유

학생의 코드는 키워드가 다른 단어의 일부분으로 포함되어도 해당 줄을 출력하기 때문에 틀렸습니다. 문제에서는 키워드가 정확히 단어로 포함된 줄만 출력해야 합니다.

1. 질문

왜 제 코드가 키워드를 포함하지 않는 줄까지 출력하나요? 특정 키워드가 다른 단어의 일부분일 때도 포함되는 것 같습니다.

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
    for matched_line in matched_lines:
        outfile.write(matched_line + '\n')
```

3. 에러 메시지

```
(없음)
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
This is an apple.
Bananas are great!
I love orange juice.
A random line.
```

- 테스트 케이스 2

```
The quick brown fox jumps over the lazy dog.
Cats are independent animals.
Dogs are loyal.
The day is sunny.
```

- 테스트 케이스 3

```
I love to code in Python.
AI is the future.
Machine learning is a subset of AI.
This sentence does not belong.
```