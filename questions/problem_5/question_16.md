0. 틀린 이유

파일에 결과를 기록할 때 줄바꿈을 \n 대신 \t를 사용하여, 결과가 의도치 않게 나옴.

1. 질문

output.txt에서 각 결과가 줄바꿈 대신 다른 이상한 문자를 기준으로 나옵니다. 줄바꿈을 어떻게 제대로 해야 하나요?

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
        outfile.write(f"{result}\t")  # 잘못된 줄바꿈 문자 사용
```

3. 에러 메시지

```
(에러 없음)
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
True	True	False	
```

- 테스트 케이스 2

```
True	True	True	
```

- 테스트 케이스 3

```
False	False	
```