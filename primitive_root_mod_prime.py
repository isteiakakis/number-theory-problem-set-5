# Usage:
# python3 primitive_root_mod_prime <prime_number:int>

### Find a primitive root mod the given prime number (it works only for prime numbers)

# Notation:
# = is for equality
# == is for congruence

import sys
from primitive_root_mod_prime_ import primitive_root_mod_prime

if len(sys.argv) != 2:
	print("Usage: python3 primitive_root_mod_prime <prime_number:int>")
	exit()

primitive_root_mod_prime(int(sys.argv[1]))

