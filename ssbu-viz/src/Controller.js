import React, { Component } from 'react';
import Viz from './Viz.js';
import * as d3 from 'd3';
import smashData from './data/smash.csv';

export default class Controller extends Component {
  constructor(props) {
    super(props);

    this.state = {
  	  color: "",
  	  width: "",
  	  toDraw: [],
      data: []
  	}

    this.parseData = this.parseData.bind(this)
  }



  componentDidMount() {
    let data = this.parseData(smashData)
  }

  parseData = (data) => {
    let parsedData = d3.csv(data, function(data) {
      return data
    });
    console.log(parsedData);
  }


  onSubmit = (evt) => {
  	evt.preventDefault();
  	const newShape = {
  	   color: this.state.color,
  	   width: this.state.width,
  	}
    this.setState({ toDraw: [...this.state.toDraw, newShape]})
  }

  onChange = (evt) => {
  	this.setState({[evt.target.name]: evt.target.value})
  }

  render() {
    return(
      <div className="controller">
        <form onSubmit={this.onSubmit}>
        <label htmlFor="colorSelect">pick a color:</label>
        <select id="colorSelect" name="color" onChange={this.onChange} value={this.state.color||"default"}>
          <option disabled value="default">choose</option>
          <option value="red">red</option>
          <option value="orange">orange</option>
          <option value="yellow">yellow</option>
        </select>
        <label htmlFor="pixelInput">how big:</label>
        <input id="pixelInput" name="width" onChange={this.onChange} />
        <button type="submit">draw!</button>
        </form>
        { this.state.toDraw.length ? <Viz shapes={this.state.toDraw}/> : null}
      </div>

    )
  }
}
