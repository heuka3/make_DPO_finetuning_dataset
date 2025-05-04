0. 틀린 이유

숫자와 특수문자를 각각 세지 않고, 같은 변수에 합산하여 세고 있음

1. 질문

숫자와 특수문자를 각각 세어야 하는데, 뭔가 제대로 되지 않는 것 같아요. 어디가 잘못된 건가요?

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    lines = infile.readlines()

# 숫자와 특수문자 개수를 초기화
char_count = 0  # 숫자와 특수문자를 같이 셈
special_chars = set('!@#$%^&*')

# 각 줄을 검사
for line in lines:
    for char in line:
        if char.isdigit() or char in special_chars:  # 숫자와 특수문자 모두 같은 변수 사용
            char_count += 1

# output.txt 파일에 숫자와 특수문자 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(f"{char_count}\n{char_count}\n")
```

3. 에러 메시지

없음

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
5
5
```

- 테스트 케이스 2

```
0
0
```

- 테스트 케이스 3

```
5
5
```