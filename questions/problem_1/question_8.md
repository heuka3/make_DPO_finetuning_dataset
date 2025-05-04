0. 틀린 이유

학생의 코드는 문자열을 공백으로 나누지 않고 전체 문장을 하나의 단어로 취급하여 잘못된 결과를 얻었습니다. 문제에서는 공백을 기준으로 단어를 나누어야 합니다.

1. 질문

왜 제 코드는 input.txt에 있는 전체 문장을 단어로 간주하고 나눠지지 않는 것 같나요? 문장을 그대로 하나의 단어로 취급하고 있어요.

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    line = infile.read().strip()

# 전체 문장을 단어로 취급
words = [line]

# 단어 개수 세기
word_count = len(words)

# output.txt 파일에 단어 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(str(word_count))
```

3. 에러 메시지

에러 메시지는 없지만, word_count가 1이 됩니다.

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
1
```

- 테스트 케이스 2

```
1
```

- 테스트 케이스 3

```
1
```