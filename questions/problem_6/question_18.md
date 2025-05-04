0. 틀린 이유

학생의 코드는 중첩된 괄호를 처리하지 않고, 가장 바깥쪽 괄호의 내용을 추출하는 방식으로 구현되어 있습니다. 따라서 중첩된 괄호의 내용이 올바르게 추출되지 않습니다.

1. 질문

중첩된 괄호를 처리할 때 문제가 생겼습니다. 어떻게 중첩된 괄호를 올바르게 처리할 수 있을까요?

2. 잘못된 코드

```python
def extract_contents(line):
    opener = set('({[')
    closer = set(')}]')

    stack = []
    results = []

    for i, ch in enumerate(line):
        if ch in opener:
            stack.append((ch, i))
        elif ch in closer:
            start = stack.pop()[1]
            if stack:
                continue
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
curly
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
inside
line
multiple
```