0. 틀린 이유

결과를 파일에 기록할 때 개행문자를 포함하지 않아서 모든 결과가 한 줄에 기록되어 판별이 잘못됨.

1. 질문

output.txt에 결과가 한 줄로 나옵니다. 각 결과를 다른 줄에 출력하려면 어떻게 해야 하나요?

2. 잘못된 코드

```python
import re

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

palindrome_results = []

for line in lines:
    cleaned_line = re.sub(r'[^a-zA-Z0-9]', '', line.lower())
    is_palindrome = cleaned_line == cleaned_line[::-1]
    palindrome_results.append(is_palindrome)

with open('output.txt', 'w') as outfile:
    outfile.write(''.join(str(result) for result in palindrome_results))
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