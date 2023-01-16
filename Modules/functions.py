def read_todos(filename="todos.txt"):
    """ Read a text file and return the list of
    to-do items.
    """
    with open("Files/" + filename, "r") as file_read:
        todos_read = file_read.readlines()
    return todos_read


def write_todos(todos_write, filename="todos.txt"):
    """ Write the to-do items list in the text file """
    with open("Files/" + filename, "w") as file_write:
        file_write.writelines(todos_write)

