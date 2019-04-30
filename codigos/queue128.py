
def fat(n):

	if n==1 or n==0: 
		return 1
	else: 
		return fat(n-1)*n

def bt(left,right,not_seen,n,p,r):

	if left<p or right<r or not_seen<0 or p<0 or r<0: 
		return 0

	if left==0 and right==0: 
		if p>0 or r>0:
			return 0
		else:
			return fat(not_seen)

	_sum = 0
	for new_left in range(0,left):
		
		new_not_seen = (left-1) - new_left + not_seen
		_sum += bt(new_left,right,new_not_seen,n,p-1,r)
	
	for new_right in range(0,right):
		
		new_not_seen = (right-1) - new_right + not_seen
		_sum += bt(left,new_right,new_not_seen,n,p,r-1)

	_sum += not_seen*bt(left,right,not_seen-1,n,p,r)

	return _sum


def solve(n,p,r):

	if n == 1:
		if p==1 and r==1:
			return 1
		else:
			return 0

	if n==2:
		if p==1 and r==2:
			return 1
		if p==2 and r==1:
			return 1
		else:
			return 0

	_sum = 0

	for i in range(1,n+1):
		for j in range(i+1,n+1):
			left = i-1
			right = n-j
			not_seen = n-2-left-right
			_sum += bt(left, right, not_seen, n, p-1, r-2)
			_sum += bt(left, right, not_seen, n, p-2, r-1)
	
	return _sum		




def main():

	T = int(input())
	#print(fat(T))
	while(T):
		n,p,r = list(map(int(),input().split()))
		_input = input()
		n,p,r = _input.split(" ")					
		print(solve(int(n),int(p),int(r)))
		T -= 1

if __name__ == "__main__":
	main()