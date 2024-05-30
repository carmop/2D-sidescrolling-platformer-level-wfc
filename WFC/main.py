from WFC import run
from Control import parse


def main():
    """"""
    parameters=parse()

    interact = parameters['instant']
    key_press = parameters['press']
    weighted = parameters['weight']
    use_curve = parameters['ac']

    levels = parameters['levels']
    save = parameters['save']

    # some code for settings possibly?

    print(parameters)
    print('aight')

    run(levels, weighted, use_curve, interact, key_press, save)


main()