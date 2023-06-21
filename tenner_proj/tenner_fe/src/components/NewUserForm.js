import React, { useState, useEffect } from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

/* class NewUserForm extends React.Component { */
function NewUserForm(props) {
  
  /* state = {
    pk: 0,
    name: "",
    email: "",
    phone: ""
  }; */
  const [user, setUser] = useState({'pk': 0, 'name': '', 'email': '', 'phone': ''});

  /* componentDidMount() {
    if (this.props.user) {
      const { pk, name, email, phone } = this.props.user;
      this.setState({ pk, name, email, phone });
    }
  } */
  useEffect(() => {
    if (props.user) {
      setUser({'pk': props.user.pk, 'name': props.user.name, 'email': props.user.email, 'phone': props.user.phone})
    }
  }, []);

  /* onChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  }; */
  const onChange = e => {
    setUser(values => ({...values, [e.target.name]: e.target.value}))
  }

  /* createUser = e => {
    e.preventDefault();
    axios.post(API_URL, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  }; */
  const createUser = e => {
    e.preventDefault();
    axios.post(API_URL, user).then(() => {
      props.resetState();
      props.toggle();
    });
  }

  /* editUser = e => {
    e.preventDefault();
    axios.put(API_URL + this.state.pk, this.state).then(() => {
      this.props.resetState();
      this.props.toggle();
    });
  }; */
  const editUser = e => {
    e.preventDefault();
    axios.put(API_URL + user.pk, user).then(() => {
      props.resetState();
      props.toggle();
    });
  };

  /* defaultIfEmpty = value => {
    return value === "" ? "" : value;
  }; */
  const defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  return (
    <Form onSubmit={props.user ? editUser : createUser}>
      <FormGroup>
        <Label for="name">Name:</Label>
        <Input
          type="text"
          name="name"
          onChange={onChange}
          value={defaultIfEmpty(user.name)}
        />
      </FormGroup>
      <FormGroup>
        <Label for="email">Email:</Label>
        <Input
          type="email"
          name="email"
          onChange={onChange}
          value={defaultIfEmpty(user.email)}
        />
      </FormGroup>
      <FormGroup>
        <Label for="phone">Phone:</Label>
        <Input
          type="text"
          name="phone"
          onChange={onChange}
          value={defaultIfEmpty(user.phone)}
        />
      </FormGroup>
      <Button>Send</Button>
    </Form>
  );
}

export default NewUserForm;