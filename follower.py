import action

#add a folllower to the user's account
def addFollowerToList(mydb, AuthorFollowID, FollowerID):
    mycursor = mydb.cursor()
    sql = "INSERT INTO FOLLOWER (AuthorFollowID, FollowerID) VALUES (%s, %s)"
    val = (AuthorFollowID, FollowerID)

    mycursor.execute(sql, val)
    
    mydb.commit()



#delete a follower from the user's account
def deleteFollower(mydb, FollowerID):
    mycursor = mydb.cursor()
    sql = "DELETE FROM FOLLOWER WHERE FollowerID = %s"
    FollowerID = 'radom'
    mycursor.execute(sql, (FollowerID,))
    
    mydb.commit()


#count the number of followers that an account has
def countFollowers(mydb, AuthorFollowID):
    mycursor = mydb.cursor()
    sql = "SELECT COUNT(FollowerID) FROM FOLLOWER WHERE FollowerID = %s"
    val = (AuthorFollowID,)
    mycursor.execute(sql, val)
    
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return 0
    else:
        return myresult[0][0]
    



    



