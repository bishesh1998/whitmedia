#Post queries used in the program as well as the action associated with creating posts
import action 

# createPost() simply inserts a post into the database. 
#   Input: database server, the username, and the string content to be added 
def createPost(mydb,username,content):
    mycursor = mydb.cursor()
    sql = "INSERT INTO POST (username,content) VALUES (%s,%s)"
    val = (username,content)

    mycursor.execute(sql,val)
    mydb.commit()

    postID =  mycursor.lastrowid
    action.createPost(mydb, username, postID) # an action 'Create Post' will be added every time the user posts something


# getAllUserPost() gets all the posts based on a username
# input: database server, username
def getAllUserPost(mydb, username):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM POST WHERE UserName = %s"
    val = (username, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    return myresult


# getFollowerPosts() gets posts from people that the user follows. The index makes sure we can scroll through posts 
# correctly. i.e. go from '0' to 'n' posts and from 'n'  to '0' correclty
def getFollowerPosts(mydb, username, index = 0):
    # SELECT * from POST P
    # WHERE P.UserName IN
    # 	(SELECT FollowerID FROM FOLLOWER as F
    # 	WHERE F.AuthorFollowID = 'nhatminh')
    # LIMIT 0,1;
    mycursor = mydb.cursor()
    sql = '''SELECT * from POST P
        WHERE P.UserName IN
            (SELECT FollowerID FROM FOLLOWER as F
            WHERE F.AuthorFollowID = %s)
        LIMIT %s,1;
        '''
    val = (username,index)

    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return (0,0,0)
    else:
        return myresult[0]


# countVisiblePost() counts the posts based on the followers that a user has. This is used in the feed of the user to see what
# other users are posting. 
# input: database server and username
def countVisiblePost(mydb, username):
    mycursor = mydb.cursor()
    sql = '''SELECT COUNT(P.ID) from POST P
        WHERE P.UserName IN
            (SELECT FollowerID FROM FOLLOWER as F
            WHERE F.AuthorFollowID = %s);
        '''
    val = (username,)

    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    if len(myresult) == 0:
        return 0
    else:
        return myresult[0][0]

# countPost() counts all the posts created by a specific user
# input: databaser server, username 
def countPost(mydb, username):
    mycursor = mydb.cursor()
    sql = "SELECT COUNT(ID) FROM POST WHERE UserName = %s"
    val = (username, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    return myresult[0][0]
    
