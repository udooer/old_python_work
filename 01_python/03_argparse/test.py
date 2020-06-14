from argparse import ArgumentParser
parser = ArgumentParser(prog="test.py", usage="test.py hello -n [NAME] [String]")

parser.add_argument("pos1", help="position argument 1")
parser.add_argument(help="enter the conversation", dest="sentence", type=float)
parser.add_argument("-n", help="enter your name", dest="name", default="shane")
args = parser.parse_args()
print("{}, {}, {}".format(args.pos1, args.name, args.sentence))
