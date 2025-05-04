0. 틀린 이유

정규표현식에서 공백을 남겨두어, 공백이 포함된 경우 회문을 잘못 판별함.

1. 질문

특수문자를 제외했지만 공백을 남겨두었습니다. 공백이 있을 때마다 결과가 틀리는데, 어떻게 해야 하나요?

2. 잘못된 코드

```python
import re

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

palindrome_results = []

for line in lines:
    cleaned_line = re.sub(r'[^a-zA-Z0-9 ]', '', line).lower()  # 공백을 남겨둠
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