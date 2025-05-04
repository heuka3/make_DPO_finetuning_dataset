0. 틀린 이유

파일을 여는 함수 호출에서 잘못된 인코딩을 사용하여 파일을 읽지 못함

1. 질문

왜 파일에서 데이터를 읽어올 수 없나요?

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r', encoding='utf16') as infile:  # 잘못된 인코딩
    lines = infile.readlines()

# 숫자와 알파벳 개수를 초기화
digit_count = 0
alphabet_count = 0

# 각 줄을 검사
for line in lines:
    for char in line:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            alphabet_count += 1

# output.txt 파일에 숫자와 알파벳 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(f"{digit_count}\n{alphabet_count}\n")
```

3. 에러 메시지

```
UnicodeDecodeError: 'utf-16-le' codec can't decode byte 0x20 in position 0: truncated data
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
(빈 파일)
```

- 테스트 케이스 2

```
(빈 파일)
```

- 테스트 케이스 3

```
(빈 파일)
```