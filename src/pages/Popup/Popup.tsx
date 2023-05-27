import React, { useEffect } from 'react';
import { doc, setDoc } from 'firebase/firestore';
import { useFirestore, useFirestoreDocData } from 'reactfire';
import { ChatBox } from '../../components/ChatBox';
import { SAMPLE_TITLE_INFO, TitleInfo, useWatchState } from '../../services/WatchState';

const Popup = () => {
  const userRef = doc(useFirestore(), 'users/shrey');
  const { status, data } = useFirestoreDocData(userRef);
  const watchState = useWatchState();

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
      <div className='page'>
          <button
            type='button'
            className='enter_btn my-3'
            onClick={() => watchState.setTitleInfo(SAMPLE_TITLE_INFO)}
          >
            [DEBUG] Reset watch state (BCS S2E4)
          </button>
        <div className='flex-grow'/>
        <div className='answer_div'>
          <p>🔥 Firebase status: {JSON.stringify(status)}</p>
          <p>🌴 PaLM status: {data?.status?.state}</p>
          <p>🐻 Watch status: {JSON.stringify(watchState)}</p>
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
        <ChatBox onClick={(q: string) => fetchAnswer(q, watchState)} />
      </div>
  );
};

export default Popup;
