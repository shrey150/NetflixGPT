import React from 'react';
import {  initiateAuthFlow } from '../pages/Background/index';

export const Login = () => {

  return (
    <button onClick={initiateAuthFlow}>
      <div className='group hover:scale-105 hover:ease-in-out hover:duration-300 grid grid-cols-1 items-center justify-items-center'>
          <div className="peer cursor-pointer flex relative items-center mt-6 justify-center w-72 h-20  bg-blue-500 active:bg-blue-500 active:translate-y-1 rounded-full z-20">
              <p className="absolute m-auto text-center text-2xl font-semibold text-white font-inter">Login with Google</p>
          </div>
          <div className="group-hover:shadow-md absolute w-72 h-20 mt-9 bg-gray-500 peer-active:bg-gray-500 rounded-full z-10"/>
      </div>
    </button>
  );
};
