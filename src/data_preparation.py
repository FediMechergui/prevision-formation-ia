import pandas as pd

def load_and_clean_data(filepath):
    """Load CSV, clean/standardize columns, return DataFrame."""
    df = pd.read_csv(filepath)
    # Fill missing values and convert types for new columns
    df['category'] = df['category'].fillna('Autre')
    df['instructor'] = df['instructor'].fillna('Inconnu')
    df['price_usd'] = df['price_usd'].fillna(df['price_usd'].mean()).astype(float)
    df['duration_hours'] = df['duration_hours'].fillna(df['duration_hours'].mean()).astype(float)
    df['region'] = df['region'].fillna('Inconnu')
    df['inscriptions'] = df['inscriptions'].fillna(0).astype(int)
    df['evaluations'] = df['evaluations'].fillna(df['evaluations'].mean())
    df['participation_rate'] = df['participation_rate'].fillna(df['participation_rate'].mean())
    df['date'] = pd.to_datetime(df['date'])
    return df
