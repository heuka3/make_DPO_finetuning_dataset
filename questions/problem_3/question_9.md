0. 틀린 이유

파일을 읽은 후 각 줄을 검사하지 않고 한 번에 전체 내용을 문자열로 취급하여 처리함. 이로 인해 마지막 줄바꿈 문자가 대문자로 잘못 계산됨.

1. 질문

왜 제 코드에서는 대문자의 개수가 제대로 세어지지 않나요?

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    content = infile.read()  # 전체 파일 내용을 한 문자열로 읽음

uppercase_count = 0

for char in content:  # 전체 내용을 한 번에 검사함
    if char.isupper():
        uppercase_count += 1

with open('output.txt', 'w') as outfile:
    outfile.write(f"{uppercase_count}\n")
```

3. 에러 메시지

```
(에러 메시지는 없지만, 읽는 방식 문제로 오답 발생)
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
5
```

- 테스트 케이스 2

```
0
```

- 테스트 케이스 3

```
3
```