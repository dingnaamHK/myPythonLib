# myPythonLib (beta 1.0)
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

