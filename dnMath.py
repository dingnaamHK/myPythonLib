class sim():
    def __init__(self, *addargs):
        self.addargs = list()
        for i in addargs:
            self.addargs.append(i)
        
    def __dataValidateForCal(self):
        if len(self.addargs) < 2:
            raise ValueError("Please input at least two arguments")
    def add(self):
        self.__dataValidateForCal()
        count = 0
        for j in self.addargs:
            count += j
        return count
    
    def mul(self):
        self.__dataValidateForCal()
        count = 1
        for k in self.addargs:
            count *= k
        return count
    
    def addFromRange(self):
        # Data Validation
        if len(self.addargs) != 2:
            raise ValueError("Please provide exactly 2 argument: lower and upper bound")
        elif (type(self.addargs[0]) is not int) or (type(self.addargs[1]) is not int):
            raise TypeError("Both arguments must be integers.")
        elif self.addargs[0] >= self.addargs[1]:
            raise ValueError("Upper bound must be greater than lower bound")
        # End of Data Validation

        count = 0
        for i in range(int(self.addargs[0]), int(self.addargs[1])+1):   #inclusive both bound
            count += i
        return count