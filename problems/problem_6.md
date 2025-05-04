1. 과제 문제

괄호 내 문자열 추출 (파일 입출력)

2. 문제 설명

input.txt 파일에는 여러 줄로 구성된 텍스트가 저장되어 있다. 이 텍스트에서 소괄호 (), 중괄호 {}, 대괄호 []의 짝이 맞는 부분을 찾아, 그 안의 문자열을 추출하여 output.txt 파일에 행 별로 저장하는 프로그램을 작성하시오. 추출된 문자열은 원래의 줄 순서를 유지해야 하며, 각 줄의 끝에는 줄바꿈 문자가 포함될 수 있다. 괄호가 중첩되는 경우 가장 안쪽의 괄호 내용부터 추출하며, 추출된 안쪽의 괄호 및 괄호 내용은 바깥 괄호에서 추출하는 문자열에서 제외한다.

3. 입력 형식 (input.txt)

여러 줄의 문자열이 주어짐
각 줄의 길이는 1 이상 1,000 이하
문자열의 총 길이는 1,000 이하
문자열에는 알파벳, 숫자, 특수문자, 공백 등이 포함될 수 있음

4. 출력 형식 (output.txt)

각 괄호의 짝에 맞는 경우 안의 문자열을 줄 별로 출력

5. 테스트 케이스

- 테스트 케이스 1

input.txt
```txt
This is a test (string) with (multiple) parentheses.
Here is {another} example with {curly {braces}}.
This [one] has [brackets] and (parentheses).
No special (characters) here.
```

output.txt
```txt
string
multiple
another
braces
curly
one
brackets
parentheses
characters
```

- 테스트 케이스 2

input.txt
```txt
Example with (no closing
Another line {with unmatched}
Yet [another] with (mixed) types {of brackets}.
```

output.txt
```txt
with unmatched
another
mixed
of brackets
```

- 테스트 케이스 3

input.txt
```txt
(Nested (parentheses) {inside [brackets]})
Ignore this one (if unmatched
A single (line) with {multiple} [brackets].
```

output.txt
```txt
parentheses
brackets
inside
Nested
line
multiple
brackets
```

6. 파이썬 코드 정답

```python
def extract_contents(line):
    """
    한 줄에서 모든 괄호 쌍을 찾되,
    - 중첩된 가장 안쪽부터 처리(order 유지)
    - 각 괄호 쌍에 대해, 그 안에 또다른 괄호 영역은 **아예 제외**하고 남은 텍스트만 반환
    """
    opener = {'(': ')', '{': '}', '[': ']'}
    closer = {v: k for k, v in opener.items()}

    stack = []   # 스택에 (open_char, start_index)
    matches = [] # 발견된 매치들의 리스트: dict(start, end)

    # 1) 매치 위치 찾아 저장
    for i, ch in enumerate(line):
        if ch in opener:
            stack.append((ch, i))
        elif ch in closer and stack and stack[-1][0] == closer[ch]:
            open_char, start = stack.pop()
            matches.append({'start': start, 'end': i})

    # 2) 매치된 순서대로(안쪽→바깥쪽) content 추출
    results = []
    for m in matches:
        s, e = m['start'], m['end']
        # line[s+1:e] 에서, 내부의 다른 괄호 매치 영역들은 전부 제외
        # 그럴 interval 리스트 계산
        inner_intervals = [
            (n['start'], n['end'])
            for n in matches
            if n['start'] > s and n['end'] < e
        ]
        # 중첩 영역 정렬
        inner_intervals.sort()
        # 제외하고 남는 부분만 이어붙이기
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

# --- 파일 입출력 부분 --- #

with open('input.txt', 'r') as infile:
    lines = infile.readlines()

all_extracted = []
for line in lines:
    # 줄 끝 개행 제거하고 처리
    all_extracted.extend(extract_contents(line.rstrip('\n')))

with open('output.txt', 'w') as outfile:
    for item in all_extracted:
        outfile.write(item + '\n')
```