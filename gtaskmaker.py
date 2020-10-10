import csv 
import string

#first read the csv file 
#take a note of how many rows 
#save info into variables 
#open new csv file
#fill out rows 
#keep doing that as many times as you want

file_name = input("Name of csv file to convert? (Ex. format.csv): ")
new_file_name = input("Name of new file (Ex. format.csv): ")


with open(file_name, "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    
    with open(new_file_name, "w") as csv_file_new:
        csv_new_writer = csv.writer(csv_file_new, lineterminator = "\n")
        csv_new_writer.writerow(['STORE', 'MODE', 'PRODUCT', 'SIZE', 'TIMER', 'FIRST NAME', 'LAST NAME', 'EMAIL', 'PHONE NUMBER', 'ADDRESS LINE 1', 'ADDRESS LINE 2', 'CITY', 'STATE', 'POSTCODE / ZIP', 'COUNTRY', 'CARD NUMBER', 'EXPIRE MONTH', 'EXPIRE YEAR', 'CARD CVC', 'LIMIT'])

        #store selector
        print('1. FOOTLOCKER \n2. FOOTACTION \n3. EASTBAY \n4. CHAMPSSPORTS \n5. KIDS FTL \n6. FINISHLINE \n7. JDUSA')
        store_input = input("Store type (use the numbers): ")
        if store_input == "1":
            store = "FOOTLOCKER"
        elif store_input == "2":
            store = "FOOTACTION"
        elif store_input == "3":
            store = "EASTBAY"
        elif store_input == "4":
            store = "CHAMPSSPORTS"
        elif store_input == "5":
            store = "KIDS FTL"
        elif store_input == "6":
            store = "FINISHLINE"
        elif store_input == "7":
            store = "JDUSA"
        else:
            store = ""
        
        if store_input == "1" or store_input == "2" or store_input == "3" or store_input == "4" or store_input == "5":
            print('1. PAYPAL(If paypal fails, attempt Ayden checkout) \n2. PAYPAL ONLY \n3. None(Ayden checkout)')
            mode_input = input("Mode type (use the numbers): ")

            if mode_input == "1":
                mode = "PAYPAL"
            elif mode_input == "2":
                mode = "PAYPAL ONLY"
            elif mode_input == "3":
                mode = ""
            else:
                mode = "PAYPAL"

        elif store_input == "6" or store_input == "7":
            print('1. DESKTOP \n2. MOBILE')
            mode_input = input("Mode type (use the numbers): ")

            if mode_input == "1":
                mode = "DESKTOP"
            elif mode_input == "2":
                mode = "MOBILE"
            else:
                mode = ""
                
        else:
            mode = ""
        
        sku = str(input("Enter Footsites PID or Finishline/JDUSA prod,color,id: "))

        print("1. RANDOM (will choose any size) \n2. Size range (ex. 7-10) \n3. Select sizes (7+8+10 -> Bot will first choose size 7, if OOS it will choose size 8, if OOS it will choose size 10) \n4. Select size/range (4.5-8+10-12 -> Bot will choose random size from 4.5 to 8 and from 10 to 12.)")
        size_input = input("Size input (select 1,2,3 or 4): ")

        if size_input == "1":
            size = "RANDOM"
        elif size_input == "2":
            size = str(input("Enter a size range (ex. 7-10): "))
        elif size_input == "3":
            size = str(input("Enter your select sizes (use the '+' to separate each size ex. 4+5+6): "))
        elif size_input == "4":
            size = str(input("Enter select size ranges (ex. 7-10+12-14): "))
        else:
            size = "RANDOM"

        task_amount = int(input("How many times you want to duplicate your profiles into tasks? \n(note the limit per csv is 800 so if you have 500 profiles saying a task amount of two ganesh aint gonna run): "))
        i = 1

        
        
        for row in csv_reader:
            if(len(row) < 1):
                continue #checks for blank rows
                
            email_sole = row[0]
            profile_name_sole = row[1]
            only_one_checkout_sole = row[2]
            name_on_card_sole = row[3]
            card_type_sole = row[4]
            card_number_sole = row[5]
            expiration_month_sole = row[6]
            expiration_year_sole = row[7]
            cvv_sole = row[8]
            same_billing_as_shipping_sole = row[9]
            billing_name_sole = row[19]
            billing_phone_sole = row[20]
            billing_address_sole = row[21]
            billing_address_two_sole = row[22]
            billing_address_three_sole = row[23]
            billing_zipcode_sole = row[24]
            billing_city_sole = row[25]
            billing_state_sole = row[26]
            billing_country_sole = row[27]

            splitted_billing_sole = billing_name_sole.split(" ")
            first_name_sole = splitted_billing_sole[0]
            last_name_sole = splitted_billing_sole[1]

            for amount_of_time in range(1, task_amount + 1): 
                csv_new_writer.writerow([store, mode, sku, size, '', first_name_sole, last_name_sole, email_sole, billing_phone_sole, billing_address_sole, billing_address_two_sole, billing_city_sole, billing_state_sole, billing_zipcode_sole, billing_country_sole, card_number_sole, expiration_month_sole, expiration_year_sole, cvv_sole, '1'])

csv_file.close()
csv_file_new.close()




