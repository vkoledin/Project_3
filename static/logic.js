

//Use d3 to fetch the Json data
d3.json("countries.json").then(countries => {
    //Initialize the map 
    let myMap = L.map("map", {
        center: [20, 0],
        zoom: 2
    });

    //Adding the tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
         attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(myMap);

    
    //The heatMap data
      let heatData = countries.map(country => [
          country.location[0],
          country.location[1],
          country.Netflix_users
      ]);

    //Add the heatmap layer
    L.heatLayer(heatData, {
        radius: 25,
        blur: 15,
        maxZoom: 10,
      }).addTo(myMap);

});