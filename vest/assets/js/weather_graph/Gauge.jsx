import React from 'react';
const Gauge = require("react-svg-gauge");

export default class TemperatureGauge extends React.Component {
    static propTypes: {
        data: React.PropTypes.object.isRequired,
    }

    render () {
        return (
            <div className="row">
                <div className="col-md-6">
                    <Gauge className="gauge"
                        value={this.props.data.temperature} 
                        min={-10} max={70} 
                        width={220} height={200} 
                        color="orange" label="Temperature"
                        valueLabelStyle={{textAnchor: "middle", fontSize: '22px', opacity: 0.5}}
                    />
                </div>
                <div className="col-md-6">
                    <Gauge className="gauge"
                        value={this.props.data.humidity} 
                        width={220} height={200} 
                        color="blue" label="Humidity" 
                        valueLabelStyle={{textAnchor: "middle", fontSize: '44px', opacity: 0.5}}
                    />
                </div>
            </div>
        );
    }
}