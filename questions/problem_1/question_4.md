0. 틀린 이유

학생의 코드는 문자열의 마지막 문자를 잘못 제거하여 단어 개수를 잘못 세고 있습니다. 슬라이스를 사용하여 문자열의 마지막 문자를 제거하는 것은 불필요하며, 이로 인해 단어의 일부가 잘리거나 공백이 제거되어 단어 개수가 줄어들 수 있습니다.

1. 질문

왜 제 코드는 단어 개수를 이상하게 세나요? 슬라이스를 잘못한 것 같은데, 어디가 문제인지 모르겠습니다.

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    line = infile.read().strip()

# 잘못된 슬라이스 사용
line = line[:len(line)-1]

# 공백 기준으로 단어 분리
words = line.split()

# 단어 개수 세기
word_count = len(words)

# output.txt 파일에 단어 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(str(word_count))
```

3. 에러 메시지

에러 메시지는 없지만 word_count가 예상보다 적습니다.

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
2
```

- 테스트 케이스 2

```
3
```

- 테스트 케이스 3

```
1
```