console.log('NetflixGPT> Background script started!')

// allow Storage API to be access by content script
chrome.storage.session.setAccessLevel({ accessLevel: 'TRUSTED_AND_UNTRUSTED_CONTEXTS' });

// inject content script on Netflix watch pages
chrome.tabs.onUpdated.addListener((tabId, changeInfo, _) => {
    console.log('NetflixGPT> Tab updated:', changeInfo);
    if (changeInfo.url?.includes('netflix.com/watch') || changeInfo.url?.includes('crunchyroll.com/watch')) {
        console.log('NetflixGPT> Injecting content script!')
        chrome.scripting.executeScript({
            target: { tabId },
            files: ['contentScript.bundle.js']
        });
    }
});
