from clicp.database import addProblem

def add():
    
    entrace = input()

    parts = entrace.split(" ")

    addProblem(parts[0], parts[1], parts[2])