class Character():

    all = []

    def __init__(self, name, curr=1):
        self.name = name
        self.curr = curr
        self.evidence = []
        self.inventory = []
    
    def move(self, dest):
        self.curr = dest

    def info():
        pass

    def acting():
        pass
    
    def __repr__(self):
        return f'Name: {self.name}, Location: {self.curr}'