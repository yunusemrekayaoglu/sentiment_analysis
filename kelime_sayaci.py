import zeyrek
from nltk.tokenize import RegexpTokenizer
from collections import Counter
from wordcloud import WordCloud
from nltk.corpus import stopwords
import string
import matplotlib.pyplot as plt
import pandas as pd


noktalama = string.punctuation # string kütüphanesindeki noktalama işaretleri
stop_words = set(stopwords.words('turkish')) # nltk kütüphanesindeki türkçe stop wordsler
lemmatizer = zeyrek.MorphAnalyzer() # zeyrek kütüphanesi ile lemmatizer oluşturulur
tokenizer = RegexpTokenizer(r'[\w+]') # noktalama işaretlerini kaldırır
tr2eng = str.maketrans("çğıöşü", "cgiosu") # türkçe karakterleri ingilizce karakterlere çevirir


temp=  []
yorumlar = pd.read_csv('./data/yorumlar.csv')

yorumlar["Yorum_Icerik"] = yorumlar["Yorum_Icerik"].apply(
        lambda x: " ".join(word.lower() for word in x.split()))  # küçük harfe çevirme
yorumlar["Yorum_Icerik"] = yorumlar["Yorum_Icerik"].str.translate(tr2eng)  # türkçe karakterleri ingilizce karakterlere çevirme
yorumlar["Yorum_Icerik"] = yorumlar["Yorum_Icerik"].str.replace("[^\w\s]", "")  # noktalama işaretlerini kaldırma
yorumlar["Yorum_Icerik"] = yorumlar["Yorum_Icerik"].str.replace(noktalama, " ")  # noktalama işaretlerini kaldırma
yorumlar["Yorum_Icerik"] = yorumlar["Yorum_Icerik"].str.replace("\d", "")  # rakamları kaldırma
yorumlar["Yorum_Icerik"] = yorumlar["Yorum_Icerik"].apply(
        lambda x: " ".join(word for word in x.split() if word not in stop_words))
yorumlar["Yorum_Icerik"] = yorumlar["Yorum_Icerik"].apply(
        lambda x: " ".join(lemmatizer.lemmatize(word)[0][0] for word in x.split()))

kelime_sayaci = Counter(yorumlar["Yorum_Icerik"].str.cat(sep=' ').split()).most_common(20)
for i in kelime_sayaci:
    print(i)

cloud = WordCloud(max_font_size=80, colormap="hsv").generate_from_frequencies(dict(kelime_sayaci))
plt.figure(figsize=(16, 12))
plt.imshow(cloud, interpolation='bilinear')
plt.axis("off")
plt.show()

yorumlar.to_csv("./data/yorumlar_clean.csv", index=False)
