# Extracting Data from Hepsiburada E-commerce Website for Sentiment Analysis


## 1. Data Extraction

- External Libraries:
!pip install requests
!pip install beautifulsoup4
!pip install tqdm

- How to Use:
After running the program, it will ask for "product name, product link, page count" from you. By providing these variables to the program, you can expect it to create a suitable dataset for you.

- How it Works:
![image](https://github.com/yunusemrekayaoglu/hepsiburada_sentiment_analysis/assets/77890503/2c82fa60-4656-4484-bf22-7967264b7cf6)
We extract the data from here, including the comments and the star ratings given to the product.


## 2. Word Counter



- How to Use:
You don't need to make any manual changes at this stage after running the program. Just run it, and it will be sufficient.

- How it Works:
Here, we clean the data we have, using Turkish letters, punctuation marks, and special characters.
In the next step, it will provide us with the top 20 most frequently used words.

![image](https://github.com/yunusemrekayaoglu/hepsiburada_sentiment_analysis/assets/77890503/8c19e7e2-4ff6-4296-b629-954aad5cf4f9)

In the last step, it will generate a word cloud for us.


![image](https://github.com/yunusemrekayaoglu/hepsiburada_sentiment_analysis/assets/77890503/a9992395-ff61-47a7-9443-3221b218a5b9)

## 3. Öneri

...
