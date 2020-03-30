import React, { Component } from "react";
import "./counter.css";
import logo from "./cine.png";
import search from "./searchicon.jpg";
import Autosuggest from "react-autosuggest";

const languages = [
  {
    name: "C",
    year: 1972
  },
  {
    name: "Elm",
    year: 2012
  }
];
const getSuggestions = value => {
  const inputValue = value.trim().toLowerCase();
  const inputLength = inputValue.length;

  return inputLength === 0
    ? []
    : languages.filter(
        lang => lang.name.toLowerCase().slice(0, inputLength) === inputValue
      );
};
const getSuggestionValue = suggestion => suggestion.name;
const renderSuggestion = suggestion => (
  <div>
    <span>{suggestion.name}</span>
  </div>
);

class Counter extends Component {
  constructor() {
    super();
    this.state = {
      value: "",
      suggestions: []
    };
  }

  onChange = (event, { newValue }) => {
    this.setState({
      value: newValue
    });
  };

  onSuggestionsFetchRequested = ({ value }) => {
    this.setState({
      suggestions: getSuggestions(value)
    });
  };

  onSuggestionsClearRequested = () => {
    this.setState({
      suggestions: []
    });
  };
  render() {
    let videoid = "vi2308751129";
    let link = `https://www.imdb.com/videoembed/${videoid}`;
    const { value, suggestions } = this.state;
    const inputProps = {
      placeholder: " Enter movie name",
      value,
      onChange: this.onChange
    };
    const renderInputComponent = inputProps => (
      <div className="inputContainer">
        <img
          className="icon"
          src="https://img.icons8.com/ios-filled/50/000000/search.png"
          width="20px"
          height="20px"
        />
        <input {...inputProps} />
      </div>
    );

    function myFunction() {
      console.log("Hello!");
    }
    function sayHello() {
      alert("Hello 123!");
    }
    return (
      <div id="page">
        <div class="header">
          <span class="logoheader">
            <img
              alt=""
              src={logo}
              width="50"
              height="50"
              backgroundColor="transparent"
            />
            <text>CINEPHILE</text>
          </span>
          <Autosuggest
            suggestions={suggestions}
            onSuggestionsFetchRequested={this.onSuggestionsFetchRequested}
            onSuggestionsClearRequested={this.onSuggestionsClearRequested}
            getSuggestionValue={getSuggestionValue}
            renderSuggestion={renderSuggestion}
            inputProps={inputProps}
            renderInputComponent={renderInputComponent}
          />
        </div>
        {/* header div ends here */}
        <div id="all_details">
          <div id="moviereview">
            <div id="trailer" style={{ backgroundColor: "#cde" }}>
              <iframe
                src={link}
                width="550"
                height="260"
                allowfullscreen="true"
                mozallowfullscreen="true"
                webkitallowfullscreen="true"
                frameborder="no"
                scrolling="no"
              ></iframe>
            </div>
            <div id="tomatometer" style={{ backgroundColor: "#abc" }}>
              Tomatometer here
            </div>
            <div id="cast" style={{ backgroundColor: "#cdc" }}>
              Cast details
            </div>
          </div>
          <div id="twitterfeed">
            <div id="news">NEWS</div>
            <div id="feed"> Twitter Feed</div>
          </div>

          <div id="screen_location">
            <div id="location">LOCATION</div>
            <div id="maps"> Maps</div>
          </div>
        </div>
      </div>
    );
  }
}

export default Counter;
