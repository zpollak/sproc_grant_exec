#!/usr/bin/env python

import sys
import pyodbc

# SQL Server Info
driver = '{SQL Server Native Client 11.0}'
server = 'SERVER'
username = 'DOMAIN\YOUR_USERNAME'
database = 'DB_NAME'
users = ['DOMAIN\USERNAME1', 'DOMAIN\USERNAME2']

def input_sproc():
	print('FYI - This program will grant EXECUTE permissions to all database end users' \
	' for the user-defined stored procedure.\nPlease press CTRL+c to terminate at any point.')
	print('Please input the schema of the stored procedure and hit <Enter> (or quit with "q"): ')
	schema = str(raw_input())
	if schema.lower() == 'q':
		print('Quitting the program!')
		sys.exit(0)
	
	print('Please input the name of the stored procedure and hit <Enter> (or quit with "q"): ')
	sproc = str(raw_input())
	if sproc.lower() == 'q':
		print('Quitting the program!')
		sys.exit(0)
	
	return schema, sproc

def run_sql(cxn, schema, sproc):
	cursor = cxn.cursor()
	cursor.execute('USE ' + database)
	for user in users:
		sql = 'GRANT EXECUTE ON [' + schema + '].[' + sproc + '] TO [' + user + ']'
		try:
			cursor.execute(sql)
			print('{} can now execute {}'.format(user, sproc))
		except Exception as e:
			print(e)

def main():
	# SQL Server connection
	cxn = pyodbc.connect(Driver=driver, Trusted_Connection='yes', Server=server, UID=username)

	# Prompt user for stored procedure
	schema, sproc = input_sproc()
	
	# Grant EXECUTE for users
	run_sql(cxn, schema, sproc)

if __name__ == '__main__':
	main()
