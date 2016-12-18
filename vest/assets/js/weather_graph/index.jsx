const React = require('react');
const ReactDOM = require('react-dom');
const WeatherGraph = require('./WeatherGraph.jsx').WeatherGraph;

const datas = [
    {
        created: "2016-12-18T02:55:28.945048Z",
        temperature: 20.095,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:55:26.687672Z",
        temperature: 20.148,
        humidity: 38.0,
    },

    {
        created: "2016-12-18T02:55:24.433997Z",
        temperature: 20.174,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:55:22.146420Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:55:19.887072Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:55:17.626203Z",
        temperature: 20.095,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:55:15.365122Z",
        temperature: 22.348,
        humidity: 38.0,
    },

    {
        created: "2016-12-18T02:55:13.104100Z",
        temperature: 20.095,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:55:10.790899Z",
        temperature: 20.148,
        humidity: 38.0,
    },

    {
        created: "2016-12-18T02:55:07.457170Z",
        temperature: 20.121,
        humidity: 37.0,
    },

    {
        created: "2016-12-18T02:55:05.200300Z",
        temperature: 20.2,
        humidity: 40.0,
    },

    {
        created: "2016-12-18T02:55:02.939288Z",
        temperature: 24.469,
        humidity: 35.0,
    },

    {
        created: "2016-12-18T02:55:00.668613Z",
        temperature: 20.2,
        humidity: 40.0,
    },

    {
        created: "2016-12-18T02:54:58.408132Z",
        temperature: 22.4,
        humidity: 40.0,
    },

    {
        created: "2016-12-18T02:54:56.138080Z",
        temperature: 20.174,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:54:50.303476Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:54:46.942883Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:54:44.687358Z",
        temperature: 20.252,
        humidity: 42.0,
    },

    {
        created: "2016-12-18T02:54:42.433139Z",
        temperature: 20.2,
        humidity: 40.0,
    },

    {
        created: "2016-12-18T02:54:40.164737Z",
        temperature: 20.226,
        humidity: 41.0,
    },

    {
        created: "2016-12-18T02:54:37.901603Z",
        temperature: 22.4,
        humidity: 40.0,
    },

    {
        created: "2016-12-18T02:54:35.645485Z",
        temperature: 20.095,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:54:33.364235Z",
        temperature: 20.095,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:54:31.111333Z",
        temperature: 23.395,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:54:28.854197Z",
        temperature: 22.295,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:54:26.587458Z",
        temperature: 20.252,
        humidity: 42.0,
    },

    {
        created: "2016-12-18T02:54:24.332856Z",
        temperature: 21.3,
        humidity: 40.0,
    },

    {
        created: "2016-12-18T02:54:22.086821Z",
        temperature: 21.326,
        humidity: 41.0,
    },

    {
        created: "2016-12-18T02:54:19.776834Z",
        temperature: 20.174,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:54:17.525669Z",
        temperature: 20.095,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:54:15.247528Z",
        temperature: 20.095,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:54:12.986207Z",
        temperature: 20.095,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:54:10.700953Z",
        temperature: 21.3,
        humidity: 40.0,
    },

    {
        created: "2016-12-18T02:54:08.420420Z",
        temperature: 21.3,
        humidity: 40.0,
    },

    {
        created: "2016-12-18T02:54:06.159599Z",
        temperature: 21.248,
        humidity: 38.0,
    },

    {
        created: "2016-12-18T02:54:03.902716Z",
        temperature: 22.348,
        humidity: 38.0,
    },

    {
        created: "2016-12-18T02:54:01.639826Z",
        temperature: 24.469,
        humidity: 35.0,
    },

    {
        created: "2016-12-18T02:53:59.358173Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:57.098845Z",
        temperature: 23.369,
        humidity: 35.0,
    },

    {
        created: "2016-12-18T02:53:54.841519Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:52.589320Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:50.324092Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:47.873833Z",
        temperature: 20.095,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:45.445061Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:42.970668Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:40.709145Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:38.451449Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:36.177232Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:33.925213Z",
        temperature: 21.274,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:53:31.668922Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:29.341138Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:27.087679Z",
        temperature: 21.3,
        humidity: 40.0,
    },

    {
        created: "2016-12-18T02:53:24.824998Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:22.562692Z",
        temperature: 21.3,
        humidity: 40.0,
    },

    {
        created: "2016-12-18T02:53:20.306138Z",
        temperature: 21.274,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:53:18.033020Z",
        temperature: 21.221,
        humidity: 37.0,
    },

    {
        created: "2016-12-18T02:53:15.771583Z",
        temperature: 21.3,
        humidity: 40.0,
    },

    {
        created: "2016-12-18T02:53:13.504952Z",
        temperature: 20.095,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:11.233595Z",
        temperature: 21.274,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:53:08.964185Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:06.706707Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:04.451343Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:53:02.198244Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:52:59.945973Z",
        temperature: 22.374,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:52:57.680516Z",
        temperature: 21.221,
        humidity: 37.0,
    },

    {
        created: "2016-12-18T02:52:55.389570Z",
        temperature: 20.095,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:52:53.130038Z",
        temperature: 21.274,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:52:50.867049Z",
        temperature: 21.274,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:52:48.574435Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:52:46.305191Z",
        temperature: 20.174,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:52:44.054975Z",
        temperature: 20.148,
        humidity: 38.0,
    },

    {
        created: "2016-12-18T02:52:41.760479Z",
        temperature: 20.095,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:52:39.504984Z",
        temperature: 21.274,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:52:37.245693Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:52:33.953379Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:52:31.684580Z",
        temperature: 20.174,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:52:29.421443Z",
        temperature: 21.3,
        humidity: 40.0,
    },

    {
        created: "2016-12-18T02:52:27.128146Z",
        temperature: 21.3,
        humidity: 40.0,
    },

    {
        created: "2016-12-18T02:52:24.882366Z",
        temperature: 21.326,
        humidity: 41.0,
    },

    {
        created: "2016-12-18T02:52:22.631297Z",
        temperature: 21.274,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:52:20.379001Z",
        temperature: 21.248,
        humidity: 38.0,
    },

    {
        created: "2016-12-18T02:52:18.121007Z",
        temperature: 25.674,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:52:15.827582Z",
        temperature: 21.274,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:52:13.573893Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:52:11.283188Z",
        temperature: 22.4,
        humidity: 40.0,
    },

    {
        created: "2016-12-18T02:52:09.019711Z",
        temperature: 20.095,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:52:06.735438Z",
        temperature: 21.248,
        humidity: 38.0,
    },

    {
        created: "2016-12-18T02:52:03.462842Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:52:00.158749Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:51:57.905038Z",
        temperature: 20.174,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:51:55.645282Z",
        temperature: 22.452,
        humidity: 42.0,
    },

    {
        created: "2016-12-18T02:51:53.355889Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:51:47.733875Z",
        temperature: 22.348,
        humidity: 38.0,
    },

    {
        created: "2016-12-18T02:51:44.978480Z",
        temperature: 21.248,
        humidity: 38.0,
    },

    {
        created: "2016-12-18T02:51:42.623626Z",
        temperature: 23.474,
        humidity: 39.0,
    },

    {
        created: "2016-12-18T02:51:40.370205Z",
        temperature: 21.3,
        humidity: 40.0,
    },

    {
        created: "2016-12-18T02:51:38.075760Z",
        temperature: 21.195,
        humidity: 36.0,
    },

    {
        created: "2016-12-18T02:51:35.803621Z",
        temperature: 21.195,
        humidity: 36.0,
    },
    {
        created: "2016-12-18T02:51:33.544160Z",
        temperature: 21.3,
        humidity: 40.0,
    },

    {
        created: "2016-12-18T02:51:31.283050Z",
        temperature: 20.174,
        humidity: 39.0,
    },
]

window.weatherGraph = (datas) => {
// $(document).ready(function () {
    ReactDOM.render(
        <WeatherGraph datas={datas}/>, 
        document.getElementById('react-weather-graph')
    );
// });
}
