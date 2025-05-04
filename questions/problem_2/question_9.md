0. 틀린 이유

파일을 바이너리 모드로 열어 문자열을 처리하지 못함

1. 질문

파일을 읽고 쓰려고 하는데, 결과가 이상합니다. 왜 그럴까요?

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'rb') as infile:  # 바이너리 모드로 잘못 열음
    lines = infile.readlines()

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
with open('output.txt', 'wb') as outfile:  # 바이너리 모드로 잘못 열음
    outfile.write(f"{digit_count}\n{special_char_count}\n".encode())
```

3. 에러 메시지

없음

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
b'0\n0\n'
```

- 테스트 케이스 2

```
b'0\n0\n'
```

- 테스트 케이스 3

```
b'0\n0\n'
```