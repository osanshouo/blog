+++
title = "matplotlibでWebM動画を作成"
date = 2021-06-04
[taxonomies]
tags = ["Python", "matplotlib", "動画"]
+++

matplotlib で作成したアニメーションは mp4 で保存することが多いですが, 直接 WebM 形式で出力することもできます.
ただし, その場合コーデックを明示的に指定する必要があります.
現時点では av1 のエンコード速度は個人ユースでは実用に耐えないレベルで遅いので[^1], おそらく vp9 が唯一の選択肢でしょう.
私の体感では, 解像度 1200x1200, 30 fps (`interval=33`) のアニメーションを vp9 で出力するならば, 
ビットレート 2178 kb/s もあればデフォルトの mp4 と遜色のないクオリティのアニメーションが作れると思います.

```python
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure( figsize=(12, 12) )
ax = fig.add_subplot(111)

def update(angle):
    ax.cla()
    # 実装は省略 #
    
anim = FuncAnimation(fig, update, frames=range(128), interval=33)
anim.save("anim.webm", writer="ffmpeg", codec='libvpx-vp9', bitrate=1024*3)
#plt.show()
plt.close()
```

[^1]: rav1e と libaom の速度比較は一年以上前の記事が多く, 最新の動向が気になるところです.
