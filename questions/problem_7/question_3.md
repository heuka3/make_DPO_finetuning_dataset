0. 틀린 이유

파일을 열고 데이터를 읽어오는 과정에서 잘못된 파일 이름을 사용함

1. 질문

제 코드가 실행되지 않고 오류가 발생합니다. 파일 이름과 관련이 있는 것 같은데, 어떻게 해결할 수 있을까요?

2. 잘못된 코드

```python
with open('input_file.txt', 'r') as infile:
    lines = infile.readlines()
    keywords = set(lines[0].strip().lower().split())
    text_lines = lines[1:]

matched_lines = set()

for line in text_lines:
    lower_line = line.strip().lower()
    if any(keyword in lower_line for keyword in keywords):
        matched_lines.add(line.strip())

with open('output_file.txt', 'w') as outfile:
    for matched_line in matched_lines:
        outfile.write(matched_line + '\n')
```

3. 에러 메시지

```
FileNotFoundError: [Errno 2] No such file or directory: 'input_file.txt'
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