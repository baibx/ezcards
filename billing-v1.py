import csv 
import names
import random
import string
import json

def phone_number():
    random_area_code = random.choice(area_code) + str(random.randint(1111111, 9999999))

    return random_area_code

def address_two_jig():        
    random_number_for_addy2 = random.randint(0,999)
    address_line_two = ['Unit', 'APT', 'Apartment']
    jigged2 = random.choice(address_line_two) + " #" + str(random_number_for_addy2)

    return jigged2

def card_type_function(card_type):
    if int(card_type) == 1: 
        type_of_card = "AmericanExpress"
    elif int(card_type) == 2: 
        type_of_card = "MasterCard"
    elif int(card_type) == 3: 
        type_of_card = "Discover"
    else: 
        type_of_card = "Visa"

    return type_of_card 


name_file = input("Name this file: ")  #start of the program, naming
csv_name = name_file + ".csv"

catchall = input("Catchall format(@catchall.com or basename@yahoo.com): ")
yahoo_catch = catchall.split('@')

main_address = input("Main address: ")
number_of_letters = int(input("0, 3 or 4 letters for the address jig (if you enter 0, there will be no jig for profiles such as fnl): "))
addy2 = input("Do you want to use an address line 2 jig? Ex. Unit #194 (y/n): ")

city = input("City: ")
state = input("State format(NY as New York): ")
zipcode = int(input("Zipcode: "))

i = 1 
number_of_profiles = input("How many profiles: ")
profile_base_name = input("Base name for profiles Ex. footsites, ys...: ")



if yahoo_catch[1] == 'yahoo.com':
    text_file = open("yahoo.txt", "w")
    yahoo_yes = True
        
else: 
    print('~~~~~~~~~~~~~~~~')

with open(csv_name, "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Email Address', 'Profile Name', 'Only One Checkout', 'Name on Card', 'Card Type', 'Card Number', 'Expiration Month', 'Expiration Year', 'CVV', 'Same Billing/Shipping', 'Shipping Name', 'Shipping Phone', 'Shipping Address', 'Shipping Address 2', 'Shipping Address 3', 'Shipping Post Code', 'Shipping City', 'Shipping State', 'Shipping Country', 'Billing Name', 'Billing Phone', 'Billing Address', 'Billing Address 2', 'Billing Address 3', 'Billing Post Code', 'Billing City', 'Billing State', 'Billing Country', 'otherEntriesList', 'Size (Optional)'])

    expiration_date_all = input("Is expiration date all the same? (y/n): ")
    if expiration_date_all == 'y':
        expiration_date_global = input("Expiration date - global (XX/XX): ")

    card_type_all = input("Are card types all the same? (y/n): ")
    if card_type_all == 'y':
        print('1. AmericanExpress \n2. MasterCard \n3. Discover \n4. Visa')
        card_type_global = input("Global Card type (use the numbers): ")

    while i <= int(number_of_profiles):
        print("You are on profile #" + str(i))
        profile_name = profile_base_name + str(i)

        
        if card_type_all == 'y':
            type_card = card_type_function(card_type_global)
        else: 
            print('1. AmericanExpress \n2. MasterCard \n3. Discover \n4. Visa')
            card_type_not_global = input("Card type (use the numbers): ")

            type_card = card_type_function(card_type_not_global)

        card_number = input("Card Number: ")
        if expiration_date_all == 'y': 
            expiration_date = expiration_date_global
        else:
            expiration_date = input("Expiration date(XX/XX): ")
        
        expiration_date_splitted = expiration_date.split('/')
        expiration_month = expiration_date_splitted[0]
        expiration_year = expiration_date_splitted[1]
        cvv = input("CVV: ")

        random_name = names.get_full_name()
        random_name_splitted = random_name.split(' ')

        if yahoo_yes == True:
            basename = yahoo_catch[0]
            together_catchall = basename + '-' + random_name_splitted[0] + random_name_splitted[1] + '@yahoo.com'
        else:
            together_catchall = random_name_splitted[0] + random_name_splitted[1] + catchall

        if city.lower() == "brooklyn":
            area_code = ['347', '917', '631', '718']
        elif city.lower() == "flushing":
            area_code = ['718', '347', '917', '929']
        elif city.lower() == "pottstown":
            area_code = ['610', '484']
        else: 
            area_code = ['347', '917', '631', '718']
            
        phone = phone_number()

        line_two = ' '
        letters = string.ascii_uppercase
        rand_letters = random.choices(letters,k=number_of_letters)

        if number_of_letters == 3:
            address_line_one = rand_letters[0] + rand_letters[1] + rand_letters[2] + " " + main_address

            if addy2 == 'y':
                line_two = address_two_jig()
        
        elif number_of_letters == 0: 
            address_line_one = main_address

            if addy2 == 'y':
                line_two = address_two_jig()

        else:
            address_line_one = rand_letters[0] + rand_letters[1] + rand_letters[2] + rand_letters[3]  + " " + main_address

            if addy2 == 'y':
                line_two = address_two_jig()

        try: 
            text_file.write(random_name_splitted[0] + random_name_splitted[1])
            text_file.write("\n")
            text_file.write(random_name)
            text_file.write("\n")
        except:
            print('~~~~~~~~~~~~~~~~~~')
        
        csv_writer.writerow([together_catchall, profile_name, 'FALSE', random_name, type_card, card_number, expiration_month, expiration_year, cvv, 'TRUE', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', random_name, phone, address_line_one, line_two, ' ', zipcode, city, state, 'United States', ' ', ' '])


        i += 1

csv_file.close()


##############
##############
##############

import_to_bot = input("Sole export? (y/n): ")

sole_list = []

n = 0
if import_to_bot == 'y':
    with open(csv_name, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

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

            sole_formatting = {
                "ID": "",
                "ProfileName": "",
                "Email": "",
                "Phone": "",
                "ShippingFirstName": "",
                "ShippingLastName": "",
                "ShippingAddress1": "",
                "ShippingAddress2": "",
                "ShippingCity": "",
                "ShippingZip": "",
                "ShippingCountry": "",
                "ShippingState": "",
                "UseBilling": False,
                "BillingFirstName": "",
                "BillingLastName": "",
                "BillingAddress1": "",
                "BillingAddress2": "",
                "BillingCity": "",
                "BillingZip": "",
                "BillingCountry": "",
                "BillingState": "",
                "CardNumber": "",
                "CardName": "",
                "CardCvv": "",
                "CardExpiryMonth": "",
                "CardExpiryYear": "",
                "CardType": "",
                "CheckoutLimit": ""
            }

            sole_formatting["ID"] = n + 1
            sole_formatting["ProfileName"] = profile_name_sole
            sole_formatting["Email"] = email_sole
            sole_formatting["Phone"] = billing_phone_sole
            sole_formatting["ShippingFirstName"] = first_name_sole
            sole_formatting["ShippingLastName"] = last_name_sole
            sole_formatting["ShippingAddress1"] = billing_address_sole
            sole_formatting["ShippingAddress2"] = billing_address_two_sole
            sole_formatting["ShippingCity"] = billing_city_sole
            sole_formatting["ShippingZip"] = billing_zipcode_sole
            sole_formatting["ShippingCountry"] = billing_country_sole
            sole_formatting["ShippingState"] = billing_state_sole
            sole_formatting["UseBilling"] = False
            sole_formatting["BillingFirstName"] = first_name_sole
            sole_formatting["BillingLastName"] = last_name_sole
            sole_formatting["BillingAddress1"] = billing_address_sole
            sole_formatting["BillingAddress2"] = billing_address_two_sole
            sole_formatting["BillingCity"] = billing_city_sole
            sole_formatting["BillingZip"] = billing_zipcode_sole
            sole_formatting["BillingCountry"] = billing_country_sole
            sole_formatting["BillingState"] = billing_state_sole
            sole_formatting["CardNumber"] = card_number_sole
            sole_formatting["CardName"] = name_on_card_sole
            sole_formatting["CardCvv"] = cvv_sole
            sole_formatting["CardExpiryMonth"] = expiration_month_sole
            sole_formatting["CardExpiryYear"] = expiration_year_sole
            sole_formatting["CardType"] = card_type_sole
            sole_formatting["CheckoutLimit"] = "No checkout limit"

            sole_list.append(sole_formatting)

            n += 1

    csv_file.close()

    file_name_sole_json = input("Name this sole export: ")
    jsonformatted_file_name = file_name_sole_json + ".json"

    with open(jsonformatted_file_name, 'w') as json_file:
        json.dump(sole_list, json_file)
    
    json_file.close()

try: 
    text_file.close()
except NameError: 
    print("Bye~")
