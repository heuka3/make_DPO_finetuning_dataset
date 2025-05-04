0. 틀린 이유

대소문자 구분이 불필요한 부분에서 잘못된 조건을 사용하여 숫자와 특수문자를 제대로 세지 못함

1. 질문

숫자와 특수문자를 각각 세고 싶은데, 코드가 제대로 작동하지 않는 것 같아요. 어디가 잘못된 걸까요?

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

# 숫자와 특수문자 개수를 초기화
digit_count = 0
special_char_count = 0
special_chars = set('!@#$%^&*')

# 각 줄을 검사
for line in lines:
    for char in line:
        if char.upper().isdigit():  # 대소문자 구분이 불필요함
            digit_count += 1
        elif char.upper() in special_chars:  # 대소문자 구분이 불필요함
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