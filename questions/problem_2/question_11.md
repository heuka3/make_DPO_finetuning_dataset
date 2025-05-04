0. 틀린 이유

숫자를 세는 조건을 잘못 작성하여 제대로 된 숫자 개수가 나오지 않음. `char == digit_count` 대신 `char.isdigit()`을 사용해야 함.

1. 질문

숫자의 개수를 세고 싶어서 코드를 작성했는데, 항상 0으로 나옵니다. 조건에 문제가 있나요?

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
        if char == digit_count:  # 잘못된 조건
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
2
```

- 테스트 케이스 2

```
0
0
```

- 테스트 케이스 3

```
0
2
```