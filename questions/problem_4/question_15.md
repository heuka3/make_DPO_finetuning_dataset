0. 틀린 이유

숫자와 알파벳의 개수를 셀 때, 각각의 개수를 2씩 증가시키는 실수

1. 질문

왜 알파벳이나 숫자의 개수가 두 배로 기록되나요?

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
            digit_count += 2  # 잘못된 증가
        elif char.isalpha():
            alphabet_count += 2  # 잘못된 증가

# output.txt 파일에 숫자와 알파벳 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(f"{digit_count}\n{alphabet_count}\n")
```

3. 에러 메시지

(에러 메시지 없음)

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
8
34
```

- 테스트 케이스 2

```
20
0
```

- 테스트 케이스 3

```
0
70
```