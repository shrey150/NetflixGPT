import React, {useState} from 'react'

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
      <div className='w-screen flex flex-row opacity-75 p-5 rounded-lg space-x-4 font-bold'>
        <input className='w-full rounded-full px-5'
          type="text"
          value={text}
          onChange={handleTextChange}
          autoFocus
          placeholder='Type Here'
        />
        <button type='button'
                className='rounded-full border border-black bg-white py-2 px-6 text-black transition-all hover:bg-black hover:text-white text-center text-sm'
                onClick={() => { onClick(text) }}
                >Enter</button>
      </div>
    )
}