# Usage:
# python3 remainder.py <divisor:int> <base:int> <exponent:int>

### Compute r_d[b^e]

# Notation:
# = is for equality
# == is for congruence

import sys
from remainder_ import remainder

if len(sys.argv) != 4:
	print("Usage: python3 remainder.py <divisor:int> <base:int> <exponent:int>")
	exit()

remainder(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
