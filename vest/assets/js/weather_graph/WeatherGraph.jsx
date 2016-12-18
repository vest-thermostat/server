const React = require('react');
const Charts = require("react-timeseries-charts").Charts;
const ChartContainer = require("react-timeseries-charts").ChartContainer;
const ChartRow = require("react-timeseries-charts").ChartRow;
const YAxis = require("react-timeseries-charts").YAxis;
const LineChart = require("react-timeseries-charts").LineChart;
const TimeSeries = require("pondjs").TimeSeries;
const TimeRange = require("pondjs").TimeRange;
const styler = require("react-timeseries-charts").styler;

class WeatherGraph extends React.Component {
    constructor(props) {
        super(props);

        const sorted = props.datas;
        sorted.sort((a, b) => {
            return (a.created - b.created);
        });

        this.state = {
            datas: sorted,
            times: sorted.map((x) => {return x.created}),
            temperatures: new TimeSeries({
                    name: "temperatures", 
                    columns: ["time", "temp"],
                    points: sorted.map((x) => {return [x.created, x.temperature]}),
            }),
            humidities: new TimeSeries({
                    name: "humidities", 
                    columns: ["time", "humidity"],
                    points: sorted.map((x) => {return [x.created, x.humidity]}),
            }),
        }
        this.state.begin = this.state.times[0];
        this.state.finish = this.state.times[sorted.length - 1];
    }

    render () {
        const style = styler([
            {key: "temp", color: "orange"},
            {key: "humidity", color: "blue"},
        ]);

        const timeRange = new TimeRange(this.state.begin, this.state.finish);
        return (
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
                            series={this.state.temperatures}
                            columns={["temp"]}
                        />
                        <LineChart
                            axis="humidity"
                            style={style}
                            series={this.state.humidities}
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
        );
    }
}

WeatherGraph.propTypes = {
    datas: React.PropTypes.array.isRequired,
}

module.exports.WeatherGraph = WeatherGraph;
