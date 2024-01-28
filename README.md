# Programming_portfoilio
Task 1
=
This Python script functions as a pizza price calculator based on several input parameters. The user is prompted to input the number of pizzas desired, whether it is Tuesday, whether delivery is required, and whether the order is placed via an app. The price function calculates the total price considering factors such as the base pizza price, a discount on Tuesdays, additional delivery costs for small orders, and a discount for app orders. The script ensures user input validation, asking for correct answers if the input is invalid, and then computes the total price using the price function. Finally, it displays the total price with a formatted message. The code is well-structured, leveraging functions and input validation loops for user-friendly interactions and providing clear prompts and messages throughout the process.

The Output Will be:

BPP Pizza Price Calculator

==========================

How many pizzas would you like to order? 3

Is it Tuesday? y

Is delivery required? y

Did the customer use the app? n

Total Price: £39.00

Code is written to handle erroneous input.

Task 2
=
This Python script is designed to analyze a log file containing entries related to the activities of cats entering and leaving a house. The script takes the path to the log file as a command-line argument. It employs a try-except block to handle potential errors during file reading, such as the file not being found or encountering other exceptions. The script then initializes variables for analysis, including counters for the number of correct entries by a cat named 'OURS,' the number of times other cats were doused with water, and cumulative time spent inside by the correct cat. The script iterates through the lines of the log file, processing each entry and updating the analysis variables accordingly. After processing all lines or encountering an 'END' marker, it calculates and prints various analysis results, such as the total number of correct entries, the number of doused cats, the total time spent inside (converted to hours), the average duration of correct visits, and the longest and shortest durations. Finally, in the main block, the script checks if the correct number of command- line arguments is provided, prints a usage message if not, and calls the analyze_log function with the specified log file path if the arguments are correct.

THE OUTPUT WILL BE: Log File Analysis

================== Total number of times the correct cat has entered the house is: <correct_entry>

Number of times cats were doused with water: <doused_cats>

Total time spent in the house by the correct cat: <total_hours> hours

Average duration of each visit by the correct cat: minutes

Duration of the longest visit by the correct cat: minutes

Duration of the shortest visit by the correct cat: minutes

------IF ARGUMENT IS MORE OR EQUAL TO 2:-----------

"Usage: python script.py <log_file_path>" WILL BE PRINTED

TASK 3
=
