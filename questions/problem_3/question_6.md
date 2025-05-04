0. 틀린 이유

파일을 읽는 with 블록 내에서 line 변수를 사용하고 블록을 벗어난 후에 line 변수를 사용하려고 해서 범위를 벗어난 변수 접근 시도가 발생함.

1. 질문

왜 제 코드에서는 line 변수를 사용할 때 오류가 발생하나요?

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    for line in infile:
        pass  # line 변수를 여기서만 사용할 수 있음

uppercase_count = 0

# line 변수를 사용하려고 하지만, 이미 범위를 벗어남
for char in line:
    if char.isupper():
        uppercase_count += 1

with open('output.txt', 'w') as outfile:
    outfile.write(f"{uppercase_count}\n")
```

3. 에러 메시지

```
NameError: name 'line' is not defined
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