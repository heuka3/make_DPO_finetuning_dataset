0. 틀린 이유

학생은 input.txt 파일에서 데이터를 읽어오지 않고, 문자열을 직접 변수로 할당하여 테스트했습니다. 이로 인해 input.txt의 내용을 반영하지 않고 항상 동일한 결과를 출력하게 됩니다.

1. 질문

왜 제 코드는 input.txt의 내용을 반영하지 않고 항상 동일한 결과를 출력하나요? 직접 할당한 문자열로 테스트했는데 무엇이 문제인지 모르겠습니다.

2. 잘못된 코드

```python
# 문자열을 직접 할당해서 테스트
line = "Testing with incorrect input"

# 공백 기준으로 단어 분리
words = line.split()

# 단어 개수 세기
word_count = len(words)

# output.txt 파일에 단어 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(str(word_count))
```

3. 에러 메시지

에러 메시지는 없지만, input.txt 파일의 내용을 반영하지 않습니다.

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
4
```

- 테스트 케이스 2

```
4
```

- 테스트 케이스 3

```
4
```