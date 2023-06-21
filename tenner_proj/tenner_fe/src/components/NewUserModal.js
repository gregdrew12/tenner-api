import React, { Component, Fragment, useState } from "react";
import { Button, Modal, ModalHeader, ModalBody } from "reactstrap";
import NewUserForm from "./NewUserForm";

/*class NewUserModal extends Component {*/
function NewUserModal(props) {

  /* state = {
    modal: false
  }; */
  const [modal, setModal] = useState(false)

  /* toggle = () => {
    this.setState(previous => ({
      modal: !previous.modal
    }));
  }; */
  const toggle = () => {
    setModal(!modal)
  };


  const create = props.create;

  var title = "Editing User";
  var button = <Button onClick={toggle}>Edit</Button>;
  if (create) {
    title = "Creating New User";

    button = (
      <Button
        color="primary"
        className="float-right"
        onClick={toggle}
        style={{ minWidth: "200px" }}
      >
        Create New
      </Button>
    );
  }

  return (
    <Fragment>
      {button}
      <Modal isOpen={modal} toggle={toggle}>
        <ModalHeader toggle={toggle}>{title}</ModalHeader>

        <ModalBody>
          <NewUserForm
            resetState={props.resetState}
            toggle={toggle}
            user={props.user}
          />
        </ModalBody>
      </Modal>
    </Fragment>
  );
}

export default NewUserModal;