0. 틀린 이유

파일을 열고 닫는 순서가 잘못되어, 파일을 닫은 후에 읽으려고 시도함.

1. 질문

왜 제 코드에서는 input.txt 파일을 읽으려 할 때 오류가 발생하나요?

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    pass  # 파일을 이 시점에 닫고 아무것도 읽지 않음

lines = infile.readlines()  # 닫힌 파일을 읽으려고 함

uppercase_count = 0

for line in lines:
    for char in line:
        if char.isupper():
            uppercase_count += 1

with open('output.txt', 'w') as outfile:
    outfile.write(f"{uppercase_count}\n")
```

3. 에러 메시지

```
ValueError: I/O operation on closed file.
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
(에러로 인해 출력 없음)
```

- 테스트 케이스 2

```
(에러로 인해 출력 없음)
```

- 테스트 케이스 3

```
(에러로 인해 출력 없음)
```