0. 틀린 이유

학생의 코드는 조건문이나 반복문 내에서 정의된 변수를 지역 변수로 인식하지 못하는 문제가 있습니다. 이는 학생 코드에서 '=' 연산자를 포함한 줄을 처리할 때, 조건문이나 반복문을 시작하는 줄을 제외하도록 설정했기 때문입니다. 따라서 조건문이나 반복문 내에서 정의된 변수도 지역 변수로 인식되도록 수정이 필요합니다.

1. 질문

왜 조건문이나 반복문 안에서 정의된 변수들이 지역 변수로 인식되지 않나요?

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
        if indent >= func_indent and '=' in stripped and not stripped.startswith(('if', 'for', 'while')):
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