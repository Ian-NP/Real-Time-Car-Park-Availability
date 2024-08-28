# Lim WeiQin Ian (S10258057) – IT04

# Split function for splitting the carpark availability later in option 3
def split_function(string, split, ignore):
    string += split
    split_list = []
    character = ''
    ignore_status = False
    for i in string:
        if i == ignore:
            if ignore_status == True:
                ignore_status = False
            else:
                ignore_status = True
        elif i == split and ignore_status == False:
            split_list.append(character)
            character = ''
        else:
            character += i
    return split_list



def readcarpark_info():
    #Reading the carpark-information csv file
    data = open("carpark-information.csv", 'r')
    read = data.readlines()
    temp_list = []
    carpark_info = []

    #Storing data in a list, each element in the list is a dictionary of the information of each carpark
    for lines in range(len(read)):
        dictionary = {}
        # Split thrice to avoid the additional commas in some addresses
        # Appending each splitted line in into a temporary list
        temp_list.append(split_function(read[lines].strip('\n'), ',', "\""))

        # If condition to skip the header
        if lines != 0:
            # Changing the split version of each line into dictionaries with its keys as its header (Eg. Carpark Number : AC29)
            for each in range(len(temp_list[0])):
                # Used strip('""') due to only limiting the split thrice, hence, I need to maek sure that each element does that have quotation marks in them
                dictionary[temp_list[0][each]] = temp_list[lines][each]
            carpark_info.append(dictionary)
    
    return carpark_info


#Main Menu of the entire program
def main_menu(carpark_info, carpark_availability, timestamp):
    print("MENU\n====")
    print("[1] Display Total Number of Carparks in 'carpark-information.csv")
    print("[2] Display All Basement Carparks in 'carpark-information.csv")
    print("[3] Read Carpark Availability Data File")
    print("[4] Turn on Real Time Carpark Availability")
    print("[5] Print Total Number of Carparks")
    print("[6] Display carparks Without Available Lots")
    print("[7] Display Carparks With At Least x% Available Lots")
    print("[8] Display Addresses of Carparks With At Least x% Available Lots")
    print("[9] Display All Carparks at Given Location")
    print("[10] Display Carpark with the Most Parking Lots")
    print("[11] Create an Output File with Carpark Availability with Addresses and Sort by Lots Available")
    print("[0] Exit")
    
    # Getting the option chosen from the user
    invalid_option = True
    while invalid_option:
        try:
            option = int(input("Enter your option: "))
            if carpark_availability == 0:
                if 5 <= option <= 11:
                    print("Invalid option. Please input filename in option 3 or turn on real time data (Option 4) to proceed.")
                else:
                    invalid_option = False
            elif 0 <= option <= 11:
                invalid_option = False
            else:
                raise 
        except ValueError:
            print("Invalid option. Please enter an integer.")
        except:
            print("Invalid option. Please choose options from 0 to 10.")
            

    # Choosing the corresponding functions to the option the user chosen
    if option == 1:
        option_1(carpark_info)
    elif option == 2:
        option_2(carpark_info)
    elif option == 3:
        carpark_availability, timestamp = option_3()
    elif option == 4:
        carpark_availability, timestamp = realtime_availability()
    elif option == 5:
        option_5(carpark_availability)
    elif option == 6:
        option_6(carpark_availability)
    elif option == 7:
        option_7(carpark_availability)
    elif option == 8:
        option_8(carpark_info, carpark_availability)
    elif option == 9:
        option_9(carpark_info, carpark_availability)
    elif option == 10:
        option_10(carpark_info, carpark_availability)
    elif option == 11:
        option_11(carpark_info, carpark_availability, timestamp)
    elif option == 0:
        return 

    
    main_menu(carpark_info, carpark_availability, timestamp)


#Display the total number of carparks in carpark-information csv file
def option_1(carpark_info):
    print("\nOption 1: Display Total Number of Carparks in 'carpark-information.csv'")

    # Using len() method to find out the total number of elements(carpark) in carpark-information.csv file
    print("Total Number of carparks in 'carpark-information.csv': {}".format(len(carpark_info)))
    print()

#Display all the basement carparks in carpark-informatoin csv file
def option_2(carpark_info):
    print("\nOption 2: Display All Basement Carparks in 'carpark-information.csv")

    # defining variable to count the number of basement carparks later on in the following for loop
    count = 0
    
    # printing the header of the table
    print("{:<12}{:<19}{:<}".format('Carpark No', 'Carpark Type', 'Address'))

    for row in range(len(carpark_info)):
        #Finding out if the carpark type of the carpark is basement
        if "BASEMENT" in carpark_info[row]["Carpark Type"]:

            # Counting the number of basement carparks
            count += 1

            # Printing out the carpark number, carpark type and address
            print("{:<12}{:<19}{}"\
                  .format(carpark_info[row]["Carpark Number"], carpark_info[row]["Carpark Type"], carpark_info[row]["Address"]))
    
    # Printing total number of basement car parks from the count variable
    print("Total number: {}".format(count))
    print()


# Read carpark-availability data file
def option_3():
    # Opening file that user wants to open
    print()
    invalid_file = True
    while invalid_file:
        try:
            print("Option 3: Read Carpark Availability Data File")
            filename = str(input("Enter the file name: "))
            data = open(filename, 'r')
            invalid_file = False
        except:
            print("\nInvalid File, please try again.")
    # Reading the file into 'read' variable for later use
    read = data.readlines()
    temp_list = []
    carpark_availability = []

    # This for loop means: for the total number of lines in the file, it will loop that number of times starting from 0 to len(read)-1
    for lines in range(len(read)):
        dictionary = {}
        # Appending the split version of each line to a temporary list
        temp_list.append(read[lines].strip('\n').split(','))

        # Printing the timestamp and having a timestamp variable for option 10 later on
        if lines == 0:
            timestamp = read[lines].strip('\n')
            print(timestamp)

        # Changing the split version of each line into dictionaries with its keys as its header (Eg. Carpark Number : AC29)
        # Skipped line 0 and line 1 as they are the timetamp and headers and not the information we want
        elif lines != 1:
            # This for loops is to count the number of headers there are in the file
            for each in range(len(temp_list[1])):
                # temp_list[1] is the list containing all the headers
                # using the for loop, we can call each header that corresponds to the header of the information
                # Eg. 
                # temp_list[1][each] = Carpark Number
                # temp_list[lines][each] = AC29
                dictionary[temp_list[1][each]] = temp_list[lines][each]
            
            # After having complete the transformation from storing each data in list
            # to storing each data in a dictionary, of the information of each carpark.
            # Append the dictionary to a new final list where it will contain the dictionaries of each carpark
            carpark_availability.append(dictionary)
    
    print()
    return carpark_availability, timestamp


def realtime_availability():
    # Getting data from the data.gov.sg
    print()
    print("Option 4: Turn on Real Time Carpark Availability")
    import requests
    data = requests.get("https://api.data.gov.sg/v1/transport/carpark-availability").json()
    timestamp = data['items'][0]['timestamp']
    read = data['items'][0]['carpark_data']
    print(timestamp)
    carpark_availability = []

    for each in read:
        dictionary = {}
        dictionary["Carpark Number"] = each['carpark_number']
        dictionary["Total Lots"] = each['carpark_info'][0]['total_lots']
        dictionary["Lots Available"] = each['carpark_info'][0]['lots_available']
        carpark_availability.append(dictionary)
    
    print()
    return carpark_availability, timestamp


# Printing the total number of Carparks in the Carparks in the File Read in option 3
def option_5(carpark_availability):
    print("\nOption 5: Print Total Number of Carparks")

    # Using len() method, the number of carparks in the file raed in option 3 can be found
    print("Total Number of Carparks: {}".format(len(carpark_availability)))
    print()


# Displaying the number of caparks without available lots
def option_6(carpark_availability):
    print("\nOption 6: Display Carparks without Available Lots")

    #To count the total number of carparks without available lots
    count = 0

    for each in carpark_availability:
        # If the lots available 0, it will carry out the following statement
        if each['Lots Available'] == '0':
            # printing the carpark number that has no available lots
            print("Carpark Number: {}".format(each['Carpark Number']))

            # Counting carparks with no available lots
            count += 1
    # Printing the total number of counted carparks without available lots
    print("Total number: {}".format(count))
    print()


# Display carparks with at least x% Available Lots
def option_7(carpark_availability):
    # Getting user input for how much percentage required
    invalid_input = True
    while invalid_input:
        try:
            print("\nOption 7: Display Carparks With At Least x% Available Lots")
            percentage_required = float(input("Enter the percentage required: "))
            if 0 <= percentage_required <= 100:
                invalid_input = False
            else:
                raise
        except ValueError:
            print("Invalid Input. Please enter a number.")
        except:
            print("Invalid Input. Please enter number between 0 to 100.")

    # To count the number of carparks with at least x% available lots
    count = 0

    # Printing header of the table
    print("{:12}{:>10}{:>16}{:>12}".format("Carpark No", "Total Lots", "Lots Available", "Percentage"))

    for row in carpark_availability:
        # Finding percentage of available lots for each carpark lot, some carparks have zero total lots, so if a zero division error were to ever occur, it will count the percentage as 0.0
        try:
            percentage = float(row['Lots Available']) / float(row["Total Lots"]) * 100
        except:
            percentage = 0.0
        
        # An if condition to see if the percentage of available lots meets the user requirements
        if percentage >= percentage_required:
            # Counting the number of carparks that meet the requirement
            count += 1

            #printing the carpark number, total lots, lots available and the percentage
            print("{:12}{:>10}{:>16}{:>12.1f}".format(row["Carpark Number"], row["Total Lots"], row['Lots Available'], percentage))
    
    #printing the total number of carparks that meet the requirement
    print("Total Number: {}".format(count))
    print()
    
    
    return carpark_availability


# Display addresses of Carparks With At Least x% Available Lots
def option_8(carparkinfo, carpark_availability):
    # Getting user input for how much percentage required
    invalid_input = True
    while invalid_input:
        try:
            print("\nDisplay Addresses of Carparks With At Least x% Available Lots")
            percentage_required = float(input("Enter the percentage required: "))
            if 0 <= percentage_required <= 100:
                invalid_input = False
            else:
                raise
        except ValueError:
            print("Invalid Input. Please enter a number.")
        except:
            print("Invalid Input. Please enter number between 0 to 100.")

    # To count the number of carparks with at least x% available lots
    count = 0

    # Printing header of the table
    print("{:12}{:>10}{:>16}{:>12}  {:<}".format("Carpark No", "Total Lots", "Lots Available", "Percentage", "Address"))

    for row in carpark_availability:
        # Finding percentage of available lots for each carpark lot. 
        # Some carparks have zero total lots, so if a zero division error were to ever occur, it will count the percentage as 0.0
        try:
            percentage = float(row['Lots Available']) / float(row["Total Lots"]) * 100
        except:
            percentage = 0.0

        # An if condition to see if the percentage of available lots meets the user requirements
        if percentage >= percentage_required:
            # Counting the number of carparks that meet the requirement
            count += 1

            # Searching for the address of the carpark number that meet the requirement from carpark_info and printing out the content
            for each in carparkinfo:
                if row["Carpark Number"] == each["Carpark Number"]:
                    print("{:12}{:>10}{:>16}{:>12.1f}  {:<}".format(row["Carpark Number"], row["Total Lots"], row['Lots Available'], percentage, each["Address"]))
    
    print("Total Number: {}".format(count))
    print()


    return carpark_availability


def option_9(carpark_info, carpark_availability):
    print("\nOption 9: Display All Carparks at Given Location")

    count = 0
    location = str(input("Enter a location: ")).upper()
    # Checking if user input location can be found, if not it would return carpark not found
    for each in carpark_info:
        if location in each["Address"]:
            for row in carpark_availability:
                    count += 1
    if count == 0:
        print("No carpark found.\n")
        return
    

    print("{:12}{:<12}{:<16}{:<16}  {:<}".format("Carpark No", "Total Lots", "Lots Available", "Percentage", "Address"))
    for each in carpark_info:
        if location in each["Address"]:
            # carpark_no_status is to check if the car park number can be found in the carpark availability csv data file
            carpark_no_status = 0
            for row in carpark_availability:
                # Finding percentage of available lots for each carpark lot. 
                # Some carparks have zero total lots, so if a zero division error were to ever occur, it will count the percentage as 0.0
                try:
                    percentage = float(row['Lots Available']) / float(row["Total Lots"]) * 100
                except ZeroDivisionError:
                    percentage = 0.0

                # Searching for corresponding address to the carpark number and printing out the content
                if each["Carpark Number"] == row["Carpark Number"]:
                    print("{:12}{:<12}{:<16}{:<16.1f}  {:<}".format(row["Carpark Number"], row["Total Lots"], row['Lots Available'], percentage, each["Address"]))
                    # carpark_no_status plus so that it would not print 
                    # the following if condition below which should only activate when the carpark number is not found
                    # in carpark availability file
                    carpark_no_status += 1

            # if carpark_no_status not True then it will not print out that the carpark number has no data and information on its lots
            if not carpark_no_status:
                print("{:12}{:<12}{:<16}{:<16}  {:<}".format(each["Carpark Number"], "NA", "NA", "NA", each["Address"]))
                carpark_no_status = 0

    print()


def option_10(carpark_info, carpark_availability):
    print("\nOption 10: Display Carpark with the Most Parking Lots")

    #Bubble sort alogrithm to sort carpark_availability starting with the carpark with the most parking lots
    n = len(carpark_availability)
    for each in range(n):
        for index in range(n-each-1):
            if float(carpark_availability[index]['Total Lots']) < float(carpark_availability[index+1]['Total Lots']):
                carpark_availability[index+1], carpark_availability[index] = carpark_availability[index], carpark_availability[index+1]
    
    # Finding the percentage and output the carpark with most lots
    most_lots = carpark_availability[0]
    try:
        percentage = float(most_lots['Lots Available']) / float(most_lots["Total Lots"]) * 100
    except:
        percentage = 0.0
    for each in carpark_info:
        if each["Carpark Number"] == most_lots["Carpark Number"]:
            # Checking if the title is longer or shorter (in terms of character) than the actual carpark type
            char_type = len(each["Carpark Type"])
            if char_type < len("Carpark Type"):
              char_type = len("Carpark Type")

            # Checking if the title is longer or shorter (in terms of character) than the actual parking system
            char_system = len(each["Type of Parking System"])
            if char_system < len("Type of Parking System"):
                char_system = len("Type of Parking System")

            # Printing title and the information of the carpark with the most carpark lots
            print("{:12}{:<12}{:<16}{:<12}{}{}{}".format("Carpark No", "Total Lots", "Lots Available", "Percentage", "Carpark Type".ljust(char_type + 2, " "), "Type of Parking System".ljust(char_system + 2, " "), "Address"))
            print("{:12}{:<12}{:<16}{:<12.1f}{}{}{}".format(most_lots["Carpark Number"], most_lots["Total Lots"], most_lots["Lots Available"], percentage, each["Carpark Type"].ljust(char_type + 2, " "), each["Type of Parking System"].ljust(char_system + 2, " "), each["Address"]))
    
    print()


def option_11(carpark_info, carpark_availability,timestamp):
    print("\nOption 11: Create an Output File with Carpark Availability with Addresses and Sort by Lots Available")

    #Bubble sort alogrithm to sort carpark_availability in descending order
    n = len(carpark_availability)
    for each in range(n):
        for index in range(n-each-1):
            if float(carpark_availability[index]['Lots Available']) > float(carpark_availability[index+1]['Lots Available']):
                carpark_availability[index], carpark_availability[index+1] = carpark_availability[index+1], carpark_availability[index]
    
    # Creating new file: carpark-availability-with-addresses.csv containing all the information from option three but with the address of the carpark information added
    # Opening file
    newfile = open("carpark-availability-with-addresses.csv", "w")
    # Writing the timestamp into the file
    newfile.write(f"{timestamp}\n")
    # Writing the headers for each column
    newfile.write("Carpark Number,Total Lots,Lots Available,Address\n")
    # Writing the all the carpark information into the file
    for row in carpark_availability:
        carpark_found = 0
        for each in carpark_info:
            if each["Carpark Number"] == row["Carpark Number"]:
                newfile.write("{},{},{},{}\n".format(row["Carpark Number"], row["Total Lots"], row["Lots Available"], each["Address"]))
                carpark_found += 1
        if not carpark_found:
            newfile.write("{},{},{},{}\n".format(row["Carpark Number"], row["Total Lots"], row["Lots Available"], ""))
            carpark_found = 0

    print("Successfully created.\n")


carpark_info = readcarpark_info()
carpark_availability = 0
timestamp = 0
main_menu(carpark_info, carpark_availability, timestamp)