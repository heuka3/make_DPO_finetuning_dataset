0. 틀린 이유

read()를 사용하여 파일 전체를 하나의 문자열로 읽어오면, 각 줄을 개별적으로 처리할 수 없기 때문에 줄바꿈을 인식하지 못하고, 각 줄마다 특수문자가 있는지 확인할 수 없습니다.

1. 질문

줄마다 특수문자가 있는지 확인하고 싶은데, 제대로 작동하지 않는 것 같아요. 왜 그럴까요?

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    lines = infile.read()  # readlines() 대신 read() 사용

# 숫자와 특수문자 개수를 초기화
digit_count = 0
special_char_count = 0
special_chars = set('!@#$%^&*')

# 각 줄을 검사
for line in lines:  # 문자열을 줄로 인식하지 못함
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
3
3
```

- 테스트 케이스 2

```
0
0
```

- 테스트 케이스 3

```
3
3
```