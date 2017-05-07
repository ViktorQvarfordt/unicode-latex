#!/usr/bin/env python3

import datetime
import re

reversedJson = '{\n'

latexout = """\\ProvidesPackage{unicode-latex}[%s use unicode symbols in math input]

\\usepackage[T1]{fontenc}
\\usepackage[utf8]{inputenc}
\\usepackage{mathtools,amssymb,bm}

%% Fix font for sans-serif math.
\\DeclareMathAlphabet{\\mathss}{\\encodingdefault}{\\sfdefault}{m}{n}
\\SetMathAlphabet{\\mathss}{bold}{\\encodingdefault}{\\sfdefault}{bx}{n}

%% Fix font for sans-serif italic math.
\\DeclareMathAlphabet{\\mathssit}{\\encodingdefault}{\\sfdefault}{m}{sl}
\\SetMathAlphabet{\\mathssit}{bold}{\\encodingdefault}{\\sfdefault}{bx}{sl}

%% Fix font for ⋰ etc.
\\usepackage{mathdots}

%% Fix double-struck italic by providing the command \mathbbit.
%% The only unicode glyphs for this are ⅅ ⅆ ⅇ ⅈ ⅉ.
%% No, don't do it. Who would use it?
%%\\usepackage{bbm}
%%\\DeclareMathAlphabet{\\mathbbit}{U}{bbm}{m}{sl}

\\usepackage{newunicodechar}

""" % datetime.datetime.now().strftime("%Y/%m/%d")

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

        # LaTeX has no commands to greek symbols that look identical to the corresponding latin symbol.
        if texcmd == '\\\\Alpha':
            texcmd = 'A'
        if texcmd == '\\\\Beta':
            texcmd = 'B'
        if texcmd == '\\\\Epsilon':
            texcmd = 'E'
        if texcmd == '\\\\Zeta':
            texcmd = 'Z'
        if texcmd == '\\\\Eta':
            texcmd = 'H'
        if texcmd == '\\\\Iota':
            texcmd = 'I'
        if texcmd == '\\\\Kappa':
            texcmd = 'K'
        if texcmd == '\\\\Mu':
            texcmd = 'M'
        if texcmd == '\\\\Nu':
            texcmd = 'N'
        if texcmd == '\\\\Omicron':
            texcmd = 'O'
        if texcmd == '\\\\Rho':
            texcmd = 'P'
        if texcmd == '\\\\Tau':
            texcmd = 'T'
        if texcmd == '\\\\Chi':
            texcmd = 'X'
        if texcmd == '\\\\omicron':
            texcmd = 'o'

        # TODO: Handle sub-/superscripts
        # if texcmd[0] in '_^':
        #     ...

        symbol = symbol.replace('\\\\', '\\')
        texcmd = texcmd.replace('\\\\', '\\')
        latexout += '\\newunicodechar{%s}{\\ifmmode%%\n%s\\else%%\n%s\\fi}\n' % (symbol, texcmd, symbol)
        # TODO: Put \relax before \ifmmode https://tex.stackexchange.com/questions/197198/why-is-it-recommended-to-put-relax-before-ifmmode

reversedJson += '}\n'

with open('unicode-latex.json', 'w') as f:
    f.write(reversedJson)

with open('unicode-latex.sty', 'w') as f:
    f.write(latexout)
