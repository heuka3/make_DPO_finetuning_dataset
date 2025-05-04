0. 틀린 이유

학생의 코드는 모든 알파벳 문자를 빈 문자열로 대체하여, 단어를 공백으로 분리할 수 없게 만듭니다. 따라서 단어 개수가 항상 0이 됩니다.

1. 질문

왜 제 코드는 항상 단어 개수를 0으로 반환하나요? 알파벳 문자를 제거했더니 공백이 남았을 거라 생각했는데, 뭔가 잘못된 것 같습니다.

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    line = infile.read().strip()

# 모든 문자를 빈 문자열로 대체
line = ''.join('' if c.isalpha() else c for c in line)

# 공백 기준으로 단어 분리
words = line.split()

# 단어 개수 세기
word_count = len(words)

# output.txt 파일에 단어 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(str(word_count))
```

3. 에러 메시지

에러 메시지는 없지만 word_count가 0이 됩니다.

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
0
```

- 테스트 케이스 2

```
0
```

- 테스트 케이스 3

```
0
```