from WFC import run
from Control import parse


def main():
    """Function for handling argparse inputs for level generation and calling level generator."""

    parameters=parse()

    interact = parameters['progress']
    key_press = parameters['press']
    weighted = parameters['weight']
    use_curve = parameters['ac']

    levels = parameters['levels']
    save = parameters['save']

    print('Generation Using Following Parameters:')
    # print(parameters)
    for item in parameters:
        print(item,':',parameters[item])

    run(levels, weighted, use_curve, interact, key_press, save)


main()