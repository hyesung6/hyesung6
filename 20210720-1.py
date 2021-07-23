import matplotlib.pyplot as plt
# import numpy as np
# from sklearn.datasets import make_circles
# x, y = make_circles(n_samples=100, noise=0.09)
#
# for a,b in zip(x, y) :
#     print(a, "::", b)
#
# rgb = np.array(["r", "g", "b"])
# print(rgb)
# plt.scatter(x[:, 0], x[:, 1], color=rgb[y])
# plt.show()


######## iris #########
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split

sns.set(style='ticks', color_codes = True)
iris = sns.load_dataset("iris")
# g = sns.pairplot(iris, hue="species", palette="husl")
# plt.show()

print(iris["species"].unique())

from sklearn.preprocessing import LabelEncoder
x = iris.iloc[:, 0:4].values
y = iris.iloc[:, 4].values
encoder = LabelEncoder()
y1 = encoder.fit_transform(y);
Y = pd.get_dummies(y1).values;      print(Y)
xTrain, xTest, yTrain, yTest \
    = train_test_split(x, Y, test_size=0.2, random_state=1)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
model = Sequential()
model.add(Dense(64, input_shape=(4,), activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(3, input_shape=(4,), activation='softmax'))
model.compile(loss="categorical_crossentropy",
              optimizer="Adam", metrics=["accuracy"])
model.summary()
hist = model.fit(xTrain, yTrain, validation_data=(xTest, yTest),
                 epochs=100)
loss, accuracy = model.evaluate(xTest, yTest)
print("Accuracy = {:.2f}".format(accuracy))
plt.figure(figsize=(12, 8))
plt.plot(hist.history['loss']);
plt.plot(hist.history['val_loss'])
plt.plot(hist.history['accuracy']);
plt.plot(hist.history['val_accuracy'])
plt.legend(['loss', 'val_loss', 'acc', 'val_acc'])
plt.grid();

from sklearn.metrics import classification_report, \
    confusion_matrix

yPred = model.predict(xTest)
yTestClass = np.argmax(yTest, axis=1)
yPredClass = np.argmax(yPred, axis=1)

print(classification_report(yTestClass, yPredClass))
print(confusion_matrix(yTestClass, yPredClass))

testSet = np.array([[5,2.9, 1, 0.2]])
print("Predicted target name: {}".format(
    iris['species'].unique()[
        model.predict_classes(testSet)]))



plt.show()