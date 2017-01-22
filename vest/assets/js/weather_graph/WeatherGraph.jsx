const React = require('react');
const Charts = require("react-timeseries-charts").Charts;
const ChartContainer = require("react-timeseries-charts").ChartContainer;
const ChartRow = require("react-timeseries-charts").ChartRow;
const YAxis = require("react-timeseries-charts").YAxis;
const LineChart = require("react-timeseries-charts").LineChart;
const TimeSeries = require("pondjs").TimeSeries;
const TimeRange = require("pondjs").TimeRange;
const styler = require("react-timeseries-charts").styler;
const Gauge = require("react-svg-gauge");
const Websocket = require("react-websocket");

// require("./WeatherGraph.scss");

class WeatherGraph extends React.Component {
    constructor(props) {
        super(props);

        const sorted = props.datas;
        sorted.sort((a, b) => {
            return (a.created - b.created);
        });

        this.state = {
            datas: sorted,
        }
    }

    _getLast(key) {
        return this.state.datas[this.state.datas.length - 1][key];
    }

    newWeatherData(data) {
        const result = JSON.parse(data);
        console.log(result);
        if (result.created && result.temperature && result.humidity) {
            result.created = Date.parse(result.created);
            let newDatas = this.state.datas.concat([result]);
            newDatas.splice(0, 1);
            this.setState({
                datas: newDatas
            });
        }
    }

    render () {
        const style = styler([
            {key: "temp", color: "orange"},
            {key: "humidity", color: "blue"},
        ]);

        const d = this.state.datas;

        console.log(d);

        const times = d.map((x) => {return x.created});
        const temperatures = new TimeSeries({
                name: "temperatures", 
                columns: ["time", "temp"],
                points: d.map((x) => {return [x.created, x.temperature]}),
        });
        const humidities = new TimeSeries({
                name: "humidities", 
                columns: ["time", "humidity"],
                points: d.map((x) => {return [x.created, x.humidity]}),
        });

        const begin = times[0];
        const finish = times[d.length - 1];

        const timeRange = new TimeRange(begin, finish);
        return (
            <div>
                <ChartContainer timeRange={timeRange}>
                    <ChartRow height="150">
                        <YAxis 
                            id="temp"
                            label="Temperature (°C)" 
                            style={style.axisStyle("temp")}
                            labelOffset={-5} 
                            min={-5} max={40} type="linear"
                            format=",.1f"
                        />
                        <Charts>
                            <LineChart
                                axis="temp"
                                style={style}
                                series={temperatures}
                                columns={["temp"]}
                            />
                            <LineChart
                                axis="humidity"
                                style={style}
                                series={humidities}
                                columns={["humidity"]}
                            />
                        </Charts>
                        <YAxis 
                            id="humidity" 
                            label="Humidity (%)" 
                            style={style.axisStyle("humidity")}
                            labelOffset={5} 
                            min={0} max={100} 
                            type="linear" 
                            format=",.1f"/>
                    </ChartRow>
                </ChartContainer>
                <div className="row">
                    <div className="col-md-6">
                        <Gauge className="gauge"
                            value={this._getLast("temperature")} 
                            min={-10} max={70} 
                            width={220} height={200} 
                            color="orange" label="Temperature"
                            valueLabelStyle={{textAnchor: "middle", fontSize: '22px', opacity: 0.5}}
                        />
                    </div>
                    <div className="col-md-6">
                        <Gauge className="gauge"
                            value={this._getLast("humidity")} 
                            width={220} height={200} 
                            color="blue" label="Humidity" 
                            valueLabelStyle={{textAnchor: "middle", fontSize: '44px', opacity: 0.5}}
                        />
                    </div>
                </div>
                <Websocket url='ws://127.0.0.1:8000/' onMessage={this.newWeatherData.bind(this)}/>
            </div>
        );
    }
}

WeatherGraph.propTypes = {
    datas: React.PropTypes.array.isRequired,
}

module.exports.WeatherGraph = WeatherGraph;
