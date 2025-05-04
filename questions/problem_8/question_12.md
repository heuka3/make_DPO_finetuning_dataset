0. 틀린 이유

학생의 코드는 함수 내부에서 사용된 변수를 전역 변수로 잘못 추가하고 있습니다. 문제에서는 전역 변수는 함수 외부에서 정의된 변수로 한정하고 있으며, 함수 내부에서 사용된 변수는 지역 변수로 간주해야 합니다.

1. 질문

왜 함수 내부에서 사용하는 전역 변수가 전역 변수 목록에 포함되지 않나요?

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
        if indent >= func_indent:
            if '=' in stripped:
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
    else:  # 함수 정의에서 사용된 변수도 전역 변수로 추가
        for word in stripped.split():
            if word.isidentifier() and word not in global_vars:
                global_vars.add(word)

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
func1: a,b
func2: c,d
```

- 테스트 케이스 2

```
global_var,local_var,result,message
calculate: local_var,result
display: message
```

- 테스트 케이스 3

```
a,b,sum,product
add: sum
multiply: product
```