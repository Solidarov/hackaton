from datetime import datetime

def days_since_july_12_2004():
    start_date = datetime(2004, 7, 12)
    current_date = datetime.now()
    delta = current_date - start_date
    return delta.days

# Example usage
if __name__ == "__main__":
    print(f"Days since July 12, 2004: {days_since_july_12_2004()}")