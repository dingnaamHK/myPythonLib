class sim():
    def __init__(self, *addargs):
        self.addargs = list()
        for i in addargs:
            self.addargs.append(i)
        
    def add(self):
        count = 0
        for j in self.addargs:
            count += j
        return count
    
    def mul(self):
        count = 1
        for k in self.addargs:
            count *= k
        return count
    
