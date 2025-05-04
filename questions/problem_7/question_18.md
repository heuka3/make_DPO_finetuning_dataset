0. 틀린 이유

학생의 코드에서 `break` 문이 잘못 사용되어 첫 번째 줄만 검사하고 루프가 종료되는 문제가 있습니다. 이로 인해 모든 텍스트 줄을 검사하지 않고 첫 번째 줄만 검사하게 됩니다.

1. 질문

제 코드가 왜 일부 줄을 전혀 검사하지 않나요? 첫 번째 줄만 검사한 뒤에 다음 줄로 넘어가는 것 같습니다.

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()
    keywords = set(lines[0].strip().lower().split())
    text_lines = lines[1:]

matched_lines = set()

for i in range(len(text_lines)):
    lower_line = text_lines[i].strip().lower()
    if any(keyword in lower_line for keyword in keywords):
        matched_lines.add(text_lines[i].strip())
    break

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
I love to code in Python.
```