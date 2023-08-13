import { GoogleLogout } from 'react-google-login';
import React from 'react';

const clientId =
  '482785177008-2gvmb96n2m5p1rgj6dv40aiedaespb4b.apps.googleusercontent.com';

export const Logout = () => {
  const onSuccess = () => {
    console.log('Succesfully logged out!');
  };

  return (
    <div id="signOut">
      <GoogleLogout
        clientId={clientId}
        buttonText="Logout"
        onLogoutSuccess={onSuccess}
      ></GoogleLogout>
    </div>
  );
};
