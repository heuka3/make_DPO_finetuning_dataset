0. 틀린 이유

특수문자와 숫자를 검사하는 과정에서 알파벳 문자를 잘못 세고 있음

1. 질문

알파벳을 특수문자나 숫자로 잘못 세고 있는 것 같아요. 코드에서 어디가 잘못된 건가요?

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
        elif char in special_chars or char.isalpha():  # 알파벳을 잘못 세고 있음
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
14
```

- 테스트 케이스 2

```
0
28
```

- 테스트 케이스 3

```
3
13
```