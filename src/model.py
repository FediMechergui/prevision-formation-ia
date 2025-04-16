from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


def train_models(df):
    """Train regression models to predict inscriptions with new features."""
    features = ['evaluations', 'participation_rate', 'price_usd', 'duration_hours', 'category', 'region']
    X = df[features]
    y = df['inscriptions']
    categorical = ['category', 'region']
    numeric = ['evaluations', 'participation_rate', 'price_usd', 'duration_hours']

    preprocessor = ColumnTransformer([
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical)
    ], remainder='passthrough')

    linreg = Pipeline([
        ('pre', preprocessor),
        ('reg', LinearRegression())
    ]).fit(X, y)

    rf = Pipeline([
        ('pre', preprocessor),
        ('reg', RandomForestRegressor(n_estimators=100, random_state=42))
    ]).fit(X, y)
    return linreg, rf

def predict_popularity(model, df):
    features = ['evaluations', 'participation_rate', 'price_usd', 'duration_hours', 'category', 'region']
    return model.predict(df[features])
