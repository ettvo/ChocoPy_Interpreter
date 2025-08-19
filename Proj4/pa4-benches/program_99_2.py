posbuf: [int] = None
negbuf: [int] = None
stdin: str = ""
prog: str = ""


PRINTABLE_ASCII: str = "                                 !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[ ]^_`abcdefghijklmnopqrstuvwxyz{|}~'"
def putchar(c: int):
    if c == 92:
        # Bug in reference: \\ is treated as two characters, but \ fails to
        # parse since it'prog not escaped.
        print("\\"[0])
    else:
        print(PRINTABLE_ASCII[c])

def getchar(c: str) -> int:
    j: int = 32 # space; first printable character
    if c == "$":
        print("stdin EOF, exiting!")
        print(None)

    while j < len(PRINTABLE_ASCII):
        if c == PRINTABLE_ASCII[j]:
            return j
        j = j + 1

    # Abort!
    print("getchar failed; aborting!")
    print(c)
    print(None)
    return -1


def load(bufPtr: int, posbuf: [int], negbuf: [int]) -> int:
    if bufPtr >= 0:
        return posbuf[bufPtr]
    else:
        return negbuf[-bufPtr]


def store(bufPtr: int, posbuf: [int], negbuf: [int], v: int):
    if bufPtr >= 0:
        posbuf[bufPtr] = v
    else:
        negbuf[-bufPtr] = v


def expand(buf: [int], bufPtr: int) -> [int]:
    tmp: int = 0
    if bufPtr >= len(buf):
        buf = buf + buf
        tmp = bufPtr
        while tmp < len(buf):
            buf[tmp] = 0
            tmp = tmp + 1
    return buf


def do_bf(prog: str, stdin: str, posbuf: [int], negbuf: [int]):
    p: int = 0
    stdinPtr: int = 0
    progLen: int = 0
    bufPtr: int = 0
    c: str = ""
    r: int = 0
    braceCount: int = 0

    progLen = len(prog) - 1  # newline
    while p < progLen:
        c = prog[p]
        if c == "+":
            r = load(bufPtr, posbuf, negbuf)
            store(bufPtr, posbuf, negbuf, r + 1)
            p = p + 1

        elif c == "-":
            r = load(bufPtr, posbuf, negbuf)
            store(bufPtr, posbuf, negbuf, r - 1)
            p = p + 1

        elif c == "<":
            bufPtr = bufPtr - 1
            p = p + 1
            negbuf = expand(negbuf, -bufPtr)

        elif c == ">":
            bufPtr = bufPtr + 1
            p = p + 1
            posbuf = expand(posbuf, bufPtr)


        elif c == ".":
            r = load(bufPtr, posbuf, negbuf)
            putchar(r)
            p = p + 1

        elif c == ",":
            r = getchar(stdin[stdinPtr])
            store(bufPtr, posbuf, negbuf, r)
            stdinPtr = stdinPtr + 1
            p = p + 1

        elif c == "[":
            r = load(bufPtr, posbuf, negbuf)

            if r == 0:
                braceCount = 1
                while braceCount > 0:
                    p = p + 1
                    if prog[p] == "[":
                        braceCount = braceCount + 1
                    elif prog[p] == "]":
                        braceCount = braceCount - 1

            p = p + 1

        elif c == "]":
            r = load(bufPtr, posbuf, negbuf)

            if r != 0:
                braceCount = 1
                while braceCount > 0:
                    p = p - 1
                    if prog[p] == "]":
                        braceCount = braceCount + 1
                    elif prog[p] == "[":
                        braceCount = braceCount - 1

            p = p + 1

posbuf = [0, 0, 0, 0, 0, 0, 0, 0]
negbuf = [0, 0, 0, 0, 0, 0, 0, 0]

input() # read comment
prog = input()
stdin = input()
do_bf(prog, stdin, posbuf, negbuf)

