import argparse

# Command Line:
# python3 main.py -h
# python3 main.py
# usage: main.py [-h] -x X [-y Y] [-z Z]
# arg_demo2.py: error: the following arguments are required: -x
# python3 main.py -x something
# python3 arg_demo2.py -x something -y text
# python3 arg_demo2.py -x something -z 10
# python3 main.py --execute something (long argument)
#


def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage",
    )
    # required arguments
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-x", "--execute", action="store", required=True, help="Help text for option X"
    )
    # Optional arguments
    group.add_argument("-y", help="Help text for option Y", default=False)
    group.add_argument("-z", help="Help text for option Z", type=int)
    print(parser.parse_args())


if __name__ == "__main__":
    get_args()
