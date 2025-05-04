0. 틀린 이유

함수의 매개변수를 잘못된 방식으로 처리하여 전역 변수 목록에 포함시킴.

1. 질문

왜 함수의 매개변수가 전역 변수로 표시되나요?

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

    if stripped.startswith('def ') and '(' in stripped:
        name = stripped[4:stripped.index('(')].strip()
        current_func = name
        params = stripped[stripped.index('(')+1:stripped.index(')')].split(',')
        for param in params:  # 매개변수를 전역 변수로 잘못 추가
            if param.strip().isidentifier():
                global_vars.add(param.strip())
        local_vars[name] = set()
        func_indent = indent + 4
        continue

    if current_func:
        if indent >= func_indent and '=' in stripped:
            var = stripped.split('=', 1)[0].strip()
            if var.isidentifier():
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
func1: 
func2: 
```

- 테스트 케이스 2

```
global_var,local_var,result,message
calculate: 
display: 
```

- 테스트 케이스 3

```
a,b,sum,product
add: 
multiply: 
```