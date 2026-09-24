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

