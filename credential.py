
#create credential
def createCredential(mydb, username, password, email):
    mycursor = mydb.cursor()
    sql = "INSERT INTO CREDENTIAL (UserName, Password, Email) VALUES (%s, %s, %s)"
    val = (username, password, email)

    mycursor.execute(sql, val)
    mydb.commit()

#change the password of the user
def changePassword(mydb, username, newPassword):
    mycursor = mydb.cursor()
    sql = "UPDATE CREDENTIAL SET Password = %s WHERE UserName = %s"
    val = (newPassword, username)

    mycursor.execute(sql, val)
    mydb.commit()

#change the email of the user
def changeEmail(mydb, username, newEmail):
    mycursor = mydb.cursor()
    sql = "UPDATE CREDENTIAL SET Email = %s WHERE UserName = %s"
    val = (newEmail, username)

    mycursor.execute(sql, val)
    mydb.commit()

#check if the username and password are correct to login
def checkCredential(mydb, username, password):
    mycursor = mydb.cursor()
    sql = "SELECT Password from CREDENTIAL where UserName = %s"
    val = (username,)
    mycursor.execute(sql, val)

    myresult = mycursor.fetchall()

    if len(myresult) == 0:
        return False
    if myresult[0][0] == password:
        return True
    else:
        return False

