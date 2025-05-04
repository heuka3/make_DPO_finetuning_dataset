1. 과제 문제 

단어 개수 세기 (파일 입출력)

2. 문제 설명

input.txt 파일에는 한 줄로 구성된 문장이 저장되어 있다. 이 문장에서 공백을 기준으로 단어를 나누고, 단어의 개수를 output.txt 파일에 저장하는 프로그램을 작성하시오. 단, 문장에 불필요한 공백이 있을 수도 있으며, 단어는 영어로만 구성되어 있다.

3. 입력 형식 (input.txt)

한 줄의 문자열이 주어짐
문자열의 길이는 1 이상 1,000 이하
단어는 알파벳 소문자 또는 대문자로 구성됨
단어는 공백 하나 이상으로 구분됨

4. 출력 형식 (output.txt)

공백을 기준으로 구분된 단어의 개수를 정수로 출력

5. 테스트 케이스

- 테스트 케이스 1

input.txt
```txt
hello world
```

output.txt
```txt
2
```

- 테스트 케이스 2

input.txt
```txt
OpenAI ChatGPT is helpful
```

output.txt
```txt
4
```

- 테스트 케이스 3

input.txt
```txt
Python
```

output.txt
```txt
1
```

6. 파이썬 코드 정답

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
	line = infile.read().strip()

# 공백 기준으로 단어 분리 (연속된 공백 자동 처리)
words = line.split()

# 단어 개수 세기
word_count = len(words)

# output.txt 파일에 단어 개수 저장
with open('output.txt', 'w') as outfile:
	outfile.write(str(word_count))
```