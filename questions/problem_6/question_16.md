0. 틀린 이유

괄호를 여는 문자와 닫는 문자를 잘못 처리하여, 괄호 사이의 내용이 아닌 전체 문자열을 추출하고 있습니다. 또한, 괄호의 짝을 맞추는 로직이 없어서, 괄호 사이의 내용을 정확히 추출하지 못하고 있습니다.

1. 질문

괄호 사이의 내용만 추출해야 하는데, 전체 문자열이 출력됩니다. 어떤 점을 수정해야 할까요?

2. 잘못된 코드

```python
def extract_contents(line):
    opener = set('({[')
    closer = set(')}]')

    stack = []
    results = []

    for i, ch in enumerate(line):
        if ch in opener:
            stack.append(i)
        elif ch in closer:
            start = stack.pop()
            results.append(line[start+1:i])  # 괄호 사이의 내용을 추가해야 함

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