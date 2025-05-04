0. 틀린 이유

학생은 input.txt 파일 대신 wrong_input.txt 파일을 열려고 시도했기 때문에 파일을 찾을 수 없다는 에러가 발생했습니다.

1. 질문

왜 제 코드는 input.txt 파일의 내용을 읽어오지 못하나요? 파일 이름을 잘못 입력한 것 같은데 어떻게 해야 하나요?

2. 잘못된 코드

```python
# 잘못된 파일 이름 사용
with open('wrong_input.txt', 'r') as infile:
    line = infile.read().strip()

# 공백 기준으로 단어 분리
words = line.split()

# 단어 개수 세기
word_count = len(words)

# output.txt 파일에 단어 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(str(word_count))
```

3. 에러 메시지

```
FileNotFoundError: [Errno 2] No such file or directory: 'wrong_input.txt'
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

에러 발생으로 인해 파일에 출력되지 않음

- 테스트 케이스 2

에러 발생으로 인해 파일에 출력되지 않음

- 테스트 케이스 3

에러 발생으로 인해 파일에 출력되지 않음