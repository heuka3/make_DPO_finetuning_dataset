0. 틀린 이유

출력할 때 줄바꿈을 추가하지 않아 모든 결과가 한 줄로 연속해서 기록됨.

1. 질문

output.txt 파일에 회문 여부가 한 줄에 모두 나옵니다. 어떻게 하면 각 결과를 줄바꿈해서 출력할 수 있을까요?

2. 잘못된 코드

```python
import re

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

palindrome_results = []

for line in lines:
    cleaned_line = re.sub(r'[^a-zA-Z0-9]', '', line).lower()
    is_palindrome = cleaned_line == cleaned_line[::-1]
    palindrome_results.append(is_palindrome)

with open('output.txt', 'w') as outfile:
    for result in palindrome_results:
        outfile.write(f"{result}")
```

3. 에러 메시지

```
(에러 없음)
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
TrueTrueFalse
```

- 테스트 케이스 2

```
TrueTrueTrue
```

- 테스트 케이스 3

```
FalseFalse
```