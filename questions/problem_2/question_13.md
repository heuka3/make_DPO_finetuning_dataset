0. 틀린 이유

변수 이름이 잘못되어 계산된 값을 출력할 때 사용하지 못함

1. 질문

변수 이름이 잘못된 걸까요? 숫자와 특수문자가 제대로 세어지지 않는 것 같아요.

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

# 숫자와 특수문자 개수를 초기화
digits_count = 0  # 잘못된 변수 이름
specialChars_count = 0  # 잘못된 변수 이름
special_chars = set('!@#$%^&*')

# 각 줄을 검사
for line in lines:
    for char in line:
        if char.isdigit():
            digits_count += 1
        elif char in special_chars:
            specialChars_count += 1

# output.txt 파일에 숫자와 특수문자 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(f"{digit_count}\n{special_char_count}\n")  # 잘못된 변수 이름 사용
```

3. 에러 메시지

```
NameError: name 'digit_count' is not defined
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
[No output due to error]
```

- 테스트 케이스 2

```
[No output due to error]
```

- 테스트 케이스 3

```
[No output due to error]
```