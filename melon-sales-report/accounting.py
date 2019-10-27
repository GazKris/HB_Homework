SALESPERSON_INDEX = 0
INTERNET_INDEX = 1

#Sets melon prices
melon_prices = {"Musk": 1.15, "Hybrid": 1.30, 
    "Watermelon": 1.75, "Winter": 4.00 }

#Prints pretty line of stars
print("*" * 80)


def get_melon_sales(melon_type_orders):
    """ Takes in a sales order and provides data on # of each melon sold,
        price of melon, and total sales revenue for each melon."""
    
    #Opens file
    melon_order = open(melon_type_orders)
    #Sets empty dictionary
    melon_type_data = {}

    #sets up count dictionary per melon
    for line in melon_order:
        order_num, melon_type, melon_count  = line.split("|")
        melon_count = int(melon_count)
        if melon_type in melon_type_data:
            melon_type_data[melon_type]["Count"] += melon_count
        else:
            melon_type_data[melon_type] = {"Count": melon_count}

    #adds Price and Sales_Total dictionary per melon
    for melon_type in melon_prices:
        melon_type_data[melon_type]["Price"] = melon_prices[melon_type]
        melon_type_data[melon_type]["Sales_Total"] = \
            melon_type_data[melon_type]["Price"] * \
            melon_type_data[melon_type]["Count"]
    
    #Prints the sales report per melon   
    for melon_type in melon_type_data:
        print("We sold {} {} melons at ${:.2f} each for a total of ${:.2f}"\
            .format(melon_type_data[melon_type]["Count"],\
            melon_type, melon_type_data[melon_type]["Price"],\
            melon_type_data[melon_type]["Sales_Total"]))
    
    melon_order.close()
get_melon_sales("orders-by-type.txt")


print("*" * 80)

def sales_type_summary(sales_file):
    sales_info = open(sales_file)
    
    sales_person_revenue = 0
    online_revenue = 0

    #Unpacks sales info doc
    for line in sales_info:
        sale_num, id_num, name, revenue = line.split("|")
        id_num = int(id_num)

        #adds revenue to appropriate sales type
        if id_num > 0:
            sales_person_revenue += float(revenue)
        else:
            online_revenue += float(revenue)

    #Prints sales type summary        
    print("Salespeople generated ${:.2f} in revenue.".format(sales_person_revenue))
    print("Internet sales generated ${:.2f} in revenue.".format(online_revenue))

    #evaluates efficacy of sales people 
    if sales_person_revenue > online_revenue:
        print("Guess there's some value to those salespeople after all.")
    else:
        print("Time to fire the sales team! Online sales rule all!")

sales_type_summary("orders-with-sales.txt")
print("*" * 80)

# sales = [0, 0]
# for line in f:
#     d = line.split("|")
#     if d[1] == "0":
#         sales[0] += float(d[3])
#     else:
#         sales[1] += float(d[3])
# print("Salespeople generated ${:.2f} in revenue.".format(sales[1]))
# print("Internet sales generated ${:.2f} in revenue.".format(sales[0]))
# if sales[1] > sales[0]:
#     print("Guess there's some value to those salespeople after all.")
# else:
#     print("Time to fire the sales team! Online sales rule all!")
# print("******************************************")
