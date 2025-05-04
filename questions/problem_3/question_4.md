0. 틀린 이유

파일을 열 때 읽기 모드를 사용하지 않고 잘못된 모드를 사용하여 파일을 읽을 수 없음.

1. 질문

왜 제 코드에서는 input.txt 파일을 열 수 없다고 나오나요?

2. 잘못된 코드

```python
with open('input.txt', 'w') as infile:  # 읽기 모드가 아닌 쓰기 모드를 사용함
    lines = infile.readlines()

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
io.UnsupportedOperation: not readable
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