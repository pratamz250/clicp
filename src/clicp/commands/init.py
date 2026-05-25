from clicp.database import createDataDir
from clicp.database import initializeDataBase

def init():
    createDataDir()
    initializeDataBase()

    print("clicp inicilizado")