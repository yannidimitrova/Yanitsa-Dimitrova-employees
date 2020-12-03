This is the first version of the task "Employee pair with longest time together in team". 
This version is without functions and classes. Just a test. Its working.

Structure of decision:
1. Making the file readable. Checking if its readable;
2. If so - creating a list with the raw data;
3. Removing empty rows - if there is any;
4. Making nested list;
5. Sorting the big list by project (position [1] in the sub lists) - not mandatory, can work without it;
6. Making dictionary - to contain the employee-pairs and dates, when the same project;
6.1. Finding two projects with the same ID;
6.2. Defining the Employee ID;
6.3 Defining DateFrom - the later from the two DateFrom. This is the moment both employees start to work together on the project;
6.4. Defining DateTo - the earlier from the two DateTo. This is the moment till when both of the employees work together. Check - if it is NULL or date format (YYYY-MM-DD);
6.5. Check - if DateTo is after DateFrom. If so - it is valid;
6.6. Making the employee pair. To be sure it will be unique - we always put first the smaller ID. To keep info where ends first employee ID and where starts the second - we put dush ("-") between;
6.7. Check - if dictionary already contain as a key this employee pair. If not - we add it with value empty list;
6.8. Making tuple pair with DateFrom and DateTo;
6.9. Appending the tuple to the according list;
7. Removing duplicated dates for each employee pair. In this way we avoid calculating twice if there is some days, when the employee pair work together on more than one project;
8. Calculating common duration for each employee pair;
9. Picking the employee pair with biggest common working time on projects - as we sort the dictionary;
10. Printing the result on the console;
11. Closing the txt file.


Thank you for the attention!

    
