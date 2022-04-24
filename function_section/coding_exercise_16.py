from re import A


def sum_eo (n, t):
    result =0
    if t == 'e':
        for i in range (1, n):
            if i%2 == 0:
                result +=i
        return(result)
    elif t =='o':
        for i in range (1, n):
            if i%2 !=0:
                result +=i
        return(result)
    else :
        return (-1)
temp = int(input())
stringTemp = str(input())
value = sum_eo(temp, stringTemp)
print (value)
        
