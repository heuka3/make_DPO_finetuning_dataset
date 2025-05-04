0. 틀린 이유

파일을 한 글자씩 읽는 방식은 문제가 없으나, 학생의 코드에서는 줄바꿈 문자를 포함하여 모든 문자를 개별로 처리하고 있어 대문자 개수가 잘못 계산될 가능성은 없습니다. 문제는 학생이 제시한 오답이 줄바꿈 문자와 관련이 없으며, 코드 자체는 대문자 개수를 올바르게 세고 있습니다. 학생이 제시한 오답은 코드의 문제와 관련이 없습니다.

1. 질문

왜 제 코드에서는 대문자 개수가 올바르게 계산되지 않나요? 한 글자씩 읽어서 세고 있는데요.

2. 잘못된 코드

```python
# 파일을 한 글자씩 읽으려 함
with open('input.txt', 'r') as infile:
    char = infile.read(1)
    uppercase_count = 0

    while char:
        if char.isupper():
            uppercase_count += 1
        char = infile.read(1)  # 한 글자씩 읽음

with open('output.txt', 'w') as outfile:
    outfile.write(f"{uppercase_count}\n")
```

3. 에러 메시지

```
(에러 메시지는 없지만, 한 글자씩 읽는 방식으로 인해 누락 발생)
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
5
```

- 테스트 케이스 2

```
0
```

- 테스트 케이스 3

```
3
```