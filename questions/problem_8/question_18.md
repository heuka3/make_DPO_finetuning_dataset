0. 틀린 이유

파일을 읽고 쓸 때 경로가 잘못되어 파일 입출력 에러가 발생함.

1. 질문

왜 input.txt와 output.txt 파일을 열 때 에러가 발생하나요?

2. 잘못된 코드

```python
global_vars = set()
local_vars = {}
current_func = None
func_indent = 0

try:
    with open('inputs.txt', 'r') as f:  # 잘못된 파일명
        lines = f.readlines()
except FileNotFoundError:
    print("Input file not found")

for line in lines:
    indent = len(line) - len(line.lstrip(' '))
    stripped = line.strip()

    if stripped.startswith('def ') and stripped.endswith('):'):
        name = stripped[4:stripped.index('(')].strip()
        current_func = name
        local_vars[name] = set()
        func_indent = indent + 4
        continue

    if current_func:
        if indent >= func_indent and '=' in stripped:
            var = stripped.split('=', 1)[0].strip()
            if var.isidentifier() and var not in global_vars:
                local_vars[current_func].add(var)
            continue
        if indent < func_indent:
            current_func = None

    if current_func is None and '=' in stripped:
        var = stripped.split('=', 1)[0].strip()
        if var.isidentifier():
            global_vars.add(var)

try:
    with open('output.txt', 'w') as f:
        f.write(','.join(sorted(global_vars)) + '\n')
        for func, vars in local_vars.items():
            f.write(f"{func}: {','.join(sorted(vars))}\n")
except IOError:
    print("Error writing to output file")
```

3. 에러 메시지

```
Input file not found
```

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

(출력이 없음)

- 테스트 케이스 2

(출력이 없음)

- 테스트 케이스 3

(출력이 없음)