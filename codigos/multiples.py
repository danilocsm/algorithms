
import math as m
#from jutge import read

def countMultiples(a,b,c):

    count = 0

    if a%c == 0 or b%c == 0:
        count+=1

    aux = (b-a)

    if aux+c>=b:
        count += m.floor((b-a)/c)
        return count

    count += m.ceil((b-a)/c)

    return count

def main():
    
    a = int(input())
    b = int(input())
    c = int(input())

    count = countMultiples(a,b,c)

    print("{0}".format(count))

main()