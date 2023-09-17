Hepsiburada E ticaret sitesinden veri çekerek Sentiment Analysis

## 1. Ürün Çekme

- Harici Kütüphaneler:
!pip install requests
!pip install beautifulsoup4
!pip install tqdm
- Nasıl Kullanılır?
Programı çalıştırdıktan sonra sizden, "ürün adı, ürün linki, sayfa sayısı" isteyecektir. Bu değişkenleri programa vererek size uygun verisetini oluşturmasını bekleyebilirsiniz.
- Nasıl Çalışır?
![image](https://github.com/yunusemrekayaoglu/hepsiburada_sentiment_analysis/assets/77890503/2c82fa60-4656-4484-bf22-7967264b7cf6)
buradaki veriyi alıp içerisindeki yorumu ve ürüne verilen yıldızı çekiyoruz.


## 2. Kelime Sayacı


- Nasıl Kullanılır?
1. programı çalıştırdıktan sonrasında bu aşamada manuel değişim yapmanıza gerek yoktur. Çalıştırsanız yeterli olacaktır.
- Nasıl Çalışır?
Burada elimizde bulunan verileri daha temiz bir hale getiriyoruz. Türkçe harfleri, noktalama işaretleri ve özel karakterleri kullanarak temizliyoruz.
Sonraki adımda bize en çok kullanılan 20 kelimeyi getirecek.
![image](https://github.com/yunusemrekayaoglu/hepsiburada_sentiment_analysis/assets/77890503/8c19e7e2-4ff6-4296-b629-954aad5cf4f9)
En sondaki adımımızda ise bize wordCloud getirecek.
![image](https://github.com/yunusemrekayaoglu/hepsiburada_sentiment_analysis/assets/77890503/a9992395-ff61-47a7-9443-3221b218a5b9)

## 3. Öneri
