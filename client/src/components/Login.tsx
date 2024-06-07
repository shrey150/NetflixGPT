import React from 'react';

const clientId =
  '482785177008-2gvmb96n2m5p1rgj6dv40aiedaespb4b.apps.googleusercontent.com';

export const Login = () => {
  // const onSuccess = (res: any) => {
  //   console.log('Success! Current User: ', res.profileObj);
  // };

  // const onFailure = (res: any) => {
  //   console.log('Failure! res: ', res);
  // };
  return (
    <div className='group hover:scale-105 hover:ease-in-out hover:duration-300 grid grid-cols-1 items-center justify-items-center'>
        <div className="peer cursor-pointer flex relative items-center mt-6 justify-center w-72 h-20  bg-blue-500 active:bg-blue-500 active:translate-y-1 rounded-full z-20">
            <p className="absolute m-auto text-center text-2xl font-semibold text-white font-inter">Login with Google</p>
        </div>
        <div className="group-hover:shadow-md absolute w-72 h-20 mt-9 bg-gray-500 peer-active:bg-gray-500 rounded-full z-10"/>
    </div>
  );
};
