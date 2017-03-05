import React from 'react';
import { Grid, Row, Col, ButtonGroup, Button, Panel } from 'react-bootstrap';
import Gauge from "react-svg-gauge";
import Center from 'react-center';

export default class Container extends React.Component {
    static propTypes: {
        current: React.PropTypes.integer.isRequired,
    }

    static defaultProps: {
        current: 20,
    }

    constructor (props) {
        super(props);

        this.state = {
            custom: false,
        }

        this.handleClick.bind(this);
    }

    toggleCustom (e) {
        this.setState({ custom: !this.state.custom });
    }

    handleClick (e) {
    
    }

    render () {
        return (
            <div>
                <Center>
                    <Panel>
                        <Gauge 
                            className="gauge"
                            value={this.props.current} 
                            min={-10} max={70} 
                            color="orange" label="Temperature"
                            width={220} height={200} 
                            valueLabelStyle={{textAnchor: "middle", fontSize: '22px', opacity: 0.5}}
                        />                    
                    </Panel>
                </Center>
                <Center>
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
                        <Button onClick={this.toggleCustom}>
                            <span className="glyphicon glyphicon-cog" aria-hidden="true"></span>
                        </Button>
                    </ButtonGroup>
                </Center>
            </div>
        );
    }
}
