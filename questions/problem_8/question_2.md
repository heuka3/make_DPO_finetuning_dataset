0. 틀린 이유

줄 바꿈 문자를 포함하지 않아서 문제가 발생함.

1. 질문

왜 output.txt 파일에 변수 목록이 줄 바꿈 없이 모두 한 줄로 붙어 나오나요?

2. 잘못된 코드

```python
global_vars = set()
local_vars = {}
current_func = None
func_indent = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()

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
            var = stripped.split('=', 1)[0]
            if var.isidentifier() and var not in global_vars:
                local_vars[current_func].add(var.strip())
            continue
        if indent < func_indent:
            current_func = None

    if current_func is None and '=' in stripped:
        var = stripped.split('=', 1)[0]
        if var.isidentifier():
            global_vars.add(var.strip())

with open('output.txt', 'w') as f:
    f.write(','.join(sorted(global_vars)) + '\n')
    for func, vars in local_vars.items():
        f.write(f"{func}: {','.join(sorted(vars))}\n")
```

3. 에러 메시지

(에러 메시지가 발생하지 않음)

4. 테스트 케이스에 대해 학생의 코드가 출력한 오답

- 테스트 케이스 1

```
x,y
func1: a,b
func2: c,d
```

- 테스트 케이스 2

```
global_var
calculate: local_var,result
display: message
```

- 테스트 케이스 3

```
a,b
add: sum
multiply: product
```