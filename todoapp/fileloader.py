import json

class FileLoader:
    def __init__(self):
        self.filename=""

    def load_file(self,file):
        self.filename=file
        with open (self.filename,"r") as doc:
            temp_tasklist= json.load(doc)
            return temp_tasklist

    def close(self,close):
        with open(self.filename, "w") as doc:
            json.dump(close, doc)
