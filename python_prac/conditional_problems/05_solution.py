# *************************************** WEATHER ACTIVITY SUGGESTION ***************************************

# Asking the user for the current weather and converting input to lowercase for consistency
weather = input("How is the weather? (Sunny/Rainy/Snowy): ").lower()

# Checking the weather condition and suggesting an activity
if weather == "sunny":  
    print("Go for a walk")  # Suggests going for a walk on a sunny day

elif weather == "rainy":  
    print("Read a book")  # Suggests reading a book on a rainy day

elif weather == "snowy":  
    print("Build a snowman")  # Suggests building a snowman on a snowy day

else:  
    # Handles unexpected weather conditions
    print(f"I don't have a suggestion for {weather} weather")  
