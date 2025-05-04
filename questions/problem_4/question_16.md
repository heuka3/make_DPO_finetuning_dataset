0. 틀린 이유

파일을 읽어올 때 read() 대신 readlines()를 사용해야 하는데 실수로 read()를 사용함. read()는 파일의 모든 내용을 하나의 문자열로 반환하므로, 각 줄을 개별적으로 처리할 수 없게 된다.

1. 질문

왜 모든 줄이 합쳐진 하나의 문자열로 처리되나요?

2. 잘못된 코드

```python
# input.txt 파일에서 문자열을 읽어옴
with open('input.txt', 'r') as infile:
    lines = infile.read()  # readlines()가 아니라 read() 사용

# 숫자와 알파벳 개수를 초기화
digit_count = 0
alphabet_count = 0

# 각 줄을 검사
for line in lines:
    for char in line:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            alphabet_count += 1

# output.txt 파일에 숫자와 알파벳 개수 저장
with open('output.txt', 'w') as outfile:
    outfile.write(f"{digit_count}\n{alphabet_count}\n")
```

3. 에러 메시지

(에러 메시지 없음)

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
4
17
```

- 테스트 케이스 2

```
10
0
```

- 테스트 케이스 3

```
0
35
```