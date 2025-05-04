0. 틀린 이유

파일을 다 읽지 않고 한 줄만 읽고, 그 줄에 대해서만 처리해서 전체 결과가 잘못 나옴.

1. 질문

파일에서 한 줄만 읽어서 처리했는데 결과가 이상합니다. 모든 줄에 대해 확인하려면 어떻게 해야 하나요?

2. 잘못된 코드

```python
import re

with open('input.txt', 'r') as infile:
    line = infile.readline()  # 파일에서 한 줄만 읽음

palindrome_results = []

cleaned_line = re.sub(r'[^a-zA-Z0-9]', '', line).lower()
is_palindrome = cleaned_line == cleaned_line[::-1]
palindrome_results.append(is_palindrome)

with open('output.txt', 'w') as outfile:
    outfile.write(f"{palindrome_results[0]}\n")
```

3. 에러 메시지

```
(에러 없음)
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
True
```

- 테스트 케이스 2

```
True
```

- 테스트 케이스 3

```
False
```