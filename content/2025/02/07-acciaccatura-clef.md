+++
title = "[Lilypond] 楽曲冒頭の装飾音符と音部記号の位置に関するバグ"
date = 2025-02-07
[taxonomies]
tags = [ "Lilypond", ]
+++

Lilypond でピアノ譜を作成する際に, 左手譜のヘ音記号は冒頭に配置されるべきですが,
右手譜の冒頭が装飾音符から始まる場合, 左手譜がト音記号から開始し装飾音符の位置にヘ音記号が配置されてしまう現象があります.

```tex
\version "2.24.4"

\score {
  \new PianoStaff <<
    \new Staff \new Voice \relative c' {
      \acciaccatura d8 c1
    }
    \new Staff \new Voice \relative c {
      \clef "bass"
      c1
    }
  >>

  \layout{}
}
```

<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.2" width="49.67mm" height="39.73mm" viewBox="0.0000 -0.0000 28.2639 22.6096">
<style type="text/css">
<![CDATA[
tspan { white-space: pre; }
]]>
</style>
<g transform="translate(5.6906, 9.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 8.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 7.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 6.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 5.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(21.2110, 7.6213)">
<rect x="0.0000" y="-2.0000" width="0.1900" height="4.0500" ry="0.0000" fill="currentColor"/>
</g>
<g transform="translate(21.2110, 16.6213)">
<rect x="0.0000" y="-2.0500" width="0.1900" height="4.0500" ry="0.0000" fill="currentColor"/>
</g>
<g transform="translate(21.2110, 3.8453)">
<rect x="0.0000" y="5.8260" width="0.1900" height="4.9500" ry="0.0000" fill="currentColor"/>
</g>
<g transform="translate(5.6906, 18.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 17.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 16.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 15.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 14.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 10.6213)">
<rect x="9.0391" y="-0.1000" width="2.8737" height="0.2000" ry="0.1000" fill="currentColor"/>
</g>
<a style="color:inherit;" xlink:href="textedit:///home/sugiura/.local/src/lilypond-2.24.4/share/lilypond/2.24.4/ly/grace-init.ly:41:6:7">
<g transform="translate(13.3905, 7.6213)">
<path stroke-width="0.0800" stroke-linejoin="round" stroke-linecap="round" stroke="currentColor" fill="currentColor" d="M0.3750 3.3940C0.8007 4.1429 1.7961 4.4392 2.5620 4.0450L2.5620 4.0450C1.8303 4.3242 0.8350 4.0279 0.3750 3.3940z"/>
</g>
</a>
<g transform="translate(5.3306, 12.1213)">
<path transform="scale(0.0040, -0.0040)" d="M-189 -1146c0 267 108 528 108 780c0 135 -33 261 -129 360c-3 3 -3 3 -3 6s0 3 3 6c96 99 129 225 129 360c0 252 -108 513 -108 780c0 189 45 366 177 501c3 3 9 6 12 6c9 0 15 -9 15 -18c0 -3 0 -9 -3 -12c-99 -99 -129 -225 -129 -360c0 -249 102 -504 102 -765
c0 -186 -45 -363 -174 -498c129 -135 174 -312 174 -498c0 -261 -102 -516 -102 -765c0 -135 30 -261 129 -360c3 -3 3 -9 3 -12c0 -9 -6 -18 -15 -18c-3 0 -9 3 -12 6c-132 135 -177 312 -177 501z" fill="currentColor"/>
</g>
<g transform="translate(5.6306, 12.1213)">
<rect x="0.0000" y="-6.5500" width="0.1600" height="13.1000" ry="0.0500" fill="currentColor"/>
</g>
<a style="color:inherit;" xlink:href="textedit:///mnt/c/Users/sugiura/Desktop/workdesk/tmp/grace.ly:10:20:21">
<g transform="translate(13.3905, 10.1213)">
<path transform="scale(0.0028, -0.0028)" d="M208 139c61 0 117 -33 117 -99c0 -71 -52 -119 -99 -147c-34 -20 -71 -32 -110 -32c-61 0 -116 33 -116 99c0 71 51 119 98 147c34 20 71 32 110 32z" fill="currentColor"/>
</g>
</a>
<g transform="translate(6.4906, 8.6213)">
<path transform="scale(0.0040, -0.0040)" d="M376 262c4 0 9 1 13 1c155 0 256 -128 256 -261c0 -76 -33 -154 -107 -210c-22 -17 -47 -28 -73 -36c3 -35 5 -70 5 -105c0 -19 -1 -39 -2 -58c-7 -120 -90 -228 -208 -228c-108 0 -195 88 -195 197c0 58 53 103 112 103c54 0 95 -47 95 -103c0 -52 -43 -95 -95 -95
c-11 0 -21 2 -31 6c26 -39 68 -65 117 -65c96 0 157 92 163 191c1 18 2 37 2 55c0 31 -1 61 -4 92c-29 -5 -58 -8 -89 -8c-188 0 -333 172 -333 374c0 177 131 306 248 441c-19 62 -37 126 -45 191c-6 52 -7 103 -7 155c0 115 55 224 149 292c3 2 7 3 10 3c4 0 7 0 10 -3
c71 -84 133 -245 133 -358c0 -143 -86 -255 -180 -364c21 -68 39 -138 56 -207zM461 -203c68 24 113 95 113 164c0 90 -66 179 -173 190c24 -116 46 -231 60 -354zM74 28c0 -135 129 -247 264 -247c28 0 55 2 82 6c-14 127 -37 245 -63 364c-79 -8 -124 -61 -124 -119
c0 -44 25 -91 81 -123c5 -5 7 -10 7 -15c0 -11 -10 -22 -22 -22c-3 0 -6 1 -9 2c-80 43 -117 115 -117 185c0 88 58 174 160 197c-14 58 -29 117 -46 175c-107 -121 -213 -243 -213 -403zM408 1045c-99 -48 -162 -149 -162 -259c0 -74 18 -133 36 -194
c80 97 146 198 146 324c0 55 -4 79 -20 129z" fill="currentColor"/>
</g>
<g transform="translate(10.6906, 7.6213)">
<path transform="scale(0.0040, -0.0040)" d="M359 27c-49 0 -75 42 -75 75c0 38 27 77 72 77c4 0 9 0 14 -1c-28 37 -72 59 -120 59c-106 0 -113 -73 -113 -186v-51v-51c0 -113 7 -187 113 -187c80 0 139 70 158 151c2 7 7 10 12 10c6 0 13 -4 13 -12c0 -94 -105 -174 -183 -174c-68 0 -137 21 -184 70
c-49 51 -66 122 -66 193s17 142 66 193c47 49 116 69 184 69c87 0 160 -64 175 -150c1 -5 1 -9 1 -13c0 -40 -30 -72 -67 -72z" fill="currentColor"/>
</g>
<g transform="translate(6.4906, 17.6213)">
<path transform="scale(0.0040, -0.0040)" d="M376 262c4 0 9 1 13 1c155 0 256 -128 256 -261c0 -76 -33 -154 -107 -210c-22 -17 -47 -28 -73 -36c3 -35 5 -70 5 -105c0 -19 -1 -39 -2 -58c-7 -120 -90 -228 -208 -228c-108 0 -195 88 -195 197c0 58 53 103 112 103c54 0 95 -47 95 -103c0 -52 -43 -95 -95 -95
c-11 0 -21 2 -31 6c26 -39 68 -65 117 -65c96 0 157 92 163 191c1 18 2 37 2 55c0 31 -1 61 -4 92c-29 -5 -58 -8 -89 -8c-188 0 -333 172 -333 374c0 177 131 306 248 441c-19 62 -37 126 -45 191c-6 52 -7 103 -7 155c0 115 55 224 149 292c3 2 7 3 10 3c4 0 7 0 10 -3
c71 -84 133 -245 133 -358c0 -143 -86 -255 -180 -364c21 -68 39 -138 56 -207zM461 -203c68 24 113 95 113 164c0 90 -66 179 -173 190c24 -116 46 -231 60 -354zM74 28c0 -135 129 -247 264 -247c28 0 55 2 82 6c-14 127 -37 245 -63 364c-79 -8 -124 -61 -124 -119
c0 -44 25 -91 81 -123c5 -5 7 -10 7 -15c0 -11 -10 -22 -22 -22c-3 0 -6 1 -9 2c-80 43 -117 115 -117 185c0 88 58 174 160 197c-14 58 -29 117 -46 175c-107 -121 -213 -243 -213 -403zM408 1045c-99 -48 -162 -149 -162 -259c0 -74 18 -133 36 -194
c80 97 146 198 146 324c0 55 -4 79 -20 129z" fill="currentColor"/>
</g>
<g transform="translate(10.6906, 16.6213)">
<path transform="scale(0.0040, -0.0040)" d="M359 27c-49 0 -75 42 -75 75c0 38 27 77 72 77c4 0 9 0 14 -1c-28 37 -72 59 -120 59c-106 0 -113 -73 -113 -186v-51v-51c0 -113 7 -187 113 -187c80 0 139 70 158 151c2 7 7 10 12 10c6 0 13 -4 13 -12c0 -94 -105 -174 -183 -174c-68 0 -137 21 -184 70
c-49 51 -66 122 -66 193s17 142 66 193c47 49 116 69 184 69c87 0 160 -64 175 -150c1 -5 1 -9 1 -13c0 -40 -30 -72 -67 -72z" fill="currentColor"/>
</g>
<g transform="translate(14.2434, 7.6213)">
<rect x="-0.0650" y="-0.3000" width="0.1300" height="2.6856" ry="0.0400" fill="currentColor"/>
</g>
<g transform="translate(12.5405, 15.6213)">
<path transform="scale(0.0040, -0.0040)" d="M446 -100c0 23 18 41 41 41s41 -18 41 -41s-18 -41 -41 -41s-41 18 -41 41zM446 100c0 23 18 41 41 41s41 -18 41 -41s-18 -41 -41 -41s-41 18 -41 41zM179 213c140 0 241 -69 241 -201c0 -211 -210 -333 -411 -421c-3 -3 -6 -4 -9 -4c-7 0 -13 6 -13 13c0 3 1 6 4 9
c150 98 307 217 307 393c0 92 -38 185 -119 185c-52 0 -87 -38 -104 -90c5 1 10 2 15 2c44 0 80 -36 80 -80c0 -46 -35 -85 -80 -85c-48 0 -90 38 -90 85c0 104 77 194 179 194z" fill="currentColor"/>
</g>
<a style="color:inherit;" xlink:href="textedit:///mnt/c/Users/sugiura/Desktop/workdesk/tmp/grace.ly:15:6:7">
<g transform="translate(15.1509, 17.1213)">
<path transform="scale(0.0040, -0.0040)" d="M213 112c-50 0 -69 -43 -69 -88c0 -77 57 -136 134 -136c50 0 69 43 69 88c0 77 -57 136 -134 136zM491 0c0 -43 -34 -75 -72 -96c-53 -29 -114 -40 -174 -40s-120 11 -173 40c-38 21 -72 53 -72 96s34 75 72 96c53 29 113 40 173 40s121 -11 174 -40
c38 -21 72 -53 72 -96z" fill="currentColor"/>
</g>
</a>
<a style="color:inherit;" xlink:href="textedit:///mnt/c/Users/sugiura/Desktop/workdesk/tmp/grace.ly:10:23:24">
<g transform="translate(15.1509, 10.6213)">
<path transform="scale(0.0040, -0.0040)" d="M213 112c-50 0 -69 -43 -69 -88c0 -77 57 -136 134 -136c50 0 69 43 69 88c0 77 -57 136 -134 136zM491 0c0 -43 -34 -75 -72 -96c-53 -29 -114 -40 -174 -40s-120 11 -173 40c-38 21 -72 53 -72 96s34 75 72 96c53 29 113 40 173 40s121 -11 174 -40
c38 -21 72 -53 72 -96z" fill="currentColor"/>
</g>
</a>
<g transform="translate(14.3084, 7.3613)">
<path transform="scale(0.0028, -0.0028)" d="M206 -219c18 0 32 -14 32 -32c0 -9 -4 -17 -11 -23l-357 -290c-5 -5 -11 -7 -18 -7h-1c-17 0 -31 15 -31 32c0 9 4 17 11 23l357 290c5 5 11 7 18 7z" fill="currentColor"/>
</g>
<g transform="translate(14.3084, 7.3613)">
<path transform="scale(0.0028, -0.0028)" d="M0 0c0 -196 207 -334 207 -530c0 -71 -15 -140 -41 -206c-5 -10 -14 -13 -23 -13c-14 0 -28 10 -28 26c0 2 1 3 1 5c26 59 42 123 42 188c0 101 -90 205 -158 280h-21v250h21z" fill="currentColor"/>
</g>
<g transform="translate(28.8852, 165.1062)">
<a xlink:href="https://lilypond.org/">
<rect x="0.0000" y="-0.4888" width="61.7311" height="2.1604" fill="none" stroke="none" stroke-width="0.0"/>
</a>
</g>
<g transform="translate(28.8852, 165.1062)">
<text font-family="serif" font-size="2.2001" text-anchor="start" fill="currentColor">
<tspan>Music engraving by LilyPond 2.24.4—www.lilypond.org</tspan>
</text>
</g>
</svg>


上の例では `\acciaccatura` を用いていますが, `\grace` 等でも再現します.

これは既知のバグで, 左手譜に空の装飾音符を追加することにより解決できます.

```tex
\version "2.24.4"

\score {
  \new PianoStaff <<
    \new Staff \new Voice \relative c' {
      \acciaccatura d8 c1
    }
    \new Staff \new Voice \relative c {
      \clef "bass"
      \grace { s8 } %ここを追加する
      c1
    }
  >>

  \layout{}
}
```


<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" version="1.2" width="49.67mm" height="37.16mm" viewBox="0.0000 -0.0000 28.2639 21.1463">
<style type="text/css">
<![CDATA[
tspan { white-space: pre; }
]]>
</style>
<g transform="translate(5.6906, 9.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 8.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 7.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 6.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 5.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(21.2110, 16.6213)">
<rect x="0.0000" y="-2.0500" width="0.1900" height="4.0500" ry="0.0000" fill="currentColor"/>
</g>
<g transform="translate(21.2110, 7.6213)">
<rect x="0.0000" y="-2.0000" width="0.1900" height="4.0500" ry="0.0000" fill="currentColor"/>
</g>
<g transform="translate(21.2110, 3.8453)">
<rect x="0.0000" y="5.8260" width="0.1900" height="4.9500" ry="0.0000" fill="currentColor"/>
</g>
<g transform="translate(5.6906, 18.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 17.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 16.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 15.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 14.6213)">
<line stroke-linejoin="round" stroke-linecap="round" stroke-width="0.1000" stroke="currentColor" x1="0.0500" y1="0" x2="15.6604" y2="0"/>
</g>
<g transform="translate(5.6906, 10.6213)">
<rect x="9.0391" y="-0.1000" width="2.8737" height="0.2000" ry="0.1000" fill="currentColor"/>
</g>
<a style="color:inherit;" xlink:href="textedit:///mnt/c/Users/sugiura/Desktop/workdesk/tmp/grace.ly:15:6:7">
<g transform="translate(15.1509, 17.1213)">
<path transform="scale(0.0040, -0.0040)" d="M213 112c-50 0 -69 -43 -69 -88c0 -77 57 -136 134 -136c50 0 69 43 69 88c0 77 -57 136 -134 136zM491 0c0 -43 -34 -75 -72 -96c-53 -29 -114 -40 -174 -40s-120 11 -173 40c-38 21 -72 53 -72 96s34 75 72 96c53 29 113 40 173 40s121 -11 174 -40
c38 -21 72 -53 72 -96z" fill="currentColor"/>
</g>
</a>
<a style="color:inherit;" xlink:href="textedit:///home/sugiura/.local/src/lilypond-2.24.4/share/lilypond/2.24.4/ly/grace-init.ly:41:6:7">
<g transform="translate(13.3905, 7.6213)">
<path stroke-width="0.0800" stroke-linejoin="round" stroke-linecap="round" stroke="currentColor" fill="currentColor" d="M0.3750 3.3940C0.8007 4.1429 1.7961 4.4392 2.5620 4.0450L2.5620 4.0450C1.8303 4.3242 0.8350 4.0279 0.3750 3.3940z"/>
</g>
</a>
<g transform="translate(14.2434, 7.6213)">
<rect x="-0.0650" y="-0.3000" width="0.1300" height="2.6856" ry="0.0400" fill="currentColor"/>
</g>
<g transform="translate(5.3306, 12.1213)">
<path transform="scale(0.0040, -0.0040)" d="M-189 -1146c0 267 108 528 108 780c0 135 -33 261 -129 360c-3 3 -3 3 -3 6s0 3 3 6c96 99 129 225 129 360c0 252 -108 513 -108 780c0 189 45 366 177 501c3 3 9 6 12 6c9 0 15 -9 15 -18c0 -3 0 -9 -3 -12c-99 -99 -129 -225 -129 -360c0 -249 102 -504 102 -765
c0 -186 -45 -363 -174 -498c129 -135 174 -312 174 -498c0 -261 -102 -516 -102 -765c0 -135 30 -261 129 -360c3 -3 3 -9 3 -12c0 -9 -6 -18 -15 -18c-3 0 -9 3 -12 6c-132 135 -177 312 -177 501z" fill="currentColor"/>
</g>
<g transform="translate(5.6306, 12.1213)">
<rect x="0.0000" y="-6.5500" width="0.1600" height="13.1000" ry="0.0500" fill="currentColor"/>
</g>
<a style="color:inherit;" xlink:href="textedit:///mnt/c/Users/sugiura/Desktop/workdesk/tmp/grace.ly:10:20:21">
<g transform="translate(13.3905, 10.1213)">
<path transform="scale(0.0028, -0.0028)" d="M208 139c61 0 117 -33 117 -99c0 -71 -52 -119 -99 -147c-34 -20 -71 -32 -110 -32c-61 0 -116 33 -116 99c0 71 51 119 98 147c34 20 71 32 110 32z" fill="currentColor"/>
</g>
</a>
<g transform="translate(6.4906, 8.6213)">
<path transform="scale(0.0040, -0.0040)" d="M376 262c4 0 9 1 13 1c155 0 256 -128 256 -261c0 -76 -33 -154 -107 -210c-22 -17 -47 -28 -73 -36c3 -35 5 -70 5 -105c0 -19 -1 -39 -2 -58c-7 -120 -90 -228 -208 -228c-108 0 -195 88 -195 197c0 58 53 103 112 103c54 0 95 -47 95 -103c0 -52 -43 -95 -95 -95
c-11 0 -21 2 -31 6c26 -39 68 -65 117 -65c96 0 157 92 163 191c1 18 2 37 2 55c0 31 -1 61 -4 92c-29 -5 -58 -8 -89 -8c-188 0 -333 172 -333 374c0 177 131 306 248 441c-19 62 -37 126 -45 191c-6 52 -7 103 -7 155c0 115 55 224 149 292c3 2 7 3 10 3c4 0 7 0 10 -3
c71 -84 133 -245 133 -358c0 -143 -86 -255 -180 -364c21 -68 39 -138 56 -207zM461 -203c68 24 113 95 113 164c0 90 -66 179 -173 190c24 -116 46 -231 60 -354zM74 28c0 -135 129 -247 264 -247c28 0 55 2 82 6c-14 127 -37 245 -63 364c-79 -8 -124 -61 -124 -119
c0 -44 25 -91 81 -123c5 -5 7 -10 7 -15c0 -11 -10 -22 -22 -22c-3 0 -6 1 -9 2c-80 43 -117 115 -117 185c0 88 58 174 160 197c-14 58 -29 117 -46 175c-107 -121 -213 -243 -213 -403zM408 1045c-99 -48 -162 -149 -162 -259c0 -74 18 -133 36 -194
c80 97 146 198 146 324c0 55 -4 79 -20 129z" fill="currentColor"/>
</g>
<g transform="translate(10.6906, 7.6213)">
<path transform="scale(0.0040, -0.0040)" d="M359 27c-49 0 -75 42 -75 75c0 38 27 77 72 77c4 0 9 0 14 -1c-28 37 -72 59 -120 59c-106 0 -113 -73 -113 -186v-51v-51c0 -113 7 -187 113 -187c80 0 139 70 158 151c2 7 7 10 12 10c6 0 13 -4 13 -12c0 -94 -105 -174 -183 -174c-68 0 -137 21 -184 70
c-49 51 -66 122 -66 193s17 142 66 193c47 49 116 69 184 69c87 0 160 -64 175 -150c1 -5 1 -9 1 -13c0 -40 -30 -72 -67 -72z" fill="currentColor"/>
</g>
<g transform="translate(6.4906, 15.6213)">
<path transform="scale(0.0040, -0.0040)" d="M557 -125c0 28 23 51 51 51s51 -23 51 -51s-23 -51 -51 -51s-51 23 -51 51zM557 125c0 28 23 51 51 51s51 -23 51 -51s-23 -51 -51 -51s-51 23 -51 51zM232 263c172 0 293 -88 293 -251c0 -263 -263 -414 -516 -521c-3 -3 -6 -4 -9 -4c-7 0 -13 6 -13 13c0 3 1 6 4 9
c202 118 412 265 412 493c0 120 -63 235 -171 235c-74 0 -129 -54 -154 -126c11 5 22 8 34 8c55 0 100 -45 100 -100c0 -58 -44 -106 -100 -106c-60 0 -112 47 -112 106c0 133 102 244 232 244z" fill="currentColor"/>
</g>
<g transform="translate(10.6906, 16.6213)">
<path transform="scale(0.0040, -0.0040)" d="M359 27c-49 0 -75 42 -75 75c0 38 27 77 72 77c4 0 9 0 14 -1c-28 37 -72 59 -120 59c-106 0 -113 -73 -113 -186v-51v-51c0 -113 7 -187 113 -187c80 0 139 70 158 151c2 7 7 10 12 10c6 0 13 -4 13 -12c0 -94 -105 -174 -183 -174c-68 0 -137 21 -184 70
c-49 51 -66 122 -66 193s17 142 66 193c47 49 116 69 184 69c87 0 160 -64 175 -150c1 -5 1 -9 1 -13c0 -40 -30 -72 -67 -72z" fill="currentColor"/>
</g>
<a style="color:inherit;" xlink:href="textedit:///mnt/c/Users/sugiura/Desktop/workdesk/tmp/grace.ly:10:23:24">
<g transform="translate(15.1509, 10.6213)">
<path transform="scale(0.0040, -0.0040)" d="M213 112c-50 0 -69 -43 -69 -88c0 -77 57 -136 134 -136c50 0 69 43 69 88c0 77 -57 136 -134 136zM491 0c0 -43 -34 -75 -72 -96c-53 -29 -114 -40 -174 -40s-120 11 -173 40c-38 21 -72 53 -72 96s34 75 72 96c53 29 113 40 173 40s121 -11 174 -40
c38 -21 72 -53 72 -96z" fill="currentColor"/>
</g>
</a>
<g transform="translate(14.3084, 7.3613)">
<path transform="scale(0.0028, -0.0028)" d="M206 -219c18 0 32 -14 32 -32c0 -9 -4 -17 -11 -23l-357 -290c-5 -5 -11 -7 -18 -7h-1c-17 0 -31 15 -31 32c0 9 4 17 11 23l357 290c5 5 11 7 18 7z" fill="currentColor"/>
</g>
<g transform="translate(14.3084, 7.3613)">
<path transform="scale(0.0028, -0.0028)" d="M0 0c0 -196 207 -334 207 -530c0 -71 -15 -140 -41 -206c-5 -10 -14 -13 -23 -13c-14 0 -28 10 -28 26c0 2 1 3 1 5c26 59 42 123 42 188c0 101 -90 205 -158 280h-21v250h21z" fill="currentColor"/>
</g>
<g transform="translate(28.8852, 165.1062)">
<a xlink:href="https://lilypond.org/">
<rect x="0.0000" y="-0.4888" width="61.7311" height="2.1604" fill="none" stroke="none" stroke-width="0.0"/>
</a>
</g>
<g transform="translate(28.8852, 165.1062)">
<text font-family="serif" font-size="2.2001" text-anchor="start" fill="currentColor">
<tspan>Music engraving by LilyPond 2.24.4—www.lilypond.org</tspan>
</text>
</g>
</svg>

他にも繰り返し記号などに関しても同様のバグが発生しますが, 同じように空の装飾音符を挿入することで解決できます.


# 参考文献

* [Clef que ne s'affiche pas correctement avec une acciaccatura, grace ou appoggiatura... - Général - LilyPond](https://lilypond.community/t/clef-que-ne-saffiche-pas-correctement-avec-une-acciaccatura-grace-ou-appoggiatura/5702)

