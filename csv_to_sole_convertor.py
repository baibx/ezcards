import csv 
import json

file_name = input("What is the file name?: (Ex. format.csv)")

sole_list = []
n = 0
with open(file_name, "r") as csv_file: 
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

