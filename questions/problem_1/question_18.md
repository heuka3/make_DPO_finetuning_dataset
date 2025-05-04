0. 틀린 이유

학생의 코드는 split('')을 사용하여 빈 문자열을 구분자로 설정하려고 했기 때문에 ValueError가 발생했습니다. split() 메서드는 빈 문자열을 구분자로 사용할 수 없으며, 단어를 공백으로 나누기 위해서는 split() 또는 split(None)을 사용해야 합니다.

1. 질문

왜 제 코드는 단어 개수가 아니라 각 문자별로 나누어서 개수를 세고 있는 것 같나요? 문장을 단어로 나누고 싶은데, 어떻게 해야 하나요?

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    line = infile.read().strip()

# 모든 문자를 기준으로 나눠서 리스트 생성
words = line.split('')

# 단어 개수 세기
word_count = len(words)

# output.txt 파일에 단어 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(str(word_count))
```

3. 에러 메시지

```
ValueError: empty separator
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

에러 발생으로 인해 파일에 출력되지 않음

- 테스트 케이스 2

에러 발생으로 인해 파일에 출력되지 않음

- 테스트 케이스 3

에러 발생으로 인해 파일에 출력되지 않음