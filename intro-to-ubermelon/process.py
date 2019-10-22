log_file = open("um-server-01.txt") #Opens a log file from the server


def sales_reports(log_file):    #Defines a function called "sales_reports"
    for line in log_file:       #Starts a For loop for every line in log_file
        line = line.rstrip()    #Strips the line of... something? Maybe spaces?
        day = line[0:3]         #Sets the 1st 3 characters of the line to variable "day"
        if day == "Mon":        
            print(line)         #Prints out the line if the day is Tuesday (changed to Monday based on Homework instructions)


sales_reports(log_file)         #Runs the pre-defined function above
