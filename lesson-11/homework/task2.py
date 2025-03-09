import sqlite3

# Create a new SQLite database named library.db
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Define a table called Books with the specified schema
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
"""
)

# Populate the Books table with the specified entries
books = [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic"),
]
cursor.executemany(
    "INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)",
    books,
)

# Update the Year_Published of 1984 to 1950
cursor.execute('UPDATE Books SET Year_Published = 1950 WHERE Title = "1984"')

# Retrieve and display the Title and Author of all books where the Genre is Dystopian
cursor.execute('SELECT Title, Author FROM Books WHERE Genre = "Dystopian"')
dystopian_books = cursor.fetchall()
print("Dystopian Books:")
for book in dystopian_books:
    print(book)

# Remove all books published before the year 1950 from the table
cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")

# Add a new column called Rating to the Books table
cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")

# Update the data with the specified ratings
ratings = [("To Kill a Mockingbird", 4.8), ("1984", 4.7), ("The Great Gatsby", 4.5)]
for title, rating in ratings:
    cursor.execute("UPDATE Books SET Rating = ? WHERE Title = ?", (rating, title))

# Retrieve all books sorted by their Year_Published in ascending order
cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
sorted_books = cursor.fetchall()
print("Books sorted by Year_Published:")
for book in sorted_books:
    print(book)

# Commit the changes and close the connection
conn.commit()
conn.close()
