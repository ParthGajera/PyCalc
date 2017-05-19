import operator

a = "114 + 9".split()

oldResult = int(a[0])
newInput= int(a[2])
mathOperator = "-"

dict1=  {
        "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "/" : operator.truediv,
        }

def calculate(oldResult, newInput, mathOperator):
        func= dict1[mathOperator]
        result = func(newInput,oldResult)
        return result

calc = calculate(oldResult,newInput,mathOperator)

print('Result: ', calc)