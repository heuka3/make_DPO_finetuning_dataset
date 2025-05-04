0. 틀린 이유

파일에 기록할 때 두 개의 정수를 쉼표로 구분하여 기록함

1. 질문

왜 output.txt가 예상한 형식으로 기록되지 않나요?

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
        elif char.isalpha():
            alphabet_count += 1

# output.txt 파일에 숫자와 알파벳 개수 저장 (쉼표로 구분)
with open('output.txt', 'w') as outfile:
    outfile.write(f"{digit_count}, {alphabet_count}\n")
```

3. 에러 메시지

(에러 메시지 없음)

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
4, 17
```

- 테스트 케이스 2

```
10, 0
```

- 테스트 케이스 3

```
0, 35
```