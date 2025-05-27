# Function to flatten a nested list
def flatten(nested_list):
    flat_list = []
    stack = nested_list[::-1]  # Reverse the list to process it from end to start

    while stack:
        item = stack.pop()  # Get the last item in the stack
        if isinstance(item, list):
            stack.extend(item[::-1])  # If item is a list, extend stack with its elements in reverse
        else:
            flat_list.append(item)  # Otherwise, add item to flat list

    return flat_list

# Example usage
nested_list = [1, [2, [3, 4], 5], 6]
flat_list = flatten(nested_list)
print(flat_list)
