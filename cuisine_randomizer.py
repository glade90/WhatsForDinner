import csv
import os
import random

def load_cuisines(csv_file):
    cuisines = []
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cuisines.append(row)
    return cuisines

def pick_random_cuisine(cuisines):
    return random.choice(cuisines)

def main():
    # Assume CSV is in the same directory as this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_file = os.path.join(base_dir, "top_100_cuisines.csv")
    if not os.path.exists(csv_file):
        print(f"CSV file not found at {csv_file}")
        return

    cuisines = load_cuisines(csv_file)
    choice = pick_random_cuisine(cuisines)

    print("\n=== Dinner Inspiration ===")
    print(f"ID: {choice['id']}")
    print(f"Region: {choice['country_or_region']}")
    print(f"Cuisine: {choice['cuisine']}")
    print(f"Example dishes: {choice['example_dishes']}")
    print("==========================\n")

if __name__ == "__main__":
    main()
