0. 틀린 이유

파일에서 읽어온 데이터를 문자열로 처리해야 하는데, 이를 리스트로 처리하려고 시도해서 문제가 발생했습니다.

1. 질문

파일에서 읽어온 데이터를 리스트로 취급하려고 했는데, 문자열을 리스트처럼 다룰 수 없다는 오류가 발생합니다. 어떻게 수정해야 할까요?

2. 잘못된 코드

```python
def extract_contents(lines):
    opener = {'(': ')', '{': '}', '[': ']'}
    closer = {v: k for k, v in opener.items()}

    stack = []
    results = []

    for line in lines:  # lines를 리스트로 가정
        for i, ch in enumerate(line):
            if ch in opener:
                stack.append((ch, i))
            elif ch in closer and stack and stack[-1][0] == closer[ch]:
                open_char, start = stack.pop()
                results.append(line[start+1:i].strip())

    return results

with open('input.txt', 'r') as infile:
    lines = infile.read()  # 파일 내용을 한 문자열로 읽음

all_extracted = extract_contents(lines)  # 문자열을 리스트처럼 처리

with open('output.txt', 'w') as outfile:
    for item in all_extracted:
        outfile.write(item + '\n')
```

3. 에러 메시지

TypeError: 'str' object is not iterable

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
(출력 없음)
```

- 테스트 케이스 2

```
(출력 없음)
```

- 테스트 케이스 3

```
(출력 없음)
```