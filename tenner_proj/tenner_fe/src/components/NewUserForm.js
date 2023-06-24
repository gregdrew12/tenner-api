import React, { useState, useEffect } from "react";
import { Button, Form, FormGroup, Input, Label } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

function NewUserForm(props) {
  
  const [user, setUser] = useState({'pk': 0, 'email': '', 'password': ''});

  useEffect(() => {
    if (props.user) {
      setUser({'pk': props.user.pk, 'email': props.user.email, 'password': props.user.password})
    }
  }, []);

  const onChange = e => {
    setUser(values => ({...values, [e.target.name]: e.target.value}))
  }

  const createUser = e => {
    e.preventDefault();
    axios.post(API_URL, user).then(() => {
      props.resetState();
      props.toggle();
    });
  }

  const editUser = e => {
    e.preventDefault();
    axios.put(API_URL + user.pk, user).then(() => {
      props.resetState();
      props.toggle();
    });
  };

  const defaultIfEmpty = value => {
    return value === "" ? "" : value;
  };

  return (
    <Form onSubmit={props.user ? editUser : createUser}>
      <FormGroup>
        <Label for="email">Email:</Label>
        <Input
          type="text"
          name="email"
          onChange={onChange}
          value={defaultIfEmpty(user.email)}
        />
      </FormGroup>
      <FormGroup>
        <Label for="password">Password:</Label>
        <Input
          type="text"
          name="password"
          onChange={onChange}
          value={defaultIfEmpty(user.password)}
        />
      </FormGroup>
      <Button>Send</Button>
    </Form>
  );
}

export default NewUserForm;