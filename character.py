class Character():

    all = []

    def __init__(self, name, curr=1):
        self.name = name
        self.curr = curr
        self.evidence = []
        self.inventory = []
        Character.all.append( self )

    def search():
        pass

    def move(self, dest):
        self.curr = dest

    def info():
        pass

    def acting():
        pass

