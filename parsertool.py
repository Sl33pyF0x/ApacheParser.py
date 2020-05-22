#!/bin/python3

import re

from collections import Counter

import csv

### Menu function
def options_menu():

	print("1. Show the events related to a specific IP address.")
	print("2. Make a csv list of IP addresses and number their occurences.")
	print("3. Count how many unique IP addresses there are in the log file.")
	print("4. Count how many 404 error codes there are. (Failed connections).")
	print("5. Count how many 200 success codes there are.(successful connections).")
	print('\n')
	print("What would you like the parser to find for you?")
	selection = input()
	return selection

### Function 1

def ur_in_trouble(logFile):
	address = input("What IP address are you investigating? ")

	f = open(logFile, "r")
	for line in f:
		itemized = (line.split(' '))
		for word in itemized:
			if word == address:
				print(line)

### Function-set 2

def IP_finder(logFile):
	with open(logFile) as f:
		log = f.read()

		regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

		ips_list = re.findall(regexp, log)

		return ips_list


def count(ips_list):
	return Counter(ips_list)

def write_csv(counter):
	with open('output.csv', 'w') as csvfile:
		writer = csv.writer(csvfile)
		header = ['IP', 'Frequency']
		writer.writerow(header)
		for item in counter:
			writer.writerow( (item, counter[item]) )

### Function-set 3
def Census():
	write_csv(count(IP_finder(logFile)))
	with open('output.csv', mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		line_count = 0
		for row in csv_reader:
			line_count += 1
		print("There are "+ str(line_count) + " unique IPs in this log.")

### Function 4

def error_not_found(logFile):
	f = open(logFile, "r")
	for line in f:
		itemized = (line.split(' '))
		for word in itemized:
			if word == "404":
				print(line)
	f.close()

### Function 5

def success(logFile):
	f = open(logFile, "r")
	for line in f:
		itemized = (line.split(' '))
		for word in itemized:
			if word == "200":
				print(line)
	f.close()

### Main: Welcome Screen ###

print("*" * 75)
print("")
print("Welcome to the Apache Log Parser!")
print("")
print("*" * 75)
print("")
logFile = input("What is the path to your log file? ")

print("Your log file is: " + logFile + ".")
print("*" * 75)
print("")
selection = str(options_menu())
print('\n')

### Part 2: The Switchboard ###

if selection == "1":
	print("You selected option 1")
	ur_in_trouble(logFile)

elif selection == "2":
	print("You selected option 2")
	write_csv(count(IP_finder(logFile)))
	print("There is now a file called output.csv. You will find it in the same directory as this tool.")

elif selection == "3":
	print("You selected option 3")
	Census()

elif selection == "4":
	print("You selected option 4. If there are no results, none were found in the log.")
	error_not_found(logFile)

elif selection == "5":
	print("You selected option 5. If there are no results, none were found in the log.")
	success(logFile)
else:
	print("Not a valid option.")
