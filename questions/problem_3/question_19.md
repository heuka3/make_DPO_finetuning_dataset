0. 틀린 이유

파일의 내용을 여러 번 읽으려고 해서, 이미 읽은 이후에는 빈 결과를 반환함.

1. 질문

왜 제 코드에서는 대문자 개수가 0으로 나오는 걸까요? 줄을 읽을 때 첫 번째 시도에서는 잘 읽히는 것 같은데요.

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()  # 파일의 내용을 읽음

uppercase_count = 0

for line in lines:  # 이미 읽은 내용을 다시 읽으려 함
    lines = infile.readlines()  # 두 번째 시도는 빈 결과를 반환
    for char in line:
        if char.isupper():
            uppercase_count += 1

with open('output.txt', 'w') as outfile:
    outfile.write(f"{uppercase_count}\n")
```

3. 에러 메시지

```
(에러 메시지는 없지만, 잘못된 파일 읽기로 인해 결과가 항상 0으로 나옴)
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