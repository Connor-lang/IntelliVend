import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
import pickle

df = pd.read_csv('customers_data_final.csv')
df = df.iloc[:,1:6].copy()

df['Gender'].replace(['Female','Male'],[1,0], inplace=True)
training_data = df.iloc[:,2:5]
X = training_data[['Gender','Age']].to_numpy()
Y = training_data['label'].to_numpy()

X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, Y, test_size=0.25)
model = LogisticRegression()

model.fit(X_train, y_train)

print(model.coef_)

filename = 'Logistic_regression_model.pkl'
pickle.dump(model, open(filename, 'wb'))

loaded_model = pickle.load(open(filename,'rb'))

print(f'Logistic regression model with accuracy of {loaded_model.score(X_test, y_test)}')

y_predicted = loaded_model.predict(X_test)
print(model.predict([[0,50]]))

print(confusion_matrix(y_test, y_predicted))