from random import randint

def gcd(a, b):
	return a if b == 0 else gcd(b, a % b)			 

def bez_gcd(a, b):
	'''
		returns gcd(a,b),u,v such that au + bv = gcd(a,b) u and v are integers 
	'''
	u,g,x,y = 1,a,0,b

	while(True):
		if(y == 0):
			if(b == 0):
				return (a,1,1)

			v = (g - a*u) / b 
			return (g, u, v)
		else:
			q = g / y
			t = g % y
			s = u - q*x
			u,g = x,y
			x,y = s,t

def exp_naive(g,A,N):
	'''
		naive exponentiation g^A mod N
	'''
	count = 1
	prod = g
	while(count < A):
		prod = (g * prod) % N
		count += 1
	return prod  

def sq_multiply(g,A,N):
	'''
		square and multiply for fast exponentiation g^A mod N
	'''
	bin_pow_list = map(int, list(bin(A)[2:]))
	prod = g
	fin_prod = 1
	bin_max = len(bin_pow_list)  
	for i in range(bin_max):
		if(bin_pow_list[bin_max-i-1] == 1):
			fin_prod = fin_prod * prod
		prod = (prod**2) % N 
	return fin_prod % N	

def fermats_primality_test(m):
	'''
		randomized primality test 
	'''
	cycles = 10
	while(cycles > 0):
		a = randint(1, m-1)
		if(gcd(a,m) != 1):
			return "not prime"
		else:
			if(sq_multiply(a, m-1, m) != 1):
				return "not prime"
		cycles -= 1

	return "prime"		

def est_no_of_prime(n):
	'''
		estimated number of primes till n
		try out n=7919, the 1000th prime
		not the fastest way to estimate though 
	'''
	count = 0
	for i in range(2,n+1):
		if(fermats_primality_test(i) == 'prime'):
			count += 1

	return count

def relatively_prime_list(n):
	rpl = []
	for i in range(1,n):
		if(gcd(i,n) == 1):
			rpl.append(i)
	return rpl		
