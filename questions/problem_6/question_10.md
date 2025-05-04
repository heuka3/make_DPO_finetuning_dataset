0. 틀린 이유

파일을 읽을 때 각 줄을 처리하는 대신, 전체 내용을 한 번에 처리하도록 코드를 작성하여 잘못된 결과가 나왔습니다. 또한, 중첩된 괄호의 경우 가장 안쪽부터 추출해야 하는데, 이 부분이 제대로 구현되지 않았습니다.

1. 질문

파일의 내용을 전체가 아닌 줄 단위로 처리해야 하는데, 어떻게 하면 될까요?

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
    content = infile.read()  # 파일 전체를 읽어버림

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