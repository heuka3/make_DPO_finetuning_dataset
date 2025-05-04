1. 과제 문제

파이썬 코드에서 전역 변수와 함수 내 변수를 구분하기 (파일 입출력)

2. 문제 설명

input.txt 파일에는 여러 개의 함수가 포함된 파이썬 코드가 저장되어 있다. 이 코드에서 전역 변수와 각 함수 내부에서 사용하는 변수를 구분하여 각각의 목록을 output.txt 파일에 저장하는 프로그램을 작성하시오. 각 줄의 끝에는 줄바꿈 문자가 포함될 수 있으며, 변수명은 알파벳, 숫자, 밑줄(_)로만 구성된다. 전역 변수는 함수 밖에서 정의된 변수이며, 함수 내에서 정의된 변수를 지역 변수로 간주한다.

3. 입력 형식 (input.txt)

여러 줄의 파이썬 코드가 주어짐
각 줄의 길이는 1 이상 200 이하
문자열의 총 길이는 1,000 이하
코드에는 함수 정의, 변수 할당, 연산자 등이 포함될 수 있음

4. 출력 형식 (output.txt)

첫 번째 줄에 전역 변수들의 이름을 쉼표로 구분하여 출력
두 번째 줄부터 각 함수명에 대해 그 함수의 지역 변수들을 쉼표로 구분하여 출력

5. 테스트 케이스

- 테스트 케이스 1

input.txt
```python
x = 10
y = 20

def func1():
    a = 1
    b = 2
    return a + b

def func2():
    c = 3
    d = 4
    return c * d
```

output.txt
```txt
x,y
func1: a,b
func2: c,d
```

- 테스트 케이스 2

input.txt
```python
global_var = 100

def calculate():
    local_var = 10
    result = global_var + local_var
    return result

def display():
    message = "Hello, World!"
    print(message)
```

output.txt
```txt
global_var
calculate: local_var,result
display: message
```

- 테스트 케이스 3

input.txt
```python
a = 5
b = 10

def add():
    sum = a + b
    return sum

def multiply():
    product = a * b
    return product
```

output.txt
```txt
a,b
add: sum
multiply: product
```

6. 파이썬 코드 정답

```python
# input.txt 읽어서 전역/지역 변수 분리 후 output.txt에 쓰기

# 1) 데이터 구조 초기화
global_vars = set()
local_vars = {}     # { 함수명: set(지역변수들) }
current_func = None # 현재 보고 있는 함수명
func_indent = 0     # 함수 몸체의 들여쓰기 기준(스페이스 수)

# 2) 파일 읽기
with open('input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    # 원본 라인 그대로 들여쓰기 계산
    indent = len(line) - len(line.lstrip(' '))
    stripped = line.strip()

    # --- 함수 정의 시작 ---
    if stripped.startswith('def ') and stripped.endswith('):'):
        # def funcname():
        name = stripped[4:stripped.index('(')].strip()
        current_func = name
        local_vars[name] = set()
        func_indent = indent + 4  # 보통 함수 몸체는 def보다 +4 스페이스
        continue

    # --- 함수 내부 처리 ---
    if current_func:
        # 아직 함수 블록 안이라면
        if indent >= func_indent and '=' in stripped:
            var = stripped.split('=', 1)[0].strip()
            # 유효한 식별자면서, 전역 변수로 미리 등록된 이름이 아니면 지역으로 추가
            if var.isidentifier() and var not in global_vars:
                local_vars[current_func].add(var)
            continue
        # 들여쓰기가 함수 블록 밖으로 내려가면 종료
        if indent < func_indent:
            current_func = None

    # --- 최상위 전역 처리 ---
    if current_func is None and stripped and '=' in stripped:
        # 최상위 할당문
        var = stripped.split('=', 1)[0].strip()
        if var.isidentifier():
            global_vars.add(var)

# 3) 결과 출력
with open('output.txt', 'w') as f:
    # 전역 변수 (알파벳 순)
    f.write(','.join(sorted(global_vars)) + '\n')
    # 함수별 지역 변수
    for func, vars in local_vars.items():
        f.write(f"{func}: {','.join(sorted(vars))}\n")
```