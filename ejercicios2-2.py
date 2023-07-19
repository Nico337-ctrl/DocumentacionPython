def numerosPrimos(num):
    for i in range(2, num-1):
        if(num%i == 0):
            return False

