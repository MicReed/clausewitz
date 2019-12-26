import tokenize

from clausewitz.tokenize import prepare


def test_prepare(sample):
    expected = b'''\
a = { x """y""" }
b= 0
c =1
d=-2.1
e = """hello
worl\\"d"""
'''

    readline = prepare(sample)
    for line in expected.splitlines(keepends=True):
        assert readline() == line
    assert readline() == b''


def test_tokenize(sample):
    expected = (
        (tokenize.ENCODING, 'utf-8'),

        (tokenize.NAME, 'a'),
        (tokenize.OP, '='),
        (tokenize.OP, '{'),
        (tokenize.NAME, 'x'),
        (tokenize.STRING, '"""y"""'),
        (tokenize.OP, '}'),
        (tokenize.NEWLINE, '\n'),

        (tokenize.NAME, 'b'),
        (tokenize.OP, '='),
        (tokenize.NUMBER, '0'),
        (tokenize.NEWLINE, '\n'),

        (tokenize.NAME, 'c'),
        (tokenize.OP, '='),
        (tokenize.NUMBER, '1'),
        (tokenize.NEWLINE, '\n'),

        (tokenize.NAME, 'd'),
        (tokenize.OP, '='),
        (tokenize.OP, '-'),
        (tokenize.NUMBER, '2.1'),
        (tokenize.NEWLINE, '\n'),

        (tokenize.NAME, 'e'),
        (tokenize.OP, '='),
        (tokenize.STRING, '"""hello\nworl\\"d"""'),
        (tokenize.NEWLINE, '\n'),

        (tokenize.ENDMARKER, ''),
    )

    tokens = tokenize.tokenize(prepare(sample))
    for t, s in expected:
        token = next(tokens)
        assert token.type == t
        assert token.string == s

    assert tuple(tokens) == ()
