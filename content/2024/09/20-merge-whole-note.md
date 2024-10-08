+++
title = "[Lilypond] 衝突する全音符をマージ"
date = 2024-09-20
[taxonomies]
tags = [ "Lilypond", ]
+++

デフォルトでは Lilypond は複数声部の全音符が衝突するとき, マージしません. 例えば次のソース

```tex
\version "2.24.3"

\new Staff \new Voice \relative c'' {
  << { \voiceOne c1 } \\ { \voiceTwo c1 } >>
}
```

を Lilypond で処理すると, 全音符がふたつの楽譜が得られます.

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.2" width="48.00mm" height="23.92mm" viewBox="0.0000 -0.0000 27.3121 13.6096">
<style type="text/css">
<![CDATA[
tspan { white-space: pre; }
]]>
</style>
<g transform="translate(5.6906, 9.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.8810" y2="0"/>
</g>
<g transform="translate(5.6906, 8.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.8810" y2="0"/>
</g>
<g transform="translate(5.6906, 7.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.8810" y2="0"/>
</g>
<g transform="translate(5.6906, 6.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.8810" y2="0"/>
</g>
<g transform="translate(5.6906, 5.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.8810" y2="0"/>
</g>
<g transform="translate(21.4316, 7.6213)">
<rect x="0.0000" y="-2.0000" width="0.1900" height="4.0000" ry="0.0000" fill="currentColor"/>
</g>
<g transform="translate(10.6906, 7.6213)">
<path transform="scale(0.0040, -0.0040)" d="M359 27c-49 0 -75 42 -75 75c0 38 27 77 72 77c4 0 9 0 14 -1c-28 37 -72 59 -120 59c-106 0 -113 -73 -113 -186v-51v-51c0 -113 7 -187 113 -187c80 0 139 70 158 151c2 7 7 10 12 10c6 0 13 -4 13 -12c0 -94 -105 -174 -183 -174c-68 0 -137 21 -184 70
c-49 51 -66 122 -66 193s17 142 66 193c47 49 116 69 184 69c87 0 160 -64 175 -150c1 -5 1 -9 1 -13c0 -40 -30 -72 -67 -72z" fill="currentColor"/>
</g>
<a style="color:inherit;">
<g transform="translate(14.3905, 7.1213)">
<path transform="scale(0.0040, -0.0040)" d="M213 112c-50 0 -69 -43 -69 -88c0 -77 57 -136 134 -136c50 0 69 43 69 88c0 77 -57 136 -134 136zM491 0c0 -43 -34 -75 -72 -96c-53 -29 -114 -40 -174 -40s-120 11 -173 40c-38 21 -72 53 -72 96s34 75 72 96c53 29 113 40 173 40s121 -11 174 -40
c38 -21 72 -53 72 -96z" fill="currentColor"/>
</g>
</a>
<a style="color:inherit;">
<g transform="translate(16.3525, 7.1213)">
<path transform="scale(0.0040, -0.0040)" d="M213 112c-50 0 -69 -43 -69 -88c0 -77 57 -136 134 -136c50 0 69 43 69 88c0 77 -57 136 -134 136zM491 0c0 -43 -34 -75 -72 -96c-53 -29 -114 -40 -174 -40s-120 11 -173 40c-38 21 -72 53 -72 96s34 75 72 96c53 29 113 40 173 40s121 -11 174 -40
c38 -21 72 -53 72 -96z" fill="currentColor"/>
</g>
</a>
<g transform="translate(6.4906, 8.6213)">
<path transform="scale(0.0040, -0.0040)" d="M376 262c4 0 9 1 13 1c155 0 256 -128 256 -261c0 -76 -33 -154 -107 -210c-22 -17 -47 -28 -73 -36c3 -35 5 -70 5 -105c0 -19 -1 -39 -2 -58c-7 -120 -90 -228 -208 -228c-108 0 -195 88 -195 197c0 58 53 103 112 103c54 0 95 -47 95 -103c0 -52 -43 -95 -95 -95
c-11 0 -21 2 -31 6c26 -39 68 -65 117 -65c96 0 157 92 163 191c1 18 2 37 2 55c0 31 -1 61 -4 92c-29 -5 -58 -8 -89 -8c-188 0 -333 172 -333 374c0 177 131 306 248 441c-19 62 -37 126 -45 191c-6 52 -7 103 -7 155c0 115 55 224 149 292c3 2 7 3 10 3c4 0 7 0 10 -3
c71 -84 133 -245 133 -358c0 -143 -86 -255 -180 -364c21 -68 39 -138 56 -207zM461 -203c68 24 113 95 113 164c0 90 -66 179 -173 190c24 -116 46 -231 60 -354zM74 28c0 -135 129 -247 264 -247c28 0 55 2 82 6c-14 127 -37 245 -63 364c-79 -8 -124 -61 -124 -119
c0 -44 25 -91 81 -123c5 -5 7 -10 7 -15c0 -11 -10 -22 -22 -22c-3 0 -6 1 -9 2c-80 43 -117 115 -117 185c0 88 58 174 160 197c-14 58 -29 117 -46 175c-107 -121 -213 -243 -213 -403zM408 1045c-99 -48 -162 -149 -162 -259c0 -74 18 -133 36 -194
c80 97 146 198 146 324c0 55 -4 79 -20 129z" fill="currentColor"/>
</g>
<g transform="translate(28.8852, 165.1062)">
<a xlink:href="https://lilypond.org/">
<rect x="0.0000" y="-0.4888" width="61.7311" height="2.1604" fill="none" stroke="none" stroke-width="0.0"/>
</a>
</g>
</svg>

この全音符を強制的にマージするには, 次のように `\once \override NoteColumn.ignore-collision = ##t` を指定します.

```tex
\version "2.24.3"

\new Staff \new Voice \relative c'' {
  << { 
    \voiceOne \once \override NoteColumn.ignore-collision = ##t c1 
  } \\ { 
    \voiceTwo c1 
  } >>
}
```

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.2" width="46.27mm" height="23.92mm" viewBox="0.0000 -0.0000 26.3311 13.6096">
<style type="text/css">
<![CDATA[
tspan { white-space: pre; }
]]>
</style>
<g transform="translate(5.6906, 9.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="14.9000" y2="0"/>
</g>
<g transform="translate(5.6906, 8.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="14.9000" y2="0"/>
</g>
<g transform="translate(5.6906, 7.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="14.9000" y2="0"/>
</g>
<g transform="translate(5.6906, 6.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="14.9000" y2="0"/>
</g>
<g transform="translate(5.6906, 5.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="14.9000" y2="0"/>
</g>
<g transform="translate(20.4506, 7.6213)">
<rect x="0.0000" y="-2.0000" width="0.1900" height="4.0000" ry="0.0000" fill="currentColor"/>
</g>
<g transform="translate(10.6906, 7.6213)">
<path transform="scale(0.0040, -0.0040)" d="M359 27c-49 0 -75 42 -75 75c0 38 27 77 72 77c4 0 9 0 14 -1c-28 37 -72 59 -120 59c-106 0 -113 -73 -113 -186v-51v-51c0 -113 7 -187 113 -187c80 0 139 70 158 151c2 7 7 10 12 10c6 0 13 -4 13 -12c0 -94 -105 -174 -183 -174c-68 0 -137 21 -184 70
c-49 51 -66 122 -66 193s17 142 66 193c47 49 116 69 184 69c87 0 160 -64 175 -150c1 -5 1 -9 1 -13c0 -40 -30 -72 -67 -72z" fill="currentColor"/>
</g>
<a style="color:inherit;">
<g transform="translate(14.3905, 7.1213)">
<path transform="scale(0.0040, -0.0040)" d="M213 112c-50 0 -69 -43 -69 -88c0 -77 57 -136 134 -136c50 0 69 43 69 88c0 77 -57 136 -134 136zM491 0c0 -43 -34 -75 -72 -96c-53 -29 -114 -40 -174 -40s-120 11 -173 40c-38 21 -72 53 -72 96s34 75 72 96c53 29 113 40 173 40s121 -11 174 -40
c38 -21 72 -53 72 -96z" fill="currentColor"/>
</g>
</a>
<a style="color:inherit;">
<g transform="translate(14.3905, 7.1213)">
<path transform="scale(0.0040, -0.0040)" d="M213 112c-50 0 -69 -43 -69 -88c0 -77 57 -136 134 -136c50 0 69 43 69 88c0 77 -57 136 -134 136zM491 0c0 -43 -34 -75 -72 -96c-53 -29 -114 -40 -174 -40s-120 11 -173 40c-38 21 -72 53 -72 96s34 75 72 96c53 29 113 40 173 40s121 -11 174 -40
c38 -21 72 -53 72 -96z" fill="currentColor"/>
</g>
</a>
<g transform="translate(6.4906, 8.6213)">
<path transform="scale(0.0040, -0.0040)" d="M376 262c4 0 9 1 13 1c155 0 256 -128 256 -261c0 -76 -33 -154 -107 -210c-22 -17 -47 -28 -73 -36c3 -35 5 -70 5 -105c0 -19 -1 -39 -2 -58c-7 -120 -90 -228 -208 -228c-108 0 -195 88 -195 197c0 58 53 103 112 103c54 0 95 -47 95 -103c0 -52 -43 -95 -95 -95
c-11 0 -21 2 -31 6c26 -39 68 -65 117 -65c96 0 157 92 163 191c1 18 2 37 2 55c0 31 -1 61 -4 92c-29 -5 -58 -8 -89 -8c-188 0 -333 172 -333 374c0 177 131 306 248 441c-19 62 -37 126 -45 191c-6 52 -7 103 -7 155c0 115 55 224 149 292c3 2 7 3 10 3c4 0 7 0 10 -3
c71 -84 133 -245 133 -358c0 -143 -86 -255 -180 -364c21 -68 39 -138 56 -207zM461 -203c68 24 113 95 113 164c0 90 -66 179 -173 190c24 -116 46 -231 60 -354zM74 28c0 -135 129 -247 264 -247c28 0 55 2 82 6c-14 127 -37 245 -63 364c-79 -8 -124 -61 -124 -119
c0 -44 25 -91 81 -123c5 -5 7 -10 7 -15c0 -11 -10 -22 -22 -22c-3 0 -6 1 -9 2c-80 43 -117 115 -117 185c0 88 58 174 160 197c-14 58 -29 117 -46 175c-107 -121 -213 -243 -213 -403zM408 1045c-99 -48 -162 -149 -162 -259c0 -74 18 -133 36 -194
c80 97 146 198 146 324c0 55 -4 79 -20 129z" fill="currentColor"/>
</g>
<g transform="translate(28.8852, 165.1062)">
<a xlink:href="https://lilypond.org/">
<rect x="0.0000" y="-0.4888" width="61.7311" height="2.1604" fill="none" stroke="none" stroke-width="0.0"/>
</a>
</g>
</svg>


# 参考文献

* [Re: combining two whole notes into one](https://lists.gnu.org/archive/html/lilypond-user/2023-09/msg00210.html)
