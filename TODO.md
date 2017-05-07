# To do

```
\documentclass{article}

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}

\usepackage{amsmath}
\usepackage{amssymb} % AMS Math

\usepackage{mathbbol}


\DeclareSymbolFontAlphabet{\mathbba}{AMSb}
\DeclareSymbolFontAlphabet{\mathbbl}{bbold}

\makeatletter
\def\instring#1#2{TT\fi\begingroup
  \edef\x{\endgroup\noexpand\in@{#1}{#2}}\x\ifin@}
\makeatother

\renewcommand{\mathbb}[1]{%
  \if\instring{#1}{abcdefghijklmnopqrstuvwxyz0123456789ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρςστυφχψωϑϕ}%
  \mathbbl{#1}\else%
  \mathbba{#1}%
  \fi%
}


% \def\foo#1#2{\mathbbinner{#1} \ifx#2\relax\else \foo#2\fi}

% \renewcommand{\mathbb}[1]{%
%   \ifthenelse{\equal{#1}{1}}%
%   {\mathbbl{#1}}%
%   {\mathbbams{#1}}%
% }

\usepackage{unicode-latex}

\begin{document}

\begin{equation}
  𝟙ℝ\mathbb{Δ}\mathbb{\alpha}\mathbb{β}
\end{equation}


\end{document}
```

```
\documentclass{article}
\usepackage[bbgreekl]{mathbbol}
\usepackage{amsfonts}
\DeclareSymbolFontAlphabet{\mathbbams}{AMSb}
\DeclareSymbolFontAlphabet{\mathbbl}{bbold}
\usepackage{xstring}

\begin{document}

$\mathbb{aA}$
alpha $\alpha$\\
bbalpha $\bbalpha$\\
mathbb alphau$\mathbb{α}$\\
mathbb alpha $\mathbb{\alpha}$\\
\makeatletter
\def\instring#1#2{TT\fi\begingroup
  \edef\x{\endgroup\noexpand\in@{#1}{#2}}\x\ifin@}
\makeatother
\renewcommand{\mathbb}[1]{%
%  \switchbb#1\relax%
%}
%\def\switchbb#1#2{
  \if\instring{#1}{abcdefghijklmnopqrstuvwxyz0123456789ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρςστυφχψωϑϕ}%
  \mathbbl{#1}\else%
  \mathbbams{#1}%
  \fi%
 % \ifx#2\relax\else\switchbb#2\fi%
}
$\mathbb{aA}$

\def\mymathbb#1{%
  \newcount\n%
  \n=0%
  \StrLen{#1}[\mystrlen]%
  \loop% -> repeat
  \ifnum\n<\mystrlen % break condition, no fi!
  \advance\n by 1%
  \StrChar{#1}{\n}[\mymathbbexpander]%
  \mymathbbchardecider{\mymathbbexpander}%
  \repeat%
}

\def\mymathbbchardecider#1{%
  \if\instring{#1}{abcdefghijklmnopqrstuvwxyz0123456789ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩαβγδεζηθικλμνξοπρςστυφχψωϑϕ}%
  \mathbbl{#1}\else%
  \mathbbams{#1}%
  \fi%
}
$\mymathbb{aA1bΔ2}$

\end{document}
```
