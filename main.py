import argparse
from src.data_preparation import load_and_clean_data
from src.model import train_models, predict_popularity
from src.visualization import plot_top5_formations, plot_trends

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_path', type=str, required=True, help='Chemin du fichier CSV')
    args = parser.parse_args()

    df = load_and_clean_data(args.data_path)
    linreg, rf = train_models(df)
    print('Modèles entraînés.')

    # Prédictions avec Random Forest (exemple)
    df['predicted_inscriptions'] = predict_popularity(rf, df)
    print(df[['formation_name', 'inscriptions', 'predicted_inscriptions']])

    # Visualisations
    plot_top5_formations(df)
    plot_trends(df)
    print('Graphiques enregistrés : top5_formations.png, trend_inscriptions.png')

if __name__ == '__main__':
    main()
