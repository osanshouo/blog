+++
title = "[Lilypond] 総譜とパート譜を同時に生成するテクニック"
date = 2024-05-20
[extra]
toc = true
[taxonomies]
tags = [ "音楽", "Lilypond", ]
+++

総譜 (スコア) とパート譜をともに Lilypond で作成することを考えます.
ベースとなる音楽情報は総譜とパート譜で (ほぼ) 同じものですから,
総譜とパート譜はソースコードの大部分を共有するべきです.
基本的なことは公式ドキュメントにまとまっています.

* [GNU LilyPond 学習マニュアル: 4.4.5 楽譜とパート](https://lilypond.org/doc/v2.23/Documentation/learning/scores-and-parts.ja.html)
* [LilyPond 記譜法リファレンス: 1.6.3 パートを記述する](https://lilypond.org/doc/v2.23/Documentation/notation/writing-parts.ja.html)

ただし, パート譜には以下の考慮事項があります.

* 奇数ページの改ページ位置をできるだけ長い休符に合わせたい. 
そのために手動で `\pageBreak` を挿入したいが, これは総譜には反映されるべきではない.
* 必要に応じて, 休符部分に他のパートの音符を示しておきたい (影譜, `CueVoice`).

このあたりをいい感じに行うワークアラウンドを考えたので, まとめておきます.
もっと良い方法があるかもしれませんが...

なお, 以下では弦楽四重奏を想定して説明します.


# プロジェクト構造

以下のファイルを作成します. 

* `String Quartet.ly`: メインとなる Lilypond ファイル. 
* `score.ily`: 総譜部分を担当する.
* `part.ily`: パート譜部分を担当する.
* `violin1.ily`, `violin2.ily`, `viola.ily`, `cello.ily`: 各パートの音楽データを入力する.
* (任意) `common.ily`: 共通のソースコードをまとめておくファイル 
(調や拍子, 発想標語, その他共通で使用する Lilypond コードなど).


# 各パート

まず各パート `violin1.ily`, `violin2.ily`, `viola.ily`, `cello.ily` ですが, 
これらのファイルには, `Staff` を含めず, 音楽データ (`Voice`) だけをまとめておきます.
さらに, 各パートの `CueVoice` もここに入力しておくと良いでしょう.
要点は, `CueVoice` は総譜には読み込まずパート譜だけで使用されるため, 
`CueVoice` 内に改ページなどのパート譜のためのレイアウト設定を持たせておくことができる, という点です.

例えば `violin1.ily` は次のような内容になるでしょう.

```tex
violinFirst = \new Voice \relative c' {
  %{ 音楽データを入力 %}
}

violinFirstCue = \new CueVoice {
  %{ 全小節を `s` で埋める (影譜が必要な部分のみ入力). \pageBreak 等はここに入力 %}
}
```


# `score.ily`

次に `score.ily` ですが, 総譜で単独の PDF ファイルを作成したいため, この中でひとつの `book` を作成します.

```tex
\book {
  \score { 
    \new StaffGroup <<
      \new Staff \with { instrumentName = #"Violin I" } { \violinFirst }
      \new Staff \with { instrumentName = #"Violin II" } { \violinSecond }
      \new Staff \with { instrumentName = #"Viola" } { \viola }
      \new Staff \with { instrumentName = #"Cello" } { \cello }
    >>
    
    \layout {}
  }

  \paper {
    #(layout-set-staff-size 17)
    systems-per-page = #4
  }
}
```

複数の楽章からなる楽曲の場合は, `\score` ブロックを増やしてください.


# `part.ily`

パート譜ですが, ほぼ同じものをパートの数だけ作成するのは面倒です.
そこで以下の方法で手間やソースコードの無駄を省くことができます.

`part.ily` には, 以下のように, 各パートによって異なる部分を変数とした Lilypond コードを入力します.
この場合には `\INSTRUMENT`, `\PART`, `\CUE` が各パートによって異なる変数です.

```tex
\book {
  \bookOutputSuffix \INSTRUMENT 

  \score {
    <<
      \new Staff << \PART \CUE >>
    >>
    \layout {}
  }

  \paper {
    #(layout-set-staff-size 20)

    bookTitleMarkup = \markup \center-column {
      \fill-line {
        \fontsize #4 \bold \fromproperty #'header:title
      }
      \fill-line {
        \rounded-box { \fontsize #2 \INSTRUMENT }
        \fromproperty #'header:composer
      }
    }
  }
}
```

`\bookOutputSuffix` を指定することで各パートの出力ファイル名を制御することができます.
今回の場合では, `String Quartet-Violin I.pdf` といった感じで出力されます.
また, どのパートの楽譜か明示するために `bookTitleMarkup` を設定しておきました.
このあたりは好みで自由に調整できます.

複数の楽章からなる楽曲の場合は, 楽章の数だけ `\score` を増やすと同時に, 
`\PART`, `\CUE` といった変数も楽章の数だけ用意します.


# メインファイル

それではメインファイル `String Quartet.ly` ですが, ここで今まで作成してきたファイルを `\include` していきます.

```tex
\version "2.24.0"
\language "deutsch"
\pointAndClickOff

\header {
  title = "String Quartet"
  %composer = ""
  tagline = ##f
}

%\include "./common.ily"
\include "./violin1.ily"
\include "./violin2.ily"
\include "./viola.ily"
\include "./cello.ily"


%%% 総譜を作成 %%%
\include "./score.ily"


%%% パート譜を作成 %%%
INSTRUMENT = "Violin I"
PART = \violinFirst
CUE = \violinFirstCue
\include "./part.ily"

INSTRUMENT = "Violin II"
PART = \violinSecond
CUE = \violinSecondCue
\include "./part.ily"

INSTRUMENT = "Viola"
PART = \viola
CUE = \violaCue
\include "./part.ily"

INSTRUMENT = "Cello"
PART = \cello
CUE = \celloCue
\include "./part.ily"
```

総譜は単に別ファイルで作ったものを `\include` するだけです. 
問題はパート譜ですが, 見ての通り, `\include "./part.ily"` 
する直前でパートによって異なる変数に各パートの音楽データ等を代入することで, 
ソースコードの重複を最小限にしてパート譜を作成することができます.

以上で, 音楽データそのものは一か所に入力されており, それが総譜とパート譜の双方に反映されていますが,
パート譜ではさらに追加の `\pageBreak` や影譜を自由に入力できる, という目標が達成できました.
