import math as m

def ComputeAngle(hour,minute):

	angleA = (hour+minute/60)*30
	angleB = minute*6
	
	if angleA > angleB:
		output = angleA - angleB
	else:
		output = angleB - angleA

	if output>180:
		return m.ceil(360-output)
	else
		return m.ceil(output)

while True:
	try:
		entry = input()

		aux = entry.split(":")

		hour = int(aux[0])
		minute = int(aux[1])

		if hour>12 or hour<1:
			raise ValueError
		elif minute<0 or minute>59:
			raise ValueError
	except ValueError:
		break
	except IndexError:
		break
	else:
		if minute==0 and hour==0:
			break
		print("{:.3f".format(ComputeAngle(hour,minute)))	
		