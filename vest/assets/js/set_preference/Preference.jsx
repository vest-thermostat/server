import React, { PropTypes } from 'react';
import { Grid, Row, Col, Button } from 'react-bootstrap';
import { ContextMenu, MenuItem, ContextMenuTrigger, SubMenu } from "react-contextmenu";
import './react-contextmenu.css'

import Slider from 'rc-slider';
const createSliderWithTooltip = Slider.createSliderWithTooltip;
const Range = createSliderWithTooltip(Slider.Range);
import 'rc-slider/assets/index.css';

import moment from 'moment'

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

const MAX = 1440;

export default class Preference extends React.Component {
  static propTypes: {
    datas: React.PropTypes.array  
  }

  static defaultProps: {
      datas: [],
  }

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

  fillHoles (values) {
    let result = [];

    for (let i = 0; i < values.length; ++i) {
      result.push(values[i][0]);
      if (!values[i + 1]) {
        result.push(values[i][1]);
      } else if (values[i][1] != values[i + 1][0]) {
        result.push(values[i][1]);
      }
    }

    return result;
  }

  createTimeMapping (datas) {
    const values = datas.map(x => {
      const from = new moment(x.start, 'HH:mm:ss');
      const to = new moment(x.finish, 'HH:mm:ss');
      return [from.hour() * 60 + from.minute(), to.hour() * 60 + to.minute()];
    });

    

    if (values.length) {
      // Set midnight to max value instead of zero.
      if (values[values.length - 1][1] == 0) {
        values[values.length - 1][1] = MAX;
      }

      // Set a new value if no value from midnight
      if (values[0][0] != 0) {
        values.splice(0, 0, [0, values[0][0]]) 
      }

      // Set a new value if no value until midnight
      if (values[values.length - 1][1] != MAX) {
        values.splice(values.length - 1, 0, [values[values.length - 1][1], MAX]) 
      }

      return values;
    }

    return [[0, MAX]];
  }

  renderRange (dayDatas) {
    const values = this.createTimeMapping(dayDatas);

    const range = this.fillHoles(values);

    return (
      <Range
        min={0}
        max={MAX}
        step={10}
        allowCross={true}
        count={range.length}
        defaultValue={range}
        handle={handle}
      />
    )
  }

  renderByDay (day, context) {
    return (
      <div>
        <Row>
          <Col md={2}>
            {day}
          </Col>
          <Col md={10}>
            <ContextMenuTrigger>
              {this.renderRange(context.data)}
            </ContextMenuTrigger>
          </Col>
        </Row>
        <hr/>
      </div>
    );
  }

  render () {
    return (
      <Grid>
        {this.props.datas.map(x => this.renderByDay(x.day, x))}
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
