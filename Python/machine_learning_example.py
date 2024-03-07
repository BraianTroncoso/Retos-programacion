import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.feature_extraction.text import CountVectorizer

# Load data
df = pd.read_csv("datos.csv")

# Preprocess the data
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Title'])

# Define input and output variables
X = X.toarray()
y = df['Price']

# Training the model
model = DecisionTreeRegressor()
model.fit(X, y)

# Make a prediction
new_title = "Samsung Galaxy S20"
new_title_vectorized = vectorizer.transform([new_title])
prediction = model.predict(new_title_vectorized)
print("Suggested price:", prediction[0])
