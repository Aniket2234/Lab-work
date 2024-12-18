# Question 3: Customer ID and name dictionary

# Creating a dictionary to store customer IDs and their names
customer_info = {
    1001: "Alice",
    1002: "Bob",
    1003: "Charlie",
    1004: "Diana"
}

# Printing the entire dictionary
print("Customer Information:", customer_info)

# Accessing the name of a specific customer ID (e.g., 1002)
print("Customer with ID 1002:", customer_info[1002])

# Adding a new customer ID and name
customer_info[1005] = "Eve"
print("Updated Customer Information:", customer_info)

# Updating the name of an existing customer
customer_info[1001] = "Alex"
print("Updated Customer with ID 1001:", customer_info[1001])

# Deleting a customer from the dictionary
del customer_info[1003]
print("Customer Information after deletion:", customer_info)
