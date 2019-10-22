#creates the function to intake the sales info file
def summary(file):

    #opens the file passes in as an argument to the function and sets it to a variable
    the_file = open(file)

    #loops through each line in the file 
    for line in the_file:
        #strips the line of leading white space
        line = line.rstrip()
        #splits each line by the given character to create a list
        words = line.split('|')

        #sets each item in the list to an appropriately named variable
        melon = words[0]
        count = words[1]
        amount = words[2]

        #prints the summary report in the format desired
        print("Delivered {} {}s for total of ${}".format(
            count, melon, amount))
    #closes the file
    the_file.close()

#runs the summary report on Day 1, 2, and 3, respectively
print("Day 1")
summary("um-deliveries-20140519.txt")


print("Day 2")
summary("um-deliveries-20140520.txt")


print("Day 3")
summary("um-deliveries-20140521.txt")
