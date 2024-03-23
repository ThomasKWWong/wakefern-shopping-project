import pymysql

def mysqlconnect(): 
    # To connect MySQL database 
    conn = pymysql.connect( 
        host='localhost', 
        user='root',  
        password = "Thoma123$", 
        db='users', 
        )
    
    
def add_member(id, username, password):
    # To connect MySQL database 
    conn = pymysql.connect( 
        host='localhost', 
        user='root',  
        password = "Thoma123$", 
        db='users', 
        )
    cursorObject = conn.cursor()
    sqlQuery = "INSERT INTO profile VALUES (%s, %s, %s, 0)"
    t = (str(id), username, password)
    cursorObject.execute(sqlQuery, t)
    conn.commit()
    conn.close()


def login(username, password):
    # To connect MySQL database 
    conn = pymysql.connect( 
        host='localhost', 
        user='root',  
        password = "Thoma123$", 
        db='users', 
        )
    try:
        # Create a cursor object
        with conn.cursor() as cursor:
            # SQL query to retrieve user information based on the provided username and password
            sql = "SELECT * FROM profile WHERE username=%s AND password=%s"
            
            # Execute the query
            cursor.execute(sql, (username, password))
            
            # Fetch the result
            result = cursor.fetchone()
            
            # Check if a matching user was found
            if result:
                print("Login successful!")
                return {'id' : result[0], 'username' : result[1], 'password' : result[2]}
            else:
                print("Invalid username or password")
                return False
            
    except pymysql.Error as e:
        print(f"Error: {e}")
        return False
    
    finally:
        # Close the database connection
        conn.close()

  
# Driver Code 
if __name__ == "__main__" : 
    add_member(100, "timmy", "timiscool")
    print(login("timmy", "timiscool"))
