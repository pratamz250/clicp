from clicp.database import delete_data

def reset():
    delete_data()

    print("Database deleted.")