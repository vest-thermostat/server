import React, { PropTypes } from 'react';
import { OrderedSet } from 'immutable';
import { NotificationStack } from 'react-notification';
import { Map, Marker, Popup, TileLayer } from 'react-leaflet';
import L from 'leaflet';
import cookie from 'react-cookie';
import axios from 'axios';
import RoutingMachine from './RoutingMap.jsx';

import './LocationMap.scss';

const MAX_SIZE = 20;

export default class LocationMap extends React.Component {
    constructor (props) {
        super(props);

        let c = [50.81438, 4.38223];

        let locs = this.props.locations.features;
        if (locs && locs.length > MAX_SIZE) {
            locs = locs.slice(0, MAX_SIZE);
        }

        this.state = {
            current: c,
            notifications: OrderedSet(),
            count: 0,
            nests: [],
            locations: locs
        };

        this.addLocation = this.addLocation.bind(this);
    }

    componentDidMount () {
        this.ws = new WebSocket('ws://' + location.host +  '/ws/location/');
        this.ws.onmessage = e => {
            const json = JSON.parse(e.data) ;
            if (json.type && json.geometry) {
                let newLocations = this.state.locations
                newLocations.splice(0, 0, json);
                
                if (newLocations.length > MAX_SIZE) {
                    newLocations.splice(newLocations.length - 1, 1);
                }
                this.setState({ locations: newLocations });
            } else if (json.type == 'notification' && json.message) {
                const { notifictions, count } = this.state;
                const newCount = count + 1;
                return this.setState({
                    count: newCount,
                    notifications: notifications.add({
                        message: json.message,
                        key: newCount,
                        action: 'Dismiss',
                        dismissAfter: 3400,
                        onClick: () => this.removeNotification(newCount),
                    })
                }); 
            } else if (json.type == 'nest') {
            
            }
         };
         this.ws.onerror = e => this.setState({ error: ['WebSocket error'] })
         this.ws.onclose = e => !e.wasClean && this.setState({ error: [`WebSocket error: ${e.code} ${e.reason}`] })
    }

    removeNotification (count) {
        const { notifications } = this.state;
        this.setState({
            notifications: notifications.filter(n => n.key !== count)
        })
    }

    addLocation (e) {
        const pos = e.latlng;
        if (!pos) {
            return;
        }
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
        //         if (newLocations.length > MAX_SIZE) {
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

    renderMarkers () {
        return this.state.locations.map(x => {
            const coord = x.geometry.coordinates;
            return (
                <Marker position={[coord[1], coord[0]]}/>
            );
        })
    }

    render () {
        // <RoutingMachine locations={this.state.locations}/>
        return (
            <div>
                <Map center={this.state.current} zoom={13} onClick={this.addLocation} ref='map'>
                    <TileLayer
                        url='http://{s}.tile.osm.org/{z}/{x}/{y}.png'
                        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                    />
                    {this.renderMarkers ()}
                </Map>
                <NotificationStack
                    notifications={this.state.notifications.toArray()}
                    onDismiss={notification => this.setState({
                        notifications: this.state.notifications.delete(notification)
                    })}
                />
            </div>
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
