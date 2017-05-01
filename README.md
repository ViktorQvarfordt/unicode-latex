# Unicode LaTeX

Provides maps between unicode symbols and LaTeX commands.

- `latex-unicode.json` map from latex to unicode.
- `unicode-latex.json` map from unicode to latex.
- `unicode-latex.sty` LaTeX package for using `α` instead of `\alpha` for improved readability of math commands.

This package strives to cover all symbols and to use standard LaTeX commands. Please open an issue if you see something missing/wrong.


## Notes

This package uses standard LaTeX commands, e.g. `\mathbb{C}` instead of `\BbbC`, in contrast to other unicode packages (e.g. [unicode-math](https://github.com/wspr/unicode-math) and [Julia](https://github.com/JuliaLang/julia/) REPL).

The files are generated from the file `unicode-math-table.tex` (taken from [unicode-math](https://github.com/wspr/unicode-math)) with the script `generate.py` which modernizes and normalizes the data, and adds missing symbols and synonyms.


## ToDo

Currently there is no support for subscripts and superscripts in the LaTeX packge. This cannot be done trivially by mapping `¹` to `^1` because then sub/superscritps cannot be joined (`^1^2` gives latex error "double superscritps"). The solution should be to parse unicode sub/superscripts like [unicode-math](https://github.com/wspr/unicode-math) does.


## Sublime Text unicode input

The package [InstantUnicode](https://github.com/ViktorQvarfordt/Sublime-InstantUnicode) provides easy input of unicode symbols, it uses `latex-unicode.json`.
