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
    
class calculus:
    def __init__(self, power, *coefficents):    

        self.power = power
        self.coefficients = list()
        for i in coefficents:
            self.coefficients.append(i)
        # Data Validation: no. of coeffecients = power+1
        if self.power != (len(self.coefficients) - 1):
            raise ValueError("Number of coefficients must be equal to power + 1")
        
    def ddxp(self):
        # Differentiation of a polynomial
        #### Data Validation
        # TODO
        ################################
        ##Logic:  c * p -> c AND p - 1 -> p
        newCoefficents = list()
        c = 0
        p = self.power 
        while c < len(self.coefficients) and (p <= self.power and p >= 0):
            newCoefficentsElement = self.coefficients[c] * p
            newCoefficents.append(newCoefficentsElement)
            p -= 1
            c += 1
            if len(newCoefficents) == c:
                continue
            else:
                break        
        return newCoefficents
    
    def ddxf(self):
        # get the formula
        cList = self.ddxp()
        print("d/dx = ", end="")
        for (i,j) in enumerate(cList):
            if self.power - i > 0:
                print(j, "x ^", self.power - i, "+ ", end="")
            elif self.power - i == 0:
                print(j) 
            else:
                break

        ### TODO IMPROVE: unexpected "None" after last term.


    def itg(self):
        # integration to a polynomial
        newCoefficents = list()
        #Logic : p + 1 -> p THEN c / p -> c
        c = 0
        p = self.power
        while c < len(self.coefficients) and (p <= self.power and p >= 0):
            x = p + 1
            newCoefficientsElement = self.coefficients[c] / x
            newCoefficents.append(newCoefficientsElement)
            c += 1
            p -= 1
            if len(newCoefficents) == c:
                continue
            else:
                break        
        return newCoefficents

    def itgf(self):
        cList = self.itg()
        print("∫f(x) dx = ", end="")
        for (i,j) in enumerate(cList):
            if self.power - i > 0:
                print(j, "x ^", self.power - i, "+ ", end="")
            elif self.power - i == 0:
                print(j, end="") 
            else:
                break
        print(" + C")  # Indefinite integral constant