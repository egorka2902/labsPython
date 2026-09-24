import re

class CalcErr(Exception):
    pass

def tok(s: str):
    s = s.replace(' ','')
    p = re.compile(r'\d+(?:\.\d+)?|[+\-*/]')
    if not s:
        raise CalcErr("пустое выражение")
    toks = p.findall(s)
    if len(''.join(toks)) != len(s):
        raise CalcErr("че за символы")

    un_toks = []
    for i, t in enumerate(toks):
        if t in('+','-'):
            is_un = (i == 0) or (toks[i-1] in ('+','-','/','*'))
            if is_un:
                un_toks.append(f"u{t}")
            else:
                un_toks.append(t)
        else:
            un_toks.append(t)
    return un_toks

def validate(toks):
    j = ('+','-','/','*')
    if not toks:
        raise CalcErr("пустой список токенов")
    if toks[-1] in j:
        raise CalcErr("в конце выражения оператор")
    for i in range(0,len(toks)-1):
        if toks[i] in j and toks[i+1] in j:
            raise CalcErr(f"два оператора рядом: {tok[i]} и {tok[i+1]}")
def calc(expr) -> float:
    toks = tok(expr)
    validate(toks)
    prior = {'u+':3,'u-':3,'*':2,'/':2,'+':3,'-':3}
    out,st = [],[]
    for t in toks:
        if t not in prior:
            out.append(t)
        else:
            while st and prior.get(st[-1],0) >= prior[t] and not (t[0] == 'u') and (st[-1])[0] == 'u':
                out.append(st.pop())
            st.append(t)

    out += st[::-1]
    stack = []
    for t in out:
        if t[0] == 'u':
            a = stack.pop()
            stack.append(-a if t == 'u-' else a)
        elif t in '+-/*':
            b,a = stack.pop(),stack.pop()
            if t == '+': stack.append(a+b)
            if t == '-': stack.append(a-b)
            if t == '*': stack.append(a*b)
            if t == '/':
                if b == 0: raise CalcErr('деление на 0')
                stack.append(a/b)
        else:
            stack.append(float(t))
    if len(stack) != 1:
        raise CalcErr('неправильно выражение')
    return stack[0]

a = input()
print(calc(a))
                        
                        