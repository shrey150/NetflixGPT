import React, {useState} from 'react'
import { SearchButton } from './SearchButton';
import autoAnimate from '@formkit/auto-animate';

interface ChatBoxProps {
  question?: string;
  onClick?: any;
  firstClick: boolean;
  setFirstClick: (status: boolean) => void;
  enableAnimations: any;
}
export const ChatBox = ({question, onClick, firstClick, setFirstClick, enableAnimations}: ChatBoxProps) => {
    const [text, setText] = useState(question ?? '');

    const handleTextChange = (e: any) => {
      setText(e.target.value);
    };

    const handleClick = () => {

      onClick(text)
      enableAnimations(false)

      if(!firstClick) {
        setFirstClick(true)
      }
      
      setText('');
    };

    return (
      <div className='w-screen flex flex-col items-center justify-center p-5 rounded-lg'>
        <div className='flex flex-row p-2 bg-gray-600 rounded-full max-w-full align-middle'>
          <input className='font-inter p-5 font-medium subpixel-antialisased border-none bg-transparent outline-none text-white text-xl' 
            id='chat'
            style={{width: 400, height: 36,}}
            type='type'
            value={text}
            onChange={handleTextChange}
            autoFocus></input>
          <img className='max-h-full' src="icon_search.png"/>
        </div>
        <button type='button' className='grow' onClick={handleClick}>
          <SearchButton/>
        </button>
      </div>
    )
}

ChatBox.defaultProps = {
  click: false,
}


