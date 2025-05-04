0. 틀린 이유

특수문자를 제외하려고 했으나, 정규표현식에서 잘못된 패턴을 사용하여 알파벳과 숫자만 남겨야 하는데, 오히려 알파벳과 숫자만 제거하고 특수문자만 남김.

1. 질문

특수문자를 제외하려고 했지만 알파벳과 숫자도 제거된 것 같습니다. 이럴 때 어떻게 수정해야 하나요?

2. 잘못된 코드

```python
import re

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

palindrome_results = []

for line in lines:
    cleaned_line = re.sub(r'[a-zA-Z0-9]', '', line).lower()  # 잘못된 패턴
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
True
True
True
```

- 테스트 케이스 2

```
True
True
True
```

- 테스트 케이스 3

```
True
True
```