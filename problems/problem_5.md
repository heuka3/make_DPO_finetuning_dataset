1. 과제 문제

특수문자가 포함된 회문 문자열 판별 (파일 입출력)

2. 문제 설명

input.txt 파일에는 여러 줄로 구성된 텍스트가 저장되어 있다. 각 줄의 문자열에서 특수문자(!, @, #, $, %, ^, &, *)를 제외한 나머지 문자로 회문 여부를 판별하고, 각 줄이 회문인지 여부를 output.txt 파일에 True 또는 False로 저장하는 프로그램을 작성하시오. 각 줄의 끝에는 줄바꿈 문자가 포함될 수 있으며, 텍스트에는 알파벳, 숫자, 특수문자, 공백 등이 포함될 수 있다.

3. 입력 형식 (input.txt)

여러 줄의 문자열이 주어짐
각 줄의 길이는 1 이상 1,000 이하
문자열의 총 길이는 1,000 이하
문자열에는 알파벳, 숫자, 특수문자, 공백 등이 포함될 수 있음

4. 출력 형식 (output.txt)

각 줄에 대해 회문 여부를 True 또는 False로 출력

5. 테스트 케이스

- 테스트 케이스 1

input.txt
```txt
A man, a plan, a canal, Panama!
No 'x' in Nixon
Not a palindrome
```

output.txt
```txt
True
True
False
```

- 테스트 케이스 2

input.txt
```txt
Was it a car or a cat I saw?
Evil is a name of a foeman, as I live.
No lemon, no melon!
```

output.txt
```txt
True
True
True
```

- 테스트 케이스 3

input.txt
```txt
Hello, World!
Palindrome@123
```

output.txt
```txt
False
False
```

6. 파이썬 코드 정답

```python
import re

# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

# 회문 여부 결과 리스트 초기화
palindrome_results = []

# 각 줄을 검사
for line in lines:
    # 특수문자를 제외하고 알파벳과 숫자만 남기고 소문자로 변환
    cleaned_line = re.sub(r'[^a-zA-Z0-9]', '', line).lower()
    # 회문 여부 판별
    is_palindrome = cleaned_line == cleaned_line[::-1]
    palindrome_results.append(is_palindrome)

# output.txt 파일에 회문 여부 결과 저장
with open('output.txt', 'w') as outfile:
    for result in palindrome_results:
        outfile.write(f"{result}\n")
```