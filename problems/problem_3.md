1. 과제 문제

줄바꿈 포함된 문장에서 대문자 개수 세기 (파일 입출력)

2. 문제 설명

input.txt 파일에는 여러 줄로 구성된 텍스트가 저장되어 있다. 이 텍스트에서 대문자의 개수를 세어, output.txt 파일에 정수를 저장하는 프로그램을 작성하시오. 각 줄의 끝에는 줄바꿈 문자가 포함될 수 있으며, 텍스트에는 알파벳, 숫자, 특수문자, 공백 등이 포함될 수 있다.

3. 입력 형식 (input.txt)

여러 줄의 문자열이 주어짐
각 줄의 길이는 1 이상 1,000 이하
문자열의 총 길이는 1,000 이하
문자열에는 알파벳, 숫자, 특수문자, 공백 등이 포함될 수 있음

4. 출력 형식 (output.txt)

대문자의 개수를 정수로 출력

5. 테스트 케이스

- 테스트 케이스 1

input.txt
```txt
Hello World!
This Is A Test.
```

output.txt
```txt
5
```

- 테스트 케이스 2

input.txt
```txt
no capitals here
```

output.txt
```txt
0
```

- 테스트 케이스 3

input.txt
```txt
Python3.8
Is Great!
```

output.txt
```txt
3
```

6. 파이썬 코드 정답

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

# 대문자 개수를 초기화
uppercase_count = 0

# 각 줄을 검사
for line in lines:
    for char in line:
        if char.isupper():
            uppercase_count += 1

# output.txt 파일에 대문자 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(f"{uppercase_count}\n")
```