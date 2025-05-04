0. 틀린 이유

학생의 코드는 각 단어의 첫 글자만을 리스트에 추가하고 있습니다. 따라서 전체 단어 개수를 세는 것이 아니라 각 단어의 첫 글자만을 리스트에 추가하여 그 개수를 세고 있습니다.

1. 질문

왜 제 코드는 각 단어의 첫 글자만을 세고 있는 것 같나요? 전체 단어 개수를 세고 싶습니다.

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    line = infile.read().strip()

# 첫 글자만을 나눠서 리스트 생성
words = [word[0] for word in line.split()]

# 단어 개수 세기
word_count = len(words)

# output.txt 파일에 단어 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(str(word_count))
```

3. 에러 메시지

에러 메시지는 없지만 word_count가 각 단어의 첫 글자 수와 동일합니다.

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
2
```

- 테스트 케이스 2

```
4
```

- 테스트 케이스 3

```
1
```