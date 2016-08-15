import csv
import json

# Hold dates after join Convert them from list character to list string
dates = []

# Hold pre_taxes after join
pre_taxes = []

# Hold taxes after join
taxes = []
# Hold _pre_taxes after join
pre_taxes_newSet = []

# ---------- Hold Current Month taxes and pre taxes for calculation
selected_taxes = []
selected_pre_taxes = []

##---------- total expenses amount per-month
total_result = []
taxes_result = 0
pre_taxes_result = 0


def Total_Expenses_Amount_Per_Month():
    selected_taxes = []
    selected_pre_taxes = []
    with open('data_example.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            date = list(row['date'])
            dates.append(int(''.join(date).split('/')[0]))

            pre_tax = list(row['pre-tax amount'])
            pre_taxes.append(''.join(pre_tax))

            tax = list(row['tax amount'])
            taxes.append((''.join(tax)))

    # find Month Indexes
    dates_index_12 = list(i for i, x in enumerate(dates) if x == 12)
    dates_index_11 = list(i for i, x in enumerate(dates) if x == 11)
    dates_index_10 = list(i for i, x in enumerate(dates) if x == 10)
    dates_index_9 = list(i for i, x in enumerate(dates) if x == 9)
    dates_index_8 = list(i for i, x in enumerate(dates) if x == 8)
    dates_index_7 = list(i for i, x in enumerate(dates) if x == 7)
    dates_index_6 = list(i for i, x in enumerate(dates) if x == 6)
    dates_index_5 = list(i for i, x in enumerate(dates) if x == 5)
    dates_index_4 = list(i for i, x in enumerate(dates) if x == 4)
    dates_index_3 = list(i for i, x in enumerate(dates) if x == 3)
    dates_index_2 = list(i for i, x in enumerate(dates) if x == 2)
    dates_index_1 = list(i for i, x in enumerate(dates) if x == 1)

    # Store List of Month Indexes
    Months_list = [dates_index_12,
                   dates_index_11,
                   dates_index_10,
                   dates_index_9,
                   dates_index_8,
                   dates_index_7,
                   dates_index_6,
                   dates_index_5,
                   dates_index_4,
                   dates_index_3,
                   dates_index_2,
                   dates_index_1,
                   ]

    for dates_index in Months_list:
        # i is Month List (e.g i = dates_index_12, dates_index_11, etc. )
        for j in dates_index:
            selected_taxes.append(taxes[j])
            selected_pre_taxes.append(pre_taxes[j].replace(',', ''))

        #Taxes total amount in each month
        taxes_result = sum(map(float, selected_taxes))

        # Pre-Taxes total amount in each month
        pre_taxes_result = sum(map(float, selected_pre_taxes))

        # Sum taxes + pre_tax in order to find the total expenses amount
        sum_result = taxes_result + pre_taxes_result

        # Store each month total expenses amount in the list
        total_result.append(sum_result)

        # Reset buffers and variables for next month
        sum_result = 0
        taxes_result = 0
        pre_taxes_result = 0
        selected_taxes = []
        selected_pre_taxes = []

    # I used dictionary in order to connect PASS data From Python to PHP
    # 1-12  January-December
    D = {'12': total_result[0],
         '11': total_result[1],
         '10': total_result[2],
         '9': total_result[3],
         '8': total_result[4],
         '7': total_result[5],
         '6': total_result[6],
         '5': total_result[7],
         '4': total_result[8],
         '3': total_result[9],
         '2': total_result[10],
         '1': total_result[11],
         }
    # PASS values to DISPLAY.php
    print json.dumps(D)


def main():
    Total_Expenses_Amount_Per_Month()


if __name__ == '__main__':
    main()
