import requests
import sqlite3
import pandas as pd

def main():
    print("1. EXTRACT: Downloading data from API...")
    url = 'https://fakestoreapi.com/products'
    raw_data = requests.get(url).json()

    print("2. TRANSFORM & LOAD: Preparing database and loading data...")
    conn = sqlite3.connect("ecommerce_data.db")
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            title TEXT,
            price REAL,
            category TEXT,
            rating REAL
        )
    ''')
    
    cursor.execute('DELETE FROM products')

    for item in raw_data:
        query = "INSERT INTO products (id, title, price, category, rating) VALUES (?, ?, ?, ?, ?)"
        payload = (item['id'], item['title'], item['price'], item['category'], item['rating']['rate'])
        cursor.execute(query, payload)

    conn.commit()

    print("3. ANALYZE: Extracting business insights (Pandas)...")
    df = pd.read_sql_query("SELECT * FROM products", conn)
    
    print("\n--- QUICK BUSINESS REPORT ---")
    print(f"Total products loaded: {len(df)}")
    print(f"Average store price: ${df['price'].mean():.2f}")
    
    categories = df.groupby('category')['price'].mean().sort_values(ascending=False)
    print("\nMost expensive categories (average price):")
    print(categories.to_string())
    
    conn.close()
    print("\nSuccess!")

if __name__ == "__main__":
    main()