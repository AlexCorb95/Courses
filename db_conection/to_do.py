import pymysql

class ToDoApp:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database=""
        )
        with self.connection.cursor() as c:
            c.execute("CREATE SCHEMA IF NOT EXISTS `ToDo_DB` DEFAULT CHARACTER SET utf8;")
        self.connection.close()
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="ToDo_DB"
        )
        with connection.cursor() as c:
            c.execute("CREATE TABLE IF NOT EXISTS `todo_list`(taskID int primary key auto_increment,task varchar(255),done boolean);")
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
            print(c.fetchall())

    def mark(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="ToDo_DB"
        )
        pass
    # ask user for id to mark and mark it
    def add(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="root",
            database="ToDo_DB"
        )
        with connection.cursor() as c:
            user_get=str(input("State the task you wish to enter:"))
            c.execute("INSERT INTO `todo_list` (task,done) values (%s,false);",(user_get))
            connection.commit()

    # ask user for task details and save it to db

    def start(self):
        while True:
            user_input=int(input("Select your next action: "))
            if user_input == 1:
                self.add()
            if user_input == 2:
                self.show()
            if user_input == 0:
                break

        # ask user for action
        # repeat until action = exit

ToDoApp().start()
