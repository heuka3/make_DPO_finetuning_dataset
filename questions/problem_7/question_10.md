0. 틀린 이유

학생의 코드는 키워드를 추출할 때 `replace(' ', '')`를 사용하여 모든 공백을 제거하고 있어, 키워드가 제대로 분리되지 않고 하나의 긴 문자열로 인식됩니다. 이로 인해 키워드를 제대로 인식하지 못하고, 결과적으로 아무 줄도 출력되지 않습니다.

1. 질문

왜 제 코드가 키워드를 제대로 인식하지 못하나요? 공백이나 다른 문자를 처리하는 데 문제가 있는 것 같습니다.

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()
    keywords = set(lines[0].strip().lower().replace(' ', '').split())
    text_lines = lines[1:]

matched_lines = set()

for line in text_lines:
    lower_line = line.strip().lower().replace(' ', '')
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