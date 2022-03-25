+++
title = "[Lilypond] 拍子記号を非表示にする"
date = 2022-03-25
[taxonomies]
tags = [ "音楽", "Lilypond" ]
+++

Lilypond において拍子記号の表示/非表示を設定するには, 基本的には

```tex
\override Score.TimeSignature.break-visibility = ##(#f #f #f)
```

のようにすれば良いです.

* [LilyPond 記譜法リファレンス: 5.4.7 オブジェクトの可視性](https://lilypond.org/doc/v2.22/Documentation/notation/visibility-of-objects.ja.html#using-break_002dvisibility)

しかし, これでは楽譜冒頭の拍子記号は表示されたままです. 
これを非表示にするには以下のようにします.

```tex
\score {
    \new Staff <<
        % ここに楽譜データを入力 %
    >>

    \layout {
        \context {
            \Staff
            \remove "Time_signature_engraver"
        }
    }
}
```


* [LilyPond 記譜法リファレンス: 2.9.6 古代音楽に取り組む—事例とその解決法](https://lilypond.org/doc/v2.21/Documentation/notation/working-with-ancient-music_002d_002dscenarios-and-solutions.ja.html#transcribing-gregorian-chant)


# ページサイズを自動調整

この設定を行うのは主に協奏曲のカデンツァや古楽だと思いますが, 
譜例作成のために採用する場合, ページサイズを楽譜に合わせて縮小する

```tex
\paper {
     page-breaking = #ly:one-line-auto-height-breaking
}
```

というオプションと併用すると思います.

* [LilyPond 記譜法リファレンス: 4.3.2 改ページ](https://lilypond.org/doc/v2.21/Documentation/notation/page-breaking#one_002dline_002dauto_002dheight-page-breaking)
