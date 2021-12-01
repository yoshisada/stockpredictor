# Stock Predictor

## Introduction
This was built in order to expiriment with building a react frontend on top of a python backend.  The python server utilizes Flask and analyzes stock data with Facebook Prophet pulled from Yahoo Finance.  The python server then saves a image of the two graphs for the React frontend to access.  Deployed on Google Cloud Engine at http://104.198.205.248:3000/.

## ToDo
+ Tokenize data per browser instance so more than 1 user can create forecasts at any given time.


## Requirements
The User Search App should be able to:
+ Display user information (at least name, email, phone, and city)
+ Remove entries from list (do not try to delete from databse, data will refresh on pull)
+ Search for users by name
+ Search for users by city
+ Sort users by city