import React, { PropTypes } from 'react';
import { Grid, Row, Col, Button } from 'react-bootstrap';
import { ContextMenu, MenuItem, ContextMenuTrigger, SubMenu } from "react-contextmenu";
import './react-contextmenu.css'

import Slider from 'rc-slider';
const createSliderWithTooltip = Slider.createSliderWithTooltip;
const Range = createSliderWithTooltip(Slider.Range);
import 'rc-slider/assets/index.css';

const Handle = Slider.Handle;

const handle = (props) => {
  const { value, dragging, index } = props;
  return (
    <Tooltip
      overlay={value}
      visible={dragging}
      placement="top"
      key={index}
    />
  );
};

export default class Preference extends React.Component {
  constructor (props) {
    super(props);
  }


  handleAdd (e) {
  }

  handleDelete (e) {
  
  }

  setEco (e) {
  
  }

  setStandard (e) {
  
  }

  setHot (e) {
  
  }

  setNight (e) {
  
  }

  renderByDay (day) {
    return (
      <div>
        <Row>
          <Col md={2}>
            {day}
          </Col>
          <Col md={10}>
            <ContextMenuTrigger>
              <Range
                min={0}
                max={1439}
                step={10}
                handle={handle}
              />
            </ContextMenuTrigger>
          </Col>
        </Row>
        <hr/>
      </div>
    );
  }

  renderByWeek () {
    const self = this;
    return [
      'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'
    ].map(x => self.renderByDay(x));
  }

  render () {
    return (
      <Grid>
        {this.renderByWeek()}
        <ContextMenu>
          <MenuItem onClick={this.handleAdd}>
            Ajouter
          </MenuItem>
          <MenuItem onClick={this.handleDelete}>
            Supprimer
          </MenuItem>
          <SubMenu title={"Type"}>
            <MenuItem onClick={this.setEco}>
              Eco
            </MenuItem>
            <MenuItem onClick={this.setStandard}>
              Standard
            </MenuItem>
            <MenuItem onClick={this.setHot}>
              Chaud
            </MenuItem>
            <MenuItem onClick={this.setNight}>
              Nuit
            </MenuItem>
          </SubMenu>
        </ContextMenu>
      </Grid>
    );
  }
}

Preference.propTypes = {
    data: PropTypes.array,
};

Preference.defaultProps = {
    data: [],
};
