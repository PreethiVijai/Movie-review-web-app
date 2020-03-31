import React, { Component } from "react";
import "./counter.css";
import logo from "./cine.png";
import search from "./searchicon.jpg";
import Autosuggest from "react-autosuggest";
import axios from "axios";
import { debounce } from "throttle-debounce";

class Counter extends Component {
  state = {
    value: "",
    suggestions: [],
    cacheAPISugestions: [],
    isOpen: false
  };

  SUGGEST_URL = "http://localhost:8080/suggest";

  componentWillMount() {
    this.onSuggestionsFetchRequested = debounce(
      500,
      this.onSuggestionsFetchRequested
    );
  }

  renderSuggestion = suggestion => {
    return <span>{suggestion.name}</span>;
  };

  onChange = (event, { newValue }) => {
    this.setState({
      value: newValue
    });
  };
  componentDidMount() {
    axios.get(this.SUGGEST_URL, {}).then(res => {
      this.setState({ cacheAPISugestions: res.data });
    });
  }

  onSuggestionsFetchRequested = ({ value }) => {
    this.setState({
      suggestions: this.getSuggestions(this.state.cacheAPISugestions, value)
    });
  };

  onSuggestionsClearRequested = () => {
    this.setState({
      suggestions: []
    });
  };
  onSuggestionSelected = (event, { suggestionValue }) => {
    var filterRes = this.state.suggestions;
    filterRes = filterRes.filter(item => item.name == suggestionValue);
    if (filterRes != 0) {
      this.setState({
        filterResults: filterRes
      });
    } else {
      this.setState({
        filterResults: this.state.suggestions
      });
    }
  };
  getSuggestions = (moviesNames, searchValue) => {
    const inputValue = searchValue.trim().toLowerCase();
    const inputLength = inputValue.length;
    if (inputLength === 0) return [];
    else {
      var i;
      return moviesNames.filter(
        s =>
          s.name.toLowerCase().includes(inputValue) ||
          s.year.toLowerCase().includes(inputValue)
      );
    }
  };
  render() {
    let videoid = "vi2308751129";
    let link = `https://www.imdb.com/videoembed/${videoid}`;
    const value = this.state.value;
    const suggestions = this.state.suggestions;

    const inputProps = {
      placeholder: " Enter movie name or year",
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
            getSuggestionValue={suggestion => suggestion.name}
            renderSuggestion={this.renderSuggestion}
            onSuggestionSelected={this.onSuggestionSelected}
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
