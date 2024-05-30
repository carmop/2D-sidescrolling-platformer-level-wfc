from WFC import run
from Control import parse
from Settings import *


def main():
    """"""
    parameters=parse()

    interact = parameters['instant']
    key_press = parameters['press']
    weighted = parameters['weight']
    use_curve = parameters['ac']

    # some code for settings possibly?

    print(parameters)
    print('aight')

    if use_curve:
        set_ac()

main()