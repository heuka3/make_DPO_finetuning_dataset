0. 틀린 이유

들여쓰기를 잘못 계산하여 함수 내부 변수를 전역 변수로 잘못 인식하고 있음. `len(line.lstrip()) - len(line.lstrip(' '))` 대신 `len(line) - len(line.lstrip(' '))`로 수정해야 함.

1. 질문

왜 함수 내부의 지역 변수가 전역 변수로 인식되나요?

2. 잘못된 코드

```python
global_vars = set()
local_vars = {}
current_func = None
func_indent = 0

with open('input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    indent = len(line.lstrip()) - len(line.lstrip(' '))  # 잘못된 들여쓰기 계산
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
x,y,a,b,c,d
```

- 테스트 케이스 2

```
global_var,local_var,result,message
```

- 테스트 케이스 3

```
a,b,sum,product
```