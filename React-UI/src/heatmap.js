import React, { Component } from "react";
import "./App.css";
import USAMap from "react-usa-map";

class USAmap extends Component {
  mapHandler = (event) => {
    alert(event.target.dataset.name);
  };

  statesFilling = (stateNames) => {
    const stateName1 = "navy";
    return {
      CO: {
        fill: stateName1,
      },
    };
  };

  render() {
    return (
      <div className="Usamap">
        <USAMap customize={this.statesFilling()} onClick={this.mapHandler} />
      </div>
    );
  }
}

export default USAmap;
