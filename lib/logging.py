import numpy

def print_info(title, x, N=5):
    SEP = ""
    END = ""

    ANSI_CYAN = '\033[36m' # https://stackoverflow.com/a/54955094
    ANSI_RESET = '\033[0m'
    print(ANSI_CYAN, title, ANSI_RESET, sep=SEP, end=END)

    if isinstance(x, numpy.ndarray):
        length = len(x)
        if length > N:
            print(ANSI_CYAN, "[:", N, "]", ANSI_RESET, sep=SEP, end=END)
            print(": ", x[:N], ", ", sep=SEP, end=END)
            print(ANSI_CYAN, "[-", N, ":]", ANSI_RESET, sep=SEP, end=END)
            print(": ", x[-N:], ", ", sep=SEP, end=END)
            print(ANSI_CYAN, "length", ANSI_RESET, sep=SEP, end=END)
            print(": ", length, sep=SEP)
        else:
            print(": ", x, sep=SEP)
    else:
        # isinstance(x, numpy.float64) or isinstance(x, float):
        print(": ", x, sep=SEP)

