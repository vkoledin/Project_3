

from flask import Flask, jsonify, render_template,send_file
from flask_cors import CORS
import pandas as pd
import matplotlib.pyplot as plt
import io





# Initialize the Flask application
app = Flask(__name__,template_folder="")
#load csv into dataframe
df=pd.read_csv('static/Resources/netflix_userbase.csv')
# Enbabling CORS (cross-origin)
# By using CORS(app) in Flask backend,  enable front-end JavaScript code to make HTTP requests 
# to  Flask API endpoints from different origins. This is essential for seamless integration between 
# your front-end and back-end, especially if they are hosted on different domains. 
# Without enabling CORS, these cross-origin requests would be blocked by the browser, 
# preventing your front-end from accessing the data it needs to render charts and visualizations.
# Your JavaScript code uses d3.json to make HTTP GET requests to various API endpoints
# These requests will be blocked by the browser if the API and the front-end are hosted on different 
# origins unless the server (Flask app) allows cross-origin requests via CORS.
CORS(app)


#################################################
# Flask Routes
#################################################

#Defining root route that renders home page to template
@app.route("/")
def index():
    """Render the home page"""
    return render_template('template.html')

# route to take country as a parameter and filter data of that country and count devices (device pie chart)
@app.route("/api/devices/<country>")
def devices_by_country(country):
    try:
        # Filter data for the specified country
        country_data = df[df['Country'] == country]

        # Check if there's any data for the specified country
        if country_data.empty:
            return f"No data available for {country}", 404

        # Count occurrences of each device type
        device_types = country_data['Device'].value_counts()

        
    
        return jsonify({"device_counts":device_types.to_json()})

    except Exception as e:
        import traceback
        traceback.print_exc()  # Print traceback for debugging
        return str(e), 500  # Return the actual exception message and 500 status code
    
# route to for user selected country and get country's sub data (sub type pie chart)
@app.route("/api/subscriptiontypes/<country>")
def subscription_types_by_country(country):
    try:
        # Filter data for the specified country
        country_data = df[df['Country'] == country]

        # Check if there's any data for the specified country
        if country_data.empty:
            return f"No data available for {country}", 404

        # Count occurrences of each subscription type
        subscription_types = country_data['Subscription Type'].value_counts()

        
    
        return jsonify({"subscription_counts":subscription_types.to_json()})

    except Exception as e:
        import traceback
        traceback.print_exc()  # Print traceback for debugging
        return str(e), 500  # Return the actual exception message and 500 status code 
    
# route to take subscription type as parameter and country occurences per country (dynamic bar chart)   
@app.route("/api/country/<subscription>")
def Subscriptiontypecountry(subscription):
    try:
        # Filter data for the specified country
        sub_data = df[df['Subscription Type'] == subscription]

        # Check if there's any data for the specified country
        if sub_data.empty:
            return f"No data available for {subscription}", 404

        # Count occurrences of each subscription type
        countrycount = sub_data['Country'].value_counts()

        
    
        return jsonify({"countrysubs":countrycount.to_json()})

    except Exception as e:
        import traceback
        traceback.print_exc()  # Print traceback for debugging
        return str(e), 500  # Return the actual exception message and 500 status code 
    
# route to group data by country and subscription type and count number of users (stacked bar chart)
@app.route("/api/allcountries/allsubscriptions")
def Allsubscountry():
    # Group by 'Country' and 'Subscription Type', then count 'User ID'
    results = df.groupby(['Country', 'Subscription Type'])['User ID'].count().unstack()
    # Fill NaN values with zeros
    results = results.fillna(0)
    # Reset index to make 'Country' a column
    results = results.reset_index()
    # Convert DataFrame to a dictionary
    allsubs = results.to_dict(orient='records')
    # dont have to jsonify because Flask automatically serializes python lists and dictionaries into JSON format
    return allsubs
# return all unique subscription types   
@app.route("/api/allsubtypes")
def allsubtypes():
    subs=df["Subscription Type"].unique().tolist()
    return jsonify({"subs":subs})
# return all countries
@app.route("/api/allcountries")
def allcountries():
    countries=df["Country"].unique().tolist()
    return jsonify({"countries":countries})
# return all devices
@app.route("/api/alldevices")
def alldevices():
    devices=df["Device"].unique().tolist()
    return jsonify({"device_types":devices})
   
# running flask application
if __name__ == '__main__':
    app.run(debug=True)


