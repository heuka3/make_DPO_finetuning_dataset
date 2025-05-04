0. 틀린 이유

파일을 읽은 후 줄바꿈 문자를 제거하지 않아, 잘못된 결과를 초래함.

1. 질문

왜 제 코드에서는 대문자 개수가 이상하게 나오나요? 줄바꿈 문자가 영향을 주나요?

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

uppercase_count = 0

for line in lines:
    for char in line:  # 줄바꿈 문자가 포함된 상태로 문자를 확인함
        if char.isupper():
            uppercase_count += 1

with open('output.txt', 'w') as outfile:
    outfile.write(f"{uppercase_count}\n")
```

3. 에러 메시지

```
(에러 메시지는 없지만, 줄바꿈 문자로 인해 잘못된 결과 발생)
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
6 (줄바꿈 문자를 포함하여 계산됨)
```

- 테스트 케이스 2

```
0
```

- 테스트 케이스 3

```
4 (줄바꿈 문자를 포함하여 계산됨)
```