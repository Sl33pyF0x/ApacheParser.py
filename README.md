# ApacheParser.py

ApacheParser.py is a menu driven tool. Using it is as simple as: 

Cloning the Repository:

```git clone https://github.com/Sl33pyF0x/ApacheParser.py.git```

Moving into the directory folder:

``` cd ApacheParser.py```

Changing Permissions on the python tool:

```sudo chmod 755 parsertool.py```

and running it:

```./parsertool.py```

The tool will prompt the user for a log file to parse and will provide five functions for seeing relevant information
pertaining to the file. These functions are:

1. Shows all of the actions taken by a specific machine by looking at it's IP address.
2. Creates a .csv file with a list of all of the unique IP addresses and lists the number of their occurences.
3. Gives a count of all unique IP addresses.
4. Shows how many 404 errors are in the log.
5. Shows how many 200 success codes are in the log.
