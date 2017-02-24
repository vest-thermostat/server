import React from 'react';
import { Panel, Alert, Grid } from 'react-bootstrap';
import Center from 'react-center';
import WeatherGraph from './WeatherGraph.jsx';
import TemperatureGauge from './Gauge.jsx';
import Controller from './Controller.jsx';

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
        this.ws = new WebSocket('ws://127.0.0.1:8000/weather')
        this.ws.onmessage = e => {
            const json = JSON.parse(e.data);
            if (json.created && json.temperature && json.humidity) {
                json.created = Date.parse(json.created);
                let newWeathers = this.state.weathers.concat([json]);
                if (this.state.weathers.length < 100) {
                    newWeathers.splice(0, 1);
                }
                this.setState({ weathers: newWeathers })
            }
        };
        this.ws.onerror = e => this.setState({ error: ['WebSocket error'] })
        this.ws.onclose = e => !e.wasClean && this.setState({ error: [`WebSocket error: ${e.code} ${e.reason}`] })
    }

    render_errors () {
        if (this.state.errors.length) {
            return this.state.errors.map(x => (
                <Alert bsStyle="danger">
                    <span className="glyphicon glyphicon-exclamation-sign" aria-hidden="true"></span>
                    <span className="sr-only">Erreur:</span>
                    {x}
                </Alert>
            ));
        }
        return null;
    }

    render () {
        const flexStyle = {
            'display': 'flex',
            'flex-direction': 'column',
            'justify': 'center',
            'align-items': 'center',
            'height': '100%',
        };

        const flexRow = {
            'margin': 'auto',
            // '-webkit-flex': '1',
        }

        return (
            <Grid>
                {this.render_errors()}
                <Panel header={"Température du thermostat VEST."}>
                    <Panel>
                        <WeatherGraph style={flexStyle} datas={this.state.weathers}/>
                    </Panel>
                    <Center>
                        <TemperatureGauge style={flexStyle} data={this.state.weathers.length ? this.state.weathers[this.state.weathers.length - 1] : []}/>
                    </Center>
                    <Panel header={"Controller la temperature du thermostat VEST."}>
                        <Center>
                            <Controller/>
                        </Center>
                    </Panel>
                </Panel>
            </Grid>
        );
    }
}
