0. 틀린 이유

학생은 공백의 개수를 세어 단어의 개수를 추정하려 했으나, 이는 연속된 공백이 있을 경우 잘못된 결과를 초래합니다. 공백의 개수는 단어의 개수와 일치하지 않을 수 있습니다. 문제의 요구사항에 따라 split()을 사용하여 단어를 분리해야 합니다.

1. 질문

왜 제 코드는 단어 개수가 아니라 공백 개수에 따라 계산되나요? 단어를 세고 싶었는데, 어디가 잘못된 걸까요?

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    line = infile.read().strip()

# 공백의 개수로 단어 개수를 세려고 함
word_count = line.count(' ')

# output.txt 파일에 단어 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(str(word_count))
```

3. 에러 메시지

에러 메시지는 없지만 word_count가 공백의 개수로 계산됩니다.

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
1
```

- 테스트 케이스 2

```
3
```

- 테스트 케이스 3

```
0
```