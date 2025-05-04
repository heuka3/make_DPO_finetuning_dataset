0. 틀린 이유

파일의 대문자를 세는 대신, 하드코딩된 잘못된 문자열을 사용하여 계산을 함. input.txt 파일에서 데이터를 읽어오지 않음.

1. 질문

왜 제 코드에서는 input.txt 파일의 내용을 읽지 않고 이상한 문자열을 사용하나요?

2. 잘못된 코드

```python
lines = [
    "This is not the content of input.txt"
]

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
(에러 메시지가 없고 잘못된 입력을 사용하고 있음)
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
0
```

- 테스트 케이스 2

```
0
```

- 테스트 케이스 3

```
0
```