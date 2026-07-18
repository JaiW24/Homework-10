#  Chapter 10

p0 = float(input("Enter amount to borrow: "))
r = float(input("Enter annual interest rate (decimal): "))
k = int(input("Enter number of times interest is compounded per year: "))
n = int(input("Enter loan term in years: "))

filename = input("Enter output file name: ")

payment = p0 / ((1 - (1 + r / k) ** (-n * k)) / (r / k))

balance = p0
payments = n * k
rate = r / k


# Open file for writing
outfile = open(filename, "w")


header = f"{'Payment':<10}{'Payment Amt':<15}{'Interest':<15}{'Principal':<15}{'Balance':<15}"

print()
print(header)
print("-" * 70)

outfile.write(header + "\n")
outfile.write("-" * 70 + "\n")


for i in range(1, payments + 1):

    interest = balance * rate
    principal = payment - interest
    balance = balance - principal

    if balance < 0:
        balance = 0

    line = f"{i:<10}${payment:<14.2f}${interest:<14.2f}${principal:<14.2f}${balance:<14.2f}"

    print(line)
    outfile.write(line + "\n")


outfile.close()

print()
print("Amortization report saved to", filename)