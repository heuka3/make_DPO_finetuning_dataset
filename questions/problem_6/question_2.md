0. 틀린 이유

괄호 안의 문자열을 추출할 때, 중첩된 괄호가 있을 경우 가장 안쪽부터 처리해야 하지만 이를 구현하지 않았습니다. 학생의 코드는 중첩된 괄호를 고려하지 않고, 가장 바깥쪽 괄호 쌍만을 처리합니다.

1. 질문

중첩된 괄호를 처리할 때 가장 안쪽부터 추출해야 하는데, 어떻게 구현해야 할까요?

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
with unmatched
another
mixed
of brackets
```

- 테스트 케이스 3

```
parentheses
inside [brackets
if unmatched
line
multiple
brackets
```