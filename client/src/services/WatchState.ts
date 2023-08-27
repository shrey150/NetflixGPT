import {immer} from "zustand/middleware/immer";
import {create} from "zustand";

export interface TitleInfo {
  title: string;
  ep_title: string;
  season_num: number;
  ep_num: number;
  summary: string;
  subtitles: string[];
}

export interface WatchProps {
  answer: string;
  loading: boolean;
}
  
export interface TitleActions {
  setTitleInfo: (titleInfo: TitleInfo) => void;
  fetchTitleInfo: (titleId: string) => Promise<void>;
  addSubtitles: (subtitle: string) => void;
  ask: (question: string) => Promise<void>;
  setLoading: (status: boolean) => void;
}
  
export interface NetflixPayload {
  version: string;
  trackIds: {
    nextEpisode: number;
    episodeSelector: number;
  };
  video: {
    title: string;
    synopsis: string;
    rating: string;
    artwork: {
      w: number;
      h: number;
      url: string;
    }[];
    boxart: {
      w: number;
      h: number;
      url: string;
    }[];
    storyart: {
      w: number;
      h: number;
      url: string;
    }[];
    type: string;
    unifiedEntityId: string;
    id: number;
    userRating: {
      matchScore: number;
      tooNewForMatchScore: boolean;
      type: string;
      userRating: number;
    };
    skipMarkers: {
      credit: {
        start: null | number;
        end: null | number;
      };
      recap: {
        start: null | number;
        end: null | number;
      };
      content: any[];
    };
    currentEpisode: number;
    hiddenEpisodeNumbers: boolean;
    requiresAdultVerification: boolean;
    requiresPin: boolean;
    requiresPreReleasePin: boolean;
    seasons: {
      year: number;
      shortName: string;
      longName: string;
      hiddenEpisodeNumbers: boolean;
      title: string;
      id: number;
      seq: number;
      episodes: {
        start: number;
        end: number;
        synopsis: string;
        episodeId: number;
        liveEvent: {
          hasLiveEvent: boolean;
        };
        taglineMessages: {
          tagline: string;
          classification: string;
        };
        requiresAdultVerification: boolean;
        requiresPin: boolean;
        requiresPreReleasePin: boolean;
        creditsOffset: number;
        runtime: number;
        displayRuntime: number;
        watchedToEndOffset: number;
        autoplayable: boolean;
        title: string;
        id: number;
        bookmark: {
          watchedDate: number;
          offset: number;
        };
        skipMarkers: {
          credit: {
            start: number | null;
            end: number | null;
          };
          recap: {
            start: number;
            end: number;
          };
          content: any[];
        };
        hd: boolean;
        thumbs: {
          w: number;
          h: number;
          url: string;
        }[];
        stills: {
          w: number;
          h: number;
          url: string;
        }[];
        seq: number;
        hiddenEpisodeNumbers: boolean;
      }[];
    }[];
    merchedVideoId: null | string;
    cinematch: {
      type: string;
      value: string;
    };
  };
}

const findEpisodeById = (payload: NetflixPayload, id: number) => {
  for (const season of payload.video.seasons) {
    const ep = season.episodes.find(x => x.episodeId === payload.video.currentEpisode);
    if (ep) return {...ep, season_num: season.seq};
  }
}
  
export const useWatchState = create(
  immer<TitleInfo & TitleActions & WatchProps>((set, get) => ({
    title: '',
    ep_title: '',
    season_num: -1,
    ep_num: -1,
    summary: '',
    subtitles: [],
    answer: '',
    loading: false,

    setTitleInfo: ({title, ep_title, season_num, ep_num, summary}) => set({
      title, ep_title, season_num, ep_num, summary
    }),
    
    fetchTitleInfo: async (titleId) => {
      console.log('NetflixGPT> Fetching title info')
      const res = await fetch(`https://www.netflix.com/nq/website/memberapi/vaf4f97f3/metadata?movieid=${titleId}`);
      const payload: NetflixPayload = await res.json();
      console.log('NetflixGPT> Raw payload:', payload);
      
      // POST the payload to our server
      fetch('http://localhost:8000/info', {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          source: "netflix",
          data: payload,
        })
      });

      const ep = findEpisodeById(payload, payload.video.currentEpisode);

      if (!ep) {
        console.error('NetflixGPT> Unable to find episode info');
        return;
      }

      set({
        title: payload.video.title,
        ep_title: ep.title,
        season_num: ep.season_num,
        ep_num: ep.seq,
        summary: ep.synopsis,
      })
    },

    addSubtitles: (subtitle) => set((state) => ({
      subtitles: [...new Set([...state.subtitles, subtitle])]
    })),
    
    ask: async (question: string) => {
      console.log('Asking...');
      const res = await fetch('http://localhost:8000/ask', {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          title: get().title,
          ep_title: get().ep_title,
          season_num: get().season_num,
          ep_num: get().ep_num,
          question
        })
      });

      const {answer} = await res.json();
      console.log('Answer', answer);
      set({ answer, loading: false });
    },

    setLoading: (loading) => set({ loading })

  }))
)

// sync React state -> chrome storage
useWatchState.subscribe(watchState => {
  console.log("NetflixGPT> Syncing watch state...");
  chrome.storage.session.set({ watchState });
});

export const SAMPLE_TITLE_INFO: TitleInfo = {
  title: 'Better Call Saul',
  ep_title: 'Gloves Off',
  season_num: 2,
  ep_num: 4,
  summary: "The Davis & Main partners criticize Jimmy for airing his TV ad without their consent.[a] Clifford Main decides to give him a second chance, though he will be under more scrutiny in the future. Jimmy McGill leaves Kim Wexler an urgent voicemail but Howard Hamlin and Chuck McGill are already grilling her about not warning them before Jimmy's ad aired. She takes responsibility for not letting them know in advance, claiming that she did not think it was necessary. Howard reprimands her and she promises it will not happen again. Jimmy prepares to enter Chuck's house but realizes he forgot to remove his electronics, so he grudgingly turns back to Chuck's mailbox and empties his pockets. When Chuck does not answer his knock, Jimmy uses his key to enter. He finds Chuck shivering on the couch, still dressed to leave for work but covered by a space blanket. Chuck refuses to go to the hospital, so Jimmy wraps him in a second space blanket, then sits with him all night. The next morning, Jimmy condemns Chuck for allowing Howard to reprimand Kim. Chuck tells Jimmy he causes harm to everyone around him, but cannot admit his own mistakes. Jimmy offers to quit practicing law if Chuck will help Kim, but Chuck refuses. Nacho Varga and Mike monitor a restaurant and Nacho says he fears retaliation from Tuco Salamanca if Tuco discovers his secret drug dealing.[b] Nacho tells Mike he and Tuco meet there to settle accounts with their street dealers, so Nacho thinks it is an ideal place to kill Tuco. Mike refuses, saying it would attract retaliation by the Salamancas. Instead, Mike calls the police to the restaurant, then fakes a minor accident between his car and Tuco's in the parking lot. When Tuco comes out to check on his car, Mike goads Tuco into striking him repeatedly just as police arrive. Because Tuco was carrying a gun, he is arrested for assault with a deadly weapon. Nacho later pays Mike but Mike declines to give a reason for going to such trouble to avoid killing Tuco.",
  subtitles: [],
}
