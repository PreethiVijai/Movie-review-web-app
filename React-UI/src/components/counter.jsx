import React, { Component } from "react";
import "./counter.css";
import logo from "./cine.png";
import netflix_icon from "./netflix.png";
import itunes_icon from "./itunes.png";
import hulu_icon from "./hulu-icon.png";
import vudu_icon from "./vudu.png";
import Autosuggest from "react-autosuggest";
import axios from "axios";
import { debounce } from "throttle-debounce";
import { CircularProgressbar, buildStyles } from "react-circular-progressbar";
import { easeQuadInOut } from "d3-ease";
import "react-circular-progressbar/dist/styles.css";

// Animation
import AnimatedProgressProvider from "../AnimatedProgressProvider";

class Counter extends Component {
  state = {
    value: "",
    suggestions: [],
    cacheAPISugestions: [],
    isOpen: false,
    valueEnd: "0",
    avgvalueEnd: "0",
    genreitems: ["List Item 1", "List Item 2", "List Item 3"],
    castitems: ["item1", "item2", "item3", "item4", "item5"]
  };

  SUGGEST_URL = "http://34.82.210.3:8080/suggest";

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
    let plotval = "";
    let movie_image = "";
    let rating = "0";
    let language = "English";
    let year = "2020";
    let runtime = "1880";
    let avgsentiment = "0";
    /* Initialize all hrefs */
    let fandango_href = "http://www.fandangonow.com";
    let netflix_href = "http://www.netflix.com";
    let itunes_href = "http://www.itunes.com";
    let hulu_href = "http://www.hulu.com";
    let vudu_href = "http://www.vudu.com";

    /*To show disable icons*/
    let nset = false,
      iset = false,
      hset = false,
      vset = false,
      fset = false;
    const value = this.state.value;
    const suggestions = this.state.suggestions;
    if (this.state.filterResults != null) {
      var results = this.state.filterResults[0];
      var stringname = (results.name + " (" + results.year + ")").toUpperCase();
      document.getElementById("moviename").textContent = stringname;
      videoid = results.trailer;
      link = `https://www.imdb.com/videoembed/${videoid}`;
      document.getElementById("iframeid").src = link;

      plotval = results.plot;
      document.getElementById("plot_Val").textContent = plotval;

      movie_image = results.imageurl;
      document.getElementById("mv_img").src = movie_image;

      console.log(results);

      rating = results.rating;
      this.state.valueEnd = rating;

      if (results.avgsentiment != null) {
        avgsentiment = results.avgsentiment;
        this.state.avgvalueEnd = avgsentiment;
      }

      language = results.language;
      document.getElementById("lang_span").textContent = language;

      year = results.year;
      document.getElementById("year_span").textContent = year;

      runtime = results.runtime;
      document.getElementById("runtime_span").textContent = runtime;

      if (results.genreList != null) {
        for (i in results.genreList) {
          this.state.genreitems[i] = results.genreList[i];
        }
      }

      if (results.cast != null) {
        for (i in results.cast) {
          this.state.castitems[i] = results.cast[i];
        }
      }

      if (results.watchList != null) {
        function setIcons(href_id, idName, href) {
          document.getElementById(href_id).href = href;
          document.getElementById(href_id).title = href;
          document.getElementById(idName).classList.add("ishover");
          document.getElementById(idName).style.opacity = "1.0";
          document.getElementById(idName).style.cursor = "pointer";
        }
        for (var i in results.watchList) {
          var href = results.watchList[i];
          if (href.includes("netflix")) {
            nset = true;
            setIcons("netflix_watchlink", "netflix", href);
          } else if (href.includes("hulu")) {
            hset = true;
            setIcons("hulu_watchlink", "hulu", href);
          } else if (href.includes("vudu")) {
            vset = true;
            setIcons("vudu_watchlink", "vudu", href);
          } else if (href.includes("itunes")) {
            iset = true;
            setIcons("itunes_watchlink", "itunes", href);
          } else if (href.includes("fandango")) {
            fset = true;
            setIcons("fandango_watchlink", "fandango", href);
          }
        }
        function changeIcons(watchlink, idName) {
          document.getElementById(watchlink).href = "#";
          document.getElementById(watchlink).title =
            "This movie is not available on netflix";
          document.getElementById(idName).style.opacity = "0.3";
          document.getElementById(idName).style.cursor = "default";
          document.getElementById(idName).classList.remove("ishover");
        }
        if (nset == false) {
          changeIcons("netflix_watchlink", "netflix");
        }
        if (hset == false) {
          changeIcons("hulu_watchlink", "hulu");
        }
        if (vset == false) {
          changeIcons("vudu_watchlink", "vudu");
        }
        if (fset == false) {
          changeIcons("fandango_watchlink", "fandango");
        }
        if (iset == false) {
          changeIcons("itunes_watchlink", "itunes");
        }
      }
    }

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
        <div id="moviename"></div>

        <div id="all_details">
          <div id="row1">
            <div id="row1_part1">
              <div id="movie_image">
                <img
                  id="mv_img"
                  src="https://lajoyalink.com/wp-content/uploads/2018/03/Movie.jpg"
                  width="250px"
                  height="300px"
                />
              </div>
            </div>
            <div id="cast_names">
              CAST:
              <span id="cast_span">
                <ul>
                  {this.state.castitems.map(listitem => (
                    <li className="list_group_item">{listitem}</li>
                  ))}
                </ul>
              </span>
            </div>
            <div id="where_to_watch">
              <div id="netflix_hulu_vudu">
                <div id="netflix_div">
                  <a
                    href={netflix_href}
                    target="_blank"
                    title={netflix_href}
                    id="netflix_watchlink"
                  >
                    <img
                      id="netflix"
                      src={netflix_icon}
                      width="100px"
                      height="100px"
                      opacity="1.0"
                    />
                  </a>
                </div>
                <div id="hulu_div">
                  <a
                    href={hulu_href}
                    target="_blank"
                    title={hulu_href}
                    id="hulu_watchlink"
                  >
                    <img
                      id="hulu"
                      src={hulu_icon}
                      width="100px"
                      height="100px"
                      opacity="1.0"
                    />
                  </a>
                </div>
                <div id="vudu_div">
                  <a
                    href={vudu_href}
                    target="_blank"
                    title={vudu_href}
                    id="vudu_watchlink"
                  >
                    <img
                      id="vudu"
                      src={vudu_icon}
                      width="100px"
                      height="100px"
                      opacity="1.0"
                    />
                  </a>
                </div>
              </div>
              <div id="itunes_fandango">
                <div id="itunes_div">
                  <a
                    href={itunes_href}
                    target="_blank"
                    title={itunes_href}
                    id="itunes_watchlink"
                  >
                    <img
                      id="itunes"
                      src={itunes_icon}
                      width="100px"
                      height="100px"
                      opacity="1.0"
                    />
                  </a>
                </div>
                <div id="fandango_div">
                  <a
                    href={fandango_href}
                    target="_blank"
                    title={fandango_href}
                    id="fandango_watchlink"
                    opacity="1.0"
                  >
                    <img
                      id="fandango"
                      src="https://img04.mgo-images.com/image/static/content/web/logos/fandango-now.png"
                      width="270px"
                      height="90px"
                    />
                  </a>
                </div>
              </div>
            </div>
            <div id="plot">
              PLOT:
              <div id="plot_Val">{plotval}</div>
            </div>
          </div>
          <div id="row2">
            <iframe
              id="iframeid"
              src={link}
              width="570"
              height="280"
              allowfullscreen="true"
              mozallowfullscreen="true"
              webkitallowfullscreen="true"
              frameborder="no"
              scrolling="no"
            ></iframe>
            <div id="other_details">
              <div id="mv_language">
                LANGUAGE: <span id="lang_span">{language}</span>
              </div>
              <div id="mv_year">
                RELEASE YEAR: <span id="year_span">{year}</span>
              </div>
              <div id="mv_runtime">
                RUNTIME: <span id="runtime_span">{runtime}</span>
              </div>
              <div id="mv_genre">
                GENRE:
                <span id="genre_span">
                  <ul>
                    {this.state.genreitems.map(listitem => (
                      <li className="list_group_item">{listitem}</li>
                    ))}
                  </ul>
                </span>
              </div>
            </div>
            <div id="imdb_rating">
              IMDB Rating:
              <AnimatedProgressProvider
                valueStart={0}
                valueEnd={this.state.valueEnd}
                duration={1.4}
                easingFunction={easeQuadInOut}
              >
                {value => {
                  value = value * 10;
                  const roundedValue = Math.round(value);
                  return (
                    <CircularProgressbar
                      value={value}
                      text={`${roundedValue / 10}`}
                      /* This is important to include, because if you're fully managing the
        animation yourself, you'll want to disable the CSS animation. */
                      styles={buildStyles({ pathTransition: "none" })}
                    />
                  );
                }}
              </AnimatedProgressProvider>
            </div>
            <div id="twitter_rating">
              Twitter Rating:
              <AnimatedProgressProvider
                valueStart={0}
                valueEnd={this.state.avgvalueEnd}
                duration={1.4}
                easingFunction={easeQuadInOut}
              >
                {value => {
                  value = value * 100;
                  const roundedValue = Math.round(value);
                  return (
                    <CircularProgressbar
                      value={value}
                      text={`${roundedValue / 100}`}
                      /* This is important to include, because if you're fully managing the
        animation yourself, you'll want to disable the CSS animation. */
                      styles={buildStyles({ pathTransition: "none" })}
                    />
                  );
                }}
              </AnimatedProgressProvider>
            </div>
          </div>

          <div id="row3">
            <div id="reviews">REVIEW:</div>
            <div id="heatmap">HEATMAP:</div>
          </div>
        </div>
      </div>
    );
  }
}

export default Counter;
