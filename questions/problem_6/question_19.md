0. 틀린 이유

학생의 코드는 괄호 안의 문자열을 추출할 때 중첩된 괄호의 내용을 제외하지 않고, 모든 괄호 쌍의 내용을 추출하여 잘못된 결과를 출력합니다.

1. 질문

저는 괄호 안의 문자열을 추출하는 중입니다. 하지만 중첩된 괄호의 내용을 제외하지 않고 모든 괄호 쌍의 내용을 추출합니다. 이를 수정하려면 어떻게 해야 하나요?

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
            extracted = line[start+1:i]  # 중첩된 괄호 내용 제외 없이 포함
            results.append(extracted)

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
curly {braces}
braces
one
brackets
parentheses
characters
```

- 테스트 케이스 2

```
no closing
with unmatched
another
mixed
of brackets
```

- 테스트 케이스 3

```
Nested (parentheses) {inside [brackets]}
parentheses
inside [brackets]
brackets
line
multiple
brackets
```