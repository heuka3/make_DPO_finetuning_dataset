0. 틀린 이유

학생의 코드는 줄의 끝에 있는 키워드를 인식하지 못하는 것이 아니라, `words[:-1]`로 인해 마지막 단어를 검사하지 않아서 문제가 발생합니다. 따라서 줄 끝에 있는 키워드가 포함된 줄이 누락됩니다.

1. 질문

왜 제 코드가 줄의 끝에 있는 키워드를 인식하지 못하나요? 줄 끝에 키워드가 있을 때 누락되는 것 같습니다.

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()
    keywords = set(lines[0].strip().lower().split())
    text_lines = lines[1:]

matched_lines = set()

for line in text_lines:
    lower_line = line.lower()
    words = lower_line.split()
    if any(keyword in words[:-1] for keyword in keywords):
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
Bananas are great!
I love orange juice.
```

- 테스트 케이스 2

```
The quick brown fox jumps over the lazy dog.
Cats are independent animals.
```

- 테스트 케이스 3

```
I love to code in Python.
Machine learning is a subset of AI.
```