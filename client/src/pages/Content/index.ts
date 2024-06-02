import { useWatchState } from "../../services/WatchState";
import { waitForEl } from "../../utils/dom";
import listenForSubtitles from "./modules/subtitles";

console.log('NetflixGPT> Content script started!')

var parser = require('tld-extract');
const url = window.location.href;
const parsed = parser(url);
console.log('NetflixGPT> parsed', parsed);
const domain = parsed.domain;
switch(domain) {
    case 'netflix.com':
        console.log('NetflixGPT> Netflix detected');
        const titleId = window.location.href.split('watch/')[1];
        await useWatchState.getState().fetchTitleInfo(titleId);
        break;
    case 'crunchyroll.com':
        console.log('NetflixGPT> Crunchyroll detected');
        const episodeId = window.location.href.split('watch/')[1].split('/')[0];
        console.log('NetflixGPT> episodeId', episodeId);
        await useWatchState.getState().fetchTitleInfocr(episodeId);
        break;
    default:
        console.log('NetflixGPT> Unsupported domain:', domain);
}




// check if title has been indexed

///TODO: Crunchyroll implementation
// Based on the tab, we need to fetch the ratings tab first
// episodeID = whatever is after watch in the URL
// ex. chainsaw man episode 1: https://www.crunchyroll.com/watch/<episodeID>/dog--chainsaw - notice that the episode ID is GEVUZM77J
// (1) we need to fetch the ratings tab - which can be done using - https://www.crunchyroll.com/content/v2/cms/objects/<episodeID>?ratings=true&locale=en-US 
//     (1b) we need to grab the seriesID from the fetch response
// (2) After we grab the series ID from the fetch response - we need to 
//     (2b) fetch seasons from this tab https://www.crunchyroll.com/content/v2/cms/series/<seriesID>/seasons?force_locale=&locale=en-US
// (3) Individually run through each season to produce payload
//     (3b) fetch episodes from this tab https://www.crunchyroll.com/content/v2/cms/seasons/<seasonID>/episodes?locale=en-US
// (4) POST the payload to our server


console.log('NetflixGPT> Currently watching:', useWatchState.getState().title);

listenForSubtitles();