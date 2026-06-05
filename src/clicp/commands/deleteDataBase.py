from clicp.database import deleteData

def reset():
    deleteData()

    print("Database deleted.")