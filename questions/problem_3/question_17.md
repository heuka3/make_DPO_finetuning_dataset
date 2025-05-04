0. 틀린 이유

대문자 검사 대신에 소문자 검사 메서드를 사용하여 대문자를 세지 못함.

1. 질문

왜 제 코드에서는 대문자 개수가 항상 0으로 나오나요? 분명히 대문자가 있는데요.

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

uppercase_count = 0

for line in lines:
    for char in line:
        if char.islower():  # 대문자가 아닌 소문자 검사 메서드를 사용함
            uppercase_count += 1

with open('output.txt', 'w') as outfile:
    outfile.write(f"{uppercase_count}\n")
```

3. 에러 메시지

```
(에러 메시지는 없지만, 잘못된 검사로 인해 오류 발생)
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