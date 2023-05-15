console.log('NetflixGPT> Background script started!')

const {
    title,
    ep_title,
    season_num,
    ep_num,
    summary,
    question,
} = {
    title: 'Better Call Saul',
    ep_title: 'Gloves Off',
    season_num: 2,
    ep_num: 4,
    summary: "The Davis & Main partners criticize Jimmy for airing his TV ad without their consent.[a] Clifford Main decides to give him a second chance, though he will be under more scrutiny in the future. Jimmy McGill leaves Kim Wexler an urgent voicemail but Howard Hamlin and Chuck McGill are already grilling her about not warning them before Jimmy's ad aired. She takes responsibility for not letting them know in advance, claiming that she did not think it was necessary. Howard reprimands her and she promises it will not happen again. Jimmy prepares to enter Chuck's house but realizes he forgot to remove his electronics, so he grudgingly turns back to Chuck's mailbox and empties his pockets. When Chuck does not answer his knock, Jimmy uses his key to enter. He finds Chuck shivering on the couch, still dressed to leave for work but covered by a space blanket. Chuck refuses to go to the hospital, so Jimmy wraps him in a second space blanket, then sits with him all night. The next morning, Jimmy condemns Chuck for allowing Howard to reprimand Kim. Chuck tells Jimmy he causes harm to everyone around him, but cannot admit his own mistakes. Jimmy offers to quit practicing law if Chuck will help Kim, but Chuck refuses. Nacho Varga and Mike monitor a restaurant and Nacho says he fears retaliation from Tuco Salamanca if Tuco discovers his secret drug dealing.[b] Nacho tells Mike he and Tuco meet there to settle accounts with their street dealers, so Nacho thinks it is an ideal place to kill Tuco. Mike refuses, saying it would attract retaliation by the Salamancas. Instead, Mike calls the police to the restaurant, then fakes a minor accident between his car and Tuco's in the parking lot. When Tuco comes out to check on his car, Mike goads Tuco into striking him repeatedly just as police arrive. Because Tuco was carrying a gun, he is arrested for assault with a deadly weapon. Nacho later pays Mike but Mike declines to give a reason for going to such trouble to avoid killing Tuco.",
    question: "Why is Cliff so mad about Jimmy airing his commercial"
}

const LLM_prompt = `
You are a helpful movie and TV show assistant that can answer any question about a given title on Netflix. You have deep knowledge about plot, characters, actors, themes, and synopses that allow you to correctly answer any movie or TV show watcher's questions. You should aim to answer every question factually and objectively without any interpretations or subjectivity. If you do not know the answer to any question, you are to truthfully answer and say that you do not have enough information to answer their question. Reject any questions that are not within the scope of movies or TV shows.

For TV shows, you will be provided a season and episode number, as well as a brief synopsis of the current episode being watched by the user. You are to answer any questions by this user *without spoiling crucial plot points* that will come up later in the show. If the user asks you a question where truthfully answering will constitute a spoiler, say that you don't know the answer to that question based on the current point in the series. It may be helpful to imagine that you have only watched up to the same point in the show as the user, and therefore you do not possess any knowledge of plot points past this.

In your response, do not hallucinate any details that are factually incorrect or provide any opinions. Answer the question objectively and concisely to provide the user a clear answer to what they asked. Do not provide your own interpretation of plot points.

WARNING: DO NOT GIVE ANY SPOILERS. YOU WILL BE SHUT DOWN IF YOU DO

Here is your context:
- Show: "${ title }"
- Season/Episode: S${ season_num }E${ ep_num }: "${ ep_title }"
- Synopsis: "${ summary }"

Here is your question: "${ question }"

Your answer:
`;

console.log(LLM_prompt);