console.log('NetflixGPT> Background script started!');

// allow Storage API to be access by content script
chrome.storage.session.setAccessLevel({
  accessLevel: 'TRUSTED_AND_UNTRUSTED_CONTEXTS',
});

// inject content script on Netflix watch pages
chrome.tabs.onUpdated.addListener((tabId, changeInfo, _) => {
  console.log('NetflixGPT> Tab updated:', changeInfo);
  if (
    changeInfo.url?.includes('netflix.com/watch') ||
    changeInfo.url?.includes('crunchyroll.com/watch')
  ) {
    console.log('NetflixGPT> Injecting content script!');
    chrome.scripting.executeScript({
      target: { tabId },
      files: ['contentScript.bundle.js'],
    });
  }
});

export async function initiateAuthFlow() {
  const redirectUrl = chrome.identity.getRedirectURL() + 'auth0';

  const options = {
    client_id: process.env.REACT_APP_AUTH0_CLIENT_ID ?? 'default',
    redirect_uri: redirectUrl,
    response_type: 'code',
    scope: 'openid profile email',
  };

  const queryString = new URLSearchParams(options).toString();
  const url = `https://${process.env.REACT_APP_AUTH0_DOMAIN}/authorize?${queryString}`;

  const resultUrl: string = await new Promise((resolve, reject) => {
    chrome.identity.launchWebAuthFlow({ url, interactive: true }, (res) =>
      resolve(res ?? 'default')
    );
  });
  const urlObject = new URL(resultUrl);

  if (resultUrl) {
    const code = urlObject.searchParams.get('code');

    const body = JSON.stringify({
      redirect_uri: redirectUrl,
      grant_type: 'authorization_code',
      client_id: process.env.REACT_APP_AUTH0_CLIENT_ID,
      code: code,
    });

    const response = await fetch(
      `https://${process.env.REACT_APP_AUTH0_DOMAIN}/oauth/token`,
      {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: body,
      }
    );

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const result = await response.json();

    if (result && result.access_token) {
      chrome.storage.local.set({ authToken: result.access_token }).then(() => {
        console.log('Value is set');
      });

      const body = JSON.stringify({
        auth_token: result.access_token,
      });

      await fetch('http://localhost:8000/signin', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: body,
      });

      return result.access_token;
    } else {
      throw new Error('Auth0 Authentication Data was invalid');
    }
  } else {
    throw new Error('Auth0 Cancelled or error');
  }
}
