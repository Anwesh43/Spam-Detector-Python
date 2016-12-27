import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
class SpamDetector:
    def __init__(self):
        self.df = pd.read_table('sms.tsv',header=None,names=['label','message'])
        self.df['label_num'] = self.df.label.map({'ham':0,'spam':1})
        self.Y = self.df['label_num']
        self.X = self.df['message']
        self.X_train,self.X_test,self.Y_train,self.Y_test = train_test_split(self.X,self.Y,random_state=1)
        self.Y_train = self.Y_train.as_matrix()
        self.Y_test = self.Y_test.as_matrix()
        self.__convertToVectors()


    def __convertToVectors(self):
        vectorizer = CountVectorizer()
        x_train_dtm = vectorizer.fit_transform(self.X_train)
        self.x_train = x_train_dtm.toarray()
        x_test_dtm = vectorizer.transform(self.X_test)
        self.x_test = x_test_dtm.toarray()
    def train(self):
        self.nb = MultinomialNB()
        self.nb.fit(self.x_train,self.Y_train)
    def test(self):
        new_y_test = []
        for x in self.x_test:
            new_y_test.append(self.nb.predict(x))
        print len(new_y_test)
        print len(self.Y_test)
        correct = 0
        for i in range(0,len(new_y_test)):
            y = self.Y_test[i]
            new_y = new_y_test[i]
            if y == new_y:
                correct = correct+1
        print float((correct*1.0)/len(new_y_test))
spamDetector = SpamDetector()
spamDetector.train()
spamDetector.test()
