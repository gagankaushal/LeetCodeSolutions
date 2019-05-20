def iq_test(numbers):
    #your code here

    flagEven = 0
    flagOdd = 0

    for i in range(0,len(numbers)):
        if numbers[i]%2 == 0:
            flagEven = flagEven + 1
            positionEven = i

        else:
            flagOdd = flagOdd + 1
            positionOdd = i

    if flagOdd == 1:
        return positionOdd

    else:
        return positionEven

