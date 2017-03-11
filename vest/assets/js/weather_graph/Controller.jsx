import React from 'react';
import cookie from 'react-cookie';
import axios from 'axios';
import { ButtonGroup, Button, Panel } from 'react-bootstrap';
import Gauge from "react-svg-gauge";
import Center from 'react-center';

export default class Container extends React.Component {
    static propTypes: {
        current: React.PropTypes.integer.isRequired,
    }

    // static defaultProps: {
    //     current: 20,
    // }

    constructor (props) {
        super(props);

        this.state = {
            custom: false,
            current: props.current,
        }

        this.handleClick = this.handleClick.bind(this);
        this.toggleCustom = this.toggleCustom.bind(this);
        this.lowerTemperature = this.lowerTemperature.bind(this);
        this.raiseTemperature = this.raiseTemperature.bind(this);
    }

    componentWillReceiveProps (nextProps) {
        if (nextProps.current) {
            this.setState({ current: nextProps.current });
        }
    }

    toggleCustom (e) {
        const result = !this.state.custom;
        this.setState({ custom: result });
    }

    handleClick (e) {
    
    }

    send (tmp) {
        console.log(tmp);
        const self = this;
        axios.post('/weather/set/', {
            temperature: tmp,
        }, {
            headers: {
                'X-CSRFToken': cookie.load('csrftoken'),
            },
        }).then(response => {
            self.setState({ current: tmp })
        }).catch(e => {
            if (e.response) {
                console.log(e.response.data);
            } else {
                console.log('Error ', e.message);
            }
        });
    }

    lowerTemperature () {
        this.send(this.state.current - 0.5);
    }

    raiseTemperature () {
        this.send(this.state.current + 0.5);
    }

    renderCustomSettings () {
        return [
            (<Button onClick={this.lowerTemperature}> 
                <span className="glyphicon glyphicon-minus" aria-hidden="true">
                </span>
            </Button>),
            (<Button onClick={this.raiseTemperature}> 
                <span className="glyphicon glyphicon-plus" aria-hidden="true">
                </span>
            </Button>),
        ];
    }

    render () {
        return (
            <div>
                <Center>
                    <Panel>
                        <Gauge 
                            className="gauge"
                            value={this.state.current} 
                            min={-10} max={70} 
                            color="orange" label="Temperature définie"
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
                        {this.state.custom ? this.renderCustomSettings() : null}
                        <Button onClick={this.toggleCustom}>
                            <span className="glyphicon glyphicon-cog" aria-hidden="true"></span>
                        </Button>
                    </ButtonGroup>
                </Center>
            </div>
        );
    }
}
