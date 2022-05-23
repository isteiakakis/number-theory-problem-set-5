def remainder(divisor, base, exponent):
	
	### Compute r_d[b^e]

	# Notation:
	# = is for equality
	# == is for congruence

	from numpy import sign
	
	print("Calculating r_%d[%d^%d] ...\n" % (divisor,base,exponent))
	
	
	### Express the exponent as a sum of powers of 2
	
	# Express the exponent in binary system
	exponent_bits = [int(bit) for bit in bin(exponent)[2:]]
	exponent_bits.reverse() # LSB at index 0
	
	exponent_sum_terms = []; # the terms of the sum
	
	for i, val in enumerate(exponent_bits):
		if val == 1:
			# for every bit that is 1, append the corresponding power of 2 in the terms of the sum
			exponent_sum_terms.append(2**i)
	
	exponent_sum_terms.reverse(); # from biggest to smallest
	
	print("%d = %s = " % (exponent, bin(exponent)), end="") # print the binary representation
	
	# Express the exponent as sum of powers of 2 and print the sum
	for i in range(len(exponent_sum_terms) - 1):
		print("%d + " % (exponent_sum_terms[i]), end="")
	print(exponent_sum_terms[-1])
	print()
	
	
	### Now do the smart calculation process
	
	# Express the power as: base^exponent = base^p1 * base^p2 * ... * base^pm   where p1,...,pm are the exponent sum terms found above
	power_congruent_product_terms = [] 

	# Find the congruent of base^p (where p is a power of 2) for every p up to the maximum exponent sum term

	optimal_congruent = 1 # initialize congruent to 1 because base^0 = 1

	# Calculate all the congruencies up to the maximum term of the exponent_sum_terms (base^p == ... (mod divisor))
	# because every congruence computation is based on its previous congruence result
	for i in range(1, exponent_sum_terms[0]+1):
		prev_congruent = optimal_congruent
		congruent = base * prev_congruent # base * base^(p-1) == base * optimal_congruent_of(base^(p-1)) (mod divisor)
	
		# Calculate the optimal congruent
		optimal_congruent = congruent
		while abs(optimal_congruent) > divisor/2:
			optimal_congruent -= sign(optimal_congruent) * divisor # bring it as close to zero as possible
	
		if i in exponent_sum_terms:
			print("--> ", end="") # indicate which terms are used in the final product
			power_congruent_product_terms.append(optimal_congruent) # and store their optimal congruent
		else:
			print("    ", end="")

		print("%d^%d = %d * %d^%d == %d * (%d) = %d == %d (mod %d)" % (base, i, base, base, i-1, \
			base, prev_congruent, congruent, optimal_congruent, divisor))
	
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
	
