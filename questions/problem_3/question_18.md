0. 틀린 이유

파일을 열고 읽기 전에 파일이 이미 닫혔다고 가정하여 잘못된 접근을 시도함.

1. 질문

왜 제 코드에서는 파일을 읽을 때 이미 닫혀 있다고 나오나요?

2. 잘못된 코드

```python
infile = open('input.txt', 'r')
infile.close()  # 파일을 열자마자 닫음

lines = infile.readlines()  # 파일이 닫힌 상태에서 읽으려 함

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