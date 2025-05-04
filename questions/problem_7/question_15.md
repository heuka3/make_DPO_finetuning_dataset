0. 틀린 이유

학생의 코드는 줄의 시작 부분에만 키워드가 있는지 확인하고 있어, 줄 중간이나 끝부분에 있는 키워드는 인식하지 못합니다. 이는 문제에서 요구하는 "키워드가 포함된 줄"을 찾는 방식과 다릅니다.

1. 질문

왜 제 코드가 키워드가 포함된 줄을 제대로 인식하지 못하나요? 키워드가 특정 위치에 있을 때만 인식되는 것 같습니다.

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()
    keywords = set(lines[0].strip().lower().split())
    text_lines = lines[1:]

matched_lines = set()

for line in text_lines:
    lower_line = line.strip().lower()
    for keyword in keywords:
        if lower_line.startswith(keyword):
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

```

- 테스트 케이스 3

```

```