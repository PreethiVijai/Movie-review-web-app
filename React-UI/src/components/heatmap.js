import React, { Component } from "react";
import "./App.css";
import USAMap from "react-usa-map";

class App extends Component {
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
      <div className="App">
        <h1>react-usa-map</h1>
        <USAMap
          customize={this.statesFilling()}
          onClick={this.mapHandler}
        />
        <p>
          More information:{" "}
          <a href="http://github.com/gabidavila/react-usa-map">GitHub</a>
        </p>
      </div>
    );
  }
}

export default App;
