+++
title = "URLをコピーするブックマークレット"
date = 2021-05-09
[taxonomies]
tags = ["JavaScript"]
+++

マークダウン形式で表示しているページのタイトルと URL をコピーするブックマークレット.
* [Markdownメモに便利なブックマークレット](https://zenn.dev/iwaku/articles/cfeda1c48f48991f4cf9)

Wikipedia 形式で表示しているページのタイトルと URL をコピーするブックマークレット.

```javascript
javascript:(function(){const e=document.createElement('input');var date = new Date();e.value=`{{Cite web |url=${location.href} |title=${document.title} |accessdate=${date.getFullYear()}-${(date.getMonth()+1).toString().padStart(2,'0')}-${(date.getDate()).toString().padStart(2,'0')}}}`;document.querySelector('body').append(e);e.select();document.execCommand('copy');e.remove();})();
```

いずれも Firefox 88.0.1 (Win10) で動作確認済み.


# メモ

* いつからか Firefox ではアドレスバーから直接 JavaScript を実行する機能はデフォルトでは無効に変更されている模様 (ブックマークレットの動作には影響しない). 開発はウェブ開発ツールで行うのが簡単.
* ファビコンを設定する過去のハックはすべて動作しなくなっている模様 ([参考文献](https://superuser.com/questions/56823/how-can-i-add-a-favicon-to-a-bookmarklet-in-firefox)).


# 参考文献
* [Bookmarkletを作ろう(準備編） - Qiita](https://qiita.com/kanaxx/items/63debe502aacd73c3cb8)
* [日付（Date） - とほほのWWW入門](https://www.tohoho-web.com/js/date.htm)
