import sqlite3

def create_database():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Create Customers Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        city TEXT NOT NULL
    )
    """)

    # Create Orders Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_id INTEGER,
        product TEXT NOT NULL,
        amount INTEGER,
        FOREIGN KEY(customer_id) REFERENCES customers(id)
    )
    """)

    # Insert Sample Customers
    customers_data = [
        ("Ravi", "Hyderabad"),
        ("Priya", "Mumbai"),
        ("Arjun", "Delhi"),
        ("Sneha", "Chennai")
    ]

    cursor.executemany("""
    INSERT INTO customers (name, city)
    VALUES (?, ?)
    """, customers_data)

    # Insert Sample Orders
    orders_data = [
        (1, "Laptop", 55000),
        (2, "Mobile", 20000),
        (3, "Tablet", 15000),
        (1, "Headphones", 3000),
        (4, "Camera", 45000)
    ]

    cursor.executemany("""
    INSERT INTO orders (customer_id, product, amount)
    VALUES (?, ?, ?)
    """, orders_data)

    conn.commit()
    conn.close()
    print("Database created successfully!")

if __name__ == "__main__":
    create_database()