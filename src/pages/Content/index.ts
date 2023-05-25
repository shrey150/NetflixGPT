console.log('NetflixGPT> Content script started!')

const fetchTitleData = async (titleId: string) => {
    console.log('NetflixGPT> Fetching title data');
    const res = await fetch(`https://www.netflix.com/nq/website/memberapi/vaf4f97f3/metadata?movieid=${titleId}`);
    console.log('NetflixGPT>', await res.json());
}

const titleId = window.location.href.split('watch/')[1];
fetchTitleData(titleId);
