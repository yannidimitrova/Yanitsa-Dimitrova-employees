import datetime

employee_file = open("Testing_data.txt", "r")

if employee_file.readable():
    raw_data_list = employee_file.readlines()
    if "\n" in raw_data_list:
        raw_data_list.remove("\n")

    # making nested list
    nested_list = []
    for line in raw_data_list:
        line_elements = line.split(", ")
        nested_list.append(line_elements)

    # sorting by project (position [1] in the sub lists)
    for i in range(len(nested_list)):
        for j in range(len(nested_list) - i - 1):
            current_row_sorting = int(nested_list[j][1])
            next_row = int(nested_list[j + 1][1])
            if current_row_sorting > next_row:
                copied_nested_list = nested_list[j]
                nested_list[j] = nested_list[j + 1]
                nested_list[j + 1] = copied_nested_list

    # Making dictionary - to contain the employee-pairs and dates, when the same project
    pairs_dates = {}
    for current_row in range(len(nested_list)):
        for extra_rows in range(len(nested_list) - current_row - 1):
            project_id_current_row = nested_list[current_row][1]
            project_id_next_row = nested_list[current_row + extra_rows + 1][1]
            if project_id_current_row == project_id_next_row:

                # DateFrom
                datefrom_current_row = nested_list[current_row][2].split("-")
                if datefrom_current_row[0] != "NULL":
                    datefrom_year_current_row = int(datefrom_current_row[0])
                    datefrom_month_current_row = int(datefrom_current_row[1])
                    datefrom_date_current_row = int(datefrom_current_row[2])
                    date_from_current_row = datetime.date(datefrom_year_current_row, datefrom_month_current_row, datefrom_date_current_row)
                else:
                    date_from_current_row = datetime.date.today()

                datefrom_next_row = nested_list[current_row + extra_rows + 1][2].split("-")
                if datefrom_next_row[0] != "NULL":
                    datefrom_year_next_row = int(datefrom_next_row[0])
                    datefrom_month_next_row = int(datefrom_next_row[1])
                    datefrom_date_next_row = int(datefrom_next_row[2])
                    date_from_next_row = datetime.date(datefrom_year_next_row, datefrom_month_next_row, datefrom_date_next_row)
                else:
                    date_from_next_row = datetime.date.today()

                if date_from_current_row < date_from_next_row:
                    later_datefrom = date_from_next_row
                else:
                    later_datefrom = date_from_current_row

                # DateTo
                dateto_current_row = nested_list[current_row][3].split("-")
                for element in range(len(dateto_current_row)):
                    if "\n" in dateto_current_row[element]:
                        dateto_current_row[element] = dateto_current_row[element].replace("\n", "")
                if dateto_current_row[0] != "NULL":
                    dateto_year_current_row = int(dateto_current_row[0])
                    dateto_month_current_row = int(dateto_current_row[1])
                    dateto_date_current_row = int(dateto_current_row[2])
                    date_to_current_row = datetime.date(dateto_year_current_row, dateto_month_current_row,
                                                          dateto_date_current_row)
                else:
                    date_to_current_row = datetime.date.today()

                dateto_next_row = nested_list[current_row + extra_rows + 1][3]
                if "\n" in dateto_next_row:
                    dateto_next_row = dateto_next_row.replace("\n", "")
                dateto_next_row = dateto_next_row.split("-")
                if dateto_next_row[0] != "NULL":
                    dateto_year_next_row = int(dateto_next_row[0])
                    dateto_month_next_row = int(dateto_next_row[1])
                    dateto_date_next_row = int(dateto_next_row[2])
                    date_to_next_row = datetime.date(dateto_year_next_row, dateto_month_next_row,
                                                       dateto_date_next_row)
                else:
                    date_to_next_row = datetime.date.today()

                if date_to_current_row > date_to_next_row:
                    earlier_dateto = date_to_next_row
                else:
                    earlier_dateto = date_to_current_row

                if later_datefrom < earlier_dateto:
                    # checking the EmpID and making the keys - concatenating the smaller employee ID with the bigger ID
                    emp_id_current_row = nested_list[current_row][0]
                    emp_id_next_row = nested_list[current_row + extra_rows + 1][0]
                    if emp_id_current_row < emp_id_next_row:
                        key = str(emp_id_current_row) + "-" + str(emp_id_next_row)
                    else:
                        key = str(emp_id_next_row) + "-" + str(emp_id_current_row)
                    if key not in pairs_dates:
                        pairs_dates[key] = []
                    tuple = (later_datefrom, earlier_dateto)
                    pairs_dates[key].append(tuple)

    # Removing duplicated dates for each employee pair
    for key, values in pairs_dates.items():
        pairs_dates[key] = sorted(values, key=lambda x: x[0])

    for key, values in pairs_dates.items():
        temporary_list = []
        index = 0
        while index < len(values):
            if index + 1 < len(values):
                current_end_date = values[index][1]
                next_start_date = values[index + 1][0]
                if next_start_date <= current_end_date:
                    new_tuple = (values[index][0], values[index + 1][1])
                    index += 1
                else:
                    new_tuple = (values[index][0], values[index][1])
            else:
                new_tuple = (values[index][0], values[index][1])
            temporary_list.append(new_tuple)
            index += 1
        pairs_dates[key] = temporary_list

    # Calculating duration for each employee pair
    pairs_duration = {}
    for key, values in pairs_dates.items():
        duration = 0
        for start_end_date in values:
            number_of_days = (start_end_date[1] - start_end_date[0]).days
            duration += number_of_days
        pairs_duration[key] = duration

    #Sorting employee pairs by days of working in team
    pairs_duration = dict(sorted(pairs_duration.items(), key=lambda x: -x[1]))

    for employee_pair, time_together in pairs_duration.items():
        the_employee_pair = employee_pair.split("-")
        first_employee = the_employee_pair[0]
        second_employee = the_employee_pair[1]
        the_time_together = time_together
        break

    print(f"The employees who have been working together in team the longest are: Employee number {first_employee}  and Employee number {second_employee}. They have been working in team {the_time_together} days!")


else:
    print("File is not readable.")

employee_file.close()
