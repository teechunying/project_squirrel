# Squirrel Tracker
A Django-based web application for tracking all known squirrels in Central Park. 
The data is based on the <a href="https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw">2018 Central Park Squirrel Census data</a>. 

# Team Members
<li>Ian Ho & Tee Chun Ying
<li>UNIs: [ih2350, cyxxxx]
<li>Group Name: Group xxxx Section 2

# Main Features
- Import Function: to import data from the 2018 census file
- Export Function: to export data in CSV format
- Mapping: displays location of squirrel sightings on an OpenStreets map 
- List of all squirrel sightings, with quick access to the following functions:
	- Update Function: Allows for updating of details for each squirrel sighting
	- Adding new sightings
	- Delete sightings
- General statistics about squirrel sightings

# Importing Data
To import data from a CSV file, execute the following line of code:

In this example, <b>rows.csv</b> is the file name.

```sh
# on Bash command line
python manage.py import_squirrel_data rows.csv
```

# Exporting Data
To import data into a CSV file, execute the following line of code:

In this example, <b>export.csv</b> is the file name we want to export the data into.

```sh
# on Bash command line
python manage.py import_squirrel_data export.csv
```
# Dependencies
- Django   (2.2.7)
- pytz     (2019.3)
- sqlparse (0.3.0)

# Additional Features
- Function to Delete ALL existing squirrel sightings in the database
```sh
# on Bash command line
python manage.py delete
```

# Additional Notes
- The map might take a while to load for larger datasets
- When a new sighting is added, if the Unique Squirrel ID is already in use, the web application automatically adds a suffix <i>-R</i> to the end of the squirrel ID
- When a new sighting is added, if the input date is after today, the form automatically corrects the date to the current date, and the following message will show up at the bottom of the form: <i>'Date automatically corrected to today!'</i> 
