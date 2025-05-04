0. 틀린 이유

학생은 파일에서 읽어온 데이터를 저장한 변수 이름을 잘못 사용하여, 실제로는 존재하지 않는 변수를 참조하고 있습니다. 이로 인해 UnboundLocalError가 발생합니다.

1. 질문

왜 제 코드는 input.txt에서 데이터가 아닌 잘못된 변수를 참조하고 있나요? 어떤 변수를 사용해야 할지 혼란스럽습니다.

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    correct_line = infile.read().strip()

# 잘못된 변수 사용
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