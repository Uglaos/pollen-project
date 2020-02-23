Pollen Project
===========

Application that scrapes pollen information from http://www.stampar.hr/hr/peludna-prognoza-za-hrvatsku every day and stores the data.


Pollen API
------------

Returns all pollen levels for Osijek, Split and Zagreb

### GET http://localhost:5000/all


### PARAMS

- city - Zagreb, Split or Osijek

- name - Pollen Name

- date - Specific date (%Y-%m-%d)

- date_from -  Date From (%Y-%m-%d)

- date_to  - Date To (%Y-%m-%d)

Example

```json
{
    "city": "Zagreb", 
    "date": "2020-02-16T00:00:00", 
    "id": 48, 
    "level": "6.3", 
    "name": "Joha"
  }
```

Zagreb Pollen Report
--------------------

Shows pollen data chart for Zagreb in the last 30 days
http://localhost:5000/zagreb 

![Zagreb pollen](https://i.ibb.co/cktfdRs/zagreb.png)

 
