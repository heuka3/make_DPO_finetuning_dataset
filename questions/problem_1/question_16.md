0. 틀린 이유

학생의 코드는 readlines()를 사용하여 파일의 각 줄을 리스트로 읽어온 후, 줄 수를 단어 개수로 잘못 계산하고 있습니다. 문제에서는 한 줄의 문장을 공백으로 나누어 단어의 개수를 세어야 합니다.

1. 질문

왜 제 코드는 단어 개수가 아니라 줄 수만 세고 있는 것 같죠? 문장을 제대로 나누고 싶었는데, 어떻게 해야 하나요?

2. 잘못된 코드

```python
# input.txt 파일에서 각 줄을 리스트로 읽어옴
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

# 줄 수를 단어 개수로 셈
word_count = len(lines)

# output.txt 파일에 단어 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(str(word_count))
```

3. 에러 메시지

에러 메시지는 없지만, word_count가 줄 수로 계산됩니다.

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