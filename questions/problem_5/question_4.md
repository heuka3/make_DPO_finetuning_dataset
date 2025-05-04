0. 틀린 이유

파일 경로를 잘못 지정하여 input.txt 파일을 찾지 못하고, output.txt 파일을 잘못된 경로에 생성하려고 시도함.

1. 질문

코드를 실행했는데 파일이 생성되지 않거나 읽히지 않습니다. 파일 경로가 맞는지 확인해야 하나요?

2. 잘못된 코드

```python
import re

with open('non_existent_input.txt', 'r') as infile:
    lines = infile.readlines()

palindrome_results = []

for line in lines:
    cleaned_line = re.sub(r'[^a-zA-Z0-9]', '', line).lower()
    is_palindrome = cleaned_line == cleaned_line[::-1]
    palindrome_results.append(is_palindrome)

with open('/wrong_path/output.txt', 'w') as outfile:
    for result in palindrome_results:
        outfile.write(f"{result}\n")
```

3. 에러 메시지

```
FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_input.txt'
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