0. 틀린 이유

학생은 split() 메서드의 인자로 숫자를 입력하여 잘못된 결과를 얻었습니다. split() 메서드는 문자열을 분리할 때 구분자를 지정하는데, 숫자가 아닌 문자열이나 None을 사용해야 합니다.

1. 질문

왜 제 코드는 split()을 사용했는데도 단어 개수가 제대로 나오지 않나요? 인자를 숫자로 줘도 된다고 생각했는데 잘못된 것 같습니다.

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    line = infile.read().strip()

# 잘못된 split 인자 사용
words = line.split(2)

# 단어 개수 세기
word_count = len(words)

# output.txt 파일에 단어 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(str(word_count))
```

3. 에러 메시지

```
TypeError: must be str or None, not int
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

에러 발생으로 인해 파일에 출력되지 않음

- 테스트 케이스 2

에러 발생으로 인해 파일에 출력되지 않음

- 테스트 케이스 3

에러 발생으로 인해 파일에 출력되지 않음