import React, { Fragment, useState } from "react";
import { Button } from "reactstrap";
import axios from "axios";

function Spotify() {

  const [isAuth, setIsAuth] = useState(false)
  const [song, setSong] = useState([])

  const authenticateSpotify = () => {
    axios.get("http://localhost:8000/spotify/is-authenticated", {
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
      params: {
        email: localStorage.getItem('email')
      }
    })
        .then(res => {
            setIsAuth(res.data['status']);
            if (!res.data['status']) {
            axios.get("http://localhost:8000/spotify/get-auth-url", {
              headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
              },
              params: {
                email: localStorage.getItem('email')
              } 
            })
                .then(res => {
                  //window.location.replace(res.data['url']);
                  window.open(res.data['url'],'callBackWindow','height=500,width=400');
                  window.addEventListener("storage",function(event){
                    if (event.key == "spotify_token"){
                      var spotifyToken = event.newValue;
                      console.log(spotifyToken);
                      //do things with spotify API using your access token here!!
                    }
                  });
                });
            }
        });
    };

    const getCurrentSong = () => {
      fetch("http://localhost:8000/spotify/current-song")
        .then((response) => {
          if (!response.ok) {
            return {};
          } else {
            return response.json();
          }
        })
        .then((data) => {
          setSong(data);
          console.log(data);
        });
    }

  return (
    <Fragment>
      <br/>
      <Button
        color="primary"
        className="float-right"
        onClick={authenticateSpotify}
        style={{ minWidth: "200px" }}
      >
        Link Spotify Account
      </Button>
      {localStorage.getItem('spotify_token')}
      <br/>
      <Button
        color="green"
        className="float-right"
        onClick={getCurrentSong}
        style={{ minWidth: "200px" }}
      >
        Current Song
      </Button>
      <h1>
        {song['title']}
      </h1>
    </Fragment>
  );
}

export default Spotify;