0. 틀린 이유

키워드 추출 시 strip()을 사용하지 않아 키워드 앞뒤에 공백이 남아있어서 매칭에 실패함

1. 질문

제 코드가 키워드를 찾지 못하는 이유가 뭔가요? 공백과 관련이 있을 것 같은데, 어떻게 해결해야 하나요?

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()
    keywords = set(lines[0].lower().split())
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