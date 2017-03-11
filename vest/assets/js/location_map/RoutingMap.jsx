import React, { PropTypes } from 'react';
import { MapLayer } from 'react-leaflet';
import Leaflet from 'leaflet';
import 'leaflet-routing-machine';
import './RoutingMap.scss';


export default class RoutingMachine extends MapLayer {
    // static contextTypes: {
    //     map: PropTypes.instanceOf(Leaflet.Map),
    // }

    static propTypes: {
        locations: PropTypes.array.isRequired,
    }

    static defaultProps: {
        locations: [],
    }


    constructor (props) {
        super(props);
    
        this.state = {
            locations: props.locations,        
        }
    }

    componentWillReceiveProps (nextProps) {
        if (nextProps.locations) {
            this.setState({ locations: nextProps.locations });
        }
    }

    componentWillMount () {
        super.componentWillMount()
    }

    createLatLng () {
        return this.props.locations.map(x => {
            const coord = x.geometry.coordinates;
            return Leaflet.latLng(coord[1], coord[0]);
        });
    }

    createLeafletElement (props) {
        const { map } = props;
        return Leaflet.Routing.control({
            position: 'topleft',
            waypoints: this.createLatLng(),
            show: false,
        }).addTo(map);
    }

    updateLeafletElement (fromProps, toProps) {
        const { map } = toProps;
        return Leaflet.Routing.control({
            position: 'topleft',
            waypoints: this.createLatLng(),
            show: false,
        }).addTo(map);
    }

    render () {
        return null;
    }
}
