1. 과제 문제

키워드 포함 줄 찾기 (파일 입출력)

2. 문제 설명

input.txt 파일에는 첫 번째 줄에 여러 개의 키워드가 공백으로 구분되어 나열되어 있다. 나머지 줄은 각각의 텍스트로 구성되어 있으며, 이 중 키워드가 포함된 줄만 output.txt 파일에 저장하는 프로그램을 작성하시오. 단, 키워드가 포함된 줄은 중복 없이 저장해야 하며, 대소문자를 구분하지 않는다.

3. 입력 형식 (input.txt)

첫 번째 줄에 키워드가 공백으로 구분되어 나열됨
각 키워드와 텍스트 줄의 길이는 1 이상 1,000 이하
총 키워드와 텍스트의 길이는 1,000 이하
텍스트에는 알파벳, 숫자, 특수문자, 공백 등이 포함될 수 있음

4. 출력 형식 (output.txt)

키워드가 포함된 각 줄을 중복 없이 출력

5. 테스트 케이스

- 테스트 케이스 1

input.txt
```txt
apple banana orange
This is an apple.
Bananas are great!
I love orange juice.
A random line.
```

output.txt
```txt
This is an apple.
Bananas are great!
I love orange juice.
```

- 테스트 케이스 2

input.txt
```txt
cat dog
The quick brown fox jumps over the lazy dog.
Cats are independent animals.
Dogs are loyal.
The day is sunny.
```

output.txt
```txt
The quick brown fox jumps over the lazy dog.
Cats are independent animals.
Dogs are loyal.
```

- 테스트 케이스 3

input.txt
```txt
code python AI
I love to code in Python.
AI is the future.
Machine learning is a subset of AI.
This sentence does not belong.
```

output.txt
```txt
I love to code in Python.
AI is the future.
Machine learning is a subset of AI.
```

6. 파이썬 코드 정답

```python
# input.txt 파일에서 첫 번째 줄을 키워드로 분리하고, 나머지 줄들을 읽어온다.
with open('input.txt', 'r') as infile:
    lines = infile.readlines()
    keywords = set(lines[0].strip().lower().split())
    text_lines = lines[1:]

# 키워드가 포함된 줄을 찾기 위한 집합 초기화
matched_lines = set()

# 각 줄을 검사하여 키워드가 포함된 줄을 찾는다
for line in text_lines:
    lower_line = line.strip().lower()
    if any(keyword in lower_line for keyword in keywords):
        matched_lines.add(line.strip())

# output.txt 파일에 중복 없이 키워드가 포함된 줄 저장
with open('output.txt', 'w') as outfile:
    for matched_line in matched_lines:
        outfile.write(matched_line + '\n')
```