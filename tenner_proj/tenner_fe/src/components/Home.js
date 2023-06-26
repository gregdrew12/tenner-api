import React, { useState, useEffect } from "react";
import { Col, Container, Row } from "reactstrap";
import UserList from "./UserList";
import NewUserModal from "./NewUserModal";

import axios from "axios";

import { API_URL } from "../constants";
import Spotify from "./Spotify";

const Home = () => {

  const [users, setUsers] = useState([]);
  const [message, setMessage] = useState(''); 

  useEffect(() => {
    resetState();
    if(localStorage.getItem('access_token') === null){                   
      window.location.href = '/login'
    }
    else{
      (async () => {
        try {
          const {data} = await axios.get('http://localhost:8000/home/', {
          headers: {
            'Content-Type': 'application/json'
          }
        });

          setMessage(data.message);
        } catch (e) {
          console.log('not auth')
        }
      })()
    };
  }, []);

  const getUsers = () => {
    axios.get(API_URL).then(res => setUsers(res.data));
  };

  const resetState = () => {
    getUsers();
  };

  return (
    <Container style={{ marginTop: "20px" }}>
      <Row>
        <Col>
          <UserList
            users={users}
            resetState={resetState}
          />
        </Col>
      </Row>
      <Row>
        <Col>
          <NewUserModal create={true} resetState={resetState} />
        </Col>
      </Row>
      <Row>
        <Col>
          <Spotify/>
        </Col>
      </Row>
    </Container>
  );
}

export default Home;