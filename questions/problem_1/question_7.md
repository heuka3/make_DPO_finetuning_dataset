0. 틀린 이유

학생은 문자열을 줄바꿈 문자로 나누고, 각 줄의 길이를 단어의 개수로 잘못 계산했습니다. 문제에서는 공백을 기준으로 단어를 나누어야 합니다.

1. 질문

왜 제 코드는 단어 개수가 아니라 문자열의 줄 수만 세나요? 각 줄의 길이를 단어 개수로 세고 싶습니다.

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    line = infile.read().strip()

# 줄바꿈을 기준으로 나누고 각 줄의 길이를 사용
lines = line.split('\n')
word_count = sum(len(l) for l in lines)

# output.txt 파일에 단어 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(str(word_count))
```

3. 에러 메시지

에러 메시지는 없지만 word_count가 잘못 계산됩니다.

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
11
```

- 테스트 케이스 2

```
23
```

- 테스트 케이스 3

```
6
```