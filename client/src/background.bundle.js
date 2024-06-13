const dotenv = require('dotenv');
dotenv.config();

async function promptUserLogin() {

  const redirectUrl = chrome.identity.getRedirectURL()

  const inputBytes = getRandomBytes()
  const verifier = buf2Base64(inputBytes)

  const shaHash = await sha256(verifier)
  const codeChallenge = buf2Base64(shaHash)

  let options = {
    client_id: process.env.AUTH0_CLIENT_ID,
    redirect_uri: redirectUrl,
    response_type: "code",
    scope: "openid",
    code_challenge: codeChallenge,
    code_challenge_method: "S256"
  }

  let resultUrl = await new Promise((resolve, reject) => {
    let queryString = new URLSearchParams(options).toString()
    let url = `https://${process.env.AUTH0_DOMAIN}/authorize?${queryString}`
    console.log("url", url)
    chrome.identity.launchWebAuthFlow(
      {
        url,
        interactive: true
      },
      (callbackUrl) => {
        resolve(callbackUrl)
      }
    )
  })

  if (resultUrl) {
    const code = getParameterByName("code", resultUrl)
    console.log("code", code)

    const body = JSON.stringify({
      redirect_uri: redirectUrl,
      grant_type: 'authorization_code',
      client_id: process.env.AUTH0_CLIENT_ID,
      code_verifier: verifier,
      code: code,
    });

    const response = await fetch(
      `https://${process.env.AUTH0_DOMAIN}/oauth/token`,
      {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: body
      }
    )

    if (!response.ok) {
      throw new Error("Network response was not ok")
    }

    const result = await response.json()
    console.log("result", result)

    if (result && result.access_token && result.expires_in) {
      return result.access_token
    } else {
      console.log("Auth0 Authentication Data was invalid")
    }
  } else {
    console.log("Auth0 Cancelled or error. resultUrl", resultUrl)
  }
}

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === "login") {
    promptUserLogin().then(token => {
      sendResponse({ success: true, token });
    }).catch(error => {
      console.error(error);
      sendResponse({ success: false });
    });
    return true; // Keep the message channel open for sendResponse
  }
});