import React from 'react';
import { Login } from '../components/Login';

export const Auth = () => {
  return (
    <div id='unauthorized' className='flex flex-col items-center justify-center bg-stone-900 h-screen overflow-hidden'>
            <Login/>
    </div>
  )
};

export default Auth;