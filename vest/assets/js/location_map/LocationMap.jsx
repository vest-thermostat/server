import React, { PropTypes } from 'react';
import { Map, Marker, Popup, TileLayer, GeoJSON } from 'react-leaflet';
// import RoutingMachine from './RoutingMap.jsx';
import L from 'leaflet';

import './LocationMap.scss';

export default class LocationMap extends React.Component {
    constructor (props) {
        super(props);

        // let currentLoc = props.currentPosition;
        // if (!currentLoc) {
        //     let latSum = 0;
        //     for (let i = 0; i < this.props.positions.length; ++i) {
        //          latSum += this.props.positions[0][i];
        //     }
        //     const avrgLat = latSum / this.props.postitions.length;

        //     let lngSum = 0;
        //     for (let i = 0; i < this.props.positions.length; ++i) {
        //          lngSum += this.props.positions[1][i];
        //     }
        //     const avrgLng = latSum / this.props.postitions.length;
        //     let currentLoc = [avrgLat, avrgLng];
        // }
        let c = [50.81438, 4.38223];

        this.state = {
            current: c,
            locations: props.locations.features,
        };

        this.addLocation = this.addLocation.bind(this);
    }

    componentDidMount () {
        this.ws = new WebSocket('ws://127.0.0.1:8000/location');
        this.ws.onmessage = e => {
            const json = JSON.parse(e.data) ;
            if (json.type && json.geometry) {
                let newLocations = this.state.locations.concat([json]);
                if (newLocations.length > 100) {
                    newLocations.splice(0, 1);
                }
                this.setState({ locations: newLocations });
             }
         };
         this.ws.onerror = e => this.setState({ error: ['WebSocket error'] })
         this.ws.onclose = e => !e.wasClean && this.setState({ error: [`WebSocket error: ${e.code} ${e.reason}`] })

    }

    addLocation (e) {
        const pos = e.latlng;
        this.ws.send(JSON.stringify({
            position: {
                type: "Point",
                coordinates: [pos.lng, pos.lat],
            } 
        }));
    }

    createGeoJson () {
        console.log(JSON.stringify(this.state.locations));
        return {
            type:"FeatureCollection",
            features: this.state.locations,
        };
    }

    render () {
                // <GeoJsonCluster data={this.createGeoJson()} />
                // <RoutingMachine locations={this.state.locations.map(x => x.geometry.coordinates)} />
        return (
            <Map center={this.state.current} zoom={13} onClick={this.addLocation} ref='map'>
                <TileLayer
                    url='http://{s}.tile.osm.org/{z}/{x}/{y}.png'
                    attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                />
                <GeoJSON data={this.createGeoJson()}/>
            </Map>
        );
    }
}

LocationMap.propTypes = {
    locations: PropTypes.object,
    currentPosition: PropTypes.object,
};

LocationMap.defaultProps = {
    locations: [],
};
