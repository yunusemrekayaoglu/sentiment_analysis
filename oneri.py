from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


import pandas as pd

train = pd.read_excel("./data/lemmali_isaretli_1524.xlsx")
test = pd.read_csv("./data/yorumlar_clean.csv")

# X_train, X_test, y_train, y_test = train_test_split(train["Yorum_Icerik"], train["Isaret"], test_size=0.2, random_state=42)
# XX_train, XX_test = train_test_split(test["Yorum_Icerik"], test_size=0.2, random_state=42)
#
# count_vect = CountVectorizer()
# X_train_counts = count_vect.fit_transform(X_train)
#
# tfidf_transformer = TfidfTransformer()
# X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
#
# clf = MultinomialNB().fit(X_train_tfidf, y_train)
#
# XX_test_counts = count_vect.transform(XX_test)
# XX_test_tfidf = tfidf_transformer.transform(XX_test_counts)
#
# y_pred = clf.predict(XX_test_tfidf)
# counter = 0
# for review, sentiment in zip(XX_test[:], y_pred[:]):
#     print("\nReview:", review, "\nSentiment:", sentiment)




# MultinomialNB

# vectorizer = CountVectorizer()
# X_train = vectorizer.fit_transform(train["Yorum_Icerik"])
# Y_train = train["Isaret"]
#
# clf = MultinomialNB()
# clf.fit(X_train, Y_train)
#
# X_test = vectorizer.transform(test["Yorum_Icerik"])
# y_pred = clf.predict(X_test)
#
# new_df = []
#
# for comment, prediction in zip(test["Yorum_Icerik"], y_pred):
#     print("\nReview:", comment, "\nSentiment:", prediction)
#     print("-----------------------------------------")
#     new_df.append([comment, prediction])


# DecisionTreeClassifier

# vectorizer = CountVectorizer()
# X_train = vectorizer.fit_transform(train["Yorum_Icerik"])
# Y_train = train["Isaret"]
#
# clf = DecisionTreeClassifier()
# clf.fit(X_train, Y_train)
#
# X_test = vectorizer.transform(test["Yorum_Icerik"])
# y_pred = clf.predict(X_test)
#
# new_df = []
#
# for comment, prediction in zip(test["Yorum_Icerik"], y_pred):
#     print("\nReview:", comment, "\nSentiment:", prediction)
#     print("-----------------------------------------")
#     new_df.append([comment, prediction])
#


# RandomForestClassifier

# vectorizer = CountVectorizer()
# X_train = vectorizer.fit_transform(train["Yorum_Icerik"])
# Y_train = train["Isaret"]
#
# clf = RandomForestClassifier()
# clf.fit(X_train, Y_train)
#
# X_test = vectorizer.transform(test["Yorum_Icerik"])
# y_pred = clf.predict(X_test)
#
# new_df = []
#
# for comment, prediction in zip(test["Yorum_Icerik"], y_pred):
#     print("\nReview:", comment, "\nSentiment:", prediction)
#     print("-----------------------------------------")
#     new_df.append([comment, prediction])
#



# accuracy_score

vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(train["Yorum_Icerik"])
Y_train = train["Isaret"]

clf = RandomForestClassifier()
clf.fit(X_train, Y_train)

X_test = vectorizer.transform(test["Yorum_Icerik"])
y_pred = clf.predict(X_test)

new_df = []

for comment, prediction in zip(test["Yorum_Icerik"], y_pred):
    print("\nReview:", comment, "\nSentiment:", prediction)
    print("-----------------------------------------")
    new_df.append([comment, prediction])

new_df = pd.DataFrame(new_df, columns=["Yorum_Icerik", "Isaret"])
new_df.to_excel("./data/sonuclar.xlsx", index=False)