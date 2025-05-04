0. 틀린 이유

함수의 지역 변수를 탐색할 때 문자열 안에 존재하는 변수 이름도 지역 변수로 잘못 인식하고 있음. 또한, 'return'과 같은 키워드도 변수로 잘못 인식하고 있음.

1. 질문

왜 함수 내부의 문자열에 포함된 단어들이 지역 변수로 표시되나요?

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
            elif '"' in stripped or "'" in stripped:  # 문자열 내 단어들도 잘못 처리
                words = stripped.replace('"', '').replace("'", "").split()
                for word in words:
                    if word.isidentifier():
                        local_vars[current_func].add(word)
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
func1: a,b,return,a,b
func2: c,d,return,c,d
```

- 테스트 케이스 2

```
global_var
calculate: local_var,result,return,result
display: message,print
```

- 테스트 케이스 3

```
a,b
add: sum,return,sum
multiply: product,return,product
```