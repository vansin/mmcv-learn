def multiply_by(factor):
    def multiply(value):
        return value*factor
    return multiply

time2 = multiply_by(2)

print(time2(10))
print(multiply_by(2)(10))