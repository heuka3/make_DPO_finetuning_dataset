0. 틀린 이유

파일의 모든 줄을 읽어야 하는데, 한 줄만 읽고 종료했기 때문에 모든 줄을 처리하지 못함.

1. 질문

파일의 모든 줄을 처리하고 싶은데, 한 줄만 결과가 나옵니다. 모든 줄을 어떻게 처리할 수 있나요?

2. 잘못된 코드

```python
import re

with open('input.txt', 'r') as infile:
    line = infile.readline()  # 한 줄만 읽음

cleaned_line = re.sub(r'[^a-zA-Z0-9]', '', line).lower()
is_palindrome = cleaned_line == cleaned_line[::-1]

with open('output.txt', 'w') as outfile:
    outfile.write(f"{is_palindrome}\n")
```

3. 에러 메시지

```
(에러 없음)
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
True
```

- 테스트 케이스 2

```
True
```

- 테스트 케이스 3

```
False
```