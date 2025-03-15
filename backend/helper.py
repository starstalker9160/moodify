import os
import shutil


def foreplay():
    """Initialization of the app, (foreplay before the good stuff)
        1. Create db if not existing
        2. Clear pycache to avoid bugs
    """
    filepath = "db/moodJournal.csv"
    folder = os.path.dirname(filepath)

    out = "I-"

    if not os.path.exists(folder):
        os.makedirs(folder)
        out += "2"
    else:
        out += "1"

    if not os.path.exists(filepath):
        with open(filepath, "w") as file:
            file.write("S,Rating,Happy,Anger\n")
        out += "2"
    else:
        out += "1"

    pycache_path = os.path.join(os.getcwd(), "backend/__pycache__")
    if os.path.exists(pycache_path):
        shutil.rmtree(pycache_path)
        print("Deleted __pycache__ directory.")
    
    return out