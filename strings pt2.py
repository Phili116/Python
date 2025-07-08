#Advanced concepts - strings

message = 'Hello , World!'

print(message[0])
print(message[1])

print(message[-1])
print(len(message))

print(message.strip()) # Remove leading and trailing whitspace
print(message.lower()) # Covert to lowercase
print(message.split(',')) #Split the string into a list based on the comma
print(message.upper())# Convert to uppercase
print(message.replace('World', 'Python')) #Replace 'World' with Python