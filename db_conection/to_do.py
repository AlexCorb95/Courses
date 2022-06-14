import pymysql


def execute_query(query, database=""):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="root",
        database=database
    )
    with connection.cursor() as c:
        c.execute(query)
        connection.commit()
        results = c.fetchall()
    connection.close()
    return results


class ToDoApp:
    def __init__(self):
        execute_query("CREATE SCHEMA IF NOT EXISTS `ToDo_DB` DEFAULT CHARACTER SET utf8;")
        execute_query("CREATE TABLE IF NOT EXISTS `todo_list`(taskID int primary key auto_increment,task varchar(255),done boolean);","ToDo_DB")

    def show(self):
        results = execute_query("select * from `todo_list`;","ToDo_DB")

        for elem in results:
            s = lambda x: 'Status: Done' if x == 1 else 'Status: Not Done'
            print(f"TaskID :{elem[0]} | Task: {elem[1]} | {s(elem[2])} ")

    def mark(self):

        get_id: int = int(input("Enter the task ID: "))
        get_mark: int = int(input("Type 1 if the task is Done else 0: "))

        execute_query(f"UPDATE `todo_list` SET done={get_mark} WHERE taskID={get_id};","ToDo_DB")


    def add(self):
        user_get = input("State the task you wish to enter:")
        execute_query(f"INSERT INTO `todo_list` (task,done) values ('{user_get}',false);","ToDo_DB")


    def delete(self):
        user_id = int(input("Select the ID of the task you wish to delete: "))
        execute_query(f"DELETE FROM `todo_list` WHERE taskID='{user_id}';","ToDo_DB")



    def start(self):
        print("Available Tasks are:\n show \n mark \n add/delete")
        while True:
            user_input = input("Select your action: ")

            if hasattr(self, user_input) and callable(getattr(self, user_input)):
                getattr(self, user_input)()
            else:
                break


ToDoApp().start()
