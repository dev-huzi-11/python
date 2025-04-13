# Try block

try:
    result1 = 10 / 0
except:
    print("Error")

# Exception block
try:
    result2 = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as excep:
    print("Error occured: ", excep)

# Else block
try:
    result3 = 20 / 2
except ZeroDivisionError:
    print("Cannot devide by zero")
else:
    print(f"Result: {result3}")

# Finally block
try:
    result4 = 20 / 2
except ZeroDivisionError:
    print("Cannot devide by zero")
finally:
    print("Rate our program")

# Putting all together
def divide(num1, num2):
    try:
        result5 = num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except TypeError:
        print("Error: Invalid input")
    else:
        print(f"Result: {result5}")
    finally:
        print("Operation completed")

divide(20, 2)
divide(10, 0)
divide("Huzaifa", 2)

def divide_numbers(a, b):
    try:
        result = a / b  # Test this block for errors
        raise FloatingPointError("Testing FloatingPointError") #3. Uncomment to see execution flow

    except Exception as e:    # 1. Uncomment to see execution flow
        print(f"Exception: An unexpected error occurred: {e}")
    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero!")
    except TypeError:
        print("TypeError: Invalid input type. Numbers required.")
    except Exception as e:    # 2. Uncomment to see execution flow
        print(f"Exception: An unexpected error occurred: {e}")
    else:
        print(f"else: Division successful. Result: {result}")
    finally:
        print("finally: Operation complete.\n")

# Test cases
divide_numbers(10, 2)  # Successful division
divide_numbers(10, 0)  # ZeroDivisionError
divide_numbers(10, "2")  # TypeError