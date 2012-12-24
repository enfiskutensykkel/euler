#!/usr/bin/env python

days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun' ]

def is_leap(year):
	if year % 400 == 0:
		return True
	elif year % 100 == 0:
		return False

	return year % 4 == 0

def first_of_year(year):
	if year == 1900:
		return 0

	return (first_of_year(year-1) + (366 if is_leap(year-1) else 365)) % 7

def day_of_year(year, month):
	days = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
	if is_leap(year):
		days[1] = 29

	return sum(days[0:month])

def first_of_month(year, month):
	return (first_of_year(year) + day_of_year(year, month)) % 7


if __name__ == '__main__':
	sundays = 0
	for year in xrange(1901, 2001):
		for month in xrange(0, 12):
			if first_of_month(year, month) == 6:
				sundays += 1

	print sundays
