#!/usr/bin/env python3

import re

reversedJson = '{\n'

latexout = """\\ProvidesPackage{unicode-latex}[2017/04/30 use unicode symbols in math input]

\\usepackage[T1]{fontenc}
\\usepackage[utf8]{inputenc}
\\usepackage{mathtools,amssymb,bm,bbm,mathdots}

\\DeclareMathAlphabet{\\mathss}{\\encodingdefault}{\\sfdefault}{m}{n}
\\SetMathAlphabet{\\mathss}{bold}{\\encodingdefault}{\\sfdefault}{bx}{n}

\\DeclareMathAlphabet{\\mathssit}{\\encodingdefault}{\\sfdefault}{m}{sl}
\\SetMathAlphabet{\\mathssit}{bold}{\\encodingdefault}{\\sfdefault}{bx}{sl}

\DeclareMathAlphabet{\mathbbmsl}{U}{bbm}{m}{sl}

\\usepackage{newunicodechar}

"""
with open('./latex-unicode.json') as f:
    for line in f.readlines():

        if line[0] is not '"':
            continue

        m = re.search(r'"(.*?)":"(.*?)"', line)
        texcmd = m.group(1)
        symbol = m.group(2)

        reversedJson += '"%s":"%s",\n' % (symbol, texcmd)

        # Don't add ascii to LaTeX package
        if symbol == '\\\\' or ord(symbol) < 128:
            continue

        # Normalization
        if texcmd.startswith('\\\\mathit{'):
            m = re.search(r'\\\\mathit{(.*?)}', texcmd)
            texcmd = m.group(1)

        # TODO: Handle sub-/superscripts
        # if texcmd[0] in '_^':
        #     ...

        symbol = symbol.replace('\\\\', '\\')
        texcmd = texcmd.replace('\\\\', '\\')
        latexout += '\\newunicodechar{%s}{\\ifmmode%%\n%s\\else%%\n%s%%\n\\fi}\n' % (symbol, texcmd, symbol)
        # TODO: Put \relax before \ifmmode https://tex.stackexchange.com/questions/197198/why-is-it-recommended-to-put-relax-before-ifmmode

reversedJson += '}\n'

with open('unicode-latex.json', 'w') as f:
    f.write(reversedJson)

with open('unicode-latex.sty', 'w') as f:
    f.write(latexout)
