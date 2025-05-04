0. 틀린 이유

학생의 코드는 괄호의 짝이 맞지 않아도 추출하도록 작성되어 문제가 발생했습니다. 스택이 비어있을 때 pop을 시도하거나, 짝이 맞지 않는 경우에도 결과에 추가하는 로직이 문제입니다.

1. 질문

짝이 맞지 않는 괄호의 경우는 제외하고 싶습니다. 어떻게 코드를 수정해야 할까요?

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
        elif ch in closer:
            open_char, start = stack.pop() if stack else ('', -1)
            if open_char in opener:  # 짝이 안 맞아도 추가함
                results.append(line[start+1:i].strip())

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
curly {braces
one
brackets
parentheses
characters
```

- 테스트 케이스 2

```
Example with no closing
with unmatched
another
mixed
of brackets
```

- 테스트 케이스 3

```
parentheses
inside [brackets
line
multiple
brackets
```