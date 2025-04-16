import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
import os
from src.data_preparation import load_and_clean_data
from src.model import train_models, predict_popularity
from src.visualization import generate_all_stats_json
from src.webscraper import update_csv_with_scraped_courses

DATA_PATH = os.path.join('data', 'simulated_data.csv')

app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')

@app.on_event('startup')
def run_pipeline():
    # Scrape and update CSV with new real-world courses
    update_csv_with_scraped_courses(DATA_PATH, max_per_source=5)
    global df, stats_json
    df = load_and_clean_data(DATA_PATH)
    linreg, rf = train_models(df)
    df['predicted_inscriptions'] = predict_popularity(rf, df)
    stats_json = generate_all_stats_json(df)

@app.get('/', response_class=HTMLResponse)
def dashboard(request: Request):
    with open('static/index.html', encoding='utf-8') as f:
        return HTMLResponse(f.read())

@app.get('/api/stats')
def get_stats():
    return JSONResponse(stats_json)

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
