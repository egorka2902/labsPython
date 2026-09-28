class convErr(Exception):
    pass

def conv_t(val,f,t):
    if f == 'c':
        c = val
    elif f == 'f':
        c = (val - 32) * 5 / 9
    elif f == 'k':
        c = val - 273.15

    if t == 'c':
        if c >= -273.15: return c
        if c < -273.15: raise convErr("ниже абсолютного нуля")
    elif t == 'f':
        if c >= -459.67: return (c * 9 / 5 + 32)
        if c < -459.67: raise convErr("ниже абсолютного нуля")
    elif t == 'k':
        if c >= 0 :return c + 273
        if c < 0: raise convErr("ниже абсолютного нуля")

def change(f,t, val):
    length = {'mm':10**-3,'cm':10**-2,'m':10**0,'km':10**3}
    mass = {'g':1,'kg':1000}
    temp = {'c':0,'f':32,'k':273.15}
    if f in length and t in length:
        if val >= 0 : return float(val*length[f]/length[t])
        if val < 0: raise convErr("Отрицательное значение не поддерживается")
    elif f in mass and t in mass:
        if val >= 0: return float(val*mass[f]/mass[t])
        if val < 0: raise convErr("Отрицательное значение не поддерживается")
    elif f in temp and t in temp:
        return float(conv_t(val,f,t))
    else:
        raise convErr('ошибка в единицах измерения')