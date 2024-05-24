import argparse

def parse():
    """"""

    par = argparse.ArgumentParser()

    par.add_argument('--press', action='store_true')
    par.add_argument('--no-press', dest='press', action='store_false')
    par.set_defaults(press=False)

    par.add_argument('--weight', action='store_true')
    par.add_argument('--no-weight', dest='weight', action='store_false')
    par.set_defaults(weight=False)

    par.add_argument('--ac', action='store_true')
    par.add_argument('--no-ac', dest='ac', action='store_false')
    par.set_defaults(ac=False)

    par.add_argument('--flash', action='store_false', dest='instant')
    par.add_argument('--no-flash', dest='instant', action='store_true')
    par.set_defaults(instant=True)

    par.add_argument('levels', nargs='?', default=1, type=int)
    par.add_argument('length', nargs='?', default=10, type=int)
    


    parameter_dict=vars(par.parse_args())

    return parameter_dict