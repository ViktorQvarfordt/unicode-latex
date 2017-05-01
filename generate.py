#!/usr/bin/env python3

import re

json1 = '{\n'
json2 = '{\n'
latexout = """\\ProvidesPackage{unicode-latex}[2017/04/30 use unicode symbols in math input]

\\usepackage[T1]{fontenc}
\\usepackage[utf8]{inputenc}
\\usepackage{amsmath,amssymb,bm,bbm}

\\DeclareMathAlphabet{\\mathss}{\\encodingdefault}{\\sfdefault}{m}{n}
\\SetMathAlphabet{\\mathss}{bold}{\\encodingdefault}{\\sfdefault}{bx}{n}

\\DeclareMathAlphabet{\\mathssit}{\\encodingdefault}{\\sfdefault}{m}{sl}
\\SetMathAlphabet{\\mathssit}{bold}{\\encodingdefault}{\\sfdefault}{bx}{sl}

\DeclareMathAlphabet{\mathbbmsl}{U}{bbm}{m}{sl}

\\usepackage{newunicodechar}

"""

with open('./unicode-math-table.tex') as f:
    for line in f.readlines():

        m = re.search(r'{"(.*?)}{(.*?)[ }]', line)
        char = chr(int(m.group(1), 16))
        texcmd = m.group(2)

        texcmd = re.sub(r'\\mup(.*)', r'\\\1', texcmd)

        # \BbbA ↦ \mathbb{A}
        if texcmd.startswith('\\Bbb'):
            inner = texcmd[4:]
            if len(inner) > 1:
                texcmd = '\\mathbb{\\%s}' % inner
            else:
                texcmd = '\\mathbb{%s}' % inner

        # \mbfitsansA ↦ \bm{\mathssit{A}}
        if texcmd.startswith('\\mbfitsans'):
            inner = texcmd[10:]
            if len(inner) > 1:
                texcmd = '\\bm{\\mathssit{\\%s}}' % inner
            else:
                texcmd = '\\bm{\\mathssit{%s}}' % inner

        # \mbfitA ↦ \mathbf{A}
        if texcmd.startswith('\\mbfit'):
            inner = texcmd[6:]
            if len(inner) > 1:
                texcmd = '\\bm{\\%s}' % inner
            else:
                texcmd = '\\bm{%s}' % inner

        # \mbfscrA ↦ \mathbf{\mathfrak{A}}
        if texcmd.startswith('\\mbfscr'):
            inner = texcmd[7:]
            if len(inner) > 1:
                texcmd = '\\bm{\\mathcal{\\%s}}' % inner
            else:
                texcmd = '\\bm{\\mathcal{%s}}' % inner

        # \mbffrakA ↦ \mb{\mathfrak{A}}
        if texcmd.startswith('\\mbffrak'):
            inner = texcmd[8:]
            if len(inner) > 1:
                texcmd = '\\bm{\\mathfrak{\\%s}}' % inner
            else:
                texcmd = '\\bm{\\mathfrak{%s}}' % inner

        # \mbfsansA ↦ \mb{\mathsans{A}}
        if texcmd.startswith('\\mbfsans'):
            inner = texcmd[8:]
            if len(inner) > 1:
                texcmd = '\\bm{\\mathss{\\%s}}' % inner
            else:
                texcmd = '\\bm{\\mathss{%s}}' % inner

        # \mitBbbA ↦ \mathit{\mathbb{A}}
        if texcmd.startswith('\\mitBbb'):
            inner = texcmd[7:]
            if len(inner) > 1:
                texcmd = '\\mathbbit{\\%s}' % inner
            else:
                texcmd = '\\mathbbit{%s}' % inner

        # \mscrA ↦ \mathcal{A}
        if texcmd.startswith('\\mscr'):
            inner = texcmd[5:]
            if len(inner) > 1:
                texcmd = '\\mathcal{\\%s}' % inner
            else:
                texcmd = '\\mathcal{%s}' % inner

        # \mbfA ↦ \mathbf{A}
        if texcmd.startswith('\\mbf'):
            inner = texcmd[4:]
            if len(inner) > 1:
                texcmd = '\\mathbf{\\%s}' % inner
            else:
                texcmd = '\\mathbf{%s}' % inner

        # \mfrakA ↦ \mathfrak{A}
        if texcmd.startswith('\\mfrak'):
            inner = texcmd[6:]
            if len(inner) > 1:
                texcmd = '\\mathfrak{\\%s}' % inner
            else:
                texcmd = '\\mathfrak{%s}' % inner

        # \mitsansA ↦ \mathss{A}
        if texcmd.startswith('\\mitsans'):
            inner = texcmd[8:]
            if len(inner) > 1:
                texcmd = '\\mathssit{\\%s}' % inner
            else:
                texcmd = '\\mathssit{%s}' % inner

        # \msansA ↦ \mathss{A}
        if texcmd.startswith('\\msans'):
            inner = texcmd[6:]
            if len(inner) > 1:
                texcmd = '\\mathss{\\%s}' % inner
            else:
                texcmd = '\\mathss{%s}' % inner

        # \mttA ↦ \mathtt{A}
        if texcmd.startswith('\\mtt'):
            inner = texcmd[4:]
            if len(inner) > 1:
                texcmd = '\\mathtt{\\%s}' % inner
            else:
                texcmd = '\\mathtt{%s}' % inner

        # \mitA ↦ A
        # NORMALIZATION
        normalization = False
        if texcmd.startswith('\\mit'):
            inner = texcmd[4:]
            if len(inner) > 1:
                texcmd = '\\%s' % inner
            else:
                texcmd = '%s' % inner
            normalization = True

        texcmd = texcmd.replace('{\\zero}', '{0}')
        texcmd = texcmd.replace('{\\one}', '{1}')
        texcmd = texcmd.replace('{\\two}', '{2}')
        texcmd = texcmd.replace('{\\three}', '{3}')
        texcmd = texcmd.replace('{\\four}', '{4}')
        texcmd = texcmd.replace('{\\five}', '{5}')
        texcmd = texcmd.replace('{\\six}', '{6}')
        texcmd = texcmd.replace('{\\seven}', '{7}')
        texcmd = texcmd.replace('{\\eight}', '{8}')
        texcmd = texcmd.replace('{\\nine}', '{9}')

        json1 += '"%s":"%s",\n' % (char.replace('\\', '\\\\'), texcmd.replace('\\', '\\\\'))

        # These have issues in latex, ignore them.
        if char not in '!#$%&()+,./:;<=>?@[\]{|}£¥§¶·ð' and texcmd not in [
            '\\grave',
            '\\acute',
            '\\hat',
            '\\widehat',
            '\\tilde',
            '\\widetilde'
            '\\bar',
            '\\overbar',
            '\\wideoverbar',
            '\\breve',
            '\\widebreve',
            '\\dot',
            '\\ddot',
            '\\ovhook',
            '\\ocirc',
            '\\check',
            '\\widecheck',
            '\\candra',
            '\\oturnedcomma',
            '\\ocommatopright',
            '\\droang',
            '\\wideutilde',
            '\\mathunderbar',
            '\\not',
            '\\underleftrightarrow']:
            latexout += '\\newunicodechar{%s}{%s}\n' % (char, texcmd)

        texcmd = texcmd.replace('\\', '\\\\')
        char = char.replace('\\', '\\\\')
        if normalization:
            json2 += '"%s":"%s",\n' % ('\\\\mathit{%s}' % texcmd, char)
        else:
            json2 += '"%s":"%s",\n' % (texcmd, char)

missing = {
    'bullet': '•',
}

synonyms = {
    'iff': '⟺',
    'implies': '⟹',
    'impliedby': '⟸',
    'to': '→',
}

onlyjson = {
    # Subscripts
    '_0': '₀',
    '_1': '₁',
    '_2': '₂',
    '_3': '₃',
    '_4': '₄',
    '_5': '₅',
    '_6': '₆',
    '_7': '₇',
    '_8': '₈',
    '_9': '₉',
    '_10': '⏨',
    '_+': '₊',
    '_-': '₋',
    '_=': '₌',
    '_(': '₍',
    '_)': '₎',
    '_a': 'ₐ',
    '_e': 'ₑ',
    '_h': 'ₕ',
    '_i': 'ᵢ',
    '_j': 'ⱼ',
    '_k': 'ₖ',
    '_l': 'ₗ',
    '_m': 'ₘ',
    '_n': 'ₙ',
    '_o': 'ₒ',
    '_p': 'ₚ',
    '_r': 'ᵣ',
    '_s': 'ₛ',
    '_t': 'ₜ',
    '_u': 'ᵤ',
    '_v': 'ᵥ',
    '_x': 'ₓ',
    # Superscripts
    '^0': '⁰',
    '^1': '¹',
    '^2': '²',
    '^3': '³',
    '^4': '⁴',
    '^5': '⁵',
    '^6': '⁶',
    '^7': '⁷',
    '^8': '⁸',
    '^9': '⁹',
    '^+': '⁺',
    '^-': '⁻',
    '^=': '⁼',
    '^(': '⁽',
    '^)': '⁾',
    '^a': 'ᵃ',
    '^b': 'ᵇ',
    '^c': 'ᶜ',
    '^d': 'ᵈ',
    '^e': 'ᵉ',
    '^f': 'ᶠ',
    '^g': 'ᵍ',
    '^h': 'ʰ',
    '^i': 'ⁱ',
    '^j': 'ʲ',
    '^k': 'ᵏ',
    '^l': 'ˡ',
    '^m': 'ᵐ',
    '^n': 'ⁿ',
    '^o': 'ᵒ',
    '^p': 'ᵖ',
    '^r': 'ʳ',
    '^s': 'ˢ',
    '^t': 'ᵗ',
    '^u': 'ᵘ',
    '^v': 'ᵛ',
    '^w': 'ʷ',
    '^x': 'ˣ',
    '^y': 'ʸ',
    '^z': 'ᶻ',
    '^A': 'ᴬ',
    '^B': 'ᴮ',
    '^D': 'ᴰ',
    '^E': 'ᴱ',
    '^G': 'ᴳ',
    '^H': 'ᴴ',
    '^I': 'ᴵ',
    '^J': 'ᴶ',
    '^K': 'ᴷ',
    '^L': 'ᴸ',
    '^M': 'ᴹ',
    '^N': 'ᴺ',
    '^O': 'ᴼ',
    '^P': 'ᴾ',
    '^R': 'ᴿ',
    '^T': 'ᵀ',
    '^U': 'ᵁ',
    '^V': 'ⱽ',
    '^W': 'ᵂ',
}

for texcmd, char in missing.items():
    json1 += '"%s":"\\\\%s",\n' % (char, texcmd)
    json2 += '"\\\\%s":"%s",\n' % (texcmd, char)
    latexout += '\\newunicodechar{%s}{\\%s}\n' % (char, texcmd)

for texcmd, char in synonyms.items():
    json1 += '"%s":"\\\\%s",\n' % (char, texcmd)
    json2 += '"\\\\%s":"%s",\n' % (texcmd, char)

for texcmd, char in onlyjson.items():
    json1 += '"%s":"%s",\n' % (char, texcmd)
    json2 += '"%s":"%s",\n' % (texcmd, char)

json1 += '}'
json2 += '}'

with open('unicode-latex.json', 'w') as f:
    f.write(json1)

with open('latex-unicode.json', 'w') as f:
    f.write(json2)

with open('unicode-latex.sty', 'w') as f:
    f.write(latexout)
