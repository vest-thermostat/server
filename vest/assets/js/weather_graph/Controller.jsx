import React from 'react';
import { ButtonGroup, Button } from 'react-bootstrap';

export default class Container extends React.Component {
    render () {
        return (
            <ButtonGroup>
                <Button>
                    <span className="glyphicon glyphicon-leaf" aria-hidden="true">
                        Eco
                    </span>
                </Button>
                <Button>
                    <span className="glyphicon glyphicon-home" aria-hidden="true">
                        Standard
                    </span>
                </Button>
                <Button>
                    <span className="glyphicon glyphicon-fire" aria-hidden="true">
                        Hot
                    </span>
                </Button>
                <Button>
                    <span className="glyphicon glyphicon-bed" aria-hidden="true">
                        Night
                    </span>
                </Button>
            </ButtonGroup>
        );
    }
}
