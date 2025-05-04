0. 틀린 이유

정규표현식에서 특수문자를 제외할 때, 숫자와 알파벳을 포함시키지 않아 회문 여부를 제대로 판별하지 못함.

1. 질문

특수문자를 제외하고 회문을 판별하려 했는데 숫자가 들어간 문자열에서 틀린 결과가 나옵니다. 왜 그런가요?

2. 잘못된 코드

```python
import re

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

palindrome_results = []

for line in lines:
    cleaned_line = re.sub(r'[!@#$%^&*]', '', line).lower()
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