import React, { Component, useState, useEffect } from "react";
import { Col, Container, Row } from "reactstrap";
import UserList from "./UserList";
import NewUserModal from "./NewUserModal";

import axios from "axios";

import { API_URL } from "../constants";

/*class Home extends Component*/
function Home() {

  /*state = {
    users: []
  };*/
  const [users, setUsers] = useState([]);

  /*componentDidMount() {
    this.resetState();
  }*/
  useEffect(() => {
    resetState();
  }, []);

  /*getUsers = () => {
    axios.get(API_URL).then(res => this.setState({ users: res.data }));
  };*/
  const getUsers = () => {
    axios.get(API_URL).then(res => setUsers(res.data));
  };

  /*resetState = () => {
    this.getUsers();
  };*/
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
    </Container>
  );
}

export default Home;