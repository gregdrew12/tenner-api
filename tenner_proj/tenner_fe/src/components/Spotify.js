import React, { Fragment, useState } from "react";
import { Button } from "reactstrap";

function Spotify() {

  const [isAuth, setIsAuth] = useState(false)

  const authenticateSpotify = () => {
    fetch("http://localhost:8000/spotify/is-authenticated")
        .then((response) => response.json())
        .then((data) => {
            setIsAuth(data.status);
            if (!data.status) {
            fetch("http://localhost:8000/spotify/get-auth-url")
                .then((response) => response.json())
                .then((data) => {
                    console.log('fdsfd')
                    window.location.replace(data.url);
                });
            }
        });
    };

  return (
    <Fragment>
        <br/>
      <Button
        color="primary"
        className="float-right"
        onClick={authenticateSpotify}
        style={{ minWidth: "200px" }}
      >
        Spotify
      </Button>
      {isAuth ? <h1>hi</h1>: <h1>bad</h1>}
    </Fragment>
  );
}

export default Spotify;