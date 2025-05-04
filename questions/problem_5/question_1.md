0. 틀린 이유

문자열을 소문자로 변환하지 않아서 대소문자 차이로 인해 회문 여부를 잘못 판별함.

1. 질문

문자열에서 특수문자를 제거하고 회문인지 확인했는데, 답이 계속 틀립니다. 어디서 문제인 걸까요?

2. 잘못된 코드

```python
import re

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

palindrome_results = []

for line in lines:
    cleaned_line = re.sub(r'[^a-zA-Z0-9]', '', line)
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
False
False
False
```

- 테스트 케이스 2

```
False
False
False
```

- 테스트 케이스 3

```
False
False
```