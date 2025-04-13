import math

# --- Basic Math Functions ---
print("📌 Basic Math Functions:")
print("math.ceil(4.3):", math.ceil(4.3))          # 5
print("math.floor(4.9):", math.floor(4.9))        # 4
print("math.trunc(4.9):", math.trunc(4.9))        # 4
print("math.fabs(-4.3):", math.fabs(-4.3))        # 4.3
print("math.factorial(5):", math.factorial(5))    # 120
print("math.sqrt(25):", math.sqrt(25))            # 5.0
print("math.pow(2, 3):", math.pow(2, 3))          # 8.0

# --- Logarithmic & Exponential ---
print("\n📌 Logarithmic & Exponential:")
print("math.exp(2):", math.exp(2))                # e^2
print("math.log(10):", math.log(10))              # ln(10)
print("math.log10(1000):", math.log10(1000))      # 3

# --- Trigonometry ---
print("\n📌 Trigonometry:")
print("math.sin(math.pi/2) = ", math.sin(math.pi/2))  # outputs: 1.0
print("math.cos(0) = ", math.cos(0))  # outputs: 1.0
print("math.tan(math.pi/4) = ", math.tan(math.pi/4)) 
print("math.degrees(math.pi):", math.degrees(math.pi))             # 180.0
print("math.radians(180):", math.radians(180))                     # 3.1415...

# --- Constants ---
print("\n📌 Constants:")
print("math.pi:", math.pi)
print("math.e:", math.e)
print("math.tau:", math.tau)
print("math.inf:", math.inf)
print("math.nan:", math.nan)

# --- Other Utilities ---
print("\n📌 Other Utilities:")
print("math.gcd(12, 18):", math.gcd(12, 18))          # 6
print("math.lcm(4, 6):", math.lcm(4, 6))              # 12
print("math.isfinite(5):", math.isfinite(5))          # True
print("math.isinf(math.inf):", math.isinf(math.inf))  # True
print("math.isnan(math.nan):", math.isnan(math.nan))  # True