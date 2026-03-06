import sqlite3

# Database ဖောက်မယ်
conn = sqlite3.connect('shop.db')
cursor = conn.cursor()

# Products table ဆောက်မယ်
cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        emoji TEXT
    )
''')

# Products တွေ ထည့်မယ်
cursor.execute("INSERT INTO products (name, price, emoji) VALUES ('Sneakers', 25, '👟')")
cursor.execute("INSERT INTO products (name, price, emoji) VALUES ('T-Shirt', 15, '👕')")
cursor.execute("INSERT INTO products (name, price, emoji) VALUES ('Backpack', 40, '🎒')")
cursor.execute("INSERT INTO products (name, price, emoji) VALUES ('Watch', 60, '⌚')")

conn.commit()

# Products တွေ ဖတ်မယ်
cursor.execute("SELECT * FROM products")
products = cursor.fetchall()

print("🛒 Products in Database:")
for p in products:
    print(f"  {p[3]} {p[1]} — ${p[2]}")

conn.close()
print("✅ Database အလုပ်လုပ်နေပြီ!")