def mysum(*numbers):
    output = 0
    for number in numbers:
        output +=number
    print(output)
    return output


mysum(1,2,3,4)