import argparse
def parser_args_test():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbpse", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")
    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")
    # parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="count", default=0)
    args = parser.parse_args()
    answer = args.square ** 2
    # if(args.verbosity >= 2):
    #     print("the sqaure of {} equals {}".format(args.square, answer))
    # elif(args.verbosity >= 1):
    #     print("{} ^ 2 == {}".format(args.square, answer))
    if(args.quiet):
        print(answer)
    elif(args.verbose):
        print("{} to the power {} equals {}".format(args.x, args.y, answer))
    else:
        print("{} ^ {} == {}".format(args.x, args.y, answer))
    # print(args.square ** 2)
    # print('locals:', locals())
    # print('globals:', globals())
parser_args_test()
