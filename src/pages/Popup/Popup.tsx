import React from 'react';
import { doc, setDoc } from 'firebase/firestore';
import { useFirestore, useFirestoreDocData } from 'reactfire';
import { ChatBox } from './ChatBox';


const Popup = () => {
  const userRef = doc(useFirestore(), 'users/shrey');
  const { status, data } = useFirestoreDocData(userRef);

  const fetchAnswer = async (question: string) => {

    try {
      // Update the document with the desired data
      await setDoc(userRef, { question })

      console.log('Document written successfully!');
    } catch (error) {
      console.error('Error writing document:', error);
    }
  }

  return (
      <div>
        <p>🔥 Firebase status: {JSON.stringify(status)}</p>
        <p>🌴 PaLM status: {data?.status?.state}</p>
        <p>
          {
            data?.response ?? (
              data?.status
                ? 'Processing...'
                : 'Queued.'
            )
          }
       </p>
        <ChatBox onClick={fetchAnswer} />
      </div>
  );
};

export default Popup;
