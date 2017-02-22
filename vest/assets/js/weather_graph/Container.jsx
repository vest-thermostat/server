import React from 'react';
import WeatherGraph from './WeatherGraph.jsx';
import TemperatureGauge from './Gauge.jsx';

export default class Container extends React.Component {
    static propTypes: {
        weathers: React.PropTypes.array.isRequired,
    }

    constructor(props) {
        super(props);

        const sorted = props.weathers;
        props.weathers.sort((a, b) => {
            return (a.created - b.created);
        });

        this.state = {
            errors: [],
            weathers: sorted,
        };
    }

    componentDidMount () {
        this.ws = new WebSocket('ws://127.0.0.1:8000/')
        this.ws.onmessage = e => {
            const json = JSON.parse(e.data);
            json.created = Date.parse(json.created);
            let newWeathers = this.state.weathers.concat([json]);
            if (this.state.weathers.length < 100) {
                newWeathers.splice(0, 1);
            }
            this.setState({ weathers: newWeathers })
        };
        this.ws.onerror = e => this.setState({ error: ['WebSocket error'] })
        this.ws.onclose = e => !e.wasClean && this.setState({ error: [`WebSocket error: ${e.code} ${e.reason}`] })
    }

    render_errors () {
        if (this.state.errors.length) {
            return this.state.errors.map(x => (
                <div className="alert alert-danger" role="alert">
                    <span className="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                    <span className="sr-only">Erreur:</span>
                    {x}
                </div>
            ));
        }
        return null;
    }

    render () {
        const mainStyle = {
            display: 'flex',
            flex_direction: 'column',
            justify: 'center',
            align_items: 'center',
            height: '100%',
        };

        return (
            <div style={mainStyle} className="container main-container">
                {this.render_errors()}
                <WeatherGraph datas={this.state.weathers}/>
                <TemperatureGauge data={this.state.weathers.length ? this.state.weathers[this.state.weathers.length - 1] : []}/>
            </div>
        );
    }
}
