0. 틀린 이유

괄호의 짝이 맞는지 확인하는 조건을 잘못 작성해서 에러가 발생했습니다. `stack[-1][0] == ch` 대신 `stack[-1][0] == closer[ch]`로 수정해야 합니다.

1. 질문

괄호 짝이 맞는지 확인할 때 조건이 잘못된 것 같습니다. 현재 코드를 어떻게 수정해야 할까요?

2. 잘못된 코드

```python
def extract_contents(line):
    opener = {'(': ')', '{': '}', '[': ']'}
    closer = {v: k for k, v in opener.items()}

    stack = []
    matches = []

    for i, ch in enumerate(line):
        if ch in opener:
            stack.append((ch, i))
        elif ch in closer:
            if stack and stack[-1][0] == ch:  # 잘못된 조건: closer[ch]가 아닌 ch와 비교
                open_char, start = stack.pop()
                matches.append({'start': start, 'end': i})

    results = []
    for m in matches:
        s, e = m['start'], m['end']
        inner_intervals = [
            (n['start'], n['end'])
            for n in matches
            if n['start'] > s and n['end'] < e
        ]
        inner_intervals.sort()
        buf = []
        idx = s + 1
        for a, b in inner_intervals:
            buf.append(line[idx:a])
            idx = b + 1
        buf.append(line[idx:e])
        extracted = ''.join(buf).strip()
        if extracted:
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
line
multiple
brackets
```