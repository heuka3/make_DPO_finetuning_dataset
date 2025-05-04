0. 틀린 이유

파일을 닫지 않아 파일 쓰기가 완료되지 않음

1. 질문

왜 output.txt에 결과가 기록되지 않나요?

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
infile = open('input.txt', 'r')
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
outfile = open('output.txt', 'w')
outfile.write(f"{digit_count}\n{alphabet_count}\n")
# 파일을 닫지 않음
```

3. 에러 메시지

(에러 메시지 없음)

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