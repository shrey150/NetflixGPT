import React from 'react';
import { createRoot } from 'react-dom/client';
import './Popup.css';
import Popup from './Popup';
import { Auth0Provider } from '@auth0/auth0-react';
// import { FirebaseAppProvider, FirestoreProvider, useFirebaseApp } from 'reactfire';
// import { getFirestore } from 'firebase/firestore';

const container = document.getElementById('app-container');
const root = createRoot(container!); // createRoot(container!) if you use TypeScript

const App = () => {
    return (
        <Popup />
    )
}

root.render(
    <Auth0Provider
    domain="{process.env.REACT_APP_AUTH0_DOMAIN}"
    clientId="{process.env.REACT_APP_AUTH0_CLIENT_ID}"
    authorizationParams={{
      redirect_uri:'https://kpifcefnbjlgambbiedokmiplacoidpa.chromiumapp.org/auth0'
    }}
  >
        <App />
    </Auth0Provider>
);
