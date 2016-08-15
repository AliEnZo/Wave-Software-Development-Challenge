import csv
import sys
import MySQLdb
import datetime
from datetime import datetime
import algo_2
import json

path = 'uploads/data_example.csv'
employee_names = []
pre_tax_data = []
tax_data = []
date = []
category = []
employee_address = []
expense_description = []
tax_name = []
package = []

# Open CSV file
def open_File():
    try:
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:

                #Record Raw data from CSV in separate Buffers
                names_content = list(row['employee name'])
                data_pre_tax_content = list(row['pre-tax amount'])
                data_tax_content = list(row['tax amount'])
                data_month = list(row['date'])
                category_data = list(row['category'])
                employee_address_data = list(row['employee address'])
                expense_description_data = list(row['expense description'])
                tax_name_data = list(row['tax name'])

                #concatenate the raw data (characters)in order to make String
                employee_names.append(''.join(names_content))
                pre_tax_data.append(''.join(data_pre_tax_content))
                tax_data.append(''.join(data_tax_content))
                date.append(''.join(data_month))
                category.append(''.join(category_data))
                employee_address.append(''.join(employee_address_data))
                expense_description.append(''.join(expense_description_data))
                tax_name.append(''.join(tax_name_data))

    except Exception as e:
        sys.exit('Can Not Open CVS File...')


#connect to DB and store all CSV data
def connect_DB():
    try:
        db = MySQLdb.connect(
            host='localhost',
            user='root',
            passwd='',
            db='mydb')
    except Exception as e:
        sys.exit('Can Not Connect to DB......')

    #create an instance of a cursor From MySQLdb
    cursor = db.cursor()

    #loop through array to retrive data for each ROW
    for index in range(1, 19):
        e_name = employee_names[index]
        e_tax = tax_data[index]
        e_tax_name = tax_name[index]
        e_category = category[index]
        e_address = employee_address[index]
        e_date = date[index]
        e_expense_description = expense_description[index]
        e_pre_tax = pre_tax_data[index]

        # datetime.strptime(date[index], '%m/%d/%Y') our format, strftime('%Y/%m/%d') SQL format
        date_object = datetime.strptime(date[index], '%m/%d/%Y').strftime('%Y/%m/%d')

        # Since you use a tuple, change the placeholders to "%s": for tax Value
        insert_employee_name = "INSERT INTO tax_payment (employee, tax_amount,tax_name,category,employee_address,date,expense_description, pre_tax_amount) " \
                               "VALUES(%s, %s, %s,%s, %s, %s, %s, %s)"
        cursor.execute(insert_employee_name, [e_name, e_tax, e_tax_name,
                                              e_category, e_address, date_object,
                                              e_expense_description, e_pre_tax])
        # Save Changes
        db.commit()
        result = cursor.fetchall()
    db.close()

def ui():
    open_File()
    connect_DB()


def main():
    ui()
    #use this algorithm to find total expenses amount per-month
    algo_2.Total_Expenses_Amount_Per_Month()


if __name__ == '__main__':
    main()
