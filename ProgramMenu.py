from Final import Connector
import mysql.connector
from tabulate import tabulate
import os.path
import csv
import random


class Main:
#default constructor
	def __init__(self):
		QUIT = False
		self.num = 0
		self.closeday = False #I didn't do this, but I would reset this variable at the "start of the day"

		while (QUIT == False):
			print("""
			1.Add Investor
			2.Add Cyptocurrency
			3.Buy Investment
			4.Sell Investment
			5.View All Investments 
			6.View All Investors
			7.---
			8.Quit
			""")

			Database = Connector()
			mysql_username = 'ab107'  # Username
			mysql_password = 'aijeNah8'  # MySQL password
			Database.open_database('localhost', mysql_username, mysql_password, mysql_username)  # open database
			ans=input("Select from the menu of options (Enter number):")
			if ans=="1":
				print("-")
				print("New Investor Information:")
				investorid=input("Investor ID: ")
				investorname=input("Investor Name: ")
				investoremail=input("Investor Email: ")
				i_values=investorid+ ", '" + investorname + "', " + investoremail 
				Database.insert('INVESTOR', i_values)
			elif ans=="2":
				print("-")
				print("New Cyptocurrency Information:")
				cyptocurrencyid=input("Cyptocurrency ID: ")
				cyptocurrencyname=input("Cyptocurrency Name: ")
				cyptocurrencycv=input("Cyptocurrency Current Value: ")
				c_values=cyptocurrencyid+ ", '" + cyptocurrencyname + "', " + cyptocurrencycv 
				Database.insert('CYPTOCURRENCY', c_values)
			elif ans=="3":
				print("This should always add a new record")
				print("Newly Bought Investment Information:")
				I_investorid=input("Investor ID: ")
				I_cyptocurrencyid=input("Cyptocurrency ID: ")
				I_cyptocurrencyns=input("Number of Shares: ")
				I_pp=input("Purchase Price: ")
				I_so=INPUT("Still Owned: ")
				I_values=I_investorid+ ", '" + I_cyptocurrencyid + "', " + I_cyptocurrencyns + "', " +  I_pp + "', " + I_so
				Database.insert('INVESTMENT', I_values)
			elif ans=="4":
				print("This should update a record and display profit/loss")
			elif ans=="5":
				print("and total value for given investor. Sort in decending order by value. (This should aggregate the total investments by cyptocurrency")\
			elif ans=="6":
				print("and total shares for each. for a given crptocurrency. Sort in ascending order by name.")
			elif ans=="7":
				print("We will see")				
			elif ans=="8":
				QUIT = True
				Database.close_db()
				
			else:
				print("\n Not a Option Try again")
		quit()
