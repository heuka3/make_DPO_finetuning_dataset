0. 틀린 이유

output.txt 파일에 기록할 때, 알파벳 개수를 먼저 기록함.

1. 질문

왜 output.txt의 첫 번째 줄이 알파벳의 개수로 기록되나요?

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

# output.txt 파일에 숫자와 알파벳 개수 저장 (잘못된 순서로 기록)
with open('output.txt', 'w') as outfile:
    outfile.write(f"{alphabet_count}\n{digit_count}\n")
```

3. 에러 메시지

(에러 메시지 없음)

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
17
4
```

- 테스트 케이스 2

```
0
10
```

- 테스트 케이스 3

```
35
0
```