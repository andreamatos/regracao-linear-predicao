import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

# Carregar os dados
data = pd.read_csv('sao-paulo-properties-april-2019.csv')

# Separar features e target
X = data.drop('Price', axis=1)
y = data['Price']

# Separar dados numéricos e categóricos
X_numeric = X.select_dtypes(include=np.number)
X_categorical = X.select_dtypes(include='object')

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline para dados numéricos
numeric_features = list(X_numeric.columns)
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean'))
])

# Pipeline para dados categóricos
categorical_features = list(X_categorical.columns)
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

# Combinar pipelines
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Modelo de regressão linear
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor', LinearRegression())])

# Treinar o modelo
model.fit(X_train, y_train)

# Fazer previsões
# Use os mesmos recursos usados durante o treinamento
test_data = pd.DataFrame({
    'Area': [1000],
    'Rooms': [3],
    'Bathroom': [2],
    'Parking spaces': [1],
    'Floor': [5],
    'Animal': [1],
    'Furniture': [1],
    'hoa (R$)': [500],
    'rent amount (R$)': [2000],
    'property tax (R$)': [300],
    'fire insurance (R$)': [50],
    'city': ['Vila Mariana/São Paulo'],
    'floor': ['rent'],
    'animal': ['apartment'],
    'Suites': [1],
    'Parking': [1],
    'Swimming Pool': [0],
    'Furnished': [1],
    'District': ['Vila Mariana/São Paulo'],
    'Latitude': [-23.5898],
    'Size': [120],
    'Elevator': [1],
    'Condo': [1],
    'Toilets': [2],
    'Property Type': ['apartment'],
    'Negotiation Type': ['rent'],
    'Longitude': [-46.6346],
    'New': [0]
})

prediction = model.predict(test_data)

# Preço previsto em centavos de real
predicted_price_cents = prediction[0]

# Converter para reais
predicted_price_reais = predicted_price_cents / 100

# Formatar como moeda brasileira
predicted_price_formatado = f"R$ {predicted_price_reais:.2f}"

print("Preço previsto:", predicted_price_formatado)
