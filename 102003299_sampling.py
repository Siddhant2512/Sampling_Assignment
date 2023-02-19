# -*- coding: utf-8 -*-
"""102003299_sampling.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PDmeGBT9YD0FyVzbgzbOYpTxtqN2TgFq
"""

import pandas as pd

data = pd.read_csv('/content/Creditcard_data.csv')
data.head()

data.info()

data['Class'].value_counts()

x = data.drop(columns='Class',axis=1)

y = data['Class']

# nf = non-fraud cases
# f = fraud cases

nf = data[data.Class==0]
print(nf.shape)

f = data[data.Class==1]
print(f.shape)

import pandas as pd
import numpy as np
from imblearn.over_sampling import RandomOverSampler

# Assuming you already have a dataframe named "data"
x = data.drop("Class", axis=1)
y = data["Class"]

rus = RandomOverSampler(random_state=42)
x_res, y_res = rus.fit_resample(x, y)

# Convert numpy arrays to dataframes
x_res_df = pd.DataFrame(x_res, columns=x.columns)
y_res_df = pd.DataFrame(y_res, columns=["Class"])

# Concatenate the two dataframes horizontally to create the new balanced dataset
new_data = pd.concat([x_res_df, y_res_df], axis=1)
new_data.to_csv("Balanced_Data.csv",index=False)

new_data.head()

new_data['Class'].value_counts()

Heading = ['Simple Random', 'Systematic', 'Cluster', 'Stratified', 'Convenience']
index_names = ['Logistic Regression', 'DecisionTreeClassifier', 'RandomForestClassifier', 'GradientBoostingClassifier', 'SVC']
final = pd.DataFrame(columns=Heading, index=index_names)

import pandas as pd
import numpy as np

Z = 1.96  # Z-score corresponding to desired level of confidence (1.96 for 95% confidence)
p = 0.5  # estimated proportion of population with a certain characteristic (assumed to be 0.5 )
e = 0.05  #desired margin of error

# Sample-size detection formula
num = (pow(Z,2)*p*(1-p))/pow(e,2)
num = round(num)


random_sample = new_data.sample(n=num, random_state=0)
print(f"Random Sampling Sample Size: {len(random_sample)}")
random_sample.head()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(random_sample.drop("Class", axis=1), random_sample["Class"], test_size=0.2, random_state=0)

# Train and evaluate the models
models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Gradient Boosting": GradientBoostingClassifier(),
    "Support Vector Machine": SVC()
}

for name, model in models.items():
    accuracy = []
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracy.append(acc*100)
    print(f"{name} accuracy: {acc}")

import pandas as pd
import math

Z = 1.96 
p = 0.5  
e = 0.05
N = 1544
n = N/(1+(N-1)/(N*pow(e,2)))
n=int(n)
sys_sample = new_data.iloc[::5]

# Print the sample size
print(f"Systematic Sampling Sample Size: {len(sys_sample)}")
sys_sample.head()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(sys_sample.drop("Class", axis=1), sys_sample["Class"], test_size=0.1, random_state=0)


# Train and evaluate the models
models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Gradient Boosting": GradientBoostingClassifier(),
    "Support Vector Machine": SVC()
}

for name, model in models.items():
    accuracy = []
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracy.append(acc*100)
    print(f"{name} accuracy: {acc}")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

 
# Define the target variable and the stratification variable
target = 'Class'
stratify_by = 'Class'

# Split the data into training and test sets, stratifying by the target variable
train, test = train_test_split(new_data, test_size=0.2, stratify=new_data[stratify_by], random_state=42)


# Split the data into features and target
X_train = train.drop(target, axis=1)
y_train = train[target]
X_test = test.drop(target, axis=1)
y_test = test[target]

# Train and evaluate the models
models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Gradient Boosting": GradientBoostingClassifier(),
    "Support Vector Machine": SVC()
}

for name, model in models.items():
    accuracy = []
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracy.append(acc*100)
    print(f"{name} accuracy: {acc}")

from sklearn.cluster import KMeans

# Define the number of clusters
num_clusters = 5

# Apply K-means clustering to the data
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
clusters = kmeans.fit_predict(new_data)

# Select a random subset of clusters
cluster_ids = np.random.choice(num_clusters, size=2, replace=False)

# Include all the data points in the selected clusters in the sample
cluster_sample = new_data[np.isin(clusters, cluster_ids)]
print(f"Cluster Sampling Sample Size: {len(cluster_sample)}")
cluster_sample.head()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(cluster_sample.drop("Class", axis=1), cluster_sample["Class"], test_size=0.2, random_state=0)

# Train and evaluate the models
models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Gradient Boosting": GradientBoostingClassifier(),
    "Support Vector Machine": SVC()
}

for name, model in models.items():
    accuracy = []
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracy.append(acc*100)
    print(f"{name} accuracy: {acc}")

convenience_sample=new_data.head(400)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(convenience_sample.drop("Class", axis=1), convenience_sample["Class"], test_size=0.2, random_state=0)

# Train and evaluate the models
models = {
    "Logistic Regression": LogisticRegression(),
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(),
    "Gradient Boosting": GradientBoostingClassifier(),
    "Support Vector Machine": SVC()
}

for name, model in models.items():
    accuracy = []
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    accuracy.append(acc*100)
    print(f"{name} accuracy: {acc}")

print(final)
final.to_csv("final.csv")