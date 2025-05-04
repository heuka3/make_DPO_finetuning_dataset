0. 틀린 이유

파일을 읽고 쓰기 전에 결과 리스트를 잘못 초기화하여 이전 실행 결과가 포함됨.

1. 질문

프로그램을 여러 번 실행했는데, 이전 실행 결과가 계속 남아 있는 것 같습니다. 왜 그런 걸까요?

2. 잘못된 코드

```python
import re

palindrome_results = ["Previous result"]  # 잘못된 초기화

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

for line in lines:
    cleaned_line = re.sub(r'[^a-zA-Z0-9]', '', line).lower()
    is_palindrome = cleaned_line == cleaned_line[::-1]
    palindrome_results.append(is_palindrome)

with open('output.txt', 'w') as outfile:
    for result in palindrome_results:
        outfile.write(f"{result}\n")
```

3. 에러 메시지

```
(에러 없음)
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
Previous result
True
True
False
```

- 테스트 케이스 2

```
Previous result
True
True
True
```

- 테스트 케이스 3

```
Previous result
False
False
```