import plotly.graph_objs as go
import pandas as pd
from plotly.utils import PlotlyJSONEncoder
import json

def plot_top5_formations_json(df):
    top5 = df.nlargest(5, 'inscriptions')
    fig = go.Figure([go.Bar(x=top5['formation_name'], y=top5['inscriptions'])])
    fig.update_layout(title='Top 5 Formations par Inscriptions', xaxis_title='Formation', yaxis_title='Inscriptions')
    return json.loads(fig.to_json())

def plot_trend_json(df):
    df_sorted = df.sort_values('date')
    fig = go.Figure([go.Scatter(x=df_sorted['date'], y=df_sorted['inscriptions'], mode='lines+markers')])
    fig.update_layout(title='Tendance des Inscriptions dans le Temps', xaxis_title='Date', yaxis_title='Inscriptions')
    return json.loads(fig.to_json())

def plot_category_pie_json(df):
    cat_enrollments = df.groupby('category')['inscriptions'].sum().sort_values(ascending=False)
    fig = go.Figure([go.Pie(labels=cat_enrollments.index, values=cat_enrollments.values)])
    fig.update_layout(title='Part des Inscriptions par Catégorie')
    return json.loads(fig.to_json())

def plot_region_bar_json(df):
    reg_counts = df['region'].value_counts()
    fig = go.Figure([go.Bar(x=reg_counts.index, y=reg_counts.values)])
    fig.update_layout(title='Nombre de Formations par Région', xaxis_title='Région', yaxis_title='Nombre')
    return json.loads(fig.to_json())

def plot_price_box_by_category_json(df):
    import plotly.graph_objs as go
    fig = go.Figure()
    cats = df['category'].unique()
    for cat in cats:
        fig.add_trace(go.Box(y=df[df['category']==cat]['price_usd'], name=cat))
    fig.update_layout(title='Distribution des Prix par Catégorie', yaxis_title='Prix (USD)')
    return json.loads(fig.to_json())

def plot_ratings_hist_json(df):
    import plotly.graph_objs as go
    fig = go.Figure([go.Histogram(x=df['evaluations'], nbinsx=20)])
    fig.update_layout(title='Histogramme des Notes', xaxis_title='Note', yaxis_title='Nombre de cours')
    return json.loads(fig.to_json())

def plot_price_vs_enrollments_json(df):
    import plotly.graph_objs as go
    fig = go.Figure([go.Scatter(x=df['price_usd'], y=df['inscriptions'], mode='markers', text=df['formation_name'])])
    fig.update_layout(title='Prix vs Inscriptions', xaxis_title='Prix (USD)', yaxis_title='Inscriptions')
    return json.loads(fig.to_json())

def plot_participation_by_instructor_json(df):
    import plotly.graph_objs as go
    avg_part = df.groupby('instructor')['participation_rate'].mean().sort_values(ascending=False).head(20)
    fig = go.Figure([go.Bar(x=avg_part.index, y=avg_part.values)])
    fig.update_layout(title='Taux de Participation Moyen par Formateur (Top 20)', xaxis_title='Formateur', yaxis_title='Taux de participation')
    return json.loads(fig.to_json())

def generate_all_stats_json(df):
    return {
        'top5': plot_top5_formations_json(df),
        'trend': plot_trend_json(df),
        'category_pie': plot_category_pie_json(df),
        'region_bar': plot_region_bar_json(df),
        'price_box': plot_price_box_by_category_json(df),
        'ratings_hist': plot_ratings_hist_json(df),
        'price_vs_enrollments': plot_price_vs_enrollments_json(df),
        'participation_by_instructor': plot_participation_by_instructor_json(df)
    }
