import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from shutil import unpack_archive
from PIL import Image
import cv2
from sklearn.model_selection import train_test_split

import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import accuracy_score, classification_report

class ImageClass:
    def __init__(self, csv):
        self.read_data(csv)
    
    def read_data(self, csv):
        self.df = pd.read_csv(csv)
    
    def prepare_data(self):
        labelencoder = LabelEncoder()
        # First, split
        self.train_df, self.val_df = train_test_split(self.df, test_size=0.2)

        # Then, prepare for modeling
        self.train_images = [self.process_image(path) for path in self.train_df['file_name']]
        self.train_images = np.array(self.train_images)
        self.train_label = np.array(self.train_df['label'])

        self.val_images = [self.process_image(path) for path in self.val_df['file_name']]
        self.val_images = np.array(self.val_images)
        self.val_label = np.array(self.val_df['label'])

    def process_image(self, image_path, size = (224, 224)):
        im = cv2.imread(image_path)
        resized_im = cv2.resize(im, size)
        normalized_im = resized_im/255
        return normalized_im

    def train_model(self):
        model = models.Sequential()
        model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)))
        model.add(layers.MaxPooling2D((2, 2)))
        model.add(layers.Flatten())
        model.add(layers.Dense(1, activation=None))
        model.add(layers.Dense(1, activation='sigmoid'))
        model.compile(optimizer='adam', loss='binary_crossentropy')
        
        model.summary()
        model.fit(self.train_images, self.train_label, epochs=2)
        self.model = model
    
    def evaluate_model(self):
        self.predictions = self.model.predict(self.val_images)
        sns.histplot(self.predictions)
        plt.show()
        self.binary_predictions = (self.predictions > 0.8).astype(int)
        accuracy = accuracy_score(self.val_label, self.binary_predictions)
        print('The model has a validation accuracy of: ', accuracy)
        report = classification_report(self.val_label, self.binary_predictions)
        print(report)

if __name__ == '__main__':
    image = ImageClass('train.csv')
    print(image.df.label)
    image.prepare_data()
    print(image.train_images.shape)
    print(image.train_label.shape)
    image.train_model()
    image.evaluate_model()

    