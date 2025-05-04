0. 틀린 이유

숫자와 알파벳 개수를 세는 조건문을 잘못 작성함. `char == 'digit'`와 `char == 'alpha'`는 항상 False를 반환하므로, 숫자와 알파벳을 제대로 세지 못함.

1. 질문

왜 숫자와 알파벳의 개수가 모두 0으로 나오나요?

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
        if char == 'digit':  # 잘못된 조건
            digit_count += 1
        elif char == 'alpha':  # 잘못된 조건
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
0
0
```

- 테스트 케이스 2

```
0
0
```

- 테스트 케이스 3

```
0
0
```