0. 틀린 이유

학생의 코드는 키워드를 추출할 때 `split(' ')`을 사용하여 공백이 여러 개일 경우를 제대로 처리하지 못하고 있습니다. `split()`을 사용하면 공백이 여러 개여도 자동으로 처리됩니다. 또한, 텍스트 줄에서 키워드를 찾을 때 `split(' ')`을 사용하여 단어 단위로 비교하고 있어, 키워드가 단어의 일부로 포함된 경우를 놓치고 있습니다.

1. 질문

키워드를 추출할 때, 왜 제 코드가 제대로 작동하지 않나요? 공백이 여러 개 있는 경우를 처리하지 못하는 것 같습니다.

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()
    keywords = set(lines[0].strip().lower().split(' '))
    text_lines = lines[1:]

matched_lines = set()

for line in text_lines:
    lower_line = line.strip().lower()
    if any(keyword in lower_line.split(' ') for keyword in keywords):
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