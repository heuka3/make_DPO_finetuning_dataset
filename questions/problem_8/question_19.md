0. 틀린 이유

변수 이름을 추출할 때 strip()을 사용하지 않아 변수명 앞뒤에 불필요한 공백이 포함됨.

1. 질문

왜 output.txt에 변수 이름이 공백 때문에 잘못 나왔나요?

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
            var = stripped.split('=', 1)[0]  # strip()을 사용하지 않음
            if var.isidentifier() and var not in global_vars:
                local_vars[current_func].add(var)
            continue
        if indent < func_indent:
            current_func = None

    if current_func is None and '=' in stripped:
        var = stripped.split('=', 1)[0]  # strip()을 사용하지 않음
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
x ,y 
func1: a ,b 
func2: c ,d 
```

- 테스트 케이스 2

```
global_var 
calculate: local_var ,result 
display: message 
```

- 테스트 케이스 3

```
a ,b 
add: sum 
multiply: product 
```