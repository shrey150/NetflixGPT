import { useWatchState } from "../../services/WatchState";

console.log('NetflixGPT> Content script started!')

const titleId = window.location.href.split('watch/')[1];
await useWatchState.getState().fetchTitleInfo(titleId);

console.log('NetflixGPT> [DEBUG]', useWatchState.getState().title);