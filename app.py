# from sqlalchemy.ext.automap import automap_base
# from sqlalchemy.orm import Session
# from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template,send_file
from flask_cors import CORS
import pandas as pd
import matplotlib.pyplot as plt
import io

# engine = create_engine("")


# Base = automap_base()

# Base.prepare(autoload_with=engine)




app = Flask(__name__,template_folder="")
df=pd.read_csv('static/Resources/netflix_userbase.csv')
CORS(app)


#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    """Render the home page"""
    return render_template('template.html')

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
    return allsubs
    
@app.route("/api/allsubtypes")
def allsubtypes():
    subs=df["Subscription Type"].unique().tolist()
    return jsonify({"subs":subs})

@app.route("/api/allcountries")
def allcountries():
    countries=df["Country"].unique().tolist()
    return jsonify({"countries":countries})

@app.route("/api/alldevices")
def alldevices():
    devices=df["Device"].unique().tolist()
    return jsonify({"device_types":devices})
   

if __name__ == '__main__':
    app.run(debug=True)


