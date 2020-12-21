# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
number_months_paid = 0

extra_payment_start_month = 0
extra_payment_end_month = 11
extra_payment = 1000

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    number_months_paid = number_months_paid + 1

    if number_months_paid >= extra_payment_start_month and number_months_paid <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print(number_months_paid, round(total_paid, 2), round(principal, 2))

print(f"Total paid {round(total_paid, 2)}")

print(f"Number of months paid {number_months_paid}")
