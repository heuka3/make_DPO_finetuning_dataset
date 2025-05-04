1. 과제 문제

줄바꿈 포함된 문장에서 숫자와 알파벳 개수 세기 (파일 입출력)

2. 문제 설명

input.txt 파일에는 여러 줄로 구성된 텍스트가 저장되어 있다. 이 텍스트에서 숫자(0-9)와 알파벳(a-z, A-Z)의 개수를 각각 세어, output.txt 파일에 두 개의 정수를 저장하는 프로그램을 작성하시오. 각 줄의 끝에는 줄바꿈 문자가 포함될 수 있으며, 텍스트에는 숫자, 알파벳, 특수문자, 공백 등이 포함될 수 있다.

3. 입력 형식 (input.txt)

여러 줄의 문자열이 주어짐
각 줄의 길이는 1 이상 1,000 이하
문자열의 총 길이는 1,000 이하
문자열에는 숫자, 알파벳, 특수문자, 공백 등이 포함될 수 있음

4. 출력 형식 (output.txt)

첫 번째 줄에 숫자의 개수를 정수로 출력
두 번째 줄에 알파벳의 개수를 정수로 출력

5. 테스트 케이스

- 테스트 케이스 1

input.txt
```txt
Room 101: Available
Level 42
```

output.txt
```txt
4
17
```

- 테스트 케이스 2

input.txt
```txt
1234567890
```

output.txt
```txt
10
0
```

- 테스트 케이스 3

input.txt
```txt
The quick brown fox jumps over the lazy dog.
```

output.txt
```txt
0
35
```

6. 파이썬 코드 정답

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

# output.txt 파일에 숫자와 알파벳 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(f"{digit_count}\n{alphabet_count}\n")
```