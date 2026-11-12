import argparse



#def add_parse():


def main():
    parser = argparse.ArgumentParser(prog="python -m media")
    parser.add_argument("--db", default="catalog.json")
    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add")
    add.add_argument("id")
    add.add_argument("name")
    add.add_argument("category")
    add.add_argument("year", type=int)
    add.add_argument("mediatype")
    add.add_argument("creator")
    add.add_argument("duration", type=int)
    add.set_defaults(function=add_parse)