from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

wordcloud_dir = path.dirname(__file__)
text = open(path.join(wordcloud_dir, 'trump.txt'), 'r', encoding='utf-8').read()

# 创建背景图片的ndarray
trump_coloring = np.array(Image.open(path.join(wordcloud_dir, 'trump.png')))

# 从wordcloud中导入stopwords，这些词语多为人称、语气、连接词，要从词云中剔除
stopwords = set(STOPWORDS)
stopwords.add('said')

# 创建词云
wc = WordCloud(background_color='white', max_words=2000, mask=trump_coloring, stopwords=stopwords, max_font_size=80, random_state=42)
wc.generate(text)

image_colors = ImageColorGenerator(trump_coloring)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.figure()

plt.imshow(wc.recolor(color_func=image_colors), interpolation='bilinear')
plt.axis("off")
plt.figure()

plt.show()
