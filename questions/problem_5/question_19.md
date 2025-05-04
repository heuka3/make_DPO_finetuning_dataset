0. 틀린 이유

정규표현식을 사용하는 과정에서 특수문자만 제외하고 알파벳과 숫자는 남겨야 하는데, 특수문자만 제외하는 정규표현식이 잘못 작성되어 알파벳과 숫자도 제거되지 않음.

1. 질문

특수문자를 제외하려고 했는데, 숫자와 알파벳도 모두 제거된 것 같습니다. 올바르게 특수문자만 제거하려면 어떻게 해야 하나요?

2. 잘못된 코드

```python
import re

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

palindrome_results = []

for line in lines:
    cleaned_line = re.sub(r'[!@#$%^&*]', '', line).lower()  # 숫자와 알파벳을 포함하지 않음
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