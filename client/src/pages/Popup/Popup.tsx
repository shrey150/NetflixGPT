import React, { useEffect, useState, useRef } from 'react';
import { doc, setDoc } from 'firebase/firestore';
import { useFirestore, useFirestoreDocData } from 'reactfire';
import {ChatBox} from '../../components/ChatBox';
import { SAMPLE_TITLE_INFO, TitleInfo, useWatchState } from '../../services/WatchState';


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
  const userRef = doc(useFirestore(), 'users/shrey');
  const { status, data } = useFirestoreDocData(userRef);
  const watchState = useWatchState();  
  const [divRef, isOver] = Overflow()
  const [firstClick, setFirstClick] = useState(false)


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
      useWatchState.setState((await chrome.storage.session.get("watchState")).watchState);
    }

    fetchWatchState();
  }, []);


  const fetchAnswer = async (question: string, titleInfo: TitleInfo) => {
    try {
      await setDoc(userRef, { question: generatePrompt(question, titleInfo) });
      console.log('Document written successfully!');
    } catch (error) {
      console.error('Error writing document:', error);
    }
  }

  const generatePrompt = (question: string, {title, season_num, ep_num, ep_title, summary}: TitleInfo) => (
    `
    You are NetflixGPT, a helpful movie and TV show assistant that can answer any question about a given title on Netflix. You have deep knowledge about plot, characters, actors, themes, and synopses that allow you to correctly answer any movie or TV show watcher's questions. You should aim to answer every question factually and objectively without any interpretations or subjectivity. If you do not know the answer to any question, you are to truthfully answer and say that you do not have enough information to answer their question. Reject any questions that are not within the scope of movies or TV shows.\n\n

    For TV shows, you will be provided a season and episode number, as well as a brief synopsis of the current episode being watched by the user. You are to answer any questions by this user *without spoiling crucial plot points* that will come up later in the show. If the user asks you a question where truthfully answering will constitute a spoiler, say that you don't know the answer to that question based on the current point in the series. It may be helpful to imagine that you have only watched up to the same point in the show as the user, and therefore you do not possess any knowledge of plot points past this.\n\n

    In your response, do not hallucinate any details that are factually incorrect or provide any opinions. Answer the question objectively and concisely to provide the user a clear answer to what they asked. Do not provide your own interpretation of plot points.\n\n

    WARNING: DO NOT GIVE ANY SPOILERS. YOU WILL BE SHUT DOWN IF YOU DO\n\n

    Here is your context:\n
    - Show: "${ title }"\n
    - Season/Episode: S${ season_num }E${ ep_num }: "${ ep_title }"\n
    - Synopsis: "${ summary }"\n\n

    Here is your question: "${ question }"\n\n

    Your answer:\n\n
    `
  );
  
  
  return (
      <div className='flex flex-col items-center bg-stone-900 h-screen overflow-hidden'>
        <div className={firstClick ? 'w-1/2 h-1/2' : 'max-h-full'}>
          <img src="NetflixGPT.png"/>
        </div>
        <div className={firstClick ? 'flex flex-col items-center p-2 rounded-lg opacity-75 text-white font-bold' : 'hidden'} style={{maxWidth:400, maxHeight:500}}>
          <p>🔥 Firebase status: {JSON.stringify(status)}</p>
          <p>🌴 PaLM status: {data?.status?.state}</p>
          <p>🐻 Watch status: {JSON.stringify(watchState)}</p>
          <br/>
          <button
            type='button'
            className='enter_btn'
            onClick={() => useWatchState.setState(SAMPLE_TITLE_INFO)}
          >
            [DEBUG] Reset watch state (BCS S2E4)
          </button>
       </div>
       <div ref={divRef} className={firstClick ? 'peer grow max-w-full flex-col text-white text-center font-bold overflow-y-auto m-4 p-4 border-2 border-black/0 rounded-lg no-scrollbar hover:border-white/100' : 'hidden'}>
              <p>
                {
                  data?.response ?? (
                    data?.status
                      ? 'Processing...'
                      : 'Queued.'
                  )
                }
            </p>
        </div>
        <h1 className={isOver ? 'peer-hover:opacity-100 transition-opacity duration-300 text-xl text-white' : 'opacity-0' }>▼</h1>
        <ChatBox 
          onClick={(q: string) => fetchAnswer(q, watchState)} 
          firstClick={firstClick} 
          setFirstClick={setFirstClick}
        />
        <h1 className ={firstClick ? 'hidden' : 'text-xl font-bold text-white text-center p-4' }>Search anything about your favorite show and get an answer with ZERO spoilers!</h1>
      </div>
  );
};

export default Popup;
