# -*- coding: utf-8 -*-
"""Copy of Pancreatic cancer model

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bLNqI68Xuf6_uWay6FqpUbhK_ZxXDZBa
"""

import kagglehub
import pandas as pd
import os

# Download latest version
path = kagglehub.dataset_download("johnjdavisiv/urinary-biomarkers-for-pancreatic-cancer")

print("Path to dataset files:", path)

# List the files in the dataset directory
files = os.listdir(path)
print("Files in dataset:", files)

# Load and print the first CSV file as an example
for file in files:
  if file.endswith(".csv"):
    file_path = os.path.join(path, file)
    print(f"Loading {file_path}")
    df = pd.read_csv(file_path)
    print("Dataset Preview:")
    print(df.head()) # Print the first 5 rows

import pandas as pd
import numpy as np
import os


# File path for the main dataset

data_file_path = '/root/.cache/kagglehub/datasets/johnjdavisiv/urinary-biomarkers-for-pancreatic-cancer/versions/1/Debernardi et al 2020 data.csv'


# Load the dataset

df = pd.read_csv(data_file_path)


# Display dataset structure and preview

print("Dataset Structure:")

print(df.info())

print("First 5 rows:")

print(df.head())
df['sex'] = df['sex'].map({'M': -1, 'F': 1})

df['sample_origin'] = df['sample_origin'].map({
    'BPTB': 1,
    'LIV': 2
}).fillna(3)

Y = df["diagnosis"].tolist()

selected_columns = ['LYVE1', 'REG1B', 'plasma_CA19_9', 'age', 'sex', 'sample_origin'] #research and find suitable features


#normalize
X = df[selected_columns].values.tolist()

X = [[0 if np.isnan(value) else value for value in row] for row in X]

from sklearn.preprocessing import StandardScaler
import numpy as np

# Convert X to a NumPy array if it isn't one already
X = np.array(X, dtype=float)

# Initialize the scaler
scaler = StandardScaler()

# Fit the scaler to the data and transform it
X = scaler.fit_transform(X)

print(X)

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
#train test split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=42)

print(X_test[0])
neuralNetwork = MLPClassifier(activation='relu', max_iter=1000, hidden_layer_sizes=(500, 250, 150, 2,)).fit(X_train, y_train)

#predictions
NNpredictions  = neuralNetwork.predict(X_test)
NNTrainpredictions = neuralNetwork.predict(X_train)
"""
print(NNpredictions[2])
print(y_test[2])
"""
# testing data accuracy
test_counter = 0
for i in range(len(X_test)):
  if y_test[i] == NNpredictions[i]:
    test_counter += 1
NN_test_accuracy = test_counter/len(X_test)
print("NN test accuracy: ", NN_test_accuracy)

# training data accuracy
train_counter = 0
for i in range(len(X_train)):
  if y_train[i] == NNTrainpredictions[i]:
    train_counter += 1
NN_train_accuracy = train_counter/len(X_train)
print("NN train accuracy: ", NN_train_accuracy)


print(" ")

# 1st case predictions
NN_1 = 0
NN_1_correct = 0
for i in range(len(X_test)):
  if y_test[i] == 1:
    NN_1 +=1
    if NNpredictions[i] == 1:
      NN_1_correct+=1
NN_1_accuracy = (NN_1_correct/NN_1)
print("Cases of first class: ", NN_1)
print("Correctly predicted cases of first class", NN_1_correct)
print("first class accuracy ", NN_1_accuracy)

print(" ")
# 2nd case predictions
NN_2 = 0
NN_2_correct = 0
for i in range(len(X_test)):
  if y_test[i] == 2:
    NN_2 +=1
    if NNpredictions[i] == 2:
      NN_2_correct+=1
NN_2_accuracy = (NN_2_correct/NN_2)
print("Cases of second class: ", NN_2)
print("Correctly predicted cases of second class", NN_2_correct)
print("second class accuracy ", NN_2_accuracy)
print(" ")


# 3rd case predictions
NN_3 = 0
NN_3_correct = 0
for i in range(len(X_test)):
  if y_test[i] == 3:
    NN_3 +=1
    if NNpredictions[i] == 3:
      NN_3_correct+=1
NN_3_accuracy = (NN_3_correct/NN_3)
print("Cases of third class: ", NN_3)
print("Correctly predicted cases of third class", NN_3_correct)
print("third class accuracy ", NN_3_accuracy)
print(" ")

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
for depth in range(2, 18):
  #hyperparameter tuning
  decisionTree = DecisionTreeClassifier(criterion='entropy', random_state=0, max_depth=depth).fit(X_train, y_train)
  print(depth)
  #predictions
  DTpredictions  = decisionTree.predict(X_test)
  DTTrainpredictions = decisionTree.predict(X_train)

  # testing data accuracy
  test_counter = 0
  for i in range(len(X_test)):
    if y_test[i] == DTpredictions[i]:
      test_counter += 1
  DT_test_accuracy = test_counter/len(X_test)
  print("DT test accuracy: ", DT_test_accuracy)

  # training data accuracy
  train_counter = 0
  for i in range(len(X_train)):
    if y_train[i] == DTTrainpredictions[i]:
      train_counter += 1
  DT_train_accuracy = train_counter/len(X_train)
  print("DT train accuracy: ", DT_train_accuracy)

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
#test accuracies w for loop to find max depth. like done in DT

#model
randomForrest = RandomForestClassifier(max_depth=5, random_state=0, n_estimators = 100).fit(X_train, y_train)
#predictions
RFpredictions = randomForrest.predict(X_test)
RFTrainpredictions = randomForrest.predict(X_train)

# testing data accuracy
test_counter = 0
for i in range(len(X_test)):
  if y_test[i] == RFpredictions[i]:
    test_counter += 1
RF_test_accuracy = test_counter/len(X_test)
print("RF test accuracy: ", RF_test_accuracy)

# training data accuracy
train_counter = 0
for i in range(len(X_train)):
  if y_train[i] == RFTrainpredictions[i]:
    train_counter += 1
RF_train_accuracy = train_counter/len(X_train)
print("RF train accuracy: ", RF_train_accuracy)

from sklearn.neighbors import KNeighborsClassifier
#model
neigh = KNeighborsClassifier(n_neighbors=5).fit(X_train, y_train)
#predictions
KNpredictions = neigh.predict(X_test)

KNTrainpredictions = neigh.predict(X_train)

# testing data accuracy
test_counter = 0
for i in range(len(X_test)):
  if y_test[i] == KNpredictions[i]:
    test_counter += 1
KN_test_accuracy = test_counter/len(X_test)
print("KN test accuracy: ", KN_test_accuracy)

# training data accuracy
train_counter = 0
for i in range(len(X_train)):
  if y_train[i] == KNTrainpredictions[i]:
    train_counter += 1
KN_train_accuracy = train_counter/len(X_train)
print("KN train accuracy: ", KN_train_accuracy)

#multiplicative weight update
# every model's test accuracy shows how strong the model is. different weights

wN, wD, wR, wK = 1, 1, 1, 1
combined = []
counter = 0
accuracy = 0
mN, mD, mR, mK = [], [], [], []

for i in range(len(X_test)):
  if NNpredictions[i] == y_test[i]:
    wN+=1
  if DTpredictions[i] == y_test[i]:
    wD+=1
  if RFpredictions[i] == y_test[i]:
    wR+=1
  if KNpredictions[i] == y_test[i]:
    wK+=1

  s1, s2, s3 = 0, 0, 0



  if(NNpredictions[i] == 1):
    s1 += wN
  if(DTpredictions[i] == 1):
    s1 += wD
  if(RFpredictions[i] == 1):
    s1 += wR
  if(KNpredictions[i] == 1):
    s1 += wK

  if(NNpredictions[i] == 2):
    s2 += wN
  if(DTpredictions[i] == 2):
    s2 += wD
  if(RFpredictions[i] == 2):
    s2 += wR
  if(KNpredictions[i] == 2):
    s2 += wK

  if (NNpredictions[i] == 3):
    s3 += wN
  if(DTpredictions[i] == 3):
    s3 += wD
  if(RFpredictions[i] == 3):
    s3 += wR
  if(KNpredictions[i] == 3):
    s3 += wK

  mN.append(wN)
  mD.append(wD)
  mR.append(wR)
  mK.append(wK)

  if s1>s2 and s1>s3:
    combined.append(1)
  elif s2>s3 and s2>s1:
    combined.append(2)
  else:
    combined.append(3)
    """
print(combined)

print(y_test)"""
  if y_test[i] == combined[i]:
    counter +=1

accuracy = counter/len(X_test)
print("accuracy of all models combined", accuracy)
print("weights of different models ", wN, wD, wR, wK)
print(mN)

import matplotlib.pyplot as plt


# Get the index range
indices = range(len(mN))

# Create the plot
plt.figure(figsize=(10, 7))
plt.plot(indices, mN, marker='.', label="NN", linewidth=1)
plt.plot(indices, mD, marker='.', label="DT", linewidth=1)
plt.plot(indices, mR, marker='.', label="RF", linewidth=1)
plt.plot(indices, mK, marker='.', label="KN", linewidth=1)

# Labels and title
plt.xlabel("Index")
plt.ylabel("Weight")
plt.title("Plot of Four Lists with Respect to Index")
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
