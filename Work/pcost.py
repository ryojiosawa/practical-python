# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    total_cost = 0
    try:
        with open(filename, "rt") as f:
            rows = csv.reader(f)
            headers = next(rows)
            for rowno, row in enumerate(rows, start=1):
                record = dict(zip(headers, row))
                try:
                    total_cost = total_cost + int(record['share']) * float(record['price'])
                except ValueError:
                    print(f'Row {rowno}: Bad data: {row}')

        return total_cost
    except ValueError:
        print(f"No such file: {filename}")

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"

cost = portfolio_cost(filename)
print(f"Total cost: {cost}")
