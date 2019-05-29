# caclcula quantos multiplos de C existe(m) entre A e B
import math as m

def countMultiples(a,b,c):
    count = 0
    if a%c == 0 or b%c == 0:
        count += 1
    aux = (b-a)
    if aux+c>=b:
        count += m.floor((aux)/c)
    else:
        count += m.ceil((aux)/c)

    return count

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    count = countMultiples(a,b,c)

    print("{0}".format(int(count)))

main()
