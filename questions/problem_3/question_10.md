0. 틀린 이유

input.txt 파일이 존재하지 않거나 비어있다고 가정하여 코드를 작성했기 때문에, 실제로 파일이 존재하고 내용이 있어도 대문자 개수를 0으로 처리함.

1. 질문

왜 output.txt 파일에 0이 출력되나요? input.txt에 내용이 있는줄 알았는데요?

2. 잘못된 코드

```python
uppercase_count = 0

# input.txt 파일이 존재하지 않는다고 가정하고 진행
try:
    with open('input.txt', 'r') as infile:
        lines = infile.readlines()
except FileNotFoundError:
    # 파일이 없으면 그냥 대문자 개수를 0으로 처리
    lines = []

for line in lines:
    for char in line:
        if char.isupper():
            uppercase_count += 1

with open('output.txt', 'w') as outfile:
    outfile.write(f"{uppercase_count}\n")
```

3. 에러 메시지

```
(에러 메시지는 없지만, 파일이 있다고 가정하지 않음)
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