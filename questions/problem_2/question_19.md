0. 틀린 이유

프로그램이 숫자와 특수문자를 출력하는 순서를 반대로 작성함

1. 질문

숫자와 특수문자의 개수를 각각 출력하고 싶은데, 결과가 반대로 나와요. 어디가 잘못된 걸까요?

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
        if char.isdigit():
            digit_count += 1
        elif char in special_chars:
            special_char_count += 1

# output.txt 파일에 특수문자와 숫자 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(f"{special_char_count}\n{digit_count}\n")  # 출력 순서가 반대
```

3. 에러 메시지

없음

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
2
3
```

- 테스트 케이스 2

```
0
0
```

- 테스트 케이스 3

```
2
3
```