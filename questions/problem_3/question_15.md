0. 틀린 이유

대문자 개수를 세는 대신, 잘못된 조건문을 사용하여 대문자와 소문자를 구분하지 못함.

1. 질문

왜 제 코드에서는 대문자 개수가 항상 0으로 나열되나요? 조건문을 제대로 썼다고 생각했어요.

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

uppercase_count = 0

for line in lines:
    for char in line:
        if char == char.upper():  # 잘못된 조건문 사용; 대문자 확인 시 .isupper()를 사용해야 함
            uppercase_count += 1

with open('output.txt', 'w') as outfile:
    outfile.write(f"{uppercase_count}\n")
```

3. 에러 메시지

```
(에러 메시지는 없지만, 잘못된 조건문 사용으로 인해 결과가 항상 0으로 나옴)
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