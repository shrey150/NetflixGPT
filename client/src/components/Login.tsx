import { GoogleLogin } from 'react-google-login';
import React from 'react';

const clientId =
  '482785177008-2gvmb96n2m5p1rgj6dv40aiedaespb4b.apps.googleusercontent.com';

export const Login = () => {
  const onSuccess = (res: any) => {
    console.log('Success! Current User: ', res.profileObj);
  };

  const onFailure = (res: any) => {
    console.log('Failure! res: ', res);
  };

  return (
    <div id="signIn">
      <GoogleLogin
        clientId={clientId}
        buttonText="Login"
        onSuccess={onSuccess}
        onFailure={onFailure}
        cookiePolicy={'single_host_origin'}
        isSignedIn={true}
      ></GoogleLogin>
    </div>
  );
};
