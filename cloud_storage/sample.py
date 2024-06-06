import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",  # Docker container's IP or hostname
    port="5432",        # PostgreSQL port
    database="movies",  # Name of the database
    user="juan",        # Database user
    password="cruz"     # Password
)

# Create a cursor
cur = conn.cursor()

# SQL INSERT statement
insert_query = """
INSERT INTO actors (id, name, created_at)
VALUES (%s, %s, %s)
"""

# Sample data
data_to_insert = (1, "John Doe", "2022-06-15")

# Execute the INSERT statement
cur.execute(insert_query, data_to_insert)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cur.close()
conn.close()
fed3BTF3tat1xan.jwj
