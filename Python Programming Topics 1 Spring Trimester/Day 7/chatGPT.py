# Import necessary libraries
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
dataset = pd.read_csv('Python Programming Topics 1 Spring Trimester\Day 7\iris.csv')

# Split the dataset into features and target variable
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a k-NN classifier object
knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')

# Train the k-NN classifier on the training set
knn.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = knn.predict(X_test)

# Evaluate the performance of the k-NN classifier
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)


#OpenAI. "AI Language Model." OpenAI, OpenAI, chat.openai.com/chat. Accessed 5/11/2023 2:25PM PST
