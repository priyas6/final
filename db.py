

# Connect to PostgreSQL database

for embedding in embeddings:
    

# Commit the transaction


# Query data from the table
cur.execute("SELECT * FROM embeddings")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the cursor and connection
cur.close()
conn.close()