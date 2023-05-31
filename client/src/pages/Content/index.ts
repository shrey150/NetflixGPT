import { useWatchState } from "../../services/WatchState";
import { waitForEl } from "../../utils/dom";
import listenForSubtitles from "./modules/subtitles";

console.log('NetflixGPT> Content script started!')

const titleId = window.location.href.split('watch/')[1];
await useWatchState.getState().fetchTitleInfo(titleId);

console.log('NetflixGPT> Currently watching:', useWatchState.getState().title);

listenForSubtitles();