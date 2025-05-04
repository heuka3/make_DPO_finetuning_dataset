0. 틀린 이유

학생의 코드는 문자열을 소문자로 변환한 후 split을 사용하지 않아, 단어를 나누지 않고 전체 문자열의 길이를 단어 개수로 잘못 계산합니다. 문제의 요구사항은 공백을 기준으로 단어를 나누는 것이므로, split을 사용해야 합니다.

1. 질문

왜 제 코드는 문장에서 단어를 나누지 않고 모든 문자를 하나의 단어로 취급하나요? 대소문자 구분을 없애려 했던 건데요.

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    line = infile.read().strip()

# 잘못된 변환: 소문자로 변경 후 split 생략
line = line.lower()

# 단어 개수 세기
word_count = len(line)

# output.txt 파일에 단어 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(str(word_count))
```

3. 에러 메시지

에러 메시지는 없지만, word_count가 문자열의 길이가 됩니다.

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