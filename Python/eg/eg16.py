#!/usr/bin/python3

import datetime

if __name__ == "__main__":
	print(datetime.date.today().strftime("%d/%m/%Y"))

	mydate = datetime.date(1941,1,5)

	print(mydate.strftime("%d/%m/%Y"))

	