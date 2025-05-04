0. 틀린 이유

파일을 열고 닫지 않아서 데이터 저장에 문제가 생김

1. 질문

파일에서 데이터를 읽고 쓸 때 항상 원하는 결과가 저장되지 않아요. 뭐가 문제일까요?

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
infile = open('input.txt', 'r')
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
outfile = open('output.txt', 'w')
outfile.write(f"{digit_count}\n{special_char_count}\n")
```

3. 에러 메시지

없음

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
[No output or incomplete output due to file not being closed]
```

- 테스트 케이스 2

```
[No output or incomplete output due to file not being closed]
```

- 테스트 케이스 3

```
[No output or incomplete output due to file not being closed]
```