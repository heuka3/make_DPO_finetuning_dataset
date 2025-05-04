0. 틀린 이유

파일을 읽을 때 줄바꿈 문자를 고려하지 않아 각 줄 끝의 줄바꿈 문자가 그대로 남아 있어 회문 여부를 잘못 판별함.

1. 질문

파일의 각 줄에서 회문 여부를 판별하려고 하는데, 예상과 다른 결과가 나옵니다. 줄바꿈 문자가 영향을 주는 걸까요?

2. 잘못된 코드

```python
import re

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

palindrome_results = []

for line in lines:
    cleaned_line = re.sub(r'[^a-zA-Z0-9]', '', line.lower())
    is_palindrome = cleaned_line.strip() == cleaned_line.strip()[::-1]
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