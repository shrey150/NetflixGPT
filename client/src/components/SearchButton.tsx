import React from 'react';

export const SearchButton= () => {
    return(
    <div className='grid grid-cols-1 items-center justify-items-center'>
        <div className="flex relative items-center mt-6 justify-center w-72 h-20  bg-red-500 active:bg-red-600 active:translate-y-1 rounded-full z-20">
            <p className="absolute m-auto text-center text-4xl font-semibold text-white">SEARCH</p>
        </div>
        <div className="absolute w-72 h-20 mt-9 bg-red-700 peer-active:bg-red-700 rounded-full z-10"/>
    </div>
    )
}

/*



*/