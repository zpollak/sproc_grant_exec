# sproc_grant_exec

### Overview
This script will grant EXECUTE permissions to a stored procedure for a list of SQL Server users.

### Instructions
1. Update lines 6-9 with your server name, database name, username and the usernames of the users for whom you would like to grant EXECUTE permissions.
2. Run the script from any directory by navigating to that directory and running `python sproc_grant_exec.py`.

##### Dependencies
The only non-standard dependency is **pyodbc** which can be installed via `pip install pyodbc`.
