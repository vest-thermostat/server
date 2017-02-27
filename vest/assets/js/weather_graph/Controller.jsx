import React from 'react';
import { ButtonGroup, Button } from 'react-bootstrap';
import Gauge from "react-svg-gauge";

export default class Container extends React.Component {
    static propTypes: {
        current: React.PropTypes.integer.isRequired,
    }

    static propTypes: {
        current: 20,
    }

    constructor (props) {
        super(props);

        this.hadnelClick.bind(this);
    }

    handleClick (e) {
    
    }

    render () {
        return (
            <Panel header={"Controller la temperature du thermostat VEST."}>
                <Center>
                    <Gauge 
                        className="gauge"
                        value={this.props.current} 
                        min={10} max={50} 
                        color="orange" label="Temperature"
                        width={220} height={200} 
                        valueLabelStyle={{textAnchor: "middle", fontSize: '22px', opacity: 0.5}}
                    />                    
                    <ButtonGroup>
                        <Button onClick={this.handleClick}>
                            <span className="glyphicon glyphicon-leaf" aria-hidden="true">
                                Eco
                            </span>
                        </Button>
                        <Button onClick={this.handleClick}>
                            <span className="glyphicon glyphicon-home" aria-hidden="true">
                                Standard
                            </span>
                        </Button>
                        <Button onClick={this.handleClick}>
                            <span className="glyphicon glyphicon-fire" aria-hidden="true">
                                Hot
                            </span>
                        </Button>
                        <Button onClick={this.handleClick}>
                            <span className="glyphicon glyphicon-bed" aria-hidden="true">
                                Night
                            </span>
                        </Button>
                    </ButtonGroup>
                </Center>
            </Panel>
        );
    }
}
