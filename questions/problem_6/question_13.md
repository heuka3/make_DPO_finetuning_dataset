0. 틀린 이유

괄호의 내용 추출 시 공백을 제거하지 않아서, 공백이 포함된 결과를 출력했습니다. 또한, 중첩된 괄호의 내용을 올바르게 처리하지 못하고 있습니다.

1. 질문

괄호 안의 내용을 추출할 때 앞뒤 공백을 제거해야 하는데, 어떻게 해야 하나요? 그리고 중첩된 괄호를 올바르게 처리하려면 어떻게 해야 하나요?

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
            results.append(line[start+1:i].strip())  # 공백 제거 추가

    return results

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

all_extracted = []
for line in lines:
    all_extracted.extend(extract_contents(line.rstrip('\n')))

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