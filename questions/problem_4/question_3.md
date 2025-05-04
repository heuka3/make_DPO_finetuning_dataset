0. 틀린 이유

char.strip()을 사용하여 공백을 제거한 후 isdigit()과 isalpha()를 호출하기 때문에, 공백이 아닌 문자도 strip()에 의해 변경되어 조건문이 제대로 작동하지 않음

1. 질문

왜 숫자나 알파벳의 개수가 예상보다 적게 나오나요?

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
        if char.strip().isdigit():
            digit_count += 1
        elif char.strip().isalpha():
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