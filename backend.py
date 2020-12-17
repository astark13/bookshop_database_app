import sqlite3

class Database:

    def __init__(self,db):                   # the first function in a class must be called "__init__"; this function is executed when you call a class
                                             # the "(self)" argument is needed because when the database class is called it creates an object which has to be refered to 
        self.conn=sqlite3.connect(db)        # when using OOP/classes we declare the connection and cursor strings only in the first method;
        self.cur=self.conn.cursor()               # the following methods inherit/use these connection strings
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year INTEGER, ISBN INTEGER)")
        self.conn.commit()
        

    def insert(self,title,author,year,isbn):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn))   # only the SQL statement is between ""; no variables!!!
        self.conn.commit()
        
    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self,title="",author="",year="",isbn=""):   # the ="" means that the variable has a default value of NULL and the user must not type title, author, year, isbn, he can type just one or two...
        self.cur.execute("SELECT * FROM book where title=? OR author=? OR year=? OR isbn=?",(title,author,year,isbn))
        rows=self.cur.fetchall()
        return rows

    def delete(self,id):
        self.cur.execute("DELETE FROM book WHERE id=?",(id,))   # only the SQL statement is between ""; no variables!!!
        self.conn.commit()
        
    def update(self,id,title,author,year,isbn):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))   # only the SQL statement is between ""; no variables!!!
        self.conn.commit()
           
    def __del__(self):         #closes the connection to the database when the program exits
        self.conn.close()



    #connect()

    #insert("The Moon","John Smith",1888,5741233)

    #print(view())

    #print(search(author="John Smith"))

    #delete(4)

    #update(3,"Alabala","Pista",2222,38793435)

    #print(view())

