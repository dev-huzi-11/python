# List of items containing some duplicates
items = ["Apple", "Banana", "Mango", "Apple", "orange"]

# Create an empty set to store unique items
unique_item = set()

# Loop through each item in the list
for item in items:
    # Check if the item is already in the set (i.e., a duplicate)
    if item in unique_item:
        print(f"Duplicate: {item}")  # Print the duplicate item
        break  # Exit the loop after finding the first duplicate
    # Add the item to the set if it's not already present
    unique_item.add(item)
