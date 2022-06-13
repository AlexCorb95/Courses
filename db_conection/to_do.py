import pymysql


class ToDoApp:
    def __init__(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database=""
        )
        with connection.cursor() as c:
            c.execute("CREATE SCHEMA IF NOT EXISTS `ToDo_DB` DEFAULT CHARACTER SET utf8;")
        connection.close()
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="ToDo_DB"
        )
        with connection.cursor() as c:
            c.execute(
                "CREATE TABLE IF NOT EXISTS `todo_list`(taskID int primary key auto_increment,task varchar(255),done boolean);")
        connection.close()

    # create conection db
    # create schema if not exists
    # create table if not exists
    def show(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="ToDo_DB"
        )
        with connection.cursor() as c:
            c.execute("select * from `todo_list`;")
            results = c.fetchall()
            for elem in results:
                s = lambda x: 'Status: Done' if x == 1 else 'Status: Not Done'
                print(f"TaskID :{elem[0]} | Task: {elem[1]} | {s(elem[2])} ")
            connection.close()

    def mark(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="ToDo_DB"
        )
        with connection.cursor() as c:
            get_id = int(input("Enter the task ID: "))
            get_mark = int(input("Type 1 if the task is Done else 0: "))
            c.execute("UPDATE `todo_list` SET done=%s WHERE taskID=%s;", (get_mark, get_id))
            connection.commit()

        connection.close()

    # ask user for id to mark and mark it
    def add(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="ToDo_DB"
        )
        with connection.cursor() as c:
            user_get = str(input("State the task you wish to enter:"))
            c.execute("INSERT INTO `todo_list` (task,done) values (%s,false);", user_get)
            connection.commit()
        connection.close()

    # ask user for task details and save it to db
    def delete(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="ToDo_DB"
        )
        with connection.cursor() as c:
            user_id=int(input("Select the ID of the task you wish to delete: "))
            c.execute("DELETE FROM `todo_list` WHERE taskID=%s;",user_id)
            connection.commit()
        connection.close()


    def start(self):
        print("Available Tasks are:\n show \n mark \n add/delete")
        while True:
            user_input = input("Select your action: ")

            if hasattr(self, user_input) and callable(getattr(self, user_input)):
                getattr(self, user_input)()
            else:
                break


ToDoApp().start()
