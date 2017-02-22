import React from 'react';
import ReactDOM from 'react-dom';
import Container from './Container.jsx';

window.weatherGraph = (datas) => {
// $(document).ready(function () {
    ReactDOM.render(
        <Container weathers={datas}/>, 
        document.getElementById('react-weather-graph')
    );
// });
}
