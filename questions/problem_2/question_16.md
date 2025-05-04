0. 틀린 이유

숫자와 특수문자를 세는 조건에서 알파벳까지 잘못 세고 있음. `char.isdigit() or char.isalpha()` 조건이 숫자와 알파벳을 모두 세도록 되어 있어, 숫자만 세야 하는 부분에서 알파벳도 포함됨.

1. 질문

숫자와 특수문자를 세고 싶었는데, 알파벳까지 잘못 세고 있는 것 같습니다. 어디가 잘못된 건가요?

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
        if char.isdigit() or char.isalpha():  # 알파벳도 잘못 세고 있음
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
15
2
```

- 테스트 케이스 2

```
28
0
```

- 테스트 케이스 3

```
13
2
```