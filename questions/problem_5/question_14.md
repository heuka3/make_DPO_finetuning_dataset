0. 틀린 이유

파일을 열 때, 'r+' 모드를 사용하여 파일이 없으면 에러가 발생함.

1. 질문

input.txt 파일을 읽으려고 하는데, 파일이 없을 경우 에러가 발생합니다. 파일이 없을 때 어떻게 해야 하나요?

2. 잘못된 코드

```python
import re

with open('input.txt', 'r+') as infile:  # 'r+' 모드 사용
    lines = infile.readlines()

palindrome_results = []

for line in lines:
    cleaned_line = re.sub(r'[^a-zA-Z0-9]', '', line.lower())
    is_palindrome = cleaned_line == cleaned_line[::-1]
    palindrome_results.append(is_palindrome)

with open('output.txt', 'w') as outfile:
    for result in palindrome_results:
        outfile.write(f"{result}\n")
```

3. 에러 메시지

```
FileNotFoundError: [Errno 2] No such file or directory: 'input.txt'
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
(파일 없음)
```

- 테스트 케이스 2

```
(파일 없음)
```

- 테스트 케이스 3

```
(파일 없음)
```