Pollen Project
===========

Application that scrapes pollen information from http://www.stampar.hr/hr/peludna-prognoza-za-hrvatsku every dan and stores the data.


Pollen API
------------

Returns all pollen levels for Osijek, Split and Zagreb

### Request /all

GET http://localhost:5000/all Returns all pollen levels for Osijek, Split and Zagreb


PARAMS

city - Zagreb, Split or Osijek

name - Pollen Name

date - Specific date (%Y-%m-%d)

date_from -  Date From (%Y-%m-%d)

date_to  - Date To (%Y-%m-%d)

### Request /zagreb

GET http://localhost:5000/zagreb Gets all pollen data for Zagreb in the last 30 days

