import re
import argparse


def calc_direction(floor_string, val):
    indx = [ind.start() for ind in re.finditer(val, floor_string)]
    return indx


def santa_floor(floor_string):
    up = len(calc_direction(floor_string, "\("))
    down = len(calc_direction(floor_string, "\)"))
    print(f"Santa goes to floor {up - down}")


def basement_floor_index(floor_string):
    basement = 0
    up = calc_direction(floor_string, "\(")
    down = calc_direction(floor_string, "\)")
    for i, x in enumerate(floor_string):
        if i in up: 
            basement += 1
        else: 
            basement -= 1
        if basement == -1:
            return i+1


def basement(floor_string):
    ind = basement_floor_index(floor_string)
    print(f"Santa goes to the basement at index {ind}")


def main(args):
    santa_floor(args.floor_string)
    basement(args.floor_string)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest='floor_string', required=True, help='Santa\'s paranthesis floor string. Pass in with surronding double quotes.')
    args = parser.parse_args()
    main(args)