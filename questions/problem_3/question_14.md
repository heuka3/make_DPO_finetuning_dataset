0. 틀린 이유

파일 이름이 잘못되어 input.txt 파일을 찾지 못함.

1. 질문

왜 제 코드에서는 input.txt 파일을 찾을 수 없다고 하나요? 파일이 있다고 확신했는데요.

2. 잘못된 코드

```python
with open('inpt.txt', 'r') as infile:  # 오타로 인해 잘못된 파일 이름을 사용함
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
FileNotFoundError: [Errno 2] No such file or directory: 'inpt.txt'
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