import sqlite3

# Create a new SQLite database named roster.db
conn = sqlite3.connect("roster.db")
cursor = conn.cursor()

# Define a table called Roster with the specified schema
cursor.execute(
    """
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
"""
)

# Populate the Roster table with the specified entries
cursor.executemany(
    """
INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)
""",
    [
        ("Benjamin Sisko", "Human", 40),
        ("Jadzia Dax", "Trill", 300),
        ("Kira Nerys", "Bajoran", 29),
    ],
)

# Update the Name of Jadzia Dax to Ezri Dax
cursor.execute(
    """
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
"""
)

# Retrieve and display the Name and Age of all characters where the Species is Bajoran
cursor.execute(
    """
SELECT Name, Age FROM Roster
WHERE Species = 'Bajoran'
"""
)
bajoran_characters = cursor.fetchall()
for character in bajoran_characters:
    print(character)

# Remove all characters aged over 100 years from the table
cursor.execute(
    """
DELETE FROM Roster
WHERE Age > 100
"""
)

# Add a new column called Rank to the Roster table
cursor.execute(
    """
ALTER TABLE Roster
ADD COLUMN Rank TEXT
"""
)

# Update the data with the specified values
cursor.executemany(
    """
UPDATE Roster
SET Rank = ?
WHERE Name = ?
""",
    [
        ("Captain", "Benjamin Sisko"),
        ("Lieutenant", "Ezri Dax"),
        ("Major", "Kira Nerys"),
    ],
)

# Retrieve all characters sorted by their Age in descending order
cursor.execute(
    """
SELECT * FROM Roster
ORDER BY Age DESC
"""
)
sorted_characters = cursor.fetchall()
for character in sorted_characters:
    print(character)

# Commit the changes and close the connection
conn.commit()
conn.close()
