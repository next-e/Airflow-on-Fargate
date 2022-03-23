from argparse import ArgumentParser

parser = ArgumentParser(description='Airflow Fargate Example')
parser.add_argument('number', help='number', type=int)

if __name__ == '__main__':
    args = parser.parse_args()
    number = args.number

    print("Printing Odd numbers in given range")
    with open("/shared-volume/odd.txt", "a") as f:
        for i in range(int(number)):
            if(i % 2 != 0):
                f.write(str(i))
                print(i)
