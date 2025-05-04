0. 틀린 이유

특수문자와 숫자를 카운트하는 조건을 중복해서 작성하여 잘못된 결과를 산출함. `elif char.isdigit() and char in special_chars:` 조건은 불필요하며, 이로 인해 숫자와 특수문자가 중복 카운트됨.

1. 질문

숫자와 특수문자를 각각 세고 싶은데, 무언가 결과가 이상합니다. 조건을 잘못 작성했나요?

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
        elif char.isdigit() and char in special_chars:  # 중복된 조건
            digit_count += 1
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
6
4
```

- 테스트 케이스 2

```
0
0
```

- 테스트 케이스 3

```
6
4
```