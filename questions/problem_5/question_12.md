0. 틀린 이유

파일을 쓰기 전에 파일이 존재하면 삭제하지 않아서 이전의 잘못된 결과가 계속 남아 있음.

1. 질문

프로그램을 수정해서 다시 실행해도 이전 결과가 남아 있습니다. 이전 파일을 어떻게 초기화할 수 있나요?

2. 잘못된 코드

```python
import re

def check_palindrome():
    with open('input.txt', 'r') as infile:
        lines = infile.readlines()

    palindrome_results = []

    for line in lines:
        cleaned_line = re.sub(r'[^a-zA-Z0-9]', '', line).lower()
        is_palindrome = cleaned_line == cleaned_line[::-1]
        palindrome_results.append(is_palindrome)

    with open('output.txt', 'a') as outfile:  # 'a' 모드를 잘못 사용
        for result in palindrome_results:
            outfile.write(f"{result}\n")

check_palindrome()
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
True
True
True
True
```

- 테스트 케이스 3

```
False
False
False
False
False
```