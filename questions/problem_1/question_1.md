0. 틀린 이유

학생의 코드는 split()을 사용하지 않고 find()를 사용하여 첫 번째 공백의 위치만 찾고, 그에 따라 단어 개수를 1로 고정하고 있습니다. 이는 전체 단어 개수를 세는 문제의 요구사항과 맞지 않습니다.

1. 질문

왜 제 코드는 전체 단어 개수가 아니라 첫 번째 단어만 찾는 것 같나요? 모든 단어를 세고 싶은데 방법이 잘못된 것 같습니다.

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    line = infile.read().strip()

# 첫 번째 단어 찾기
first_space = line.find(' ')
if first_space == -1:
    word_count = 1 if line else 0
else:
    word_count = 1

# output.txt 파일에 단어 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(str(word_count))
```

3. 에러 메시지

에러 메시지는 없지만 word_count가 첫 번째 단어의 존재 여부에 따라 결정됩니다.

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