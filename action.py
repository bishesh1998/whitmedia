
from datetime import datetime
#create a action
def createAction(mydb,UserID,PostID,ActionDescr):
    mycursor = mydb.cursor()
    Time = datetime.now()
    sql = "INSERT INTO ACTION (UserName,PostID,Time,ActionDescription) VALUES (%s,%s,%s,%s)"
    val = (UserID,PostID,Time,ActionDescr)

    mycursor.execute(sql,val)
    mydb.commit()

#Save a Post
def savePost(mydb,UserId,PostID):

    mycursor = mydb.cursor()
    Time = datetime.now()
    sql = "INSERT INTO ACTION (UserName,PostID,Time,ActionDescription) VALUES (%s,%s,%s,'saved post')"
    val = (UserId,PostID,Time)

    mycursor.execute(sql,val)
    mydb.commit()

#check if a post is save
def checkSave(mydb, UserID, PostID):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM ACTION WHERE UserName = %s and PostID = %s and ActionDescription = 'saved post'"
    val = (UserID, PostID)
    mycursor.execute(sql, val)
    
    myresult = mycursor.fetchall()
    if len(myresult) > 0:
        return True
    else:
        return False

#unsave a post
def unsave(mydb, UserID, PostID):
    mycursor = mydb.cursor()
    sql = "DELETE FROM ACTION WHERE UserName = %s and PostID = %s and ActionDescription = 'saved post'"
    val = (UserID,PostID)

    mycursor.execute(sql,val)
    mydb.commit()
    return True 

#Like a Post
def likePost(mydb, UserID, PostID):
    mycursor = mydb.cursor()
    Time = datetime.now()
    sql = "INSERT INTO ACTION (UserName,PostID,Time,ActionDescription) VALUES (%s,%s,%s,'like post')"
    val = (UserID,PostID,Time)

    mycursor.execute(sql,val)
    mydb.commit()

#check if the post is liked
def checkLike(mydb, UserID, PostID):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM ACTION WHERE UserName = %s and PostID = %s and ActionDescription = 'like post'"
    val = (UserID, PostID)
    mycursor.execute(sql, val)
    
    myresult = mycursor.fetchall()
    if len(myresult) > 0:
        return True
    else:
        return False
#unlike the post
def unlike(mydb, UserID, PostID):
    mycursor = mydb.cursor()
    Time = datetime.now()
    sql = "DELETE FROM ACTION WHERE UserName = %s and PostID = %s and ActionDescription = 'like post'"
    val = (UserID,PostID)

    mycursor.execute(sql,val)
    mydb.commit()
    return True 

#Count Likes
def countLikes(mydb, PostID):
    mycursor = mydb.cursor()
    sql = "SELECT COUNT(A.PostID) FROM ACTION as A WHERE A.ActionDescription = 'like post' AND A.PostID = %s"
    val = (PostID,)

    mycursor.execute(sql,val)

    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return 0
    else:
        return myresult[0][0]

#let user create post
def createPost(mydb, UserID, PostID):
    createAction(mydb, UserID, PostID, "Create post")





