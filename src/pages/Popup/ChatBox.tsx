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
      <div className='chat_div'>
        <input className=''
          type="text"
          value={text}
          onChange={handleTextChange}
          autoFocus
          placeholder='Type here'
        />
        <button type='button' onClick={() => { onClick(text) }}>Enter</button>
      </div>
    )
}