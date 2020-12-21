# report.py
#
# Exercise 2.4

import csv
from pprint import pprint

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows) # skip headers
		# filter out empty rows
        rows = [row for row in rows if row != []]
        for name, shares, price in rows:
            portfolio.append(
                {
                    'name': name,
                    'shares': int(shares),
                    'price': float(price)
				}
            )

    return portfolio

def read_prices(filename):
    '''Returns a dictionary of prices from the given file'''
    prices = {}
    with open(filename, 'rt') as f:
        # read the file and filter out empty rows
        rows = [row for row in csv.reader(f) if row != []]

        for name, price in rows:
            prices[name] = float(price)

    return prices

def make_report(portfolio, prices):
    reports = []
    for stock in portfolio:
        name = stock['name']
        shares = stock['shares']
        price = stock['price']
        change = prices[name] - price

        reports.append((name, shares, price, change))

    return reports

portfolio = read_portfolio("Data/portfolio.csv")
#pprint(portfolio)
prices = read_prices("Data/prices.csv")
#pprint(prices)

reports = make_report(portfolio, prices)

# print portfolio in a table format
headers = ('Name', 'Shares', 'Price', 'Change')
print('%10s %10s %10s %10s' % headers)
print(('-' * 10 + ' ') * len(headers))
for name, shares, price, change in reports:
    print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")
