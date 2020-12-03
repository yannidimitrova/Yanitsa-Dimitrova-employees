import datetime


def raw_data_list():
    raw_data_list = employee_file.readlines()
    while "\n" in raw_data_list:
        raw_data_list.remove("\n")

    return raw_data_list


def making_nested_list(raw_data_list):
    list = []
    for line in raw_data_list:
        line_elements = line.split(", ")
        list.append(line_elements)

    return list


def employee_pairs_and_dates(list):
    pairs_dates = {}
    for current_row in range(len(list)):
        for extra_rows in range(len(list) - current_row - 1):
            project_id_current_row = list[current_row][1]
            project_id_next_row = list[current_row + extra_rows + 1][1]
            if project_id_current_row == project_id_next_row:
                datefrom_current_row = date_from_current_row(list, current_row)
                datefrom_next_row = date_from_next_row(list, current_row, extra_rows)
                dateto_current_row = date_to_current_row(list, current_row)
                dateto_next_row = date_to_next_row(list, current_row, extra_rows)

                if datefrom_current_row < datefrom_next_row:
                    later_datefrom = datefrom_next_row
                else:
                    later_datefrom = datefrom_current_row

                if dateto_current_row > dateto_next_row:
                    earlier_dateto = dateto_next_row
                else:
                    earlier_dateto = dateto_current_row

                if later_datefrom < earlier_dateto:
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

    return pairs_dates


def converting_in_date_format(year, month, date):

    return datetime.date(year, month, date)


def date_from_current_row(list, current_row):
    datefrom_current_row = list[current_row][2].split("-")
    if datefrom_current_row[0] != "NULL":

        return converting_in_date_format(int(datefrom_current_row[0]), int(datefrom_current_row[1]), int(datefrom_current_row[2]))
    return datetime.date.today()


def date_from_next_row(list, current_row, extra_rows):
    datefrom_next_row = list[current_row + extra_rows + 1][2].split("-")
    if datefrom_next_row[0] != "NULL":

        return converting_in_date_format(int(datefrom_next_row[0]), int(datefrom_next_row[1]), int(datefrom_next_row[2]))
    return datetime.date.today()


def date_to_current_row(list, current_row):
    dateto_current_row = list[current_row][3].split("-")
    for element in range(len(dateto_current_row)):
        if "\n" in dateto_current_row[element]:
            dateto_current_row[element] = dateto_current_row[element].replace("\n", "")
    if dateto_current_row[0] != "NULL":

        return converting_in_date_format(int(dateto_current_row[0]), int(dateto_current_row[1]), int(dateto_current_row[2]))
    return datetime.date.today()


def date_to_next_row(list, current_row, extra_rows):
    dateto_next_row = list[current_row + extra_rows + 1][3]
    if "\n" in dateto_next_row:
        dateto_next_row = dateto_next_row.replace("\n", "")
    dateto_next_row = dateto_next_row.split("-")
    if dateto_next_row[0] != "NULL":

        return converting_in_date_format(int(dateto_next_row[0]), int(dateto_next_row[1]), int(dateto_next_row[2]))
    return datetime.date.today()


def sorting_the_values_inside(pairs_dates):
    for key, values in pairs_dates.items():
        pairs_dates[key] = sorted(values, key=lambda x: x[0])
    return pairs_dates


def removing_duplicated_dates(pairs_dates):
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
    return pairs_dates


def calculating_durations_together(pairs_dates):
    pairs_duration = {}
    for key, values in pairs_dates.items():
        duration = 0
        for start_end_date in values:
            number_of_days = (start_end_date[1] - start_end_date[0]).days
            duration += number_of_days
        pairs_duration[key] = duration
    return pairs_duration


employee_file = open("Testing_data.txt", "r")

if employee_file.readable():
    data_list_without_empty_spaces = raw_data_list()
    nested_list = making_nested_list(data_list_without_empty_spaces)
    dictionary = employee_pairs_and_dates(nested_list)
    sorted_dictionary = sorting_the_values_inside(dictionary)
    dictionary_without_duplicated_periods = removing_duplicated_dates(sorted_dictionary)
    dictionary_with_employees_and_durations = calculating_durations_together(dictionary_without_duplicated_periods)

    pairs_duration = dict(sorted(dictionary_with_employees_and_durations.items(), key=lambda x: -x[1]))

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