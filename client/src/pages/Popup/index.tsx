import React from 'react';
import { createRoot } from 'react-dom/client';
import './Popup.css';
import Popup from './Popup';
// import { FirebaseAppProvider, FirestoreProvider, useFirebaseApp } from 'reactfire';
// import { getFirestore } from 'firebase/firestore';

const container = document.getElementById('app-container');
const root = createRoot(container!); // createRoot(container!) if you use TypeScript

const App = () => {
    // const firestoreInstance = getFirestore(useFirebaseApp());
    return (
        // <FirestoreProvider sdk={firestoreInstance}>
            <Popup />
        // </FirestoreProvider>
    )
}

root.render(
    // <FirebaseAppProvider firebaseConfig={JSON.parse(process.env.FIREBASE_CONFIG ?? '')}>
        <App />
    // </FirebaseAppProvider>
);
