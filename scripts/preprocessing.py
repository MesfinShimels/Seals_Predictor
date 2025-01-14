from utils.data_processing import load_data, clean_data, save_cleaned_data
from utils.logger import setup_logger

logger = setup_logger('data_processing', 'logs/data_processing.log')

def main():
    try:
        # Load raw data
        train, test, store = load_data('Data/train.csv', 'Data/test.csv', 'Data/store.csv')
        logger.info('Data loaded successfully.')

        # Clean data
        train, test = clean_data(train, test, store)
        logger.info('Data cleaned successfully.')

        # Save cleaned data
        save_cleaned_data(train, test)
        logger.info('Cleaned data saved successfully.')
    except Exception as e:
        logger.error(f'Error in data processing: {e}')
        raise

if __name__ == '__main__':
    main()
