adduser.py
=

This Python script defines a function add_user to add a new user entry to a file named 'passwd.txt' in a specific format (username:real_name:password). The script then prompts the user for input to create a new user by specifying a new username, real name, and password. It reads existing usernames from the 'passwd.txt' file and checks if the provided username already exists. If the username is found in the existing user list, it prints an error message. Otherwise, it calls the add_user function to append the new user information to the file and prints a confirmation message.

The script allows for the creation of new user entries while checking for duplicate usernames in the existing file. Note that the security of storing passwords in this manner is not recommended for actual use; it is better to use secure password hashing methods.

The output will be:

Enter new username: snehit123

Enter real name: Snehit parajuli

Enter password: psswd123

User Created.


deluser.py
=

This Python script defines a function `delete_user` to remove a user entry from a file named 'passwd.txt' based on the provided username. The script then prompts the user for input to delete a user by specifying the username. It reads all lines from the 'passwd.txt' file, writes back all lines excluding the one that starts with the specified username, effectively deleting that user's entry. It then prints a confirmation message, "User Deleted."

The script allows for the removal of a user entry from the file based on the specified username. Note that this script assumes that each line in 'passwd.txt' corresponds to a single user entry with the format "username:real_name:password." Also, it is worth noting that in a production environment, more secure methods and considerations should be taken into account for user management and password handling.

The output will be:

Enter username: snehit123

User Deleted.

login.py
=


This Python script defines a function login to check if a provided username and password match any user entries in a file named 'passwd.txt'. The script then prompts the user for input to log in, asking for a username and password. It calls the login function with the provided credentials and prints either "Access granted" or "Access denied" based on the function's result.

The login function reads each line in 'passwd.txt', splits it into fields using the ':' delimiter, and compares the provided username and password with those from the file. If a matching user is found, the function returns True; otherwise, it returns False.

Note that this script assumes that each line in 'passwd.txt' corresponds to a single user entry with the format "username:real_name:password." Additionally, for secure password handling, it is recommended to use password hashing methods and consider other security measures in a production environment.

The outut will be:

User:     snehit123

Password: psswd123

Access granted.

psswd.py
=

This Python script defines a function change_password to modify the password of a specified user in a file named 'passwd.txt'. The script then prompts the user for input to change a password, asking for the username, the current password, the new password, and a confirmation of the new password. It calls the change_password function with the provided credentials and prints either "Password changed" or "Passwords do not match. No change made."

The change_password function reads each line in 'passwd.txt', splits it into fields using the ':' delimiter, and checks if the provided username and current password match any user entries in the file. If a matching user is found, the function updates the password to the new one and prints "Password changed." If the new password and the confirmation do not match, it prints "Passwords do not match. No change made." The updated content is then written back to the file.

Note that this script assumes that each line in 'passwd.txt' corresponds to a single user entry with the format "username:real_name:password." Additionally, for secure password handling, it is recommended to use password hashing methods and consider other security measures in a production environment.

The output will be:

User:             snehit123

Current Password: psswd123

New Password:     snehit

Confirm:          snehit

Password changed.
