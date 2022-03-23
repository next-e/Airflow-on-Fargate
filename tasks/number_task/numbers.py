from argparse import ArgumentParser
import os

parser = ArgumentParser(description='Airflow Fargate Example')
parser.add_argument('number', help='number', type=int)

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"Successfully deleted file: {file_path}")
    except OSError:
        print(f"File not found: {file_path}")


if __name__ == '__main__':
    args = parser.parse_args()
    number = args.number
    print("Printing all numbers in given range")
    with open("/shared-volume/numbers.txt", "a") as f_numbers:
        with open("/shared-volume/even.txt", "r") as f_even:
            for line in f_even:
                f_numbers.write(line)
        with open("/shared-volume/odd.txt", "r") as f_odd:
            for line in f_odd:
                f_numbers.write(line)
    with open("/shared-volume/numbers.txt", "r") as f_numbers:
        for line in f_numbers:
            print(line)
            print("\n")
    # Deleting all files, to avoid EFS cost
    delete_file("/shared-volume/even.txt")
    delete_file("/shared-volume/odd.txt")
    delete_file("/shared-volume/numbers.txt")
    delete_file("/shared-volume/numbers.txt") # Will result in File not found message
