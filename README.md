# myPythonLib (beta 2.0)
```python
import dnMath
```

## dnMath.sim() 
Simple addition and multiplication with any amount of numbers
Initialisation syntax:
```python
var = dnMath.sim(*args) #Abritary amount of arguments
```

### Addition of Any Amount of Numbers
For addition (getting the sum):
```python
var = dnMath.sim(*args) #Abritary amount of arguments
var.add()
```
### Multiplication of Any Amount of Numbers
For multiplication (getting the product):
```python
var = dnMath.sim(*args) #Abritary amount of arguments
var.mul()
```

### Summation of All Consecutive Integer in Specific Range
Two arguments are required: lower bound and upper bound.
The function will return the sum of all integers within the range bounded by the upper and lower bound INCLUSIVELY.
```python
var = dnMath.sim(arg1, arg2)
var.addFromRange()
```
IMPORTANT: the value of arg2 must be larger than that of arg1.

## dnMath.calculus()
### Differentiate a Polynomial
The arguments can be divided into three parts.  Namely, power of polynomial, and coefficient(s) of the polynomial, and the constant term of the polynomial.
```python
var = dnMath.calculus(power, coefficient1, coefficient2, ..., constantTerm)
var.ddxp()
```
Please MAKE SURE the value of argument "power' is equal to the number of other proceding arguments, for example:
```python
var = dnMath.calculate(2,3,3,3)   # This is valid
var = dnMath.calculate(2,3,3,3,3,3,3) # This will cause an exceptio
```
### Show the Polynomial for Easier Reading
After running ddxp(), a list will be returned.
To show the math expression, please do the following command after that.
```python
var.ddxf()
```
For example when ddxp() returns [6,3,0], the result of ddxf() will be:
d/dx = 6 x ^ 2 + d/dx = 3 x ^ 1 + 0
None

** There is a bug that an extra None will returned by ddx(), this minor problem will be fixed soon.  No affect to the precision of the result.