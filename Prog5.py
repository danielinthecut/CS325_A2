import argparse

def test():
    parser = argparse.ArgumentParser()

    parser.add_argument(help="Enter the full path to your file now: ", dest='input_path', type=str)
    parser.add_argument(help="Enter an integer value now: ", dest='number', type=int)
    parser.add_argument(help="Enter a float value now: ", dest='float', type=float)

    args = parser.parse_args()

    path = args.input_path
    number = args.number
    float = args.float

    print("Path: ", path, "Number: ", number, "Float: ", float)

