const React = require('react');
const ReactDOM = require('react-dom');
import Preference from './Preference.jsx';

window.preferenceSelection = (datas) => {
    ReactDOM.render(
        <Preference datas={datas}/>, 
        document.getElementById('react-preference-selection')
    );
}
