import React, { Component } from "react";
import "./counter.css";
import logo from "./cinephile1.png";
class Counter extends Component {
  render() {
    let videoid = "vi2308751129";
    let link = `https://www.imdb.com/videoembed/${videoid}`;
    return (
      <div id="page">
        <div class="header">
          <img alt="" src={logo} width="60" height="60" /> <h1>CINEPHILE</h1>{" "}
          <div class="searchbar">
            <input
              type="text"
              id="myInput"
              onkeyup="myFunction()"
              placeholder=" Enter movie Name here"
            ></input>
            <button class="gosearch">GO</button>
          </div>{" "}
          {/* search bar div ends here */}
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
