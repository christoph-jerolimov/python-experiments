import sqlite3

con = sqlite3.connect("test.db")
cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS movie (
        title,
        year,
        score,
        UNIQUE(title, year)
    )
""")

data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT OR IGNORE INTO movie VALUES(?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.

res = cur.execute("SELECT count(*) FROM movie")
print(res.fetchone()[0])

for row in cur.execute("SELECT year, title, score FROM movie ORDER BY year"):
    print(row)

cur.close()
con.close()
