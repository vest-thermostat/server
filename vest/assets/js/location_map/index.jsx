const React = require('react');
const ReactDOM = require('react-dom');
import LocationMap from './LocationMap.jsx';

// import L from 'leaflet';
// import 'leaflet-routing-machine';

// window.locationMap = (datas) => {
    // var map = L.map('react-location-map');

    // L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}{r}.png', {
    //     attribution: '© OpenStreetMap contributors'
    // }).addTo(map);

    // L.Routing.control({
    //     waypoints: [
    //         L.latLng(57.74, 11.94),
    //         L.latLng(57.6792, 11.949)
    //     ],
    //     routeWhileDragging: true
    // }).addTo(map);
// }


window.locationMap = (datas) => {
    ReactDOM.render(
        <LocationMap locations={datas}/>, 
        document.getElementById('react-location-map')
    );
}
