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

export async function initiateAuthFlow() {  
    const redirectUrl = chrome.identity.getRedirectURL() + 'auth0';
    console.log('NetflixGPT> Redirect URL:', redirectUrl);
    
    const options = {
      client_id: process.env.REACT_APP_AUTH0_CLIENT_ID??'default',
      redirect_uri: redirectUrl,
      response_type: "code",
      scope: "openid",
    };

    const queryString = new URLSearchParams(options).toString();
    const url = `https://${process.env.REACT_APP_AUTH0_DOMAIN}/authorize?${queryString}`;
    console.log('NetflixGPT> Auth0 URL:', url);
    const resultUrl: string = await new Promise((resolve, reject) => {
      chrome.identity.launchWebAuthFlow({ url, interactive: true }, (res) => resolve(res??'default'));
    });
    console.log('NetflixGPT> Auth0 Result URL:', resultUrl);
    const searchParams = new URLSearchParams(resultUrl)
    
    if (searchParams) {
      const code = searchParams.get("code")
  
      const body = JSON.stringify({
        redirect_uri: redirectUrl,
        grant_type: "authorization_code",
        client_id: process.env.REACT_APP_AUTH0_CLIENT_ID,
        code: code
      });

      console.log('NetflixGPT> Auth0 Body:', body);

      const response = await fetch(
        `https://${process.env.REACT_APP_AUTH0_DOMAIN}/oauth/token`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: body
        }
      );
      console.log('NetflixGPT> Auth0 Response:', response);
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
  
      const result = await response.json();
  
      if (result && result.access_token) {
        return result.access_token;
      } else {
        throw new Error("Auth0 Authentication Data was invalid");
      }
    } else {
      throw new Error("Auth0 Cancelled or error");
    }
  }
  