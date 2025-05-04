0. 틀린 이유

코드에서 함수 이름을 제대로 추출하지 못해서 모든 라인이 전역 변수로만 처리되고 있음. 함수 이름 추출 시 `stripped.split('def ')[-1].split('(')[0]` 부분이 잘못되어 함수 이름을 정확히 가져오지 못하고 있음.

1. 질문

왜 함수 내부의 지역 변수가 함수 이름 없이 모두 전역 변수로 처리되나요?

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
        current_func = stripped.split('def ')[-1].split('(')[0]  # 함수 이름 추출이 잘못됨
        local_vars[current_func] = set()
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