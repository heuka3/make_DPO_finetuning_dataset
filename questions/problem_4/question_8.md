0. 틀린 이유

문자열을 검사할 때 공백을 포함한 문자도 알파벳으로 세는 실수를 함

1. 질문

왜 알파벳의 개수가 너무 많이 나오나요?

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

# 숫자와 알파벳 개수를 초기화
digit_count = 0
alphabet_count = 0

# 각 줄을 검사
for line in lines:
    for char in line:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha() or char == ' ':  # 공백도 알파벳으로 세는 실수
            alphabet_count += 1

# output.txt 파일에 숫자와 알파벳 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(f"{digit_count}\n{alphabet_count}\n")
```

3. 에러 메시지

(에러 메시지 없음)

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
4
22
```

- 테스트 케이스 2

```
10
1
```

- 테스트 케이스 3

```
0
43
```