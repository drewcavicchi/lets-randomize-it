import csv
import random
import uuid
from datetime import datetime, date
from faker import Faker

fake = Faker()

even_odd_counter = 1

headers = ['Client #', 'Case #', 'Service Type', 'Date Case Created', 'Resolution Date', 'Birthdate', 'Race',
           'Ethnicity', 'HH Num People', 'HH Annual Income', 'Veteran', 'Disabled', 'Gender', 'Education Level',
           '% AMI', 'age', 'Service Type', 'Resolution', 'Property Street Address', 'Property City', 'Property State',
           'Property Zip Code', 'Price Purchase', 'Closing Date', '1st Time Home Buyer', 'course', 'Client Zip',
           'Head of household']


def main():
    global even_odd_counter
    file = "C:/Users/Andrew.Cavicchi/Documents/Randomize Me.csv"

    with open(file) as infile:
        data = csv.DictReader(infile)
        with open("C:/Users/Andrew.Cavicchi/Documents/Output_File.csv", 'w', newline='') as outfile:
            fieldnames = headers
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            for line in data:
                # removes a bunch of data that only includes a client/case number
                if line['Date Case Created'] == '':
                    continue
                line['Service Type'] = remove_blanks(line['Service Type'])
                line['Resolution Date'] = remove_blanks(line['Resolution Date'])
                line['Birthdate'] = remove_blanks(line['Birthdate'])
                line['Race'] = remove_blanks(line['Race'])
                line['Ethnicity'] = remove_blanks(line['Ethnicity'])
                line['HH Num People'] = remove_blanks(line['HH Num People'])
                line['HH Annual Income'] = remove_blanks(line['HH Annual Income'])
                line['Veteran'] = remove_blanks(line['Veteran'])
                line['Disabled'] = remove_blanks(line['Disabled'])
                line['Gender'] = remove_blanks(line['Gender'])
                line['Education Level'] = remove_blanks(line['Education Level'])
                line['% AMI'] = remove_blanks(line['% AMI'])
                line['age'] = remove_blanks(line['age'])
                line['Service Type'] = remove_blanks(line['Service Type'])
                line['Resolution'] = remove_blanks(line['Resolution'])
                line['Property Street Address'] = remove_blanks(line['Property Street Address'])
                line['Property City'] = remove_blanks(line['Property City'])
                line['Property State'] = remove_blanks(line['Property State'])
                line['Property Zip Code'] = remove_blanks(line['Property Zip Code'])
                line['Price Purchase'] = remove_blanks(line['Price Purchase'])
                line['Closing Date'] = remove_blanks(line['Closing Date'])
                line['1st Time Home Buyer'] = remove_blanks(line['1st Time Home Buyer'])
                line['course'] = remove_blanks(line['course'])
                line['Client Zip'] = remove_blanks(line['Client Zip'])
                line['Head of household'] = remove_blanks(line['Head of household'])
                # Numbers that are noisified
                line['Client #'] = uuid.uuid4()
                line['Date Case Created'] = date_case_created_conversion(line['Date Case Created'])
                line['Resolution Date'] = resolution_date(line['Resolution Date'], line['Date Case Created'])
                line['age'] = noisy_number(line['age'], 0, 10)
                line['HH Annual Income'] = noisy_number(line['HH Annual Income'], 0, 5000)
                line['Price Purchase'] = noisy_number(line['Price Purchase'], 0, 50000)
                line['% AMI'] = noisy_number(line['% AMI'], 0, 20)
                even_odd_counter = random.randint(1, 2)
                writer.writerow(line)


# general formula to make fake date between two dates
def fake_date(start, end):
    fake_news = fake.date_between_dates(date_start=start, date_end=end)
    return fake_news


# adds a user defined amount of noise to the item
def noisy_number(item, lowerbound, upperbound):
    if item == '':
        item = ''
    elif item == '0':
        item = ''
    elif item == '#N/A':
        item = ''
    else:
        if even_odd_counter % 2 == 1:
            item = int(item) + random.randint(lowerbound, upperbound)
        else:
            item = abs(int(item) - random.randint(lowerbound, upperbound))
    return item


# Converts resolution date to a random date within a year of Date Case Created
def resolution_date(item, start_date):
    if item == '':
        item = ''
    else:
        end = date(start_date.year + 1, 12, start_date.day)
        item = fake_date(start_date, end)
    return item


# Coverts Date Case Created to a date within +- 1 yr of actual date
def date_case_created_conversion(item):
    if item == '':
        item = ''
    else:
        converted_date = convert_to_date(item)
        end = date(converted_date.year + 1, 12, converted_date.day)
        start = date(converted_date.year - 1, 12, converted_date.day)
        item = fake_date(start, end)
    return item


# Converts CSV date to datetime object
def convert_to_date(csv_date):
    dt = datetime.strptime(csv_date, '%m/%d/%Y')
    return dt


def remove_blanks(item):
    if item == '#N/A':
        item = ''
    elif item == '0':
        item = ''
    elif item == '':
        item = ''
    else:
        item = item
    return item


if __name__ == '__main__':
    main()
