# Unicode LaTeX

Provides maps between unicode symbols and LaTeX commands.

- `latex-unicode.json` map from latex to unicode.
- `unicode-latex.json` map from unicode to latex.
- `unicode-latex.sty` LaTeX package for using `α` instead of `\alpha` for improved readability of math commands.

This package strives to cover all symbols and to use standard LaTeX commands, e.g. `\mathbb{C}` instead of `\BbbC`, in contrast to other unicode packages (e.g. [unicode-math](https://github.com/wspr/unicode-math) and [Julia](https://github.com/JuliaLang/julia/blob/master/base/latex_symbols.jl)).

Please open an issue if you see something missing/wrong.


## Updating

The file `latex-unicode.json` is the source, from which `unicode-latex.json` and `unicode-latex.sty` are generated with `generate.py`.


## To do

Currently there is no support for subscripts and superscripts in the LaTeX packge. This cannot be done trivially by mapping `¹` to `^1` because then sub/superscritps cannot be joined (`^1^2` gives latex error "double superscritps"). The solution should be to parse unicode sub/superscripts like [unicode-math](https://github.com/wspr/unicode-math) does.


## Sublime Text unicode input

The package [InstantUnicode](https://github.com/ViktorQvarfordt/Sublime-InstantUnicode) provides easy input of unicode symbols, it uses `latex-unicode.json`.


## Other notes

- There may be multiple LaTeX commands mapping to the same unicode symbol, e.g. both `\iff` and `\Longleftrightarrow` maps to `⟺`.

- In the LaTeX package `unicode-latex.sty` the italic unicode symbols, e.g. `𝑎` are normalized to `a`, since `a` already renders as italic in math mode.

- The files where originally generated from the file [`unicode-math-table.tex`](https://github.com/wspr/unicode-math/blob/master/unicode-math-table.tex) with the script `generate_old.py` which standardized and normalized the data, and added some missing symbols and synonyms. After this I have started to make manual changes to the files, to fix errors in the original files.
