import React from "react";
import { Table } from "reactstrap";
import NewUserModal from "./NewUserModal";

import ConfirmRemovalModal from "./ConfirmRemovalModal";

function UserList(props) {
  const users = props.users;
  return (
    <Table dark>
      <thead>
        <tr>
          <th>Email</th>
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
            <tr key={user.id}>
              <td>{user.email}</td>
              <td>{user.date_joined.slice(0, 10)}</td>
              <td align="center">
                <NewUserModal
                  create={false}
                  user={user}
                  resetState={props.resetState}
                />
                &nbsp;&nbsp;
                <ConfirmRemovalModal
                  id={user.id}
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