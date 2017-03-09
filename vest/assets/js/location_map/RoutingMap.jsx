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
        locations: PropTypes.array,
    }

    static defaultProps: {
        locations: [],
    }

    componentWillMount () {
        super.componentWillMount()
    }


    createLeafletElement (props) {
        const { map } = props;
        return Leaflet.Routing.control({
            position: 'topleft',
            waypoints: [
                Leaflet.latLng([50.81438, 4.38223]),
                Leaflet.latLng(57.6792, 11.949),
            ],//this.props.locations.map(x => Leaflet.latLng(x)),
            show: false,
        }).addTo(map);
    }

    render () {
        return null;
    }
}


