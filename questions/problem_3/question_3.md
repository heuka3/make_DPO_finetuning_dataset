0. 틀린 이유

파일에 쓰기 전에 대문자 개수를 출력해 파일이 비어있음.

1. 질문

왜 제 코드에서는 output.txt 파일이 비어있나요?

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

uppercase_count = 0

for line in lines:
    for char in line:
        if char.isupper():
            uppercase_count += 1

print(uppercase_count)  # 콘솔에 출력하고 파일에 쓰지 않음

with open('output.txt', 'w') as outfile:
    # write 함수가 없어서 아무것도 파일에 쓰지 않음
    pass
```

3. 에러 메시지

```
(에러 메시지가 없고 파일이 비어있음)
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
(파일이 비어있음)
```

- 테스트 케이스 2

```
(파일이 비어있음)
```

- 테스트 케이스 3

```
(파일이 비어있음)
```