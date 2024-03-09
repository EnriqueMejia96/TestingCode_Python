def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def normalize_numbers(numbers):
    avg = calculate_average(numbers)
    return [(num - avg) / avg for num in numbers]