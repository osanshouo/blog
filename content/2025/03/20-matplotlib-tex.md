+++
title = "matplotlibでTeX数式を表示"
date = 2025-03-20
[taxonomies]
tags = ["Python", "matplotlib", "TeX", ]
+++

matplotlib で TeX 数式を表示するメモ.

```bash
sudo apt install texlive-latex-base
```

だけではダメで,

```bash
sudo apt install dvipng texlive-latex-extra texlive-fonts-recommended cm-super
```

が必要.


# 参考文献

* [Text rendering with LaTeX — Matplotlib 3.10.1 documentation](https://matplotlib.org/stable/users/explain/text/usetex.html)
* <https://stackoverflow.com/questions/11354149/python-unable-to-render-tex-in-matplotlib>
