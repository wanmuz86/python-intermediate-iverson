print("=== Lab: Classifier + Accuracy + Joblib ===")
import pandas as pd # import pandas 
from sklearn.model_selection import train_test_split #split and test
from sklearn.linear_model import LogisticRegression # model
from sklearn.metrics import accuracy_score # to get the accuracy of test
import joblib # cache the model


# open the file, read the data set
df = pd.read_csv("students.csv")
print("\nDataset preview:")

#get the first 5 dataset
print(df.head())

# create a data frame 
# We want to predict the correlation between hours_student and practice_tests agains result [passed/failed]
# features [criteria]
X = df[["hours_studied", "practice_tests"]]
# labels [ Y, N] -> prediction
y = df["passed"]

# split the dataset into 2  ( 1 is to train, 1 to verify/test/fit)

X_train, X_test, y_train, y_test = train_test_split(
    # 70% to train 30% to fit/test/verify
    X, y, test_size=0.3, random_state=42
)

print("\nTrain size:", len(X_train)) # training data (8)
print("Test size:", len(X_test)) # testing data (4)


# Train the model using the train data set provided
model = LogisticRegression() # LogisticRegression / Classficiation
# Classification - ML that normally predict based on binary [spam dection]
# X- features, y - label
model.fit(X_train, y_train)

print("\nModel trained ✅")

#Using the 30% remaining test data, we will fit the data
# Specify the accuracy

# load the test data
# create a prediction based on the test data
y_pred = model.predict(X_test)

# get the accuracy
acc = accuracy_score(y_test, y_pred) #get the accuracy based on the test data
print("\nPredictions:", list(y_pred))
print("Actual:", list(y_test))
print("Accuracy:", round(acc, 3))

sample1 = [[5,2]] #sample 1, 
pred1 = model.predict(sample1)[0] #1

sample2 = [[2,3]] #sample2
pred2 = model.predict(sample2)[0] # 0

sample3 = [[8,0]] #sample3
pred3 = model.predict(sample3)[0]

print(f"\nSample input {sample3}")
print(f"\nPrediction {pred3}")





