0. 틀린 이유

파일을 읽고 쓰는 경로를 잘못 설정하였음

1. 질문

input.txt와 output.txt 파일의 경로 설정이 잘못된 것 같은데, 어떻게 수정해야 하나요?

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('wrong_directory/input.txt', 'r') as infile:  # 잘못된 경로
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
with open('wrong_directory/output.txt', 'w') as outfile:  # 잘못된 경로
    outfile.write(f"{digit_count}\n{special_char_count}\n")
```

3. 에러 메시지

```
FileNotFoundError: [Errno 2] No such file or directory: 'wrong_directory/input.txt'
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