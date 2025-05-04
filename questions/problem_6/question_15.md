0. 틀린 이유

파일에서 데이터를 읽을 때, 전체 데이터를 한 번에 읽고 한 번에 처리하려고 해서, 줄 단위로 처리되지 않아 잘못된 결과가 나왔습니다.

1. 질문

파일의 내용을 줄 단위가 아닌 전체 내용을 한 번에 처리하고 있는데, 줄 단위로 처리하려면 어떻게 해야 할까요?

2. 잘못된 코드

```python
def extract_contents(content):
    opener = {'(': ')', '{': '}', '[': ']'}
    closer = {v: k for k, v in opener.items()}

    stack = []
    results = []

    for i, ch in enumerate(content):
        if ch in opener:
            stack.append((ch, i))
        elif ch in closer and stack and stack[-1][0] == closer[ch]:
            open_char, start = stack.pop()
            results.append(content[start+1:i].strip())

    return results

with open('input.txt', 'r') as infile:
    content = infile.read()  # 전체 내용을 한 번에 읽어버림

all_extracted = extract_contents(content)

with open('output.txt', 'w') as outfile:
    for item in all_extracted:
        outfile.write(item + '\n')
```

3. 에러 메시지

(없음)

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
string
multiple
another
braces
one
brackets
parentheses
characters
```

- 테스트 케이스 2

```
with unmatched
another
mixed
of brackets
```

- 테스트 케이스 3

```
parentheses
brackets
inside
Nested
line
multiple
brackets
```