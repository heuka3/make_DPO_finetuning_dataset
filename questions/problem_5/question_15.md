0. 틀린 이유

파일을 열고 데이터를 읽을 때 'with' 구문을 사용하지 않아 파일이 제대로 닫히지 않아 I/O 문제가 발생함.

1. 질문

파일을 읽고 쓰는 과정에서 파일이 제대로 닫히지 않는 것 같습니다. 'with' 구문을 사용하지 않았을 때 어떤 문제가 생길 수 있나요?

2. 잘못된 코드

```python
import re

infile = open('input.txt', 'r')
lines = infile.readlines()
infile.close()

palindrome_results = []

for line in lines:
    cleaned_line = re.sub(r'[^a-zA-Z0-9]', '', line).lower()
    is_palindrome = cleaned_line == cleaned_line[::-1]
    palindrome_results.append(is_palindrome)

outfile = open('output.txt', 'w')
for result in palindrome_results:
    outfile.write(f"{result}\n")
outfile.close()
```

3. 에러 메시지

```
(에러 없음, 그러나 파일이 제대로 닫히지 않아 자원 누수가 발생할 수 있음)
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