# 
# Ingest class 
#

from os import path

class Ingest():

    def __init__(self):
        None
    
    def load_nginx_logs(self, filepath: str) -> bool:
        
        # Return is file don't exist
        if (not path.isfile(filepath)):
            return (False)

        fd = open(filepath, "r")

        for line in fd.readlines():
            print(line, end="")

        return (True)
    