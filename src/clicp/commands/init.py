from clicp.database import create_data_dir
from clicp.database import initialize_data_base

def init():
    create_data_dir()
    initialize_data_base()

    print("clicp started.")