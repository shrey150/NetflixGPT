import React from 'react';

export const SearchButton= () => {
    return(
    <div className='group hover:scale-105 hover:ease-in-out hover:duration-300 grid grid-cols-1 items-center justify-items-center'>
        <div className="peer cursor-pointer flex relative items-center mt-6 justify-center w-72 h-20  bg-red-500 active:bg-red-600 active:translate-y-1 rounded-full z-20">
            <p className="absolute m-auto text-center text-4xl font-semibold text-white font-inter">SEARCH</p>
        </div>
        <div className="group-hover:shadow-md group-hover:shadow-white absolute w-72 h-20 mt-9 bg-red-700 peer-active:bg-red-700 rounded-full z-10"/>
    </div>
    )
}

/*



*/