const React = require('react');
const ReactDOM = require('react-dom');
import LocationMap from './LocationMap.jsx';

window.locationMap = (datas) => {
    ReactDOM.render(
        <LocationMap locations={datas}/>, 
        document.getElementById('react-location-map')
    );
}
