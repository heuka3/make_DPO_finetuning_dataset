0. 틀린 이유

정규표현식에서 특수문자를 제외하면서 숫자를 포함시키지 않아 숫자가 포함된 회문 문자열을 잘못 판별함.

1. 질문

문자열에 숫자가 포함되어 있을 때도 회문으로 판별해야 하는데, 숫자가 포함되어 있으면 항상 틀린 결과가 나옵니다. 뭐가 문제인가요?

2. 잘못된 코드

```python
import re

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

palindrome_results = []

for line in lines:
    cleaned_line = re.sub(r'[^a-zA-Z]', '', line).lower()  # 숫자를 포함하지 않음
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