0. 틀린 이유

파일을 한 번에 다 읽고 처리를 해야 하는 것은 아님. 문제는 파일을 한 줄씩 읽으면서 매번 파일을 열고 닫는 불필요한 I/O가 발생하여 비효율적이라는 점임. 결과는 맞게 나올 수 있지만, 파일을 매번 열고 닫는 것은 비효율적임.

1. 질문

input.txt에서 한 줄씩 읽어와서 바로 결과를 출력했는데, 결과가 예상과 다르게 나옵니다. 한 번에 읽고 처리해야 하나요?

2. 잘못된 코드

```python
import re

palindrome_results = []

with open('input.txt', 'r') as infile:
    for line in infile:
        cleaned_line = re.sub(r'[^a-zA-Z0-9]', '', line).lower()
        is_palindrome = cleaned_line == cleaned_line[::-1]
        palindrome_results.append(is_palindrome)
        with open('output.txt', 'a') as outfile:  # 잘못된 위치에 파일 열기
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
True
False
```

- 테스트 케이스 2

```
True
True
True
```

- 테스트 케이스 3

```
False
False
```