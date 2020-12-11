import sqlite3

def connect():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year INTEGER, ISBN INTEGER)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))   # only the SQL statement is between ""; no variables!!!
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("books.db") 
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()  
    return rows

def search(title="",author="",year="",isbn=""):   # the ="" means that the variable has a default value of NULL and the user must not type title, author, year, isbn, he can type just one or two...
    conn=sqlite3.connect("books.db") 
    cur=conn.cursor()
    cur.execute("SELECT * FROM book where title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
    rows=cur.fetchall()
    conn.close()  
    return rows

def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))   # only the SQL statement is between ""; no variables!!!
    conn.commit()
    conn.close()

def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))   # only the SQL statement is between ""; no variables!!!
    conn.commit()
    conn.close()    

connect()

#insert("The Moon","John Smith",1888,5741233)

#print(view())

#print(search(author="John Smith"))

#delete(4)

#update(3,"Alabala","Pista",2222,38793435)

#print(view())

