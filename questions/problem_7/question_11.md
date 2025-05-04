0. 틀린 이유

학생의 코드는 키워드 리스트 전체를 텍스트 줄과 비교하고 있습니다. 이는 항상 False를 반환합니다. 각 키워드가 텍스트 줄에 포함되어 있는지를 개별적으로 확인해야 합니다.

1. 질문

왜 제 코드가 아무런 결과도 출력하지 않나요? 키워드와 텍스트 줄을 제대로 비교하고 있는지 모르겠습니다.

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()
    keywords = lines[0].strip().lower().split()
    text_lines = lines[1:]

matched_lines = set()

for line in text_lines:
    lower_line = line.strip().lower()
    if keywords in lower_line:
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
(출력되지 않음)
```

- 테스트 케이스 2

```
(출력되지 않음)
```

- 테스트 케이스 3

```
(출력되지 않음)
```