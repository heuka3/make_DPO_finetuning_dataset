0. 틀린 이유

학생의 코드는 중첩된 괄호의 내용을 올바르게 처리하지 못하고, 가장 안쪽의 괄호 내용만 추출하고 있습니다. 문제에서는 중첩된 괄호의 경우 가장 안쪽부터 추출하고, 추출된 안쪽의 괄호 및 괄호 내용을 바깥 괄호에서 제외해야 합니다. 또한, 개행 문자를 제거하지 않아도 문제의 요구사항에 직접적인 영향을 주지 않습니다.

1. 질문

파일에서 줄을 읽어올 때 중첩된 괄호를 올바르게 처리하려면 어떻게 해야 하나요?

2. 잘못된 코드

```python
def extract_contents(line):
    opener = {'(': ')', '{': '}', '[': ']'}
    closer = {v: k for k, v in opener.items()}

    stack = []
    results = []

    for i, ch in enumerate(line):
        if ch in opener:
            stack.append((ch, i))
        elif ch in closer and stack and stack[-1][0] == closer[ch]:
            open_char, start = stack.pop()
            results.append(line[start+1:i].strip())

    return results

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

all_extracted = []
for line in lines:
    all_extracted.extend(extract_contents(line))  # 개행 문자 제거 없이 처리

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
curly
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