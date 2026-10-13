def ISBN(digits):
    counter = 0    
    for i in range(0,len(digits)):
        if (i % 2) == 0:
            counter += int(digits[i])
        else:
            counter += int(digits[i]) * 3
    # mod 10 again so a sum ending in 0 gives check digit 0, not 10
    DigitTwelth = (10 - counter%10) % 10
    return DigitTwelth    

print(ISBN("978030640615"))