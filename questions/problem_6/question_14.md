0. 틀린 이유

학생의 코드는 중첩된 괄호를 처리할 때 바깥쪽 괄호부터 추출하고 있습니다. 문제에서는 중첩된 괄호의 가장 안쪽부터 추출해야 하며, 안쪽의 괄호 및 내용을 바깥 괄호에서 제외해야 합니다. 따라서 학생의 코드는 문제의 요구사항을 충족하지 못하고 있습니다.

1. 질문

중첩된 괄호를 처리할 때 바깥쪽부터 추출하고 있는 것 같습니다. 어떻게 안쪽부터 추출할 수 있을까요?

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
            if not stack:  # 바깥쪽부터 추출
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
another
one
characters
```

- 테스트 케이스 2

```
with unmatched
another
```

- 테스트 케이스 3

```
Nested
brackets
```