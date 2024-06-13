import React, { useEffect, useState, useRef } from 'react';
import { Auth } from '../../components/Auth';
import { ChatBox } from '../../components/ChatBox';
import {useAutoAnimate} from '@formkit/auto-animate/react';
import { TitleInfo, useWatchState } from '../../services/WatchState';

//Actively checks if the answer is too big for the answer box and displays a lil jawn if it needs to be scrolled
const Overflow = (): [React.RefObject<HTMLDivElement>, boolean] => {
  const [isOver, setIsOver] = useState(false);
  const divRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const checkOverflow = () => {
    const element = divRef.current;
    if (element) {
      setIsOver(element.scrollHeight > element.clientHeight);
      }
    };
    

    const resizeObserver = new ResizeObserver(checkOverflow);

    const divElement = divRef.current;
    if (divElement) {
      resizeObserver.observe(divElement);
      checkOverflow();
    }

    return () => {
      resizeObserver.disconnect();
    };
  }, []);

  return [divRef, isOver];
};

const Popup = () => {
  const watchState = useWatchState();
  const [divRef, isOver] = Overflow()
  const [firstClick, setFirstClick] = useState(false)
  const [parent, enableAnimations] = useAutoAnimate()
  const [authToken, setAuthToken] = useState(null)

  // sync chrome storage -> React state
  useEffect(() => {
    chrome.storage.onChanged.addListener(handleSyncWatchState);
    return () => chrome.storage.onChanged.removeListener(handleSyncWatchState);
  }, []);

  const handleSyncWatchState = (changes: any) => {
    console.log('NetflixGPT> [DEBUG] updating popup watch state:', changes["watchState"].newValue);
    useWatchState.setState(changes["watchState"].newValue as TitleInfo);
  }

  // fetch title info from memory on page load
  useEffect(() => {
    const fetchWatchState = async () => {
      useWatchState.setState((await chrome.storage.session.get("watchState")).watchState ?? {});
    }

    fetchWatchState();
  }, []);


  const fetchAnswer = async (question: string) => {
    try {
      watchState.setLoading(true);
      await watchState.ask(question);
    } catch (error) {
      console.error('Error fetching answer:', error);
    }
  }

  return (
      <div>
        {!authToken ? (
          <Auth/>
        ) : (
          <div id='authorized'>
          <div className={firstClick ? 'flex flex-col items-center bg-stone-900 h-screen overflow-hidden' : 'flex flex-col items-center bg-stone-900 h-screen overflow-hidden'}>
            <div className={firstClick ? 'flex flex-col items-center justify-center hover:scale-105 hover:ease-in-out scale-75 duration-500 max-h-1/2 max-w-1/2' : 'grow mt-10'}>
              <img src="NetflixGPT.png" alt="NetflixGPT Logo" />
            </div>
            <div className = {firstClick ? 'flex flex-col items-center justify-center duration-500' : 'hidden'} >
              <hr color='white' className='w-48'/>
            </div>
          <div className={firstClick ? 'grow flex flex-col items-center justify-center' : 'hidden'}>
              <div ref={divRef} className={firstClick ? 'peer duration-700  max-w-full p-2 font-semibold text-lg text-white text-center overflow-y-auto m-4 border-2 border-black/0 rounded-lg no-scrollbar hover:border-white/100' : 'hidden'}>
                <p>
                  {
                    // data?.response ?? (
                    //   data?.status
                    //     ? 'Processing...'
                    //     : 'Queued.'
                    // )
                    !watchState?.loading ? watchState?.answer ?? 'Ask a question!' : 'Waiting...'
                  }
                </p>
              </div>
            </div>
            <h1 className={isOver ? 'peer-hover:opacity-100 opacity-0 peer-hover:animate-bounce text-xl text-white' : 'opacity-0' }>▼</h1>
            <div ref={parent} className={firstClick ? 'flex flex-col justify-center items-center m-auto self-end duration-500' : 'absolute my-48'}>
              <hr className={firstClick ? 'w-48' : 'hidden'}/>
              <ChatBox 
                onClick={(q: string) => fetchAnswer(q)} 
                firstClick={firstClick} 
                setFirstClick={setFirstClick}
                enableAnimations ={enableAnimations}
              />
              <h1 color='white' className ={firstClick ? 'hidden' : 'text-xl font-bold text-white text-center p-4' }>Search anything about your favorite show and get an answer with ZERO spoilers!</h1>
            </div>
          </div>
        </div>)}
    </div>
  );
};

export default Popup;
