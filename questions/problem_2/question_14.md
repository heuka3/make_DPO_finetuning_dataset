0. 틀린 이유

파일을 읽고 난 후 데이터를 잘못된 변수에 저장하여, 실제로 파일에서 읽어온 데이터를 사용하지 못함.

1. 질문

파일에서 데이터를 읽어 왔는데, 변수에 저장하고 나서 왜 데이터를 읽을 수 없을까요?

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    data = infile.readlines()

# 잘못된 변수에 데이터 저장
lines = "This should be the data"  # 잘못된 변수 초기화

# 숫자와 특수문자 개수를 초기화
digit_count = 0
special_char_count = 0
special_chars = set('!@#$%^&*')

# 각 줄을 검사
for line in lines:
    for char in line:
        if char.isdigit():
            digit_count += 1
        elif char in special_chars:
            special_char_count += 1

# output.txt 파일에 숫자와 특수문자 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(f"{digit_count}\n{special_char_count}\n")
```

3. 에러 메시지

없음

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
0
0
```

- 테스트 케이스 2

```
0
0
```

- 테스트 케이스 3

```
0
0
```