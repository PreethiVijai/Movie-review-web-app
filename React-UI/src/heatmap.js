import React, { Component } from "react";
import "./App.css";
import USAMap from "react-usa-map";
class USAmap extends Component {
  stateNames = [];
  results = {};
  mapHandler = (event) => {
    alert(event.target.dataset.name);
  };

  componentDidMount() {
    const stateName1 = "navy";
    this.stateNames = this.props.stateNames;
    this.results = {};
    console.log(this.stateNames);
    if (this.stateNames.length > 0) {
      var i;
      for (i = 0; i < this.stateNames.length; i++) {
        this.results[this.stateNames[i]] = { fill: stateName1 };
      }
    }
    return this.results;
  }

  render() {
    return (
      <div className="Usamap">
        <USAMap
          customize={this.componentDidMount()}
          onClick={this.mapHandler}
        />
      </div>
    );
  }
}
export default USAmap;
