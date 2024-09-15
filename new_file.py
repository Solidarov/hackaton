# Dummy data for testing purposes

# Sample list of dictionaries
data = [
    {"id": 1, "name": "Alice", "age": 30, "city": "New York"},
    {"id": 2, "name": "Bob", "age": 25, "city": "Los Angeles"},
    {"id": 3, "name": "Charlie", "age": 35, "city": "Chicago"},
    {"id": 4, "name": "David", "age": 40, "city": "Houston"},
    {"id": 5, "name": "Eve", "age": 22, "city": "Phoenix"}
]

# Sample function to print data
def print_data(data):
    for item in data:
        print(f"ID: {item['id']}, Name: {item['name']}, Age: {item['age']}, City: {item['city']}")

# Call the function to print the dummy data multiple times
if __name__ == "__main__":
    for _ in range(3):  # Change the range value to print the data more or fewer times
        print_data(data)
        print("-" * 20)  # Separator between each iteration