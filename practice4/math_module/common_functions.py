import math

# Rounding
print(math.floor(4.7))    # 4 (round down)
print(math.ceil(4.2))     # 5 (round up)
print(math.trunc(4.9))    # 4 (remove decimal part)

# Power and logarithms
print(math.pow(2, 10))    # 1024.0
print(math.sqrt(144))     # 12.0
print(math.log(math.e))   # 1.0 (natural log)
print(math.log2(1024))    # 10.0
print(math.log10(1000))   # 3.0

# Absolute value
print(math.fabs(-42))     # 42.0

# Factorial and GCD
print(math.factorial(5))  # 120 (5! = 5*4*3*2*1)
print(math.gcd(24, 36))   # 12

# Trigonometry (arguments in radians)
print(math.sin(math.pi / 2))   # 1.0
print(math.cos(0))              # 1.0
print(math.tan(math.pi / 4))   # ~1.0

# Convert between degrees and radians
print(math.degrees(math.pi))    # 180.0
print(math.radians(180))        # 3.141592653589793