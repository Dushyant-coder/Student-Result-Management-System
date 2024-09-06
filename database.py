import sqlite3

def display_table_content(table_name):
    con = sqlite3.connect("SRMS.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM {table_name};")
    rows = cur.fetchall()
    con.close()

    for row in rows:
        print(row)

# Example: Display content of the "course" table
display_table_content("course")
display_table_content("result1")
display_table_content("student")
display_table_content("employee")

