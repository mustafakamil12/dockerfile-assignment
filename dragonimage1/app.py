import cx_Oracle
import pyodbc
import selenium

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com")

search_box = driver.find_element("name","q")
search_box.send_keys("Python Selenium")

search_box.submit()
print(driver.page_source)

driver.quit()

# --------  SQL Server Connection --------- #

# Connect to the SQL Server database
conn = pyodbc.connect('DRIVER={SQL Server};'
                      'SERVER=mssqldb,1433;'
                      'DATABASE=master;'
                      'UID=sa;'
                      'PWD=P@ssw0rd;'
                      'Trusted_Connection=yes;')

# Create a cursor object
cursor = conn.cursor()

# Create database if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS School")
cursor.execute("USE School")

# Create students table if not exists
cursor.execute("CREATE TABLE IF NOT EXISTS students (id INT IDENTITY(1,1) PRIMARY KEY, name VARCHAR(255), grade INT)")

# Insert students
students = [
    ('mustafa kamil', 5),
    ('farouk kamil', 3),
    ('muhanned', 2)
]
for student in students:
    cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", student)

# Commit the transaction
conn.commit()

# Retrieve and print results
cursor.execute("SELECT * FROM students")
print("Student Table:")
print("ID\tName\t\tGrade")
for row in cursor.fetchall():
    print(f"{row.id}\t{row.name}\t{row.grade}")

# Close connections
cursor.close()
conn.close()


print("Hello Mustafa, If you reach out to this point, You already success, Congrats!!!")

