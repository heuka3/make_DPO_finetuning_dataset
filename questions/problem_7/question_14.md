0. 틀린 이유

학생의 코드는 키워드를 분리할 때 `split(' ')`을 사용하여, 키워드 리스트에 빈 문자열이 포함될 수 있습니다. 이는 모든 줄이 매칭되는 원인이 됩니다. `split()`을 사용하여 공백을 자동으로 처리하도록 수정해야 합니다.

1. 질문

왜 모든 줄이 키워드와 매칭되고 있나요? 키워드에 빈 문자열이 포함된 것 같은데, 어떻게 수정해야 하나요?

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()
    keywords = set(lines[0].lower().split(' '))
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