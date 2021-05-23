+++
title = "EPUBのファイル構造"
date = 2021-05-10
[extra]
toc = true
[taxonomies]
tags = ["EPUB"]
+++

# 仕様書

最新版である EPUB 3.2 の仕様は以下の6つのドキュメントに分かれています.
原文は当然英語ですが, ありがたいことに Wataru Yoshimura さんにより非公式の日本語訳が公開されています[^1].
* [EPUB 3.2 日本語訳](https://imagedrive.github.io/Submission/epub32/epub-spec.html)
* [EPUB Packages 3.2 日本語訳](https://imagedrive.github.io/Submission/epub32/epub-packages.html)
* [EPUB Content Documents 3.2 日本語訳](https://imagedrive.github.io/Submission/epub32/epub-contentdocs.html)
* [EPUB Media Overlays 3.2 日本語訳](https://imagedrive.github.io/Submission/epub32/epub-mediaoverlays.html)
* [EPUB Open Container Format (OCF) 3.2 日本語訳](https://imagedrive.github.io/Submission/epub32/epub-ocf.html)
* [EPUB Accessibility 1.0](http://idpf.org/epub/a11y/accessibility.html)

また, これら仕様の概要をまとめたものとして次の文書があります.
* [EPUB 3 Overview](https://imagedrive.github.io/Submission/epub32/epub-overview.html) - EPUB 3 の概要をまとめたもの.


# ファイル構造

必須ファイルおよび最小限の本文を用意した EPUB ファイルは次のような構造を持ちます.

```
├─ mimetype 
├─ META-INF
│    └─ container.xml
└─ EPUB 
     ├─ package.opf
     ├─ toc.xhtml
     └─ 001.xhtml
```

## mimetype

* [EPUB OCF §4.3](https://imagedrive.github.io/Submission/epub32/epub-ocf.html#sec-zip-container-mime)

EPUB ファイルには `mimetype` というファイルが存在しなければなりません. そして, その内容は `application/epub+zip` で, 余計な空白を入れてはいけません
(従ってファイルサイズは 20 byte になります).


## META-INF

* [EPUB OCF §3.5](https://imagedrive.github.io/Submission/epub32/epub-ocf.html#sec-container-metainf) 

EPUB ファイルには `META-INF` ディレクトリが存在しなければなりません. そして, このディレクトリに `container.xml` というファイルが存在する必要があります.
その他のファイルは optional で必要ありません.

`container.xml` では文書の情報を記述した `package.opf` のパスを指定します. 
このファイルを [パッケージ ドキュメント](https://imagedrive.github.io/Submission/epub32/epub-spec.html#dfn-package-document) と呼びます.
次の例では `EPUB` ディレクトリにある `package.opf` というファイルをパッケージドキュメントとして指定しています.

```xml
<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="EPUB/package.opf" media-type="application/oebps-package+xml" />
  </rootfiles>
</container>
```

なおパッケージドキュメントの場所は任意です. ここでは仕様書のように `EPUB` ディレクトリに収めましたが, `OEBPS` という名称もよく使われるようです
([Open EBook Publication Structure](https://imagedrive.github.io/Submission/epub32/epub-overview.html#epub2) の略のようです).


## パッケージドキュメント

ひとつのパッケージドキュメントはひとつの EPUB パッケージを定めます ([参考](https://imagedrive.github.io/Submission/epub32/epub-spec.html#dfn-epub-package)).
その詳細は [EPUB Packages 3.2 日本語訳](https://imagedrive.github.io/Submission/epub32/epub-packages.html) で定義されています.

* [EPUB Packages §3.4.1](https://imagedrive.github.io/Submission/epub32/epub-packages.html#sec-package-elem)

パッケージドキュメントのルート要素は `package` であり, 日本語文書ならばおおよそ次の例のようになるはずです. 
必要ならば `dir="rtl"` 属性も指定しますが, 以下では「左→右」 (ltr) 文書を前提とします.
`package` 要素は `metadata`, `manifest`, `spine` という要素をそれぞれひとつずつ含んでいる必要があります.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<package unique-identifier="pub-id" version="3.0" xmlns="http://www.idpf.org/2007/opf" xml:lang="ja">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:identifier id="pub-id">urn:uuid:702bb9c7-f6cb-c781-2246-da0bd72535fc</dc:identifier>
    <dc:title>EPUBのファイル構造</dc:title>
    <dc:language>ja</dc:language>
    <meta property="dcterms:modified">2021-05-10T12:00:00Z</meta>
  </metadata>

  <manifest>
    <!-- ここで文書を構成するファイルをすべて指定する -->
  </manifest>

  <spine>
    <!-- ここでファイルを表示する順番を指定する -->
  </spine>
</package>
```

`metadata` 要素については上述のものが必須です. 適当に一意識別子, タイトル, 言語, 最終更新日を埋めてください.

### manifest

* [EPUB Packages §3.4.4](https://imagedrive.github.io/Submission/epub32/epub-packages.html#sec-pkg-manifest)

パッケージドキュメントの `manifest` 要素には文書を構成するファイルをすべて順不同で並べます.
目次情報 `toc.xhtml` と本文 `001.xhtml` のふたつのファイルを指定する場合はこちら.

```xml
<manifest>
  <item id="toc" href="toc.xhtml" media-type="application/xhtml+xml" properties="nav"/>
  <item id="main-001.xhtml" href="001.xhtml" media-type="application/xhtml+xml"/>
</manifest>
```

なお, EPUB には目次ファイル (`properties="nav"`) が存在する必要があります ([EPUB Packages §5](https://imagedrive.github.io/Submission/epub32/epub-packages.html#sec-package-nav)). 
また, MathML を含むファイルにはここで `properties="mathml"` 属性を明示する必要があります.

### spine

`spine` 要素ではファイルを表示する順番を指定します.

```xml
<spine page-progression-direction="default">
  <itemref idref="toc"/>
  <itemref idref="main-001.xhtml"/>
</spine>
```


## 目次

目次は HTML をつくる感じで適当に作ればよいです. 必ずしも spine に含める必要はありません ([EPUB Packages §5.2](https://imagedrive.github.io/Submission/epub32/epub-packages.html#sec-package-nav-content-conf)).
`ol` を入れ子にする場合は, 章題を表す `span` (または `a`) が必要です.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="ja" lang="ja">
<head>
  <title>目次</title>
</head>
<body>
  <nav xmlns:epub="http://www.idpf.org/2007/ops" epub:type="toc">
    <h1>目次</h1>
    <ol>
      <li><a href="001.xhtml">二次方程式の解の公式</a></li>
	  <li>
	    <span>Galois 理論</span>
		<ol>
		  <li>Galois 群</li>
		  <li>五次方程式の解の公式</li>
	    </ol>
	  </li>
    </ol>
  </nav>
</body>
</html>
```

なお EPUB 2 では [NCX](https://imagedrive.github.io/Submission/epub32/epub-packages.html#sec-opf2-ncx) というものがありましたが, 
EPUB 3 ではこの機能は上記ファイルに置き換えられたため, EPUB 3 対応リーダーのみをサポートするならば NCX ファイルは不要です.


## 本文

ファイル名に関する制約は [EPUB-OCF §3.4](https://imagedrive.github.io/Submission/epub32/epub-ocf.html#sec-container-filenames) にまとめられています.
255bytes 以下で危なそうな文字 (ASCII だと`/`, `<`, `>`, `*`, `"`, `:`, `?`, `\`, `|` など) は含めることができません.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="ja" lang="ja">
<head>
  <title>二次方程式の解の公式</title>
</head>
<body>
  二次方程式 <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline" alttext="ax^2 + bx + c = 0"><mi>a</mi><msup><mi>x</mi><mn>2</mn></msup><mo>+</mo><mi>b</mi><mi>x</mi><mo>+</mo><mi>c</mi><mo>=</mo><mn>0</mn></math> の解の公式は次式により与えられる.
  <math xmlns="http://www.w3.org/1998/Math/MathML" display="block" alttext="x = \frac{ - b \pm \sqrt{ b^2 - 4 a c } }{ 2 a }"><mi>x</mi><mo>=</mo><mfrac><mrow><mo>-</mo><mi>b</mi><mo>±</mo><msqrt><mrow><msup><mi>b</mi><mn>2</mn></msup><mo>-</mo><mn>4</mn><mi>a</mi><mi>c</mi></mrow></msqrt></mrow><mrow><mn>2</mn><mi>a</mi></mrow></mfrac></math>
</body>
</html>
```


# EPUB ファイルの作成

## zip 圧縮

EPUB ファイルは上記の一連のファイルを zip で固めたものです. mimetype は圧縮せず, 拡張フィールドも使用してはいけないことに注意して作成します
(ZIP ファイルについては [[Rust] zip ファイルを読む - Qiita](https://qiita.com/osanshouo/items/cb1a86b8f2fdb5e12446) を参照).

```bash
zip -0X math.epub mimetype
zip -9r math.epub META-INF EPUB
```

## 妥当性検証

[EPUB Validator (beta)](http://validator.idpf.org/) にて作成した EPUB が仕様を満足するかチェックすることができます.


# 参考文献
* [EPUBファイルを手で作ってみる。 - Tech Do | メディアドゥの技術ブログ](https://techdo.mediado.jp/entry/2019/04/01/112244)
* [電子書籍づくり実践（書誌情報を書く） - 本好きに送る「電子書籍のつくり方」講座](http://k-airyuu.hatenablog.com/entry/2014/03/07/152655)

[^1]: アクセシビリティの規定は SHOULD であり, 必ずしも満たさなくてもよいです ([EPUB3.2 §2.1](https://imagedrive.github.io/Submission/epub32/epub-spec.html#sec-epub-pub-conf)). 
