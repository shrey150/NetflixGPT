import React, {useState} from 'react'
import { SearchButton } from './SearchButton';

interface ChatBoxProps {
  question?: string;
  onClick?: any;
}

export const ChatBox = ({question, onClick}: ChatBoxProps) => {
    const [text, setText] = useState(question ?? '');

    const handleTextChange = (e: any) => {
      setText(e.target.value);
    };

    return (
      <div className='w-screen flex flex-col items-center justify-center p-5 rounded-lg font-bold'>
        <div className='flex flex-row p-4 bg-gray-600 rounded-full'>
          <input className='border-none bg-transparent outline-none text-white' 
            style={{width: 436, height: 64,}}
            type="text"
            value={text}
            onChange={handleTextChange}
            autoFocus></input>
          <img src="icon_search.png"/>
        </div>
        <button type='button' className='grow' onClick={() => { onClick(text) }}>
          <SearchButton/>
        </button>
      </div>
    )
}

