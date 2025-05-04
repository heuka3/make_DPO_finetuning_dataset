0. 틀린 이유

학생의 코드는 줄바꿈 문자를 제거하기 위해 `strip()`을 사용했지만, 이는 각 줄의 끝에 있는 줄바꿈 문자만 제거할 뿐, 줄 내의 공백을 제거하지 않습니다. 문제의 요구사항은 줄바꿈 문자를 제거하는 것이 아니라, 숫자와 알파벳의 개수를 정확히 세는 것입니다. 따라서 `strip()`의 사용은 불필요하며, 코드의 논리에는 영향을 주지 않습니다. 학생의 코드가 예상보다 많은 알파벳 개수를 출력하는 이유는 `strip()`과 관련이 없습니다.

1. 질문

왜 숫자와 알파벳의 개수가 예상보다 많이 나오나요?

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
    for char in line.strip():  # .strip()을 사용하여 공백 제거
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
4
18
```

- 테스트 케이스 2

```
10
0
```

- 테스트 케이스 3

```
0
36
```