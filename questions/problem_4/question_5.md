0. 틀린 이유

파일을 열고 닫는 순서가 잘못됨

1. 질문

왜 output.txt에 올바른 결과가 저장되지 않나요?

2. 잘못된 코드

```python
# input.txt 파일에 숫자와 알파벳 개수 저장
with open('output.txt', 'w') as outfile:
    digit_count = 0
    alphabet_count = 0

    # input.txt 파일에서 문자열을 읽어옴
    with open('input.txt', 'r') as infile:
        lines = infile.readlines()

    # 각 줄을 검사
    for line in lines:
        for char in line:
            if char.isdigit():
                digit_count += 1
            elif char.isalpha():
                alphabet_count += 1

    outfile.write(f"{digit_count}\n{alphabet_count}\n")
```

3. 에러 메시지

(에러 메시지 없음)

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
(빈 파일)
```

- 테스트 케이스 2

```
(빈 파일)
```

- 테스트 케이스 3

```
(빈 파일)
```