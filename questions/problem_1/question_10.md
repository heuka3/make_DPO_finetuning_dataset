0. 틀린 이유

학생은 파일을 잘못된 모드로 열어서 데이터를 읽고 쓸 때 에러가 발생합니다. input.txt 파일을 읽기 모드로 열어야 하는데 쓰기 모드로 열었고, output.txt 파일을 쓰기 모드로 열어야 하는데 읽기 모드로 열었습니다.

1. 질문

왜 제 코드는 파일에서 데이터를 읽고 쓸 때 에러가 발생하나요? 모드를 잘못 설정한 것 같아요.

2. 잘못된 코드

```python
# input.txt 파일을 쓰기 모드로 잘못 열기
with open('input.txt', 'w') as infile:
    line = infile.read().strip()

# 공백 기준으로 단어 분리
words = line.split()

# 단어 개수 세기
word_count = len(words)

# output.txt 파일을 읽기 모드로 잘못 열기
with open('output.txt', 'r') as outfile:
    outfile.write(str(word_count))
```

3. 에러 메시지

```
UnsupportedOperation: not readable
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

에러 발생으로 인해 파일에 출력되지 않음

- 테스트 케이스 2

에러 발생으로 인해 파일에 출력되지 않음

- 테스트 케이스 3

에러 발생으로 인해 파일에 출력되지 않음