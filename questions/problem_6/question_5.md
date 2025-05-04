0. 틀린 이유

괄호의 짝을 찾았을 때 해당 내용을 추출하지 않고, 전체 문자열을 그대로 추가하는 실수를 했습니다. 각 괄호 쌍의 내부 문자열을 추출해야 합니다.

1. 질문

괄호 안의 내용만 추출해야 하는데, 전체 문자열이 출력됩니다. 어떻게 해야 하나요?

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
            results.append(line)  # 잘못된 부분: 전체 라인을 추가함

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
This is a test (string) with (multiple) parentheses.
Here is {another} example with {curly {braces}}.
This [one] has [brackets] and (parentheses).
No special (characters) here.
```

- 테스트 케이스 2

```
Example with (no closing
Another line {with unmatched}
Yet [another] with (mixed) types {of brackets}.
```

- 테스트 케이스 3

```
(Nested (parentheses) {inside [brackets]})
Ignore this one (if unmatched
A single (line) with {multiple} [brackets].
```