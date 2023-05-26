import React, {useState, ChangeEvent} from 'react'

interface boxProps {
    words: string;
}

export const ChatBox = ({words}: boxProps) => {
    const [text, setText] = useState(words);
    const [isEditing, setIsEditing] = useState(false);

    const handleTextChange = (event: React.ChangeEvent<HTMLInputElement>) => {
      setText(event.target.value);
    };

    const handleTextDoubleClick = () => {
      setIsEditing(true);
    };

    const handleTextBlur = () => {
      if (title.trim() === '') {
        setText(words);
      }
      setIsEditing(false);
    };

    return(
        <div className='chat_div'>
            {isEditing ? (
          <input className=''
            type="text"
            value={text}
            onChange={handleTextChange}
            onBlur={handleTextBlur}
            autoFocus
          />
        ) : (
          <h1 className='' onDoubleClick={handleTextDoubleClick}>{text}</h1>
      )}
          <button type='button' className=''>Enter</button>
        </div>
    )
}