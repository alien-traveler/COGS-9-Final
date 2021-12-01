import csv

with open('California_Fire_Perimeters_(all).csv') as read_file:
    with open('result2020.csv', mode='w', newline='') as write_file:
        read_file = csv.reader(read_file, delimiter=',')
        write_file = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        line_count = 0
        # read through data
        for row in read_file:
            # column row
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                write_file.writerow(row)
                line_count += 1
            # all other rows
            else:
                # if the year is between 2018 - 2020, write that row of data into the new file
                if(row[1] == '2020'):
                    # print(row)
                    write_file.writerow(row)
                    line_count += 1

        print(f'Processed {line_count} lines.')

