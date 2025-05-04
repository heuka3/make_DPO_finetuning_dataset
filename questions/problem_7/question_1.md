0. 틀린 이유

대소문자를 구분하지 않아야 하는데, 대소문자를 구분하는 비교를 함

1. 질문

왜 제 코드가 일부 테스트 케이스에서 제대로 작동하지 않나요? 대소문자와 관련이 있는 것 같습니다.

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()
    keywords = set(lines[0].strip().split())
    text_lines = lines[1:]

matched_lines = set()

for line in text_lines:
    if any(keyword in line for keyword in keywords):
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
```

- 테스트 케이스 2

```
The quick brown fox jumps over the lazy dog.
```

- 테스트 케이스 3

```

```