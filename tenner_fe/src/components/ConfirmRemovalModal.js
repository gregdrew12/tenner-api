import React, { Fragment, useState} from "react";
import { Modal, ModalHeader, Button, ModalFooter } from "reactstrap";

import axios from "axios";

import { API_URL } from "../constants";

function ConfirmRemovalModal(props) {
  const [modal, setModal] = useState(false);

  const toggle = () => {
    setModal(!modal);
  };

  const deleteUser = id => {
    axios.delete(API_URL + id).then(() => {
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
            onClick={() => deleteUser(props.id)}
          >
            Yes
          </Button>
        </ModalFooter>
      </Modal>
    </Fragment>
  );
}

export default ConfirmRemovalModal;