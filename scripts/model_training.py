import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from utils.logger import setup_logger

logger = setup_logger('model_training', 'logs/model_training.log')

def train_model():
    try:
        # Load cleaned data
        train = pd.read_csv('Cleaned_Data/clean_train.csv')

        # Prepare data
        X = train.drop(columns=['Sales', 'Date'])
        y = train['Sales']
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

        # Build pipeline
        pipeline = Pipeline([
            ('scaler', StandardScaler()),
            ('model', RandomForestRegressor(n_estimators=100, random_state=42))
        ])

        # Train model
        pipeline.fit(X_train, y_train)
        logger.info('Model trained successfully.')

        # Save model
        joblib.dump(pipeline, 'models/sales_model.pkl')
        logger.info('Model saved to models/sales_model.pkl.')
    except Exception as e:
        logger.error(f'Error in model training: {e}')
        raise

if __name__ == '__main__':
    train_model()
