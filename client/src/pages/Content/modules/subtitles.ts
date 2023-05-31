import { useWatchState } from "../../../services/WatchState";
import { waitForEl } from "../../../utils/dom";

export default async function listenForSubtitles() {
    const targetNode = await waitForEl('.player-timedtext');
    console.log('NetflixGPT> Now tracking subtitles!');

    const config = { characterData: false, attributes: false, childList: true, subtree: false };

    function callback(mutationList: MutationRecord[], observer: MutationObserver) {
        mutationList.forEach((mutation) => {
            if (mutation.type == "childList") {
                useWatchState.getState().addSubtitles(targetNode?.textContent ?? '');
            }
        })
    }

    const observer = new MutationObserver(callback);

    if (targetNode) {
        observer.observe(targetNode, config);
    }
};