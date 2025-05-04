0. 틀린 이유

괄호 안의 내용을 추출할 때, 줄에서 모든 괄호 쌍을 찾는 대신 첫 번째 괄호 쌍만 추출해서 더 이상 진행하지 않기 때문에 발생한 문제입니다. break 문이 잘못 사용되어 모든 쌍을 처리하지 못하고 있습니다.

1. 질문

텍스트 줄에서 모든 괄호 쌍을 처리해야 하는데, 제 코드에서는 첫 번째 쌍만 추출하고 끝납니다. 어떻게 모든 쌍을 처리할 수 있을까요?

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
            break  # 잘못된 부분: 첫 번째 쌍 처리 후 종료

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
another
one
characters
```

- 테스트 케이스 2

```
with unmatched
another
mixed
```

- 테스트 케이스 3

```
parentheses
if unmatched
line
```