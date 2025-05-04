0. 틀린 이유

괄호의 짝이 맞지 않을 때도 문자열을 추출하려고 시도해서 잘못된 값을 추출했습니다. 또한, 스택이 비어있을 때 pop을 시도하여 IndexError가 발생합니다.

1. 질문

괄호의 짝이 맞지 않을 때는 문자열을 추출하지 않도록 하려면 어떻게 해야 하나요?

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
            if open_char in opener and stack and stack[-1][0] == closer[ch]:
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

IndexError: pop from empty list

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
string
multiple
another
one
brackets
parentheses
characters
```

- 테스트 케이스 2

```
Example with no closing
Another line with unmatched
another
mixed
of brackets
```

- 테스트 케이스 3

```
parentheses
inside
line
multiple
brackets
```