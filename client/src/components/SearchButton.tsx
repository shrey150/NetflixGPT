import React from 'react';

export const SearchButton= () => {
    return(
    <div className='group hover:scale-105 hover:ease-in-out hover:duration-300 grid grid-cols-1 items-center justify-items-center'>
        <div className="peer cursor-pointer flex relative items-center mt-6 justify-center w-72 h-20  bg-gray-200 active:bg-gray-200 active:translate-y-1 rounded-full z-20">
            <p className="absolute m-auto text-center text-4xl font-semibold text-blue-900 font-inter">SEARCH</p>
        </div>
        <div className="group-hover:shadow-md group-hover:shadow-white absolute w-72 h-20 mt-9 bg-gray-400 peer-active:bg-gray-400 rounded-full z-10"/>
    </div>
    )
}

/*



*/