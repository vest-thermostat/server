import React, { PropTypes } from 'react';
import { Map, Marker, Popup, TileLayer, GeoJSON } from 'react-leaflet';
import L from 'leaflet';
import cookie from 'react-cookie';
import axios from 'axios';
import RoutingMachine from './RoutingMap.jsx';

import './LocationMap.scss';

export default class LocationMap extends React.Component {
    constructor (props) {
        super(props);

        let c = [50.81438, 4.38223];

        this.state = {
            current: c,
            locations: props.locations.features,
        };

        this.addLocation = this.addLocation.bind(this);
    }

    componentDidMount () {
        this.ws = new WebSocket('ws://' + location.host +  '/ws/location/');
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
        axios.post('/location/', {
            position: {
                type: "Point",
                coordinates: [pos.lng, pos.lat],
            } 
        }, {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': cookie.load('csrftoken'),
            },
        // }).then(json => {
        //     console.log(JSON.stringify(json))
        //     if (json.type && json.geometry) {
        //         let newLocations = this.state.locations.concat([json]);
        //         if (newLocations.length > 100) {
        //             newLocations.splice(0, 1);
        //         }
        //         this.setState({ locations: newLocations });
        //      }
        }).catch(e => {
            if (e.response)  {
                console.log(e.response.data);
            } else {
                console.log('Error ', e.message);
            }
        })
    }

    createGeoJson () {
        // console.log(JSON.stringify(this.state.locations));
        return {
            type:"FeatureCollection",
            features: this.state.locations,
        };
    }

    render () {
        return (
            <Map center={this.state.current} zoom={13} onClick={this.addLocation} ref='map'>
                <TileLayer
                    url='http://{s}.tile.osm.org/{z}/{x}/{y}.png'
                    attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                />
                <RoutingMachine locations={this.state.locations}/>
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
