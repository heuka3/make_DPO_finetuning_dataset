0. 틀린 이유

파일을 열고 닫는 과정에서 close()를 호출하지 않아서 ResourceWarning이 발생할 수 있지만, 이는 코드의 논리적 오류와는 무관하다. 학생의 코드가 제대로 실행되지 않는 이유는 파일을 닫지 않아서가 아니라, output.txt에 저장되는 줄의 순서가 문제의 요구사항과 다르기 때문이다. 학생의 코드는 matched_lines를 set으로 사용하여 줄의 순서를 보장하지 않는다.

1. 질문

왜 제 코드가 제대로 실행되지 않나요? 파일을 읽고 쓴 후에 close()를 호출하지 않아서 문제가 되는 걸까요?

2. 잘못된 코드

```python
infile = open('input.txt', 'r')
lines = infile.readlines()
keywords = set(lines[0].strip().lower().split())
text_lines = lines[1:]

matched_lines = set()

for line in text_lines:
    lower_line = line.strip().lower()
    if any(keyword in lower_line for keyword in keywords):
        matched_lines.add(line.strip())

outfile = open('output.txt', 'w')
for matched_line in matched_lines:
    outfile.write(matched_line + '\n')
```

3. 에러 메시지

```
ResourceWarning: unclosed file <file>
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
This is an apple.
Bananas are great!
I love orange juice.
```

- 테스트 케이스 2

```
The quick brown fox jumps over the lazy dog.
Cats are independent animals.
Dogs are loyal.
```

- 테스트 케이스 3

```
I love to code in Python.
AI is the future.
Machine learning is a subset of AI.
```