0. 틀린 이유

학생의 코드는 input.txt 파일에서 읽어온 데이터를 잘못된 변수에 저장했습니다. 그 결과 프로그램의 나머지 부분에서 의도한 대로 동작하지 않습니다. 'line' 변수를 사용해야 하는데 'wrong_variable'에 저장하여 발생한 문제입니다.

1. 질문

왜 제 코드는 input.txt의 데이터를 인식하지 못하는 것 같죠? 변수에 잘못 저장된 것 같은데, 어떻게 해결해야 하나요?

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    wrong_variable = infile.read().strip()

# 공백 기준으로 단어 분리
words = line.split()

# 단어 개수 세기
word_count = len(words)

# output.txt 파일에 단어 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(str(word_count))
```

3. 에러 메시지

```
UnboundLocalError: local variable 'line' referenced before assignment
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

에러 발생으로 인해 파일에 출력되지 않음

- 테스트 케이스 2

에러 발생으로 인해 파일에 출력되지 않음

- 테스트 케이스 3

에러 발생으로 인해 파일에 출력되지 않음