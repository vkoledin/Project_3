let myMap = L.map("map", {
    center: [45.52, -122.67],
    zoom: 13
  });

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(myMap);

let countryMarkers = [];

for (let i = 0; i < countries.length; i++) {
  
  countryMarkers.push(
    L.marker(country[i].location).bindPopup("<h1>" + country[i].name + "</h1>")
  );
}

  
  
  
  L.circle(countries[i].location, {
    fillOpacity: 0.75,
    color: "white",
    fillColor: '#F0F8FF'
    weight :2
   
  }).addTo(myMap);



  THIS ONE IS NOT DONE 
  THIS ONE IS NOT DONE 
  THIS ONE IS NOT DONE 
  THIS ONE IS NOT DONE 
  THIS ONE IS NOT DONE 