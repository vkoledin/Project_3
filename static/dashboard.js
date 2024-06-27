console.log("script");

let countries;
// Fetch countries and populate dropdown on page load
// ensures script runs only after HTML is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // making GET request to API end point, expecting JSON response
    d3.json("/api/allcountries").then(function(data) {
        // need .countries to access array of country names because data is a JSON object, 
        // with countries as the key allowing to access the array of country names
        countries = data.countries;
        console.log(countries);

        // Populate dropdown from countries array
        const select = d3.select("#selCountryDataset");
        // iteraing over each country in the 'countries' array
        countries.forEach(country => {
            select.append('option')
                // set value attribute of <option> element and text (making them visible) of <option>
                .attr('value', country)
                .text(country);
        });
        // Select the first country and trigger the change event
        const firstCountry = countries[0]; 
        select.property('value', firstCountry); // Set the selected value in the dropdown
        optionChanged(firstCountry); // Trigger the function for the first country
    }).catch(function(error) {
        console.error('Error fetching countries:', error);
    });

});
let subscriptions;
document.addEventListener('DOMContentLoaded', function() {
    d3.json("/api/allsubtypes").then(function(subdata) {
        console.log("Subscription Data:",subdata);
        subscriptions = subdata.subs;
        console.log("Subs:",subscriptions);

        // Populate dropdown from countries array
        const select = d3.select("#additionalDropdown");
        
        subscriptions.forEach(sub => {
            select.append('option')
                .attr('value', sub)
                .text(sub);
        });
        // Select the first Subscription Type and trigger the change event
        const firstSub = subscriptions[0];
        select.property('value', firstSub); // Set the selected value in the dropdown
        additionalDropdownChanged(firstSub); // Trigger the function for the first Device
    }).catch(function(error) {
        console.error('Error fetching devices:', error);
    });

});

let myPieChart;

// Function to handle dropdown change
function optionChanged(targ) {
    // Use the selected country to fetch subscription types data
    console.log(targ)
    // asynchornouly fetches subscripotion types data from endpoint
    d3.json(`/api/subscriptiontypes/${targ}`).then(function(subscriptionData) {
       // Parse the JSON string into an object
       const subscription_counts = JSON.parse(subscriptionData.subscription_counts);
       console.log(subscription_counts)
       // Extract Labels and Values from the JSON object
       const labels = Object.keys(subscription_counts);
       const values = Object.values(subscription_counts);
        console.log(labels)
        console.log(values)
       // Create data object for Plotly pie chart
       const data = [{
        labels: labels,
        values: values,
        type: 'pie',
        marker: {
            colors: ['#FF5733', '#33FF57', '#3380FF'] 
        }
    }];
    
    // Set layout for the pie chart 
    const layout = {
        title: 'Subscription Types',
        showlegend: true // Display legend
    };
    
    // Render the Plotly pie chart
    Plotly.newPlot('SubChart', data, layout);
})
.catch(function(error) {
    console.error('Error fetching subscription data:', error);
    // Handle error gracefully, e.g., display error message to the user
});
    // fetch device data from endpoint
    d3.json(`/api/devices/${targ}`).then(function(deviceData) {
        // Parse the JSON string into an object
        const device_counts = JSON.parse(deviceData.device_counts);
        console.log(device_counts)
        // Extract Labels and Values from the JSON object
        const labels = Object.keys(device_counts);
        const values = Object.values(device_counts);
        console.log(labels)
        console.log(values)
        // Create data object for Plotly pie chart
        const data = [{
        labels: labels,
        values: values,
        type: 'pie',
        marker: {
            colors: ['#FF5733', '#33FF57', '#3380FF'] 
        }
    }];
    
    // Set layout for the pie chart
    const layout = {
        title: 'Device Types',
        showlegend: true // Display legend
    };
    
    // Render the Plotly pie chart
    Plotly.newPlot('DeviceChart', data, layout);
    })
.catch(function(error) {
 console.error('Error fetching subscription data:', error);
 // Handle error gracefully, e.g., display error message to the user
});  
}
let allChart;
// Populate chart for stacked bar chart on page load
document.addEventListener('DOMContentLoaded', function() {
    d3.json("/api/allcountries/allsubscriptions").then(function(allsubs) {
        console.log(allsubs)
       // Extract relevant data
       // maps through allsubs to extract an array of country names
       const countries=allsubs.map(item=>item.Country);
       // determines subscripotion types by filtering out the Country key from the first object in allsubs
       const subTypes=Object.keys(allsubs[0]).filter(key=>key!=='Country');
       console.log(countries)

    // Create traces for each subscription type
    const traces = subTypes.map(subType => {
        return {
            x: countries,
            y: allsubs.map(item => item[subType]),
            name: subType,
            type: 'bar'
        };
    });
    // Define the layout
    const layout = {
        barmode: 'stack',
        xaxis: { title: 'Country' },
        yaxis: { title: 'Number of Subscriptions', range: [0, 250] }
    };
    // Plot the chart
    Plotly.newPlot('AllSubChart', traces, layout);
})
});

let myBarChart;
// Function to handle dropdown change
function additionalDropdownChanged(subscription) {
    // Use the selected country to fetch subscription types data
    console.log(subscription)
    d3.json(`/api/country/${subscription}`).then(function(countryData) {
       // Parse the JSON string into an object
       const countrydata = JSON.parse(countryData.countrysubs);
       console.log(countrydata)
       // Extract Labels and Values from the JSON object
       const labels = Object.keys(countrydata);
       const values = Object.values(countrydata);
        console.log(labels)
        console.log(values)
       // Create data object for Plotly bar chart
       const data = [{
        x: labels,
        y: values,
        type: 'bar',
        marker: {
            color:'rgb(255, 165, 0)',
            opacity: 0.6,
            line: {
              color: 'rgb(8,48,107)', 
              width: 1.5
            }}
    }];
    
    const layout = {
        title: 'Number of Subscriptions for Chosen Plan by Country',
        xaxis: {
          title: 'Country',
          tickmode: 'linear'
        },
        yaxis: {
          title: 'Number of Plan Members',
          range:[0,225]
        },
        bargap: 0.05 // Gap between bars
      };
      
      Plotly.newPlot('CountryChart', data, layout);
})

}



