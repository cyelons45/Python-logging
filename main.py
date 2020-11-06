from funcA import AddandMultiply
from funcB import SubtractandDivide

sums = AddandMultiply(2, 3, 4, 5, 7).add()
mult = AddandMultiply(2, 4).multiply()

sub = SubtractandDivide().subtract(6, 2)
divide = SubtractandDivide().divide(5, 3)


if __name__ == "__main__":
    print(sums)
    print(mult)
    print("-------------------------------------------------------")
    print(sub)
    print(divide)
