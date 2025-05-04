0. 틀린 이유

output.txt 파일에 대문자 개수를 문자열로 저장하지 않고, 숫자로 저장하려고 시도함.

1. 질문

output.txt에 대문자 개수가 제대로 저장되지 않는 이유가 무엇인가요? 숫자로 저장하려고 하긴 했습니다.

2. 잘못된 코드

```python
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

uppercase_count = 0

for line in lines:
    for char in line:
        if char.isupper():
            uppercase_count += 1

with open('output.txt', 'w') as outfile:
    outfile.write(uppercase_count)  # 숫자를 문자열로 변환하지 않고 그대로 저장하려고 시도함
```

3. 에러 메시지

```
TypeError: write() argument must be str, not int
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