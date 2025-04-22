import pandas as pd
import psycopg2

def extract_data(file_path):
    # Extract data from CSV file
    return pd.read_csv(file_path)

def transform_data(df):
    # Basic transformation: Handle missing values and convert data types
    df.fillna(0, inplace=True)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    return df

def load_data(df, db_conn_params):
    # Load data into PostgreSQL database
    conn = psycopg2.connect(**db_conn_params)
    df.to_sql('material_data', conn, if_exists='replace', index=False)
    conn.close()

def main():
    # ETL process
    data = extract_data('data/raw_data.csv')
    transformed_data = transform_data(data)
    db_params = {'host': 'localhost', 'database': 'quality_assessment', 'user': 'user', 'password': 'password'}
    load_data(transformed_data, db_params)

if __name__ == "__main__":
    main()
