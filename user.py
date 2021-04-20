from datetime import date

def createAccount(mydb,username, Fname, Lname, Gender, DBirth):
    #dateCreate = date.today()
    mycursor = mydb.cursor()
    sql = "INSERT INTO USER (username, Fname, Lname, Gender, DBirth) VALUES (%s, %s, %s, %s, %s)"

    val = (username, Fname, Lname, Gender,DBirth)

    mycursor.execute(sql, val)
    mydb.commit()

def getAccount(mydb, username):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM USER WHERE UserName = %s"
    val = (username,)

    mycursor.execute(sql, val)


    myresult = mycursor.fetchall()
    return myresult
