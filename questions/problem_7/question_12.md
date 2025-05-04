0. 틀린 이유

학생의 코드는 매 반복마다 키워드를 설정하고 있어, 모든 줄을 키워드로 간주하고 비교하게 됩니다. 따라서 첫 번째 줄을 제외한 모든 줄이 키워드로 간주되어 출력됩니다.

1. 질문

왜 제 코드는 키워드가 포함되지 않은 줄까지 모두 포함해서 출력하나요? 무언가 잘못 설정된 것 같은데 이게 맞나요?

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

matched_lines = set()

for line in lines:
    keywords = set(lines[0].strip().lower().split())
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