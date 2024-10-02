+++
title = "WSL2とtmuxでtrue colorが表示されない"
date = 2024-10-02
[extra]
toc = true
[taxonomies]
tags = [ "Linux", ]
+++

# 環境

* Win10 22H2, Win11 23H2
* WSL2 + Windows Terminal (1.20.11781.0)
* Debian 12.7 + tmux 3.3a, Debian 11.11 + tmux 3.1c

# 状況

tmux 使用時にターミナルが true color を表示できない.
tmux を使っていなければ表示できる.

true color が正しく表示できているかのチェックは次の記事の方法がお手軽で助かりました.

* [TrueColor対応のはなし(端末、シェル、tmux、vim) - Panda Noir](https://www.pandanoir.info/entry/2019/11/02/202146)


# 解決法

いろいろ調べると `~/.tmux.conf` の設定を見直せば解決したと言っている人が多い.

```bash
set -g default-terminal "screen-256color"
set-option -sa terminal-overrides ",xterm-256color:Tc"
```

ただこれだけでは解決せず, いろいろ調べた結果, `~/.bashrc` で環境変数 `$TERM` を指定しているのが悪さをしており,
この行を消せば true color を表示できるようになった.

```bash
#export TERM=xterm-256color
```

この設定はもともと別の環境で true color が表示されないのを解決するために入れた気がするんですけどね...


# 補足: 環境変数 `$TERM` について

`$TERM` で指定可能な値は以下の場所に格納されており, 上から順に探しに行く模様.

```
${HOME}/.terminfo
/etc/terminfo
/lib/terminfo
/usr/share/terminfo
```


# 参考文献

* [tmux 上で Vim を True Color (24 bit color) で使う #Vim - Qiita](https://qiita.com/yami_beta/items/ef535d3458addd2e8fbb)
* [TrueColor対応のはなし(端末、シェル、tmux、vim) - Panda Noir](https://www.pandanoir.info/entry/2019/11/02/202146)
