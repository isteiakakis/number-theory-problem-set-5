def primitive_root_mod_prime(n):
	
	# It is supposed that n is a prime number

	# Notation:
	# = is for equality
	# == is for congruence
	
	from random import shuffle
	from remainder_ import remainder
	
	# Tn = {1,...,n-1}
	Tn = [i for i in range(1,n)]
	shuffle(Tn)

	break_both_loops = False

	for a in Tn:
		print("############################################################# Try a=%d #############################################################" % (a))
		for k in range(1,n):
			if (n-1) % k != 0: # in order to ensure than k belongs to S_phi(n) = S_{n-1}
				continue
			
			if remainder(n, a, k) == 1:
				if k == n-1:  # k == phi(n), primitive root found
					prim_root = a
					break_both_loops = True
					
				#else just go to the next value of a

				break
		
		if break_both_loops:
			break

	print("Primitive root found.")
	print("A primitive root mod %d is: %d" % (n, prim_root))
	
	return prim_root
