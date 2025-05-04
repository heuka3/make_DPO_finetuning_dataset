0. 틀린 이유

파일을 읽을 때 잘못된 인코딩 형식을 사용하여 인코딩 에러가 발생함.

1. 질문

왜 제 코드에서는 input.txt 파일을 읽으려고 할 때 인코딩 에러가 발생하나요?

2. 잘못된 코드

```python
with open('input.txt', 'r', encoding='ascii') as infile:  # 잘못된 인코딩을 사용함
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
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 0: ordinal not in range(128)
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