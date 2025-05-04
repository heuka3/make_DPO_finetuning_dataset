0. 틀린 이유

학생의 코드는 키워드가 텍스트 줄의 첫 번째 단어로만 위치해야 한다고 잘못 가정하여, 키워드가 줄의 다른 위치에 있을 경우 이를 인식하지 못함.

1. 질문

왜 제 코드가 일부 키워드가 포함된 줄을 놓치나요? 키워드가 줄의 첫 번째 단어로만 있을 때만 인식하는 것 같습니다.

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()
    keywords = set(lines[0].strip().lower().split())
    text_lines = lines[1:]

matched_lines = set()

for line in text_lines:
    lower_line = line.strip().lower()
    words = lower_line.split()
    if words[0] in keywords:
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

```

- 테스트 케이스 2

```
The quick brown fox jumps over the lazy dog.
```

- 테스트 케이스 3

```

```