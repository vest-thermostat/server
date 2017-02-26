import React, { PropTypes } from 'react';
import { MapLayer } from 'react-leaflet';
import Leaflet from 'leaflet';
// import Routing from 'leaflet-routing-machine';
import 'leaflet-routing-machine';
import './RoutingMap.scss';


export default class RoutingMachine extends MapLayer {
    componentWillMount () {
        super.componentWillMount();

        const {map} = this.props;
        // this.leafletElement = this.createLeafletElement();
        // this.leafletElement = L.Routing.control({
        //     position: 'topleft',
        //     waypoints: this.props.locations.map(x => L.latLng(x)),
        //     show: false,
        // }).addTo(map);
        // this.leafletElement.on('routesfound', (e) => {
        // });
    }

    createLeafletElement() {
        const { map } = this.props;
        this.leafletElement = L.Routing.control({
            position: 'topleft',
            waypoints: [Leaflet.latLng([50.81438, 4.38223]),],//this.props.locations.map(x => Leaflet.latLng(x)),
            show: false,
        }).addTo(map);
        console.log(this.leafletElement);
        return this.leafletElement;
    }

    render () {
        return null;
    }
}

RoutingMachine.propTypes = {
    locations: PropTypes.array,
};

RoutingMachine.defaultProps = {
    locations: [],
}


