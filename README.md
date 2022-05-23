# number-theory-problem-set-5

Inside the "overdue/" directory the remainder function in the "remainder_.py" file is implememented in a much more efficient way than the previous implementation. 

Huge difference can be observed for big exponents.

The changes were made in the code section after the comment
```
### Now do the smart calculation process
```
and before the comment
```
# Find the final result doing the product of the congruents (smartly)
```

The comments in the code describe how the new implementation is working.

To summarize:
```
remainder(divisor, base, exponent)

### Compute r_d[b^e]

# Notation:
# = is for equality
# == is for congruence

### Express the exponent as a sum of powers of 2: exponent = p1+...+pm   where p1,...,pm are powers of 2

# Express the power as: base^exponent = base^p1 * base^p2 * ... * base^pm
# where p1,...,pm are the powers of 2 terms of the exponent sum found above, p1>...>pm

# Calculate the optimal congruent of each of the terms   base^p1, ..., base^pm
# The optimal congruent is the congruent that is closer to zero than any other one

# Find the congruent of base^p (where p is a power of 2) for every p up to the maximum exponent sum term

# Initialize: p=1
# Calculate the optimal congruent of base^1 (mod divisor)

# General step:
# Calculate all the congruencies base^p == ... (mod divisor) where p=2^i for i=1,...,exponent_bits_length
# because every congruence computation is based on its previous congruence result
# i.e. if u is the optimal congruence of base^p (which implies base^p == u (mod divisor)) then base^(2p) == u^2 == ... (mod divisor)
# The i=0 case (p=2^0=1) is calculated at the initialization step

# base^p = (base^(p/2))^2 == optimal_congruent_of(base^(p/2))^2 (mod divisor)

# Calculate the optimal congruent

# Find which congruences are needed for final result calculation 

### Find the final result doing the product of the congruents (smartly)

# Same scheme as above for smart congruence computation
```
