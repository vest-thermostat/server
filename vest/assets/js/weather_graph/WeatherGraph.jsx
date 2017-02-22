const React = require('react');
import { 
    Charts, 
    ChartContainer, 
    ChartRow, 
    YAxis,
    LineChart, 
    styler,
} from 'react-timeseries-charts';
import {
    TimeSeries, 
    TimeRange, 
} from 'pondjs';

// require("./WeatherGraph.scss");

export default class WeatherGraph extends React.Component {
    static propTypes: {
        datas: React.PropTypes.array.isRequired,
    }

    // constructor(props) {
    //     super(props);

    //     this.state = {
    //         datas: sorted,
    //     }
    // }

    render () {
        const style = styler([
            {key: "temp", color: "orange"},
            {key: "humidity", color: "blue"},
        ]);

        const mainStyle = {
            display: 'flex',
            flex_direction: 'column',
            justify: 'center',
            align_items: 'center',
            height: '100%',
        };

        const d = this.props.datas;
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
                <ChartContainer className="row" timeRange={timeRange}>
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
            </div>
        );
    }
}
