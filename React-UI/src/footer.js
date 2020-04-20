import React, { Component } from "react";
import "./App.css";
import { MDBCol, MDBContainer, MDBRow, MDBFooter } from "mdbreact";
class Footer extends Component {
render(){
  return (
    <MDBFooter color="white" className="font-small pt-4 mt-4">      
      <div className="footer-copyright text-center py-3">
        <MDBContainer fluid>
          <h5 class="text-uppercase font-weight-bold">A movie search engine</h5>  
          &copy; {new Date().getFullYear()} Copyright: <a href="https://www.mdbootstrap.com"> cinephile.com </a>
        </MDBContainer>
      </div>
    </MDBFooter>
  );
}
}
export default Footer;