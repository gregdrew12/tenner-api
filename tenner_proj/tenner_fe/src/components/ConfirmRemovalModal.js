import React, { Component, Fragment, useState, useRef, useEffect } from "react";
import { Modal, ModalHeader, Button, ModalFooter } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

/* class ConfirmRemovalModal extends Component { */
function ConfirmRemovalModal(props) {
  /* state = {
    modal: false
  }; */
  const [modal, setModal] = useState(false);

  /* toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  }; */
  const toggle = () => {
    setModal(!modal);
  };

  /* deleteUser = pk => {
    axios.delete(API_URL + pk).then(() => {
      this.props.resetState();
      this.toggle();
    });
  }; */
  const deleteUser = pk => {
    console.log(props);
    axios.delete(API_URL + pk).then(() => {
      props.resetState();
      toggle();
    });
  }

  return (
    <Fragment>
      <Button color="danger" onClick={() => toggle()}>
        Remove
      </Button>
      <Modal isOpen={modal} toggle={toggle}>
        <ModalHeader toggle={toggle}>
          Do you really wanna delete the user?
        </ModalHeader>

        <ModalFooter>
          <Button type="button" onClick={() => toggle()}>
            Cancel
          </Button>
          <Button
            type="button"
            color="primary"
            onClick={() => deleteUser(props.pk)}
          >
            Yes
          </Button>
        </ModalFooter>
      </Modal>
    </Fragment>
  );
}

export default ConfirmRemovalModal;