def accounting_discrepancies(customer_orders_file):

    customer_orders = open(customer_orders_file)
    melon_cost = 1.00

    for line in customer_orders:
      #splits the line by "|" delimiter
      line = line.split('|')

      #assigns customer #, name, order, and payment to appropriate variables
      customer_number = line[0]
      customer_name = line[1]
      melon_order = float(line[2])
      customer_payment = float(line[3])

      #assigns expected payment to a variable for re-use
      expected_payment = melon_cost * melon_order
      
      #prints a statment w/all relevant info if a customer underpayed
      if expected_payment > customer_payment:
        print(f"Customer number {customer_number} underpaid: {customer_name} paid ${customer_payment:.2f},",
              f"Expected ${expected_payment:.2f}", 
              f"Underpayment of ${expected_payment - customer_payment:.2f}"
              )

      #prints a statment w/all relevant info if a customer overpayed
      elif expected_payment < customer_payment:
        print(f"Customer number {customer_number} overpaid: {customer_name} paid ${customer_payment:.2f},",
              f"Expected ${expected_payment:.2f}", 
              f"Overpayment of ${customer_payment - expected_payment:.2f}"
              )

#runs the function passing in the relevant file
accounting_discrepancies("customer-orders.txt")