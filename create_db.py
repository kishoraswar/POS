import sqlite3
def create_db():
    con=sqlite3.connect(database=r'pos.db') # Database created
    cur=con.cursor()
    #Employee Table
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()
    #Supplier Table
    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT,name text,contact text,desc text)")
    con.commit()
    #category table
    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()  
    #product
    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Supplier text,Category text,name text,price text,qty text,status text)")
    con.commit()

create_db()