import csv


def read_csv(file_path):
    unique_professions = set()
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            unique_professions.add(row['Profession'])
    return unique_professions


def check_eligibility(profession, unique_professions):
    return profession.lower() in unique_professions


def main():
    file_path = 'bank-data.csv'
    unique_professions = read_csv(file_path)

    while True:
        user_input = input("Enter the profession (type 'END' to exit): ")

        if user_input.upper() == 'END':
            break

        eligible = check_eligibility(user_input, unique_professions)

        if eligible:
            print("Client is eligible for the marketing campaign.")
        else:
            print("Client is not eligible for the marketing campaign.")


if __name__ == "__main__":
    main()
