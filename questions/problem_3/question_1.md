0. 틀린 이유

파일을 열지 않고 직접 문자열을 처리함. input.txt 파일에서 데이터를 읽어와야 하는데, 코드에서는 하드코딩된 문자열을 사용하고 있음.

1. 질문

왜 제 코드에서는 input.txt에 있는 대문자를 세지 않고 그냥 문자열을 바로 처리하나요?

2. 잘못된 코드

```python
lines = [
    "Hello World!",
    "This Is A Test."
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
5
```

- 테스트 케이스 2

```
5
```

- 테스트 케이스 3

```
5
```