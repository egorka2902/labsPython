from argparse import *
import toolkit.calculator as calculator
import toolkit.convert as convert
import re

def calc_exp(args):
    try:
        print(calculator.calc(args.expression))
    except Exception as err:
        print(err, type(err))

def conv_expr(args):
    try:
        print(convert.change(args.f,args.t, args.value))
    except Exception as err:
        print(err)

def main():
    parser = ArgumentParser(prog="toolkit")

    sub = parser.add_subparsers(dest='command', help='доступные команды')

    calc_p = sub.add_parser("calc",help="решить пример")
    calc_p.add_argument("expression", type=str,help="выражение")
    calc_p.set_defaults(func=calc_exp)

    conv_p = sub.add_parser("convert",help="конвертация(длина,масса,температура)")
    conv_p.add_argument("value", type = float)
    conv_p.add_argument("--from",dest='f', type = str,required=True)
    conv_p.add_argument("--to", dest='t', type = str,required=True)
    conv_p.set_defaults(func=conv_expr)
    args= parser.parse_args()

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
    

if __name__ == '__main__':
    print('test')
    main()