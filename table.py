import psycopg2
#added a new comment
# Create a connection
conn = psycopg2.connect(
    host="redshift-cluster.cr3lw4pc0jrj.us-east-2.redshift.amazonaws.com",
    port="5439",
    dbname="dbdev",
    user="useradmin",
    password="Newpassword1"
)

# Create a cursor
cursor = conn.cursor()

# SQL statement to create a table
create_table_query = """
CREATE TABLE IF NOT EXISTS my_table (
    id INT,
    name VARCHAR(50)
);
"""

# Execute the query
cursor.execute(create_table_query)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
