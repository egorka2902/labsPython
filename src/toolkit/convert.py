
def conv_t(val,f,t):
    if f == 'c':
        c = val
    elif f == 'f':
        c = (val - 32) * 5 / 9
    elif f == 'k':
        c = val - 273

    if t == 'c':
        return c
    elif t == 'f':
        return c * 9 / 5 + 32
    elif t == 'k':
        return c + 273

def change(f,t, val):
    length = {'mm':10**-3,'cm':10**-2,'m':10**0,'km':10**3}
    mass = {'g':1,'kg':1000}
    temp = {'c':0,'f':32,'k':273}
    if f in length and t in length:
        return float(val*length[f]/length[t])
    elif f in mass and t in mass:
        return float(val*mass[f]/mass[t])
    elif f in temp and t in temp:
        return float(conv_t(val,f,t))