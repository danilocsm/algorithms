import math as m

vaiUm = 0

def copy(num1,num2,pos):

	while(pos>=0):
		num1.insert(0,num2[pos])
		pos-=1

def soma(num1,num2):

	global vaiUm

	output = []
	num1 = num1.lstrip("0")
	num2 = num2.lstrip("0")

	len1 = len(num1)
	len2 = len(num2)

	if(len1 == 1 and len2 == 1):
		return str(int(num1)+int(num2))

	len1-=1
	len2-=1
	while(True):
		try:
			aux = int(num1[len1]) + int(num2[len2]) + vaiUm
			vaiUm = m.floor(aux/10)
			output.insert(0,str(aux%10))
		except IndexError:
			pass
		finally:
			 len1 = len1 - 1
			 len2 = len2 - 1

		if(len1<0):
			if(vaiUm>0):
				while(vaiUm>0):
					output.insert(0,str((int(num2[len2])+vaiUm)%10))
					vaiUm = m.floor((int(num2[len2])+vaiUm)/10)
					len2-=1
			else:
				copy(output,num2,len2)
			break

		if(len2<0):
			if(vaiUm>0):
				while(vaiUm>0):
					output.insert(0,str((int(num1[len1])+vaiUm)%10))
					vaiUm = m.floor((int(num1[len1])+vaiUm)/10)
					len1-=1
			else:
				copy(output,num1,len1)
			break
	output = "".join(output)
	return output



def main():

	num1 = input()
	num2 = input()

	num3 = soma(num1,num2)

	print(num3)

if __name__ == "__main__":
	main()
