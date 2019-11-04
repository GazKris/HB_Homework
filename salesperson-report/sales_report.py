"""Generate sales report showing total melons each salesperson sold."""

# Initialize empty lists
salespeople = []
melons_sold = []

# Opens the file: could use a better name
f = open('sales-report.txt')


for line in f:
    # Strips whitespace and splits entries on delimiter
    line = line.rstrip()
    entries = line.split('|')

    # Sets variables to respective entries
    salesperson = entries[0]
    melons = int(entries[2])

    # This would be better with a dictionary; Key: saleperson, Value: melon sales
    if salesperson in salespeople:
        # Gets the index of the person already in the list to ensure melon count
        # is added to the correct person
        position = salespeople.index(salesperson)

        # Adds melons sold to saleperson's total
        melons_sold[position] += melons

    # Appends to list if salesperson is not already in list
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)

# Prints the salereport in the format desired. Could use a better variable name.
for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
