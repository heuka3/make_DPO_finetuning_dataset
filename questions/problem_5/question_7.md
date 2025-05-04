0. 틀린 이유

파일을 쓸 때 기존 데이터를 덮어쓰기 않고 추가하려고 'a' 모드를 사용하여 잘못된 결과를 유지함.

1. 질문

output.txt 파일에 계속해서 이전 결과와 새로운 결과가 모두 저장됩니다. 이전 결과를 덮어쓰려면 어떻게 해야 하나요?

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

with open('output.txt', 'a') as outfile:  # 'a' 모드 사용
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
False
True
True
False
```

- 테스트 케이스 2

```
True
True
False
True
True
True
```

- 테스트 케이스 3

```
True
True
False
False
False
```