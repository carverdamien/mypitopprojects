DOT = 1
DASH = 3
SPACE_BETWEEN_DOTS_AND_DASHES = 1
SPACE_BETWEEN_LETTERS = 3
SPACE_BETWEEN_WORDS = 7
ALPHANUM2MORSE = {
    'a':[DOT,DASH],
    'b':[DASH,DOT,DOT,DOT],
    'c':[DASH,DOT,DASH,DOT],
    'd':[DASH,DOT,DOT],
    'e':[DOT],
    'f':[DOT,DOT,DASH,DOT],
    'g':[DASH,DASH,DOT],
    'h':[DOT,DOT,DOT,DOT],
    'i':[DOT,DOT],
    'j':[DOT,DASH,DASH,DASH],
    'k':[DASH,DOT,DASH],
    'l':[DOT,DASH,DOT,DOT],
    'm':[DASH,DASH],
    'n':[DASH,DOT],
    'o':[DASH,DASH,DASH],
    'p':[DOT,DASH,DASH,DOT],
    'q':[DASH,DASH,DOT,DASH],
    'r':[DOT,DASH,DOT],
    's':[DOT,DOT,DOT],
    't':[DASH],
    'u':[DOT,DOT,DASH],
    'v':[DOT,DOT,DOT,DASH],
    'w':[DOT,DASH,DASH],
    'x':[DASH,DOT,DOT,DASH],
    'y':[DASH,DOT,DASH,DASH],
    'z':[DASH,DASH,DOT,DOT],
    '1':[DOT,DASH,DASH,DASH,DASH],
    '2':[DOT,DOT,DASH,DASH,DASH],
    '3':[DOT,DOT,DOT,DASH,DASH],
    '4':[DOT,DOT,DOT,DOT,DASH],
    '5':[DOT,DOT,DOT,DOT,DOT],
    '6':[DASH,DOT,DOT,DOT,DOT],
    '7':[DASH,DASH,DOT,DOT,DOT],
    '8':[DASH,DASH,DASH,DOT,DOT],
    '9':[DASH,DASH,DASH,DASH,DOT],
    '0':[DASH,DASH,DASH,DASH,DASH]
}

def alphanum2morse(alphanum):
    for a in alphanum:
        if a == ' ':
            for i in range(SPACE_BETWEEN_WORDS):
                yield False
        elif a in ALPHANUM2MORSE:
            for symbol in ALPHANUM2MORSE[a]:
                for i in range(symbol):
                    yield True
                for i in range(SPACE_BETWEEN_DOTS_AND_DASHES):
                    yield False
            for i in range(SPACE_BETWEEN_LETTERS):
                yield False
        else:
            # Alphanum unrecognized
            continue

if __name__ == '__main__':
    import sys
    print([i for i in alphanum2morse(sys.argv[1])])
