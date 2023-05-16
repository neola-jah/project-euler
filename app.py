import argparse
from programs import euler_p1, euler_p2


def main_switch(no, inputs):
    if no == 1:
        return euler_p1(inputs[0])
    if no == 2:
        return euler_p2()
    return 0

parser = argparse.ArgumentParser(description='Process Euler challenges program')
parser.add_argument('no', help='an integer for the number of the challenge', type=int)
parser.add_argument('--inputs', '-i', nargs='+', type=int, help='get the inputs')

args = parser.parse_args()

print(f'Program n°{args.no}')


print(f'Inputs: {args.inputs}')

print('Results: {%d}'%(main_switch(args.no, args.inputs)))