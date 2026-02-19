# here in this program we make same previous like application where we manger our youtube videos but with the help of database

# here we use the alomost inbuilt database for phthon i.e, SQLite
import sqlite3

# now we make the connection to the databse with our file
conn = sqlite3.connect("Youtube_videos.db")

# then we take the cursor from the connection for executing our query
cursor = conn.cursor()

# now we write the query for the file
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
            id  INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
    )       
''')

# lets make the list all videos defination
def list_all_videos():
    # here we write the code for showing all the data to the users 
    # first of all fetch all the data from the database then we ittrate all the data one by one
    cursor.execute("SELECT * FROM videos")
    for rows in cursor.fetchall():
        print(rows)


def add_videos(name, time):
    # now we use the insert the data in the table for add feature
    cursor.execute("INSERT INTO VIDEOS(name, time) VALUES(?, ?)", (name, time))
    # now we save the data
    conn.commit()


def update_videos(index, new_name, new_time):
    # here we write the code or updating the table
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(new_name,new_time,index))
    conn.commit()
    

def delete_videos(index):
    # here we use the query of the sql to delete the row
    cursor.execute("DELETE FROM videos WHERE id = ?",(index, ))
    # if we have only one argument to pass then we have the use one comma in the last 
    conn.commit()




# now we make the main fucntion that will run the firstly
def main():
    # now we make the while loop so our code will run in infinite loop
    while True:
        print("\nYoutube Videos Manager with DataBase")
        print("1. List all videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit App")
        choice = int(input("Enter Your Choice: "))
        
        if choice == 1:
            list_all_videos()
        elif choice == 2:
            name = input("Enter the name: ")
            time = input("Enter the time: ")
            add_videos(name,time)
        elif choice == 3:
            index = int(input("Enter the index that you want to update: "))
            name = input("Enter the name: ")
            time = input("Enter the time: ")
            update_videos(index,name,time)
        elif choice == 4:
            index = int(input("Enter the id of the video that you want to delete: "))
            delete_videos(index)
        elif choice == 5:
            break
        else:
            print("Invlaid Choice")

    # now we close the connection of the file and the database
    conn.close()


        


# now we write the same old code that ager hamre file ka naam main hai toh usse sabse pahle run karwa dena
if __name__ == "__main__":
    main()