
def save_data(file_name, data):
    with open(file_name, "w") as file:
        file.write(data)

def append_data(file_name, data):
    with open(file_name, "a") as file:
        file.write(data)

def read_data(file_name):
    with open(file_name, "r") as file:
        result = file.read()
        return result

