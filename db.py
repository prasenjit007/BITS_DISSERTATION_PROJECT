# db.py
import sqlite3

DB_PATH = "mydata.db"

def initialize_database():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Table: Users
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
    """)

    # Table: Products
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price REAL
    )
    """)

     # Table: Products
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cameras (
        id INTEGER PRIMARY KEY,
        name TEXT,
        description TEXT
    )
    """)

    cameras = [
        ("Cam1", "Cam Desc 1"),
        ("cam2", "Cam Desc 2"),
        ("HonCamera", "Cam Desc 3"),
        ("S2 Camera", "Cam Desc 4"),
        ("Lenel Camere ", "Cam Desc 5")
    ]
    cursor.executemany("INSERT INTO cameras (name, description) VALUES (?, ?)", cameras)

    
    users = [
        ("Alice Smith", "alice.smith@example.com"),
        ("Bob Johnson", "bob.johnson@example.com"),
        ("Charlie Lee", "charlie.lee@example.com"),
        ("Dana White", "dana.white@example.com"),
        ("Ethan Moore", "ethan.moore@example.com")
    ]
    cursor.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)

    products = [
        ("Laptop", 1200),
        ("Smartphone", 799),
        ("Headphones", 149),
        ("Monitor", 250),
        ("Mechanical Keyboard", 99)
    ]
    cursor.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)

    conn.commit()
    conn.close()