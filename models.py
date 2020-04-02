import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model, mixture
from sklearn.metrics import mean_squared_error, r2_score
import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

with open("output/billboardHot100_Lyrics_2000_1.csv", encoding='utf-8-sig', mode='r') as csv_file:
    df = pd.read_csv("processed/billboardHot100_Lyrics_2000_1.csv", header = None)
    #print(df.head())
    df.columns = ['title', 'artist', 'lyrics', 'peakpos', 'lastpos', 'numWeeks', 'currentPos', 'isNew', 'pos', 'neu', 'neg', 'dale', 'diff']
    #print(df['title'])
    features = list(df.columns.values)
    features.remove('title')
    features.remove('artist')
    features.remove('currentPos')
    features.remove('lyrics')
    X = df[features]
    y = df['currentPos']



# Create linear regression object
regr = GaussianNB()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
# Train the model using the training sets
regr.fit(X_train, y_train)
print(regr.score(X_train, y_train))
#pred = np.array([[13, 7, 3, 0, 3, 49, 10, 31.34, 28]])
# print('------------')
pred = regr.predict(X_test)
print(pred - y_test)
print(y_test)