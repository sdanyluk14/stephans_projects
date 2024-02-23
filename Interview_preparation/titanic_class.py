import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
import seaborn as sns

class TitanicModel:
    def __init__(self, csv):
        self.read_data(csv)

    def read_data(self, csv):
        self.df = pd.read_csv(csv)
    
    def prepare_data(self):
        self.df.dropna()
        self.x_cols = ['Age', 'Fare', 'Sex']
    
    def split_data(self):
        X = self.df[self.x_cols]
        y = self.df['2urvived']
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size = 0.2, random_state=42)

    def train(self):
        self.model = GradientBoostingClassifier()
        self.model.fit(self.X_train, self.y_train)
    
    def predict_and_evalauate(self):
        self.predictions = self.model.predict(self.X_test)
        self.probs = self.model.predict_proba(self.X_test)[:,1]
        accuracy = accuracy_score(self.y_test, self.predictions)
        print(accuracy)
        class_report = classification_report(self.y_test, self.predictions)
        print(class_report)
    
    
if __name__ == '__main__':
    titanic = TitanicModel('titanic_df.csv')
    titanic.prepare_data()
    titanic.split_data()
    titanic.train()
    titanic.predict_and_evalauate()
    
