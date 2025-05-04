0. 틀린 이유

학생의 코드는 각 줄의 첫 번째 문자만 단어로 간주하고 있습니다. 문제에서는 공백을 기준으로 단어를 나누어야 하며, 각 줄의 첫 번째 문자가 아닌 전체 문장에서 단어를 세어야 합니다.

1. 질문

왜 제 코드는 각 줄의 첫 번째 문자만 단어로 간주하고 있는 것 같죠? 모든 단어를 세고 싶어요.

2. 잘못된 코드

```python
# input.txt 파일에서 각 줄을 읽어옴
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

# 각 줄의 첫 번째 문자만 단어로 간주
words = [line[0] for line in lines if line.strip()]

# 단어 개수 세기
word_count = len(words)

# output.txt 파일에 단어 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(str(word_count))
```

3. 에러 메시지

에러 메시지는 없지만 word_count가 각 줄의 첫 번째 문자 수와 동일합니다.

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