from string import digits 
import re
import csv
import time

s = 'abc123def456ghi789zero0'
remove_digits = str.maketrans('', '', digits)
res = s.translate(remove_digits)

try: 
    to_open = input("What text file you want to open? (format: accounts.txt)")
    f = open(to_open, "r")
except:
    print("This shit ain't even a txt file")
    print("Terminating in 5 seconds")
    time.sleep(5)
    quit()

with open('splittednike.csv', 'w') as csv_file: 
    reader = csv.reader(csv_file)
    writer = csv.writer(csv_file, lineterminator = '\n')
    writer.writerow(["First Name", "Last Name"])
    for line in f:
        splitted = line.split("@")
        username = splitted[0]
        remove = username.translate(remove_digits)
        split_first_last = re.findall('[a-zA-Z][^A-Z]*', remove)
        first_name = split_first_last[0]
        last_name = split_first_last[1]
        
        writer.writerow([first_name, last_name])
    




