0. 틀린 이유

학생의 코드는 각 줄의 첫 번째 문자만 검사하기 때문에, 전체 문자열을 검사하지 않아 숫자와 알파벳의 개수가 예상보다 적게 카운트됩니다.

1. 질문

왜 숫자나 알파벳의 개수가 예상보다 적게 카운트되나요?

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

# 숫자와 알파벳 개수를 초기화
digit_count = 0
alphabet_count = 0

# 각 줄을 검사하지만, 각 줄의 첫 번째 문자만 검사
for line in lines:
    char = line[0]  # 첫 번째 문자만 검사
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
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
1
1
```

- 테스트 케이스 2

```
1
0
```

- 테스트 케이스 3

```
0
1
```