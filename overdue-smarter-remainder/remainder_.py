def remainder(divisor, base, exponent):
	
	### Compute r_d[b^e]

	# Notation:
	# = is for equality
	# == is for congruence

	from numpy import sign
	
	print("Calculating r_%d[%d^%d] ...\n" % (divisor,base,exponent))
	
	
	### Express the exponent as a sum of powers of 2: exponent = p1+...+pm   where p1,...,pm are powers of 2
	
	# Express the exponent in binary system
	exponent_bits = [int(bit) for bit in bin(exponent)[2:]]
	exponent_bits.reverse() # LSB at index 0
	
	exponent_sum_terms = []; # the terms of the sum: p1,...,pm
	
	for i, val in enumerate(exponent_bits):
		if val == 1:
			# for every bit that is 1, append the corresponding power of 2 in the terms of the sum
			exponent_sum_terms.append(2**i)
	
	exponent_sum_terms.reverse(); # from biggest to smallest: p1>...>pm
	
	print("%d = %s = " % (exponent, bin(exponent)), end="") # print the binary representation
	
	# Express the exponent as sum of powers of 2 and print the sum
	for i in range(len(exponent_sum_terms) - 1):
		print("%d + " % (exponent_sum_terms[i]), end="")
	print(exponent_sum_terms[-1])
	print()
	
	
	### Now do the smart calculation process
	
	# Express the power as: base^exponent = base^p1 * base^p2 * ... * base^pm
	# where p1,...,pm are the powers of 2 terms of the exponent sum found above, p1>...>pm

	# Calculate the optimal congruent of each of the terms   base^p1, ..., base^pm
	# The optimal congruent is the one that is closer to zero than any other one
	power_congruent_product_terms = []

	# Find the congruent of base^p (where p is a power of 2) for every p up to the maximum exponent sum term

	# Initialize: p=1
	# Calculate the optimal congruent of base^1 (mod divisor)
	p = 1
	optimal_congruent = base
	while abs(optimal_congruent) > divisor/2:
			optimal_congruent -= sign(optimal_congruent) * divisor # bring it as close to zero as possible

	# Find which terms are needed for final result calculation 
	if p in exponent_sum_terms: # if p in {p1, ..., pm} then
		print("--> ", end="") # indicate which congruences are used in the final product
		power_congruent_product_terms.append(optimal_congruent) # and store their optimal congruent
	else:
		print("    ", end="")

	print("%d^1 = %d == %d (mod %d)" % (base, base,\
		optimal_congruent, divisor))

	exponent_bits_length = len(exponent_bits)

	# General step:
	# Calculate all the congruencies base^p == ... (mod divisor) where p=2^i for i=1,...,exponent_bits_length
	# because every congruence computation is based on its previous congruence result
	# i.e. if u is the optimal congruence of base^p (which implies base^p == u (mod divisor)) then base^(2p) == u^2 == ... (mod divisor)
	# The i=0 case (p=2^0=1) is calculated at the initialization step
	for i in range(1, exponent_bits_length):
		p = 2**i;
		prev_congruent = optimal_congruent
		congruent = prev_congruent**2 # base^p = (base^(p/2))^2 == optimal_congruent_of(base^(p/2))^2 (mod divisor)
	
		# Calculate the optimal congruent
		optimal_congruent = congruent
		while abs(optimal_congruent) > divisor/2:
			optimal_congruent -= sign(optimal_congruent) * divisor # bring it as close to zero as possible
	
		# Find which terms are needed for final result calculation 
		if p in exponent_sum_terms: # if p in {p1, ..., pm} then
			print("--> ", end="") # indicate which congruences are used in the final product
			power_congruent_product_terms.append(optimal_congruent) # and store their optimal congruent
		else:
			print("    ", end="")

		print("%d^%d = (%d^%d)^2 == %d^2 = %d == %d (mod %d)" % (base, p, base, p/2,\
			prev_congruent, congruent, optimal_congruent, divisor))
	
	power_congruent_product_terms.reverse(); # from biggest to smallest
	
	print()
	
	
	# Find the final result doing the product of the congruents (smartly)
	left_side = "%d^%d" % (base, exponent_sum_terms[0])
	optimal_congruent_product = power_congruent_product_terms[0]
	
	if len(power_congruent_product_terms) > 1:

		for i in range(1, len(power_congruent_product_terms)):
			left_side += " * %d^%d" % (base, exponent_sum_terms[i])

			# Same scheme as above for smart congruence computation
			prev_product = optimal_congruent_product
			product = prev_product * power_congruent_product_terms[i]
	
			optimal_congruent_product = product
			while abs(optimal_congruent_product) > divisor/2:
				optimal_congruent_product -= sign(optimal_congruent_product) * divisor
	
			print(left_side + " == (%d) * (%d) = %d == %d (mod %d)" % (prev_product, power_congruent_product_terms[i], product, optimal_congruent_product, divisor))
	
	print()
	
	# Find the remainder
	remainder = optimal_congruent_product
	if remainder < 0:
		remainder += divisor
	
	print("%d^%d == %d == %d (mod %d)\n" % (base, exponent, optimal_congruent_product, remainder, divisor))
	
	print("r_%d[%d^%d] = %d\n\nDone" % (divisor, base, exponent, remainder))
	
	print("---------------------------------------------------------------------------------------------------------------------------------\n\n")

	return remainder
	
