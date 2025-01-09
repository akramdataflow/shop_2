import sqlite3

def init_db():
    connection = sqlite3.connect("data.db")  # Create a connection to the database
    cursor = connection.cursor()  # Create a cursor object

    # Create Materials Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Materials (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name_of_material TEXT NOT NULL,
            type_of_materials TEXT NOT NULL,
            count INTEGER NOT NULL,
            expaier DATE NOT NULL,
            price INTEGER NOT NULL
        );
    ''')

    # Create Purchases Table (المشتريات)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Purchases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            price INTEGER NOT NULL,
            company_name TEXT NOT NULL,
            bill_num INTEGER NOT NULL,
            date DATETIME NOT NULL
        );
    ''')

    # Create Customer Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone INTEGER NOT NULL,
            address TEXT NOT NULL
        );
    ''')

    # Create Deferred Table (المؤجل)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Deferred (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT NOT NULL,
            phone_num INTEGER NOT NULL,
            address TEXT NOT NULL,
            price INTEGER NOT NULL
        );
    ''')

    # Create Invoices Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Invoices (
            invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_date DATETIME NOT NULL,
            total_amount INTEGER NOT NULL
        );
    ''')

    # Create InvoiceDetails Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS InvoiceDetails (
            detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
            invoice_id INTEGER NOT NULL,
            material_name CHAR NOT NULL,
            quantity INTEGER NOT NULL,
            unit_price REAL NOT NULL,
            total_price REAL NOT NULL
        );
    ''')

    # Commit changes and close the connection
    connection.commit()
    connection.close()

# Initialize the database
init_db()