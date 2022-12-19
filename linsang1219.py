import wordcloud
import jieba

str = jieba.lcut('未来属于那些相信梦想之美的人')
text = ''.join(str)
cloud = wordcloud.WordCloud(font_path='simsun.ttc').generate(text)
cloud.to_file('chinese_cloud.jpg')
