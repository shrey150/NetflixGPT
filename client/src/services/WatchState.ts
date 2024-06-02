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
  fetchTitleInfocr: (episodeID: string) => Promise<void>;
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
      console.log('NetflixGPT> Fetching title info Test')
      const res = await fetch(`https://www.netflix.com/nq/website/memberapi/v9779f77b/metadata?movieid=${titleId}`); // TODO: Maybe replace va7b420b8 with variable
      const payload: NetflixPayload = await res.json();
      console.log('NetflixGPT> Raw payload:', payload);
      
      // POST the payload to our server
      // TODO replace with axios -- less clunky
      fetch('http://localhost:8000/metadata', {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          url: window.location.href,
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

    fetchTitleInfocr: async (episodeID) => {
      console.log('NetflixGPT> Fetching title info for Crunchyroll');

      // (0) Before anything - we need to POST to grab an anonymous token from crunchyroll
      //What it should look like:
      // POST /auth/v1/token
      // # Request Headers
      // Authorization: Basic bm9haWhkZXZtXzZpeWcwYThsMHE6
      // ETP-Anonymous-ID: ${ETP_ID}
      // Content-Type: application/x-www-form-urlencoded
      // # Request Body
      // "grant_type=client_id"

      const endpoint = "https://www.crunchyroll.com/auth/v1/token";
      const authorizationHeader = "Basic YWNmYWZtNTE3aGtpZWt4Yl93bWU6MDluclZfejBUNWxVdjRyRHp5ZlJYZk0wVmlIRHQyQV8=";
      const contentTypeHeader = "application/x-www-form-urlencoded";
      const etpAnonymousIdHeader = crypto.randomUUID();

      const body = new URLSearchParams({
          "grant_type": "client_id",
          "scope": "offline_access"
      });

      const authresponse = await fetch(endpoint, {
          method: "POST",
          headers: {
              "Authorization": authorizationHeader,
              "Content-Type": contentTypeHeader,
              "ETP-Anonymous-ID": etpAnonymousIdHeader
          },
          body: body.toString()
      });

      const authresponsepayload = await authresponse.json();
      console.log("NetflixGPT> Authorized response payload", authresponsepayload);

      // (1) we need to fetch the ratings tab - which can be done using - https://www.crunchyroll.com/content/v2/cms/objects/<episodeID>?ratings=true&locale=en-US 
      //     (1b) we need to grab the seriesID from the fetch response
      const ratingsRes = await fetch(`https://www.crunchyroll.com/content/v2/cms/objects/${episodeID}?ratings=true&locale=en-US`, {
        headers: {
          "Authorization": `Bearer ${encodeURIComponent(authresponsepayload.access_token)}` // Ensure token is properly encoded
        }
      });
      const ratingsPayload = await ratingsRes.json();
      console.log('NetflixGPT> Ratings payload:', ratingsPayload);
      const seriesId = ratingsPayload.data[0].episode_metadata.series_id;
      if (!seriesId) {
        console.error('NetflixGPT> Unable to find series ID');
        return;
      }

      // 1c - fetch the overall synopysis from https://www.crunchyroll.com/content/v2/cms/series/$seriesID?preferred_audio_language=en-US&locale=en-US
      const seriesRes = await fetch(`https://www.crunchyroll.com/content/v2/cms/series/${seriesId}?preferred_audio_language=en-US&locale=en-US`, {
        headers: {
          "Authorization": `Bearer ${encodeURIComponent(authresponsepayload.access_token)}` // Ensure token is properly encoded
        }
      });
      const seriesPayload = await seriesRes.json();
      console.log('NetflixGPT> Series payload:', seriesPayload);
    

      // (2) After we grab the series ID from the fetch response - we need to
      //     (2b) fetch seasons from this tab https://www.crunchyroll.com/content/v2/cms/series/<seriesID>/seasons?force_locale=&locale=en-US
      const seasonsRes = await fetch(`https://www.crunchyroll.com/content/v2/cms/series/${seriesId}/seasons?force_locale=&locale=en-US`, {
        headers: {
          "Authorization": `Bearer ${encodeURIComponent(authresponsepayload.access_token)}` // Ensure token is properly encoded
        }
      });
      const seasonsPayload = await seasonsRes.json();

      const allSeasonsData = [];
      for (const season of seasonsPayload.data) {
        // (3) Individually run through each season to produce payload
        //     (3b) fetch episodes from this tab https://www.crunchyroll.com/content/v2/cms/seasons/<seasonID>/episodes?locale=en-US
        const episodesRes= await fetch(`https://www.crunchyroll.com/content/v2/cms/seasons/${season.id}/episodes?locale=en-US`, {
          headers: {
            "Authorization": `Bearer ${encodeURIComponent(authresponsepayload.access_token)}` // Ensure token is properly encoded
          }
        });
        const episodesPayload = await episodesRes.json();
        allSeasonsData.push(episodesPayload);
      }

      // (4) POST the payload to our server

      // Absolutely necesssary to payload:
      // 
      const payload = {
        title: seriesPayload.data[0].title,
        current_episode: episodeID,
        lang: ratingsPayload.data[0].episode_metadata.audio_locale,
        synopsis: seriesPayload.data[0].description,
        seasons: allSeasonsData
      };
      console.log('NetflixGPT> Crunchyroll payload:', payload);
      //is this stringifiable?
      try {
        JSON.stringify(payload);
      }
      catch (e) {
        console.error('NetflixGPT> Unable to stringify payload:', e);
        return;
      }
      fetch('http://localhost:8000/metadata', {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          url: window.location.href,
          data: payload,
        })
      });

      set({
        title: ratingsPayload.data[0].title,
        ep_title: ratingsPayload.data[0].slug_title,
        season_num: ratingsPayload.data[0].season_number,
        ep_num: ratingsPayload.data[0].episode_number,
        summary: ratingsPayload.data[0].description,
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
