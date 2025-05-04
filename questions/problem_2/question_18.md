0. 틀린 이유

파일을 읽어오는 부분에서 잘못된 인코딩을 사용하여 제대로 읽지 못함

1. 질문

파일을 읽어올 때 오류가 발생하는데, 인코딩 문제가 있는 것 같아요. 어떻게 해결해야 할까요?

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r', encoding='ascii') as infile:  # 잘못된 인코딩
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
with open('output.txt', 'w') as outfile:
    outfile.write(f"{digit_count}\n{special_char_count}\n")
```

3. 에러 메시지

```
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe2 in position 10: ordinal not in range(128)
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