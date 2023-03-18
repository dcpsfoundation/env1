import sqlite3
con = sqlite3.connect('myFirst.db')
cur = con.cursor()
# cur.execute('CREATE TABLE Product (p_id INTEGER PRIMARY KEY AUTOINCREMENT, p_name TEXT NOT NULL, price REAL, quantity INTEGER)')

# cur.execute("INSERT INTO Product(p_name,price,quantity) VALUES('AutoCAD',200,20)")
# cur.execute("INSERT INTO Product(p_name,price,quantity) VALUES('Quick Hill',330,12)")
# cur.execute("INSERT INTO Product(p_name,price,quantity) VALUES('Keyboard',250,25)")
# cur.execute("INSERT INTO Product(p_name,price,quantity) VALUES('Mouse',150,34)")
# print('Data Inserted!!!')
# con.commit()

cur.execute("UPDATE Product SET quantity=quantity+(quantity*0.2)")
con.commit()

print("p_id \t p_name \t quantity\n")

cursor = cur.execute("SELECT * FROM Product")

for row in cursor:
    print(row[0], "\t" ,row[1], "\t" ,row[2], "\t" ,row[3], "\n")

con.close() 