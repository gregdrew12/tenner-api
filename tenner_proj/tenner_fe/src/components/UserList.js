import React, { Component } from "react";
import { Table } from "reactstrap";
import NewUserModal from "./NewUserModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

/*class UserList extends Component {*/
function UserList(props) {
  const users = props.users;
  return (
    <Table dark>
      <thead>
        <tr>
          <th>Username</th>
          <th>Password</th>
          <th>Registration</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        {!users || users.length <= 0 ? (
          <tr>
            <td colSpan="6" align="center">
              <b>Oops, no one here yet</b>
            </td>
          </tr>
        ) : (
          users.map(user => (
            <tr key={user.pk}>
              <td>{user.username}</td>
              <td>{user.password}</td>
              <td>{user.registrationDate}</td>
              <td align="center">
                <NewUserModal
                  create={false}
                  user={user}
                  resetState={props.resetState}
                />
                &nbsp;&nbsp;
                <ConfirmRemovalModal
                  pk={user.pk}
                  resetState={props.resetState}
                />
              </td>
            </tr>
          ))
        )}
      </tbody>
    </Table>
  );
}

export default UserList;