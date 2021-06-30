from tensorflow import keras
import random
import numpy as np


# Importing the data file.
# Data contains a lot of 16 vectors, with each vector representing a letter.
# There are about 20000 instances of letters but we only need T and K.
file = open("letter-recognition.data", "r")
letters=file.readlines()
data=[]

# Extracting only the vectors with the labels T and K (1535 instances).
for i in range(len(letters)):
    if letters[i][0]=="T" or letters[i][0]=="K":
        data.append(letters[i].strip("\n"))

# Converting the numbers of each vector from strings to ints.
for i in range(len(data)):
    data[i] = data[i].split(",")
    data[i][1:] = list(map(int, data[i][1:]))

# Shuffling the data
random.shuffle(data)

# Initializing empty arrays for train data and train labels.
train_labels=[]
train_data=[]

# Initializing empty arrays for test data and test labels.
test_labels=[]
test_data=[]

# Train data percentage (example 80%).
train_percentage_amount=80

# Selecting the first x% of the shuffled data for training (x was set above).
training_perc=round(len(data)*train_percentage_amount/100)
testing_perc=len(data)-training_perc

# Encoding 0 for K and 1 for T cause labels must be numeric.
# Transforming the data matrix into the training and testing data and (encoded) labels.

for i in range(training_perc):
    if data[i][0]=="K":
        train_labels.append(0)
    else:
        train_labels.append(1)
    train_data.append(data[i][1:])

for i in range(training_perc, len(data)):
    if data[i][0]=="K":
        test_labels.append(0)
    else:
        test_labels.append(1)
    test_data.append(data[i][1:])

# Initializing a simple sequential (feed-forward) network with 16-input input layer
# because of the 16 dimension vector of each letter.

# Initializing a second "hidden layer" and finally a 2-output
# output layer because of the 2 possible outcomes 0 for K and 1 for T.

model=keras.Sequential([
    keras.layers.Dense(16),
    keras.layers.Dense(8, activation="relu"),
    keras.layers.Dense(2, activation="softmax")
])

# Hyperparameter tuning, setting an optimizer, a loss function and what metrics to output while the model is training
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

# Train the model. The number of epochs is selected based of the outputted accuracy. If we have low accuracy we must
# increase the number of epochs, if the accuracy raises and then drops we may need to lower the epochs cause the model is over-training.
model.fit(train_data,train_labels, epochs=8)

# Inputting the test data with the wanted test labels to see the actual accuracy for the T and K letter classification,
test_loss, test_acc =model.evaluate(test_data,test_labels,verbose=1)
print("Test accuracy: ",test_acc*100,"%")


# Custom neural network

# Simple sigmoid function
def sigmoid(x):
    return 1/(1+np.exp(-x))

# Simple derivative of sigmoid function
def sigmoid_der(x):
    return sigmoid(x)*(1-sigmoid(x))

# Setting up the feature table and the labeles table.
feature_set = np.array(train_data)
labels = np.array([train_labels])
labels = labels.reshape(len(train_labels),1)

# Hyperparameter tuning
np.random.seed(42)
weights = np.random.rand(len(train_data[0]),1)
bias = np.random.rand(1)
lr = 0.05
epochs=8

for epoch in range(epochs):
    inputs = feature_set
    # feedforward step1
    XW = np.dot(feature_set, weights) + bias

    #feedforward step2
    z = sigmoid(XW)

    # backpropagation step 1
    error = z - labels

    # backpropagation step 2
    dcost_dpred = error

    dpred_dz = sigmoid_der(z)
    z_delta = dcost_dpred * dpred_dz

    inputs = feature_set.T
    weights -= lr * np.dot(inputs, z_delta)

    for num in z_delta:
        bias -= lr * num

acc=0
for i in range(len(test_data)):

    single_point = np.array(test_data[i])
    result = sigmoid(np.dot(single_point, weights) + bias)
    if (round(result[0])==test_labels[i]):
        acc+=1

print("Accuracy with custom neural network with "+str(epochs)+" epochs is "+str(acc/len(test_labels)*100)+"%.")



