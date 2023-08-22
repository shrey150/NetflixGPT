import hashlib
import json

FAKE_DB = {
    "data": [
        [
            "d3b287e8-1dce-11ee-b06f-52b307fec202",
            "them, but Louis refuses, stating that per her request, he will keep hold of them, before leaving. The judge questions what is going on, and requests Katrina bring the documents she brought with her to him, adding that if they are not legitimate court documents, she will be fined. Katrina tentatively approaches the judge with the offending documents in her hand.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "de775a8c-1dce-11ee-b06f-52b307fec202",
            "Flashing back to the past, Trevor and Mike attend a party, where they decide to win some money by playing poker. At the DA office, Harvey and Cameron celebrate after their latest win (due to Harvey's successful idea). Afterwards, Harvey begins to flirt with Donna, however Bertha interrupts with a piece of evidence, which may have screwed them over. Mike continues to play, however one of the players lures him by making him go 'all in'. Running out of money, Trevor offers to lend him $500, unaware this becomes a trap and they lose their money when one of the other players cheat. Lacking the support to call the police (due to both of them drinking) and unable to fight them off, they decide to leave.",
            {
                "title": "Suits",
                "ep_title": "The Other Time",
                "season_num": 3,
                "ep_num": 6
            }
        ],
        [
            "c4eea070-1dce-11ee-b06f-52b307fec202",
            "Plot\nJenny begins questioning Mike about his true relationship with Rachel after Louis tells her that he knows something is going on between Mike and Rachel. Mike insists that they are just friends. Jenny then insists that she and Mike go out on a double date with Rachel (that is if Rachel can find somebody she can go out with) so Jenny can get to know Rachel more and they can start a kindly friendship. Mike then says yes with hesitation.\n\nOn the way to the office, Harvey spots an old colleague in Cameron Dennis (played by Gary Cole). Harvey then introduces Mike to Cameron, telling him that he was his mentor when he was still working at the at the DA office. Cameron invites Harvey to dinner to do some catching up.",
            {
                "title": "Suits",
                "ep_title": "Rules of the Game",
                "season_num": 1,
                "ep_num": 11
            }
        ],
        [
            "c4eea1c4-1dce-11ee-b06f-52b307fec202",
            "At the office, Mike and Rachel try to find out if Harvey worked as a prosecutor while working with Cameron. He also forces Rachel to go on a double date with him and Jenny after Louis spills the beans to Jenny about what he probably saw when Rachel kissed Mike. Rachel also says yes with hesitation.",
            {
                "title": "Suits",
                "ep_title": "Rules of the Game",
                "season_num": 1,
                "ep_num": 11
            }
        ],
        [
            "26950b12-1dce-11ee-a4b1-52b307fec202",
            "\"Ozymandias\" is the fourteenth episode of the fifth season of the American television drama series Breaking Bad, and the 60th episode of the series. Written by Moira Walley-Beckett and directed by Rian Johnson, it aired on AMC in the United States and Canada on September 15, 2013. The episode's narrative concludes the previous episode's cliffhanger.\n\nBeckett and Johnson had previously worked together on the season three episode \"Fly\" and had a friendly working relationship that lasted throughout the production. Beckett was allowed greater creative freedom than she had experienced before. Due to the intensity of the episode's storyline, the production was emotionally difficult for those involved. The episode was subject to much analysis following its release. Focus was given to the episode's parallels to its namesake, Percy Shelley's \"Ozymandias\", its depiction of redemption, and Walt's (Bryan Cranston) phone call to Skyler (Anna Gunn).",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26950cac-1dce-11ee-a4b1-52b307fec202",
            "\"Ozymandias\" has been unanimously acclaimed since its initial airing, and is widely considered to be Breaking Bad'''s finest episode. Critics praised its writing, acting, direction, and payoff of storylines set up since \"Pilot\", and it is considered to be one of the greatest episodes of television ever made. At the 66th Primetime Emmy Awards, Walley-Beckett won Outstanding Writing for a Drama Series for her teleplay; Cranston and Gunn won Lead Actor and Supporting Actress, respectively, for their performances in the episode.\n\n Plot \nIn a flashback, Walter White and Jesse Pinkman conduct their first meth cook. Walt calls a pregnant Skyler White with an excuse for not being home, and she suggests the name Holly for their baby.",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26950d24-1dce-11ee-a4b1-52b307fec202",
            "Hank Schrader is wounded following the shootout with Jack's brotherhood, and Steve Gomez is dead, but Jack and his gang are unscathed. Jack prepares to kill Hank but Walt begs Jack to spare him, offering his entire $80 million in exchange. Hank chides Walt for not realizing Jack is going to kill him anyway; Jack kills Hank, and Walt collapses to the ground in despair.\n\nThe gang discovers Walt's money barrels; they take six, but at Todd Alquist's request, they leave the seventh for Walt, then bury Hank and Gomez in place of the barrels. Walt identifies Jesse's hiding place and demands Jack carry out the hit Walt requested. Todd suggests taking Jesse captive first to learn what he revealed to Hank and Steve, to which Walt consents. Walt spitefully reveals to Jesse that he allowed Jane Margolis to die. The gang detains Jesse in a cell, then forces him to cook meth for them.",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26950d60-1dce-11ee-a4b1-52b307fec202",
            "Walt's car runs out of fuel so he rolls his barrel through the desert until he reaches a house and purchases the owner's truck. Unaware of what transpired in the desert, Marie Schrader informs Skyler that Hank has arrested Walt. She demands that Skyler relinquish the false confession video implicating Hank and tell Walter White Jr. the truth. Skyler informs Walter Jr. about Walt's drug business, and he tells her she is as bad as Walt for going along. Walt arrives home and frantically tries to get Skyler and Walter Jr. to leave with him. Skyler realizes Hank has been killed and attacks Walt with a kitchen knife. Walter Jr. tackles his father to the ground and calls the police. Walt takes Holly White and flees.",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26950d9c-1dce-11ee-a4b1-52b307fec202",
            "Marie and the police arrive at the Whites' home. The police tap the phone and listen when Walt calls. Walt attempts to establish Skyler's innocence by falsely claiming he built up his drug business alone and berating her for not helping him. Walt confirms Hank's death, ends the call, and leaves Holly at a fire station with her home address written on a note. The next morning, Walt meets Ed Galbraith, Saul Goodman's new-identity contact, who drives away with Walt and the barrel.\n\n Production",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26950dd8-1dce-11ee-a4b1-52b307fec202",
            "Production \n\nthumb|upright|left|Dean Norris made his final on-screen appearance in Breaking Bad in \"Ozymandias\"\nThe episode was written by Moira Walley-Beckett and directed by Rian Johnson—self-described \"partners in crime\". As the writers are chosen in advance of the plot points being formed, Walley-Beckett's appointment was, in her own words, \"luck of the draw\". She requested to work with Johnson because of their experiences together working on the third-season episode \"Fly\". The two worked together throughout the production with them overseeing the final cut, a first for Walley-Beckett. Ultimately, Johnson said that the episode was Walley-Beckett's, who found herself deeply proud of the episode. Series creator Vince Gilligan was also enamored, thinking of it as the show's best. It aired on AMC in the United States and Canada on September 15, 2013.",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26950e14-1dce-11ee-a4b1-52b307fec202",
            "This episode marks the final appearance of Hank Schrader (Dean Norris) and Steve Gomez (Steven Michael Quezada). Hank's death was shot in a minimal number of takes, due in part to the limited time the crew had and the inconvenient weather present. Although the writers discussed many options for his death, it was agreed, from the start of talks, that his death would be dignified and honorable; Hank was originally supposed to die at the end of the previous episode, but it was moved to \"Ozymandias\" for better pacing. To preserve the drama of Hank's death, the show's producers secured special permission from Hollywood guilds to delay showing the opening credits until 19 minutes into the episode.",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26950e64-1dce-11ee-a4b1-52b307fec202",
            "The opening flashback scene was the last scene to be shot for the entire series. The crew waited to film the episode to allow for Bryan Cranston's and Aaron Paul's hair to grow in so they would look like they did before Walt began shaving his head and Jesse began wearing his hair short. Although it was filmed months after the rest of the episode, Johnson was able to return to direct the scene.",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26950ea0-1dce-11ee-a4b1-52b307fec202",
            "The shot depicting Walt's reaction to Hank's death was, according to Beckett, Johnson's invention. To emphasize the physical impact, he requested that puzzle pieces be placed on the ground, covered in dirt; the pieces were controlled by a trigger and disassembled upon the moment Walt landed, thus emulating the effect of \"shattering the earth\". The ground shots of Hank and Jesse required a special crane rig and \"periscope lens\". For the following shot of Walt rolling the barrel, Johnson wanted to emulate the stature of a dung beetle. To do so he got the \"longest possible lens\" they could afford and sent \"the B-camera crew out in a truck way the hell out\". Jesse's torture was left off-screen due to the script excluding it and Johnson feeling that it would be unfair to the audience to manipulate their emotional investment in Jesse's character.",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26950ee6-1dce-11ee-a4b1-52b307fec202",
            "Betsy Brandt said that during production she avoided reading Hank's death, as she found it too emotional. Brandt noted that seven years after airing, she had not seen the episode. Co-executive producer Melissa Bernstein described reading the script as an \"intense experience\". Anna Gunn recalled that during the scene of Holly's kidnapping there were what \"seemed like\" a hundred onlookers. This coupled with the shooting running late and the erratic weather of the day led to her feeling under pressure and seeking support from Johnson. In 2014, she named it the hardest scene she filmed but also one of the \"richest\".",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26950f22-1dce-11ee-a4b1-52b307fec202",
            "Walley-Beckett said that Walt's preceding confrontation was \"extremely complicated\" to write due to the character's differing objectives, the scene's \"operatic\" nature, and the multiple \"crescendos and decrescendos\". Johnson—who had it all \"mapped out\"—saw the scene as the hardest to film, noting that the line \"I tried to save him\" underwent multiple takes until Cranston commented that Walt should be, instead of bumbling, exasperated. Cranston and Gunn both performed the stunts themselves, barring two shots. The scene in which Walt is changing Holly's diaper had no lines for Holly in the script, but as Johnson explains: \"[t]hat baby's mom was just off camera\" which caused the baby to say \"mama\". Cranston stayed in character and went along with it, and it ended up in the episode.",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26950f54-1dce-11ee-a4b1-52b307fec202",
            "Analysis \nThe University of Colorado Boulder's Amanda Knopf noted that the shootout aligns with the conventional Western trope of improbable success in a gunfight and is an example of Walt's moral code and belief that dying in this manner would restore his masculinity and heroism. Walt is throughout the episode emasculated, in various ways. She also notes that, within the series, the desert is visually unique in that despite the destruction and loss taking place it remains \"unchanged\".\n\nThe lyrics to \"Take My True Love by the Hand\" by The Limeliters references and foreshadows Walt's isolation from his family, emphasized by Holly's first words being \"Mama\".",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26950f90-1dce-11ee-a4b1-52b307fec202",
            "Parallels to Percy Shelley's Ozymandias \nthumb|left|170px|Ramesses II—the basis for Shelley's Ozymandias—whose poetic downfall is paralleled in Walt's.\nThe episode title refers to the poem \"Ozymandias\" by Percy Bysshe Shelley, which recounts the crumbling legacy of a once-proud king. Bryan Cranston recited the entire poem in a 2013 trailer for the series. Walley-Beckett had wanted to use the poem for a long time and thus introduced it to showrunner Vince Gilligan.\n\nAlthough the episode makes no explicit references to the poem, Austin Gill of Xavier University felt that by this episode's point in Walt's progression he had embodied the \"tyrannical aspirations of invincibility and arrogance\" of the poem's king, whose downfall is paralleled in Walt's. Douglas Eric Rasmussen of the University of Saskatchewan said that Walt's reaction to Hank's death indicates that he has become the “colossal wreck” of the poem—the empire of Ramesses II, which Shelley alluded to.",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26950fcc-1dce-11ee-a4b1-52b307fec202",
            "Further parallels are seen in both the episode and poem concluding with their protagonists left with little to show for their actions and how the \"concept of hubris and being punished for grandiose projects that serve an individual's egotism are central aspects of each work\". Walt's pant-less appearance in the flashback echoes the line \"Two vast and trunk-less legs of stone\". By evoking the poem, Rasmussen said, the show is critiquing Walt's empire and his \"empty desires\"—which he sees Walt embodying. Gill said that the episode—and by extension, the show—uses the poem to \"underscore and warn of the ramifications of vanity\" and \"sustain cultural life and power\".",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26951008-1dce-11ee-a4b1-52b307fec202",
            "Redemption \nDonna Bowman of The A.V. Club said the episode portrayed \"Walt at his most human [and] most deluded... Hank [is] transformed by his pursuit of Heisenberg into the lawman he always wanted to be\". She concluded that Holly's kidnapping was the final straw for his humanity. Alberto Nahum García Martínez and colleagues provided a reading which said that Walt's actions before and, particularly, after \"Ozymandias\" indicate moral redemption with the intention of the audience once again supporting Walt; in a review for Slate, published the same day as the episode, Matthew Yglesias speculated this to be the writers' goal.",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26951044-1dce-11ee-a4b1-52b307fec202",
            "When asked if the writers were trying to get the audience to support Walt, Walley-Beckett responded opaquely, noting that \"moral ambiguity is a cornerstone of the series\" and that they always \"tried to legitimately confound expectations and put people in the moral position of rooting for somebody who's become a cancer to himself and everyone around [him]\". Cranston said that the episode \"[twisted] the allegiance, testing the audience\" and that many people told him, following Walt disclosing his involvement in Jane's death, that they lost faith in Walt.\n\n Phone call",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26951076-1dce-11ee-a4b1-52b307fec202",
            "Phone call \n\nThe most analyzed and immediately discussed aspect of the episode was the phone call between Walt and Skyler—some viewers felt Walter's rage was false in an attempt to aid Skyler in avoiding prosecution; others saw his anger as genuine. Walley-Beckett \"personally [felt] like it wasn't open to interpretation\" and hoped that audiences would view it as a ploy and thus sympathize with Skyler, who Johnson framed in a deliberately intimate manner. She did see some of Walt's words as true. In an article for IndieWire, one week after the episode's airing, Sam Adams said that \"most everyone agrees that Walt's call to Skyler was...[him] trying to exonerate her\".",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "269510b2-1dce-11ee-a4b1-52b307fec202",
            "The University of British Columbia's Brandon Taylor said that the episode's critique of Walt is, by proxy, a critique of the audience for having, beforehand, derived pleasure from witnessing his actions. Drusilla Moorhouse, an online contributor to The Today Shows website, viewed the call as selfless and said it \"rewrote the history of [Skyler's] complicity\".\n\nMatt Zoller Seitz of Vulture said that \"The controversy over Walter's phone call is really about the relationship between viewers and television...It's about the discomfort that ensues when an episode or scene or moment forces us to take a hard look at why we watch a show, what we truly get out of it, and what that says about us\". The New Yorker's Emily Nussbaum said that the episode \"trolled\" her—\"the Prissy Progressive Fan\"—and the \"bad fans\"—those who watch the show for a power fantasy. According to Nussbaum, the episode sought to critique the respective fans' views of Skyler as either \"pure victim\" or \"bitch\".\n\n Reception",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "269510ee-1dce-11ee-a4b1-52b307fec202",
            "Reception \n\n Critical reception \nthumb|alt=Bryan Cranston and Anna Gunn at the 2018 San Diego Comic-Con International in San Diego, California.|Bryan Cranston and Anna Gunn received acclaim and won Primetime Emmy Awards for their performances in \"Ozymandias\".",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "2695112a-1dce-11ee-a4b1-52b307fec202",
            "\"Ozymandias\" received universal critical acclaim, and is widely considered not only the show's best episode but also one of the best episodes in the history of television. Many publications named it the best television episode of 2013;{{efn|Year-end lists include those by Digital Spy, Entertainment Weekly, IndieWire, Time, and Vulture.}} some named it the best of the decade. TV Guide picked \"Ozymandias\" as the best television episode of the 21st century. \"Ozymandias\" frequently tops polls of the best Breaking Bad episodes. The episode, watched by 6.4 million viewers—the then-most for the show—is revered among fans, achieving a perfect 10.0 out of 10 rating on IMDb with almost 200,000 votes, putting it at the number one spot for its 'Best TV Episodes' ranking.",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "2695115c-1dce-11ee-a4b1-52b307fec202",
            "Tom Mendelsohn of The Independent praised how the episode paid off the season's build-up. Seth Amitin of IGN echoed similar sentiments. The Los Angeles Times' Emily St. James described it as \"rich\" and gave particular praise to how it made Skyler's arc as a victim to willing accomplice \"worth it\", which she felt had previously been a fault of the season. IndieWire's Kevin Jagernauth complimented how the episode delivered on each member of the White family's arcs. Maureen Ryan of The Huffington Post commended how it actualized the consequences of Walt's actions, in what she saw as a visceral manner. Tyler Hersko, in an article for IndieWire, applauded how it was a \"culmination\" of the show to that point.",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26951198-1dce-11ee-a4b1-52b307fec202",
            "Some reviewers found it hard to watch. Ryan, although calling the episode \"perfectly realized,\" said it left her feeling sick and made her cry. Tim Surette of TV.com called the episode \"terrific and awful to watch; a powerful piece of television that transcended fiction\". Linda Holmes, in a positive review of the episode, expressed relief that the show was ending, as she began to find \"the show's honesty about greed and violence...unbearable\".",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "269511d4-1dce-11ee-a4b1-52b307fec202",
            "Walley-Beckett's script and Johnson's direction were described by St. James as \"beautiful\" and \"exquisite\", respectively. Regular contributor to Paste, Ross Bonaime found Johnson's direction immersive, a sentiment echoed by Bowman. Jagernauth was grateful that Johnson \"[served] the script by keeping the stylization at a minimum and letting the emotional scenes carry through with the power that was clearly on the page\". Dustin Rowles called Johnson, in a 2014 article for Uproxx, the best working director in television directly because of his work on \"Ozymandias\".",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "26951210-1dce-11ee-a4b1-52b307fec202",
            "Alex Berenson of Esquire provided limited criticism regarding Todd's request to spare Walt and his delay—noting the latter to be \"heavy-handed and unsubtle\" but acknowledging that it did work within the story. St. James called Jesse's survival \"improbable\". Yglesias found Walt revealing his entire fortune and his eventual new life to be out-of-character decisions; the gang's imprisonment of Jesse to continue selling meth and lack of in-fighting also perplexed him.",
            {
                "title": "Breaking Bad",
                "ep_title": "Ozymandias",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "bb9a0d0c-1dce-11ee-b06f-52b307fec202",
            "Plot\nLouis Litt walks into an office at Pearson Hardman, and informs Jessica Pearson that one of their clients, Gerald Tate, is unhappy with what is happening with his deal. Jessica tells Louis to get Harvey Specter, their best closer, and after some hesitation from Louis, he leaves. Harvey is at a poker game, which he promptly wins, and receives a text from Jessica saying that she needs him to come in.\nthumb|right|250px|Harvey meets Gerald Tate",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a0e9c-1dce-11ee-b06f-52b307fec202",
            "Rushing over to the office, he interrupts an argument between Jessica and Gerald, and after Jessica introduces him, Gerald berates Harvey for his absence. Harvey retaliates by saying that when he left, there was no problem with the deal. After Gerald claims that the reason for the problem is the other side, Harvey responds by saying that Gerald is the cause of the hold up with the deal. Despite Gerald's assertions that Harvey should fix the problem, and after threatening to pay someone else to fix it, Harvey informs Gerald that since the deal was already signed by the other side, they have already been paid in full, with Jessica backing his position. Reluctantly, Gerald leaves. Jessica then discovers that Harvey had lied about their fee having already been paid, but lets him off with a smile.\nthumb|left|250px|Mike at the LSAT.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a0f00-1dce-11ee-b06f-52b307fec202",
            "Meanwhile, Mike Ross has just taken another Law School Admission Test (LSAT) when the proctor stops him, saying that he looks familiar. Despite Mike claiming otherwise, the proctor sets aside his test, separating it from the others. However, when the proctor is distracted, Mike buries his test with the others. The proctor realizes, and gives chase, but Mike manages to escape by changing his clothes. He goes to collect his fee from the student he took the LSAT for, but the student is unsatisfied with the score Mike got for him. Mike responds that the score he got was representative of the student's intelligence, only for the student to pay him half of what was agreed. The student responds sarcastically by suggesting that he go to the police.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a0f28-1dce-11ee-b06f-52b307fec202",
            "Later on, Mike reveals to his best friend, Trevor Evans, that he was high when he took the test and almost got caught. Trevor responds by suggesting that Mike join him in his business of selling pot, and tells him about a transaction that he needs Mike to do for him. Mike declines, just before the arrival of Trevor's girlfriend Jenny Griffith, who asks the two friends what they were discussing. Mike uses this as an opportunity to leave.\nthumb|right|250px|Harvey in bed with the waitress",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a0f46-1dce-11ee-b06f-52b307fec202",
            "Elsewhere, Harvey and Jessica are discussing their latest victory over dinner, and Jessica tells him that she has a new, major client for him. When a waitress approaches their table, Jessica gloats about Harvey, saying that he is the best closer in the city. The waitress assumes that he is a baseball player, but when Harvey tells her that he is an attorney, she becomes uninterested and leaves, just as Harvey begins to flirt with her. Jessica then teases him about not being the best closer, at least in that situation. However, the next morning, the waitress awakens in Harvey's bed, and after only a small amount of persuasion, Harvey proceeds to have sex with her again.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a0f5a-1dce-11ee-b06f-52b307fec202",
            "Mike visits his grandmother, Edith Ross, in the nursing center, and after some joking between them, gets her to take her pills. Edith then asks Mike to stop doing what he has been doing, telling him that while life hasn't been kind to him, she wants him to start living up to his potential. After a moments pause, Mike promises to do so.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a0f78-1dce-11ee-b06f-52b307fec202",
            "At Pearson Hardman, Louis tells Jessica of his annoyance at her choosing Harvey to deal with Gerald Tate, and that he himself could have dealt with the situation. Jessica responds by saying that she disagrees, but their discussion is interrupted by the arrival of Harvey, and the two men immediately begin to taunt one another. Their discussion is ended by Jessica, who informs Harvey that he must hold interviews for a new associate now that he is a senior partner. Louis responds to the news by saying that he deserves the promotion, but Jessica reaffirms her decision.\nthumb|left|250px|Jenny and Mike",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a0fd2-1dce-11ee-b06f-52b307fec202",
            "At the nursing center, a nurse informs Mike that due to his grandmother's worsening condition, she will need to be moved to full-time care, or else she will be transferred to a state facility. However, Mike responds by saying that he will not allow his grandmother to be moved to a state hospital, and when the nurse says that he will have to come up with $25,000, he calls Trevor to tell him that he will accept his offer, at a price of $25,000. Trevor gives Mike the instructions for the transaction, and tells him to clean himself up for the deal at the hotel. However, after the call is ended, he finds out from the dealers that the transaction might be with undercover cops, and so the dealers decide to keep Trevor with them until the deal is through. At Trevor's apartment, Mike has just finished getting changed when Jenny arrives, and compliments him on his appearance. Mike then leaves, together with a briefcase full of weed.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a0ffa-1dce-11ee-b06f-52b307fec202",
            "At the Chilton Hotel, Harvey is interviewing Harvard graduates for the position as his associate. After the first few, Harvey gets tired of the \"Harvard clones\" and tells Donna, his trusted assistant, to give the candidates a hard time before sending them in and give him a wink if the say something smart, telling her that he is looking for another him. She does so to several prospective interviewees, but none of them stand out.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1018-1dce-11ee-b06f-52b307fec202",
            "At the same hotel, Mike is somewhat nervous before making the trade, and goes to the rest room to splash water on his face. When he reaches the room for the transaction, he sees two men picking at the lock and realizes that they could be cops posing as Trevor's buyer for a bust. He distracts them by talking to them directly before leaving, although they become suspicious of the briefcase in his hand, and so one of them follows him while the other remains by the room. Mike, remembering the Harvard Law interviews sign he had passed, proceeds to the room where the interviews are being held.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1036-1dce-11ee-b06f-52b307fec202",
            "As Mike runs frantically into the room, Donna calls the name of the next interviewee, Rick Sorkin. When Donna assumes that Mike is Rick, she presses him about being late, to which Mike honestly answers by saying he only wants to get away from the cops chasing him and he does not care for the interview. Thinking this was a smart remark, she winks at Harvey and sends him in. Soon after, the undercover cop following Mike storms into the waiting room, but soon leaves when he does not find him.\nthumb|right|250px|Harvey Specter and Mike Ross meet for the first time",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1054-1dce-11ee-b06f-52b307fec202",
            "Mike decides to go along with the Rick Sorkin persona, but as he approaches Harvey, his briefcase falls open, causing the marijuana packets to fall out in front of him. Mike tells Harvey the story of how he ended up there, and Harvey happily listens. Impressed at his tactics, Harvey offers Mike the associate position, with the $25,000 he needs as a signing bonus, which Mike accepts. Harvey, however, takes it back, saying Pearson Hardman only hires from Harvard Law, and that Mike has never even gone to any law school. Mike reveals that he consumes knowledge like no one else, and that he has actually passed the bar. Harvey quizzes Mike about the law, and Mike is able to give profound answers, to Harvey's amazement. Mike then manages to easily beat Harvey's own knowledge of the law, and although Harvey is initially hesitant about hiring Mike, he decides to do so when he realizes that if he does not, he will have to interview more Harvard clones, and on Mike's assertion that if he is",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1068-1dce-11ee-b06f-52b307fec202",
            "that if he is given the opportunity, he will work as hard as he can to prove he is better than the other interviewees.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1086-1dce-11ee-b06f-52b307fec202",
            "On Harvey's instruction, Mike disposes of the rest of his pot, but decides to keep the briefcase, storing it in a pizza box in his oven, and flies to Harvard to learn about attending school there. As the tour at Harvard Law is already fully booked, he cons another attendee into giving him his name badge, and then enters the tour in his place.\nthumb|left|250px|Rachel Zane and Mike Ross meet for the first time\nOn his first day at Pearson Hardman, Mike meets Rachel Zane, who is sent to give him his orientation. After he immediately starts flirting with her, Rachel informs Mike that she is not interested, and that she will not be \"blown away by his dazzling degree\" even though she is \"just a paralegal\". Rachel then proceeds to give him a tour of Pearson Hardman, but brushes off his question about what she thinks of Louis.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a109a-1dce-11ee-b06f-52b307fec202",
            "Harvey arrives at Pearson Hardman in a good mood given his recent promotion, but finds that someone is removing the lettering marking his promotion from his door. Initially thinking that someone is messing with him, he is informed by Donna that Jessica wishes to speak with him\n\nAt the end of Mike's tour, Rachel admonishes him for not having taken any notes during the tour, and suggests that it is because he was too busy ogling her. However, Mike responds by repeating everything that he had been told and correctly interpreting Rachel's silence regarding his question about Louis, though his answer does not go down well with Rachel, who calls him a show-off.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a10ae-1dce-11ee-b06f-52b307fec202",
            "In Jessica's office, Harvey is informed by his superior that Gerald Tate discovered he lied to him about his deal, and that he has fired Pearson Hardman, which is why Harvey's promotion had been reversed. Harvey attempts to justify his actions, and regain his promotion, but Jessica holds firm in her decision, saying that Gerald Tate might not have fired the firm if Harvey hadn't humiliated him, and that he should accept what has happened.\nthumb|right|250px|Mike in Harvey's office",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a10c2-1dce-11ee-b06f-52b307fec202",
            "Harvey returns to office to find Mike there ready to begin, but he informs his new associate that due to him losing his promotion, he has to let Mike go, as he cannot afford anyone finding out that he lied about Mike having attended Harvard, an admission that is overheard by Donna. Mike responds by saying that if he is fired, he could always reveal that Harvey lied anyway, which would definitely lead to Harvey loosing his licence. Harvey realizes that his associate is right, and tells him he is rehired before leaving. He then proceeds to inform Jessica that if he isn't given his promotion back, he will go to another law firm and take his clients with him. When Jessica threatens to put him in front of the ethics board in response, Harvey tells her that if she does, he will do the same to her, as she was obliged to inform them when Harvey lied to Gerald Tate, a tactic similar to what Mike had threatened to do to him. With a slight smile, Jessica agrees to give Harvey his promotion, on",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a10e0-1dce-11ee-b06f-52b307fec202",
            "his promotion, on the condition that he take a pro-bono case. Harvey is initially reluctant to accept the case, but eventually agrees, though he passes the case on to Mike despite Jessica warning him otherwise.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a10f4-1dce-11ee-b06f-52b307fec202",
            "thumb|left|250px|Mike meeting Nancy",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1108-1dce-11ee-b06f-52b307fec202",
            "Mike goes to meet Nancy, the client in the pro bono case, and she relays to him her story, informing him how she had been sexually harassed by her boss, Charles Hunt, and then later fired form Devlin McGregor when she rebuffed his advances, despite relaying her situation to Human Resources. Mike tells Nancy that he will help her with her problem. He goes to see Harvey, telling him that the defense had sent over the investigation files, but Harvey informs his new associate that they had only sent over the files because that is where they wanted them to look. He teaches Mike that law is about \"pressing until it hurts\", and that since it was likely Hunt had done the same thing before, he should get a former employee to testify against him, and subpoena the persona files of every woman that had left the firm during Hunt's tenure. Mike reveals that he had had the same idea, but doesn't know how to fill out a subpoena. His request for help from Donna is immediately rebuffed, and he is",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1126-1dce-11ee-b06f-52b307fec202",
            "rebuffed, and he is instead told by Harvey to go see his suit guy, and spend some money on a new suit.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a113a-1dce-11ee-b06f-52b307fec202",
            "At the end of the day, Mike gets ready to leave, but he is stopped by Rachel, who tells him that Louis Litt wishes to see him. At Louis' office, Mike is given his own personal welcome from Louis, who informs Mike that he is considered the disciplinarian of the associates. Their discussion is interrupted by Gary Lipski, who is introduced to Mike as one of the most promising associates from the previous year. Louis questions Gary about one of his current tasks, but when Gary responds that he hadn't completed the task, he is promptly fired, leaving Mike looking flustered.\nthumb|right|250px|Trevor in Mike's apartment",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a114e-1dce-11ee-b06f-52b307fec202",
            "Mike returns home, only to find Trevor in his apartment. After questioning his appearance there, Mike berates Trevor for setting him up with the undercover cops. Despite Trevor's objections that it wasn't his fault, and that he had been held by the dealers to stop him from warning Mike, Mike requests that Trevor leave, which he does with some resistance. Checking his oven, he finds that the briefcase is still hidden there.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1162-1dce-11ee-b06f-52b307fec202",
            "The next day at Pearson Hardman, Mike informs Harvey that Devlin McGregor is fighting the subpoena for their personnel files, and that they had filed a motion to dismiss due to their lack of evidence. Harvey proclaims this as good news, and at Mike's surprise, tells him that the fact they do not wish to hand over the files shows they are looking in the right place.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1176-1dce-11ee-b06f-52b307fec202",
            "Mike approaches Rachel and requests her assistance in finding evidence to fight the motion to dismiss. Rachel denies his request as she has several other cases that require her attention, but when Mike informs her that the hearing for his case is the next day, and that he was told by Donna that she is the best researcher at the firm, she agrees to look over the motion. Mike annoys Rachel when he objects to the fact she has her own office, but after explaining his client's position, Rachel consents to assist Mike in finding a precedent to support their case. The two of them go to the Pearson Hardman library and order dinner.\n\nAt a bar, Harvey is in discussion with an attractive women. He begins to flirt with the woman, but she rebuffs his advances. After thanking the woman for her assistance with one of his clients, he offers to pay their cheque, despite the woman's objections. She hands him a large brown envelope, before leaving.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1194-1dce-11ee-b06f-52b307fec202",
            "Back at Pearson Hardman, Mike and Rachel are eating dinner and joking with one another. Mike enquires as to why she isn't a lawyer, and Rachel replies that despite her intelligence, she has so far been unable to pass the LSATs, and questions whether she would be able to pass the bar if she managed to do so. She jokingly asks whether there is someone that could take the test for her, which leaves Mike somewhat flustered. Harvey approaches the two of them, and asks how far along they are with their research. Mike responds by saying that they have yet to find anything, and Harvey questions his dedication to the clients problem, suggesting that he focus on the task at hand rather than flirting with Rachel, before leaving. Rachel responds to Harvey's statement by saying that their predicament is hopeless, and that they look like the bad guys putting the other side under duress, which sparks an idea in Mike's head. Flicking through one of the books in front of them, he finds something which",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a11a8-1dce-11ee-b06f-52b307fec202",
            "something which could be useful.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a11bc-1dce-11ee-b06f-52b307fec202",
            "thumb|left|250px|Harvey during the hearing\nThe next day, Mike shows what he found to Harvey, who concurs that it could be useful, and agrees to allow Mike to accompany him to the hearing, as it would be \"cruel not to let [him] witness [Harvey's] greatness\". At the hearing, using what Mike had given him, Harvey manages to convince the judge to rule in their favor, and Devlin McGregor is forced to hand over the files as requested.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a11da-1dce-11ee-b06f-52b307fec202",
            "Mike goes to the suit shop that was recommended by Harvey with the intention of purchasing a new suit. The employees at the shop are initially derisive given his appearance, but after Mike mentions Harvey's name, they become more accommodating. As he leaves the shop, he receives a call from Jenny, who says that she wants things to back to the way they were. Mike replies that he doesn't know if that can happen, before ending the call. Jenny relays what Mike said to Trevor, who is beside her, but he is unsure as to the reason for Mike's attitude.\nthumb|right|250px|Rachel and Mike in the conference room.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a11ee-1dce-11ee-b06f-52b307fec202",
            "Back at Pearson Hardman, Mike goes to see Rachel and informs her of the result of the hearing, thanking her for her assistance. Rachel receives a call, and informs Mike that the files from Devlin McGregor have arrived and placed in one of the conference rooms. Mike questions why the files were not instead sent to his cubicle, but after going to the conference room, they find out there are boxes and boxes of files that have been sent over. Rachel tells Mike that they are intending to bury him in paperwork, but Mike replies that \"they picked the wrong guy\". Harvey, who is behind the two of them, requests that Mike have it done by the end of the week, before leaving to see a new client.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1202-1dce-11ee-b06f-52b307fec202",
            "Harvey arrives at a tennis court to meet John Dockery, the new client, before handing him a brown envelope. Dockery opens the envelope, which contains an incriminating photo of himself in bed with a woman. He furiously asks Harvey what it is, to which Harvey responds by saying that it is \"a picture of [Mr. Dockery] having sex with a woman who isn't Mrs. Dockery\". Harvey states that he was asked to find out where Dockery is vulnerable to corporate takeover, and indicates the contents of the envelope as such. He suggests that Dockery trade shares with his wife so that she cannot vote him out of his own company, which he reluctantly agrees to.\nthumb|left|250px|Mike in Harvey's office after working all night",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1216-1dce-11ee-b06f-52b307fec202",
            "In Harvey's office, Mike informs his superior that he has discovered where Devlin McGregor do not want them to look. He relays to Harvey information regarding an employee that was dismissed from the company many years previously, but that the employee's name is missing, and suggests that the dismissed employee is the woman they are looking for. Harvey calls Devlin McGregor's lawyer, and mentions what Mike had found, threatening sanctions if the missing information is not returned.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1234-1dce-11ee-b06f-52b307fec202",
            "Mike goes to see Nancy, and asks whether she knows the woman that was dismissed, Joanna Webster. She states the she does not, and Mike tells her that Devlin McGregor is trying to hide her from them, and that it is likely the same thing that was done to Nancy was done to Joanna. Nancy implores Mike to find her, which he agrees to do.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1248-1dce-11ee-b06f-52b307fec202",
            "Mike is sitting on some steps in front of a house, when a woman approaches him carrying some shopping. After asking whether she is Joanna Webster, he informs her that he is a lawyer, and states that he wishes to talk to about her time at Devlin McGregor. She brushes him off and proceeds indoors, but Mike requests that she allow him to tell her about his client, and she agrees. In her house, Joanna tells Mike about what happened to her, but is reluctant to help him with his case. Mike pushes her to help him, but she declines.\nthumb|right|250px|Jessica berates Harvey for passing the case on to Mike",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1266-1dce-11ee-b06f-52b307fec202",
            "Back at Pearson Hardman, Harvey is at his desk when Mike enters looking somewhat forlorn. Harvey inquires as to what happened with Joanna, to which Mike initially replies that he failed, before revealing that he managed to convince her to testify. As Mike leaves, Jessica enters and asks Harvey how everything is going with his pro bono case. Harvey answers that he had managed to convince a witness to testify, but after being questioned as to the witness' name, Jessica reveals that she knows he passed the case on to Mike, and is unsympathetic when Harvey states that he has \"higher profile cases\" to deal with. Jessica reminds Harvey that he was \"a screw-up\" when Harvey first started at Pearson Hardman, and that she paid for him to go to Harvard. Harvey replies that he closed the Dockery case, but Jessica berates him for breaking his promise to her and then lying about it, and tells him that he better win the case.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a127a-1dce-11ee-b06f-52b307fec202",
            "Mike returns home to his apartment, only to find that it has been ransacked. He rushes to the cooker, and finds that the briefcase is still hidden there. He calls Trevor, and angrily asks him why he broke into his apartment. Trevor replies that he needs the briefcase back, and when Mike asks whether he ever cared about repairing their friendship, replies that Mike was the one that doesn't care. Mike lies and says that he got rid of the briefcase when he was being chased by the cops, but Trevor hangs up the phone before he can finish.\nthumb|left|250px|Louis giving Mike a drug test",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a128e-1dce-11ee-b06f-52b307fec202",
            "The next day, Mike takes the briefcase with him to Pearson Hardman, and becomes increasingly nervous when Louis informs him that it is time for him to take a mandated drug test. Mike attempts to briefly excuse himself so he can deposit the briefcase in his cubicle, but Louis refuses his request, and Mike is forced to go with him, briefcase in hand. On the way to the medical office, Louis informs Mike that his cousin, Mitch Samberg, was in the same year as Mike, but that he does not recall Mike being present. Mike initially states that he does not remember Mitch, but after Louis becomes suspicious, Mike flashes back to when he attended the Harvard tour, and recalls seeing Mitch's name on a list of the top ten students from the previous year. He recants his previous statement, and manages to convince Louis that he does remember Mitch.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a12a2-1dce-11ee-b06f-52b307fec202",
            "At Mike's cubicle, Harvey phones Donna to ask where his associate is, but his assistant is unaware of his location. Back at the medical office, Mike is handed a cup by the doctor, and prepares to enter the restroom, together with his briefcase. However, the doctor requests that he leave the briefcase outside restroom, otherwise he must check its contents to be sure it does not contain another sample. Not wanting to reveal its contents, Mike agrees.\n\nWhen he is finished, he picks up his briefcase and heads to his cubicle, locking the briefcase in the cabinet. Harvey appears and informs Mike that the deposition for their case is that afternoon, and that he wants Mike to grill Joanna about anything in her background that might use against her.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a12b6-1dce-11ee-b06f-52b307fec202",
            "At the deposition, Joanna speaks about her time at Devlin McGregor, and how after working there for several months, her boss, Charles Hunt, attempted to have sex with her. She relays that she requested a change in assignment, but was fired two months later for \"having a bad attitude\". Charles Hunt, who is present at the deposition, scoffs at Joanna's statement, proclaiming it to be ridiculous. Joanna berates Charles for his outburst, and questions why he is even at the deposition, to which Hunt's lawyer replies that Charles has every right to be there. He then asks Joanna whether she considers herself a truthful person, which Joanna agrees to, before questioning her regarding her arrest when she was seventeen, which contradicts Joanna's suggestion that she had never been arrested. The revelation leaves Joanna rattled, and after the lawyer suggests that she is also lying about what happened during her time at Devlin McGregor, she storms out.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a12d4-1dce-11ee-b06f-52b307fec202",
            "Harvey and Mike follow Joanna out of the room, and Harvey berates Mike for having not found out about Joanna's arrest. Mike defends himself by saying that he grilled Joanna about her background, but as the record of her arrest was sealed, there was no way he could have known. Outside Pearson Hardman, Mike manages to catch up with Joanna, but she is unwilling to stop, saying that what happened in the deposition was why she didn't want to testify. Mike attempts to calm her down by saying that what happened doesn't matter, and he still needs her to testify, as they do not have enough time to find another witness, but she leaves, telling Mike not to contact her again.\nthumb|right|250px|Mike arguing with Harvey",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a12e8-1dce-11ee-b06f-52b307fec202",
            "Back at his cubicle, Mike is staring at the briefcase that he locked in his cabinet. After a moment's contemplation, he grabs the briefcase, and drops his key card on his desk. As he leaves Pearson Hardman, Harvey catches up with him, and questions him regarding what happened with Joanna, and Mike replies that he couldn't fix the problem. Harvey, holding Mike's key card, asks his associate if he is going to quit, and Mike replies that if he doesn't, Louis will fire him anyway for screwing up the case, much like he did to Gary Lipski. Harvey tries to encourage Mike to go and see Joanna again, and Mike replies that there is no way to fix the problem, and suggests that Harvey go and see her in his place. After Mike suggests that Harvey hasn't stood up for him, Harvey replies that he \"put [his] ass\" on the line for Mike, and questions whether Mike has the courage to keep working at Pearson Hardman. When Mike replies that he does, Harvey points to the briefcase he is holding as evidence",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a12fc-1dce-11ee-b06f-52b307fec202",
            "holding as evidence that he is still undecided on whether he wants out of his old life. He walks away, leaving Mike alone.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1310-1dce-11ee-b06f-52b307fec202",
            "In the bathroom at Pearson Hardman, Harvey confronts Louis about threatening to fire Mike. When Louis responds in confusion, Harvey tells him that he knows about Louis firing Gary Lipski in front of Mike. Louis starts smiling, and informs Harvey that Gary works in the mailroom, and that him firing Gary in front of Mike is simply a ploy he uses to let new associates know what is expected of them. Louis' actions make Harvey realise something regarding his sexual harassment case, and he abruptly leaves.\n\nAt the medical center, Mike enters his grandmother's room as she is sleeping. She awakens, and Mike informs her that he wishes to quit his job at Pearson Hardman. He receives some reassuring words from his grandmother, who makes him promise not to leave Pearson Hardman unless they \"rip [him] out\".",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1324-1dce-11ee-b06f-52b307fec202",
            "Harvey confronts Joanna at her house, and reveals to her that he knows she never worked at Devlin McGregor, and that she will go to jail unless he tells him what happened. After some hesitation, Joanna reveals that her job was to waste their time until after trial, so they would not have enough time to find another witness. After Joanna says that she does not want to go to jail, Harvey informs her of what she needs to do.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1342-1dce-11ee-b06f-52b307fec202",
            "Trevor is eating dinner with Jenny when Mike enters holding the briefcase, and hands it to Trevor, saying that he no longer needs it. He walks into Trevor's room and re-appears holding several of his suits, before opening the briefcase to reveal the drugs, to Trevor's annoyance and Jenny's surprise, proclaiming them to be even.\nthumb|left|250px|Harvey and Mike in Harvey's office\nThe next day, in Harvey's office, Mike apologizes for his behavior, but Harvey reveals to his associate that when he first started, he \"quit once a month\", and only told Mike what he needed to hear. He then hands Mike a file, which Mike reads with some amazement, and on Harvey's suggestion, leaves to \"press until it hurts\".",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a1356-1dce-11ee-b06f-52b307fec202",
            "In a courtroom, Mike hands Hunt's lawyer several files, detailing payments and phone calls from Hunt to Joanna prior to her testimony, and an affidavit from Joanna stating that she was paid by Hunt to falsely testify, as Nancy watches on. Mike informs Charles Hunt that witness tampering is a criminal offence, one that carries a jail sentence. Hunt states that they will never find someone to prosecute such a small charge, only for Harvey to reveal that he went to law school with the current US attorney in New York, and was the best man at his wedding. Hunt suggests he is bluffing, but Harvey pulls out his phone and shows him several pictures confirming his statement. Hunt's lawyer asks what they want, and agrees to all of Mike's terms, which includes Nancy getting her job back, despite Hunt's objections. They leave, and Nancy thanks Mike for his help.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bb9a136a-1dce-11ee-b06f-52b307fec202",
            "As they leave the courtroom, Mike questions Harvey on why he went to Joanna's house, suggesting that he did so because he cared. Harvey replies that he did so because it was his job, and hands Mike a new case they will be working on.",
            {
                "title": "Suits",
                "ep_title": "Pilot",
                "season_num": 1,
                "ep_num": 1
            }
        ],
        [
            "bce8aae2-1dce-11ee-b06f-52b307fec202",
            "Plot\nthumb|left|250px|Harvey refuses to allow Mike to join him in the conference room\nMike is playing air hockey with Wyatt, a client, and has already lost four games in a row. Harvey approaches them and informs Wyatt that several investors have arrived, and encourages him to set get up in the conference room. Wyatt is initially nervous when he cannot find the $20 million prototype for the satellite phone he has developed, but Harvey is unfazed and pulls the prototype out of Wyatt's breast pocket. Seeing the investors arrive, they walk towards the conference room, and Harvey relays to Wyatt what he has to say. Mike goes to follow them in, but Harvey refuses to allow him to do so, saying that Mike has not yet earned the privilege to sit at the \"adult table\", and instead requests that he go back to Pearson Hardman and file a patent for the prototype. Mike informs his superior that he doesn't know how to file a patent, but Harvey is unsympathetic.",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8abbe-1dce-11ee-b06f-52b307fec202",
            "thumb|right|250px|Mike informs Rachel of the deal he made with Gregory\nAt Pearson Hardman, Mike goes to see Rachel to get her help in filing a patent, but she shuts him out of her office. In the break room, Mike meets Gregory Boone, who reveals that he knows how to file a patent claim, giving Mike an idea.",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8abe6-1dce-11ee-b06f-52b307fec202",
            "Rachel approaches Mike's cubicle, but he makes her wait in return for her lack of help with his patent claim. He informs Rachel that he negotiated a deal with Gregory to get the claim filed, and that he has to proof the Bainbridge briefs for him in return. With a slight smile, Rachel informs Mike that she was asked by Gregory to give him a key card to the Pearson Hardman print room, and that Gregory called him \"a sucker\". In the print room, Mike discovers that the Bainbridge briefs consist of several thousand pages, agreeing with Gregory's assertion that he is a sucker.\nthumb|left|250px|Louis questions Mike on why he is doing Gregory's job",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8abfa-1dce-11ee-b06f-52b307fec202",
            "The next day, Mike meets Harvey and informs his superior that he has been up all night proofing the Bainbridge briefs. Harvey questions Mike on why he has not yet received confirmation of the patent claim for the prototype having been filed, and becomes concerned at Mike's hesitance, informing his associate that the patent claim is the only thing holding up their deal. Mike lies to Harvey and replies that the claim is on his desk. He goes to see Gregory, but finds out that he has not yet filed the patent claim, much to Mike's frustration. Gregory informs Mike that he will file the claim when Mike has finished proofing the Bainbridge briefs, and refuses to do so any sooner despite its importance. Mike rushes to finish his task, before being approached Louis, who questions why he is doing so given that the job was supposed to be Gregory's. Mike lies and says that he volunteered to take the job, adding that Gregory didn't even want him to do so. However, Louis reveals that he knows what",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8ac0e-1dce-11ee-b06f-52b307fec202",
            "that he knows what happened with Gregory, praising him for his loyalty to his fellow associate. Louis questions why Mike didn't ask Harvey for help with filing the claim, and after Mike responds that Harvey was busy, Louis tells Mike that he can always come to him if he needs assistance, and hands Mike the patent claim that should have been filed. Thanking Louis for his assistance, Mike rushes to Harvey's office to hand him the claim.",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8ac22-1dce-11ee-b06f-52b307fec202",
            "thumb|right|250px|Mike and Louis in Louis' office\nLater on, Louis calls Mike to his office, and commends him for his work on the Bainbridge briefs. He informs Mike that he likes to pick a \"pony\" from the herd of associates each year, and asks whether Mike wishes to be that \"pony\". Mike responds that he works for Harvey, but Louis is unfazed, and invites Mike to lunch with him the next day at the tennis club.",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8ac36-1dce-11ee-b06f-52b307fec202",
            "Back at his cubicle, Mike discovers Harvey waiting for him, who promptly informs his associate that their patent claim has been denied, as a similar claim had been filed before theirs. He reveals to Mike that he knows he lied about filing the claim, and Mike tries to defend himself by saying that he told Harvey he didn’t know how to file such a claim. Harvey responds by pointing out that Mike lied to him about filing the claim, and suggests that he phone the Patent Office to find out who filed the other claim, and that they will try to get an injunction to stop them releasing their product first.\nthumb|left|250px|Harvey, perplexed at the judge's attitude toward him",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8ac4a-1dce-11ee-b06f-52b307fec202",
            "At the court house, Harvey is on the phone with Wyatt trying to calm him down regarding the patent issue. As he ends the call, Mike hands him a folder containing information on the company that filed the competing claim. As they enter the court room, Harvey is immediately berated by the judge, Donald Pearl, for having his phone in his hand and for their lateness, fining Harvey $1,000 for \"failing to follow the posted rules of the court\". The opposing counselor petitions the judge to dismiss the case, and in turn Harvey presents a request for an injunction, but the judge cuts him off mid-sentence, and questions why he was not given a courtesy copy of the injunction. Scolding him again for his attitude, the judge denies his request for an injunction. After issuing his verdict, the judge angrily tells Harvey \"better luck next time\", prompting Harvey to visit the judge in his office. Harvey questions the judge's behaviour towards him in the court room, his unwillingness to consider his",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8ac5e-1dce-11ee-b06f-52b307fec202",
            "to consider his argument, and his apparent hatred of him. The reason for the judge's attitude is revealed when he claims that Harvey had an affair with his wife Lauren, much to Harvey's bewilderment.",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8ac72-1dce-11ee-b06f-52b307fec202",
            "thumb|right|250px|Harvey visiting Lauren Pearl at an art gallery\nOutside the court house, Mike questions Harvey on what happened, but Harvey doesn't respond, phoning Donna to request she clear his afternoon. He directs Mike to return to Pearson Hardman and file an interference claim with the Patent Office, which may give them a chance to win their case. Taking his leave, he visits an art gallery and approaches a woman who works there, revealed to be the judge's wife, Lauren. He questions her on why she lied to her husband about having an affair with him, reminding her that he sent her home after she made a pass at him. Lauren is unsympathetic, however, and refuses to tell her husband the truth, informing Harvey that her husband paid more attention to her after he believed she had had an affair.",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8ac86-1dce-11ee-b06f-52b307fec202",
            "Back at Pearson Hardman, Mike is speaking rather agitated on the phone with the Patent Office, papers spread out over his desk. Louis approaches him to remind him of their scheduled lunch, but Mike informs Louis that he cannot attend due to the importance of the task he has to do for Harvey. Louis is undeterred, however, and promptly ends Mike's call, reminding Mike that he works for him too. When Mike repeats the importance of filing the interference claim, Louis calls over Gregory, and requests that he file the claim in Mike's place, much to Gregory's annoyance.\nthumb|left|250px|Mike and Louis at the tennis club",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8ac90-1dce-11ee-b06f-52b307fec202",
            "At the tennis club, after easily beating Mike, Louis strikes up a conversation with another attendee, Tom Keller, who runs his own fantasy football site, and invites him and his companion to play, but Tom is uninterested and brushes him off. Louis informs Mike that despite the fact that Tom's company generates $200 million a year, he still uses one of his fraternity brothers as his general counsel, before suggesting they hit the showers.",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8aca4-1dce-11ee-b06f-52b307fec202",
            "Harvey goes to see Pearl once again, and barges into his office despite the protests of Pearl's assistant. Harvey informs Pearl that if he refuses to renege on his previous judgement and sign his injunction, he will sue him and have his verdict overturned anyway, ruining Pearl's \"sterling reputation\". However, Pearl reveals that he has decided to leave the bench, and is divorcing his wife as a result of her affair with Harvey. He makes a proposal to Harvey, stating that he will give Harvey his injunction if he is willing to sign a document confirming that he slept with Pearl's wife, which would prevent her from claiming from taking half of his money.",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8acb8-1dce-11ee-b06f-52b307fec202",
            "Whilst being driven back to Pearson Hardman, Harvey receives a call from Wyatt, who professes his nervousness regarding the state of their deal. Harvey reminds Wyatt of similar instances that have happened previously when Wyatt was equally nervous, and that they agreed he would remind Wyatt of those times. He promptly ends the call, despite Wyatt's protests.\nthumb|right|250px|Mike striking up a conversation with Tom Keller",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8accc-1dce-11ee-b06f-52b307fec202",
            "Back at the tennis club, Mike and Louis are getting changed, and Louis again bemoans his failure to convince Tom to converse with him, saying that Tom doesn't believe him to be cool because he doesn't smoke pot. He suggests that Mike may be able to have more luck as he is younger, and asks Mike whether he has ever done pot. Mike replies that he doesn't smoke, but Louis states that the drug test Mike took reveals otherwise, before handing him a copy of his test. Louis then requests that Mike smoke pot with Tom to help him land Tom as a client, and that it would be bad for Mike if he refused to do so. He leaves to take a shower just as Tom arrives, and Tom states to Mike that Louis creeps him out. Mike informs him that he is a fan of his site, and easily proves his knowledge of the game. Tom commends Mike for his team selection, to which Mike replies that he would have done better had he not been high before the draft.",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8ace0-1dce-11ee-b06f-52b307fec202",
            "thumb|left|250px|Mike riding in the elevator with Jessica whilst he is high\nMike returns to Pearson Hardman, having just got high with Tom, and meets Jessica in the elevator. She questions Mike on how he is doing working with Harvey, to which Mike replies that he is learning a lot from him, though he does so with some degree of nervousness. He returns to his cubicle and is approached by Gregory, who hands him the interference claim that he filed on Mike's behalf. Mike immediately delivers the claim to Harvey, barging into his office whilst Harvey is on the phone with Wyatt. Harvey berates him for doing so, and comments on Mike's strange appearance, asking him why he looks so flushed and sunburnt. Mike informs Harvey about his lunch at the tennis club with Louis, but after asking how he then had the time to file the interference claim, Harvey realizes that Mike is high, and tells him to leave his office.",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8acea-1dce-11ee-b06f-52b307fec202",
            "Mike is washing his face in the restroom when Rachel suddenly appears. Mike questions her appearance, but Rachel informs him that he is in the ladies room. She inquires about his appearance, but Mike leaves, stating that he needs to get some air. Outside Pearson Hardman, Mike tells Rachel what happened at the tennis club with Tom Keller, and chastises himself for having let Harvey down, but Rachel replies by saying that Harvey was the one that let Mike down, and that he has to tell Harvey what happened.\nthumb|right|250px|Mike pleading with Harvey to let him keep his job\nHarvey is on the phone with the counsel for Velocity, the firm that filed the competing patent claim, but is unwilling to accept their low settlement offer. He counters by claiming that the verdict on his injunction will be over turned, and after some deliberation, they double their offer to $20 million, which would match the cost of creating the prototype.",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8acfe-1dce-11ee-b06f-52b307fec202",
            "The next day, Mike goes to see Harvey in his office, and tells him what happened at the tennis club, and how Louis blackmailed him with his failed drug test. Harvey, however, is still angry that Mike followed Louis' orders over his own, and states that Mike should come to him if something like that ever happens. Mike responds by pointing out that he came to Harvey regarding filing the patent claim, and that Harvey should be showing some loyalty to him, but Harvey counters by saying that he was the one to take the fall with Wyatt, and that if Mike wants loyalty from him, he should earn it. Mike pleads with Harvey to trust him, even offering to work for free. This gives Harvey an idea on how to deal with the patent problem, and gets Donna to inform Wyatt he is on his way to see him. Donna then informs them that Jessica wishes to see Mike in her office.\nthumb|left|250px|Jessica congratulating Mike on landing his first client",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8ad12-1dce-11ee-b06f-52b307fec202",
            "In Jessica's office, Jessica congratulates Mike on landing his first client in the form of Tom Keller, remarking that he reminds her of Harvey. Louis then enters with Tom, wishing to discuss with Jessica some concerns that Tom has regarding the retainer. Tom suggests that it isn't a big deal, but Louis insists. As Jessica and Louis discuss the issues Tom has, Mike approaches him and asks why he is working with Louis, when before he said that Louis creeps him out. Tom, however, says that \"a little deviousness is the thing you look for in a good lawyer\", and that he has insisted that Mike be his point man. Mike thanks Tom, saying that Jessica would never have known he existed if Tom hadn't done that, as Louis would never have told her that he helped land Tom as a client. Tom says the three of them will make a pretty good team, but Mike proposes another idea.\nthumb|right|250px|Harvey and Wyatt discussing the settlement offer from Velocity",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8ad26-1dce-11ee-b06f-52b307fec202",
            "Harvey is talking to Wyatt about the $20 million offer the other company has made, an offer that Wyatt is less than enthused about taking, but Harvey informs him that they are going to offer any better. Wyatt asks Harvey whether he thinks he should take the offer, and Harvey replies that he thinks Wyatt should tell them to \"shove it up their ass\". They go to discuss the settlement with the opposing company, and inform them that rather than fighting the issue in court, they are instead going to release the specifications for the satellite phone on the web for free in 48 hours. The opposing lawyer says that they will file an injunction, but Harvey informs him that by the time they have, the specifications will already be on-line, and Wyatt will have credit for the design, which would be worth more than the settlement offer they have made.",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8ad3a-1dce-11ee-b06f-52b307fec202",
            "Harvey goes to see Judge Pearl, and informs him that there is an investigation into the his attempt to blackmail Harvey, suggesting that if he was willing to do it to him, he has probably done it before. He then informs Pearl that, despite what he thought, he never slept with Lauren, but that now they are getting divorced, she is free to date whomever she likes, including him.\nthumb|left|250px|Louis attempting to blackmail Mike into taking another drug test",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8ad4e-1dce-11ee-b06f-52b307fec202",
            "Back at Pearson Hardman, Harvey visits Mike in the file room, and asks him to prepare a settlement memorandum for the case with Wyatt, saying that the opposing company has agreed to settle for $400 million. He then gives Mike his real drug test results, which shows that Mike passed, and that Louis used a fake test to blackmail him. Harvey says that he is going to have a talk with Louis, but Mike convinces Harvey to let him go instead. Mike shows the real test results to Louis, and berates him for blackmailing him into doing what he wanted. Louis is unsympathetic, however, and says that because of what he did, Jessica knows Mike's name now, and they managed to bring in a big new client for the firm. Mike agrees, but says that he intends to tell Jessica exactly what Louis did. Louis tried to get Mike to run another drug test, which he knows he will fail, but Mike informs him that according to the Pearson Hardman drug policy, Louis has to wait three months before requesting another drug",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bce8ad58-1dce-11ee-b06f-52b307fec202",
            "another drug test. As he leaves, he tells Louis that he spoke to Tom Keller, and convinced him that he would do better working with Mike and Harvey, rather than with Louis, leaving Louis looking dumbfounded.",
            {
                "title": "Suits",
                "ep_title": "Errors and Omissions",
                "season_num": 1,
                "ep_num": 2
            }
        ],
        [
            "bdf60984-1dce-11ee-b06f-52b307fec202",
            "Plot\nthumb|250px|\"Eight o'clock means eight o'clock.\"\nMike Ross is running late for his meeting with Harvey Specter at the Gotham Car Club. Meanwhile, Harvey is checking out a Tesla when Laurence shows up, also wanting the Tesla. The two decide to quiz each other about the car, and whoever knows more about it to see gets to test drive it. Harvey wins but decides to let Lawrence get the car anyway. When asked why he let him have it, Harvey says that it never hurts to have man with a 2 billion hedge fund to owe you one, and that he merely competed with him first so Lawrence would feel like he actually does owe Harvey one. Harvey then rents out a vintage car instead and leaves a note for Mike to meet him at the Javits Center, and leaves a message with the car saleswoman about Mike's tardiness.\nthumb|250px|left|\"Wow. Yeah, he really appreciates what you've done for the company.\"",
            {
                "title": "Suits",
                "ep_title": "Inside Track",
                "season_num": 1,
                "ep_num": 3
            }
        ],
        [
            "bdf60d94-1dce-11ee-b06f-52b307fec202",
            "At a car show, Harvey tells Mike about the first client he ever brought to the firm: Avery McKernon, the late CEO of McKernon Motors. He then introduces him to Dominic Barone, the engineer responsible for the winning engine of McKernon Motors. And since Mike will now be handling their paperwork, Harvey then introduces him to Robert Stensland, the new CEO of the company, who is initially skeptical about him but is impressed when Mike talks about his 364-page lease terms.",
            {
                "title": "Suits",
                "ep_title": "Inside Track",
                "season_num": 1,
                "ep_num": 3
            }
        ],
        [
            "bdf60e3e-1dce-11ee-b06f-52b307fec202",
            "Robert shocks Harvey when he informs him of his plan to sell their factory land here in the U.S. and move manufacturing overseas, saying that \"the real asset of McKernon Motors is the name\". Harvey disagrees with him, later telling Mike that the asset is the quality, but Harvey decides not to tell this to Robert. As a lawyer and a racing-junkie, Harvey knows that these plans will jeopardize the company, which would in turn affect the firm through its connection.\n\nHarvey tasks Mike to find a flaw in the company's bylaw that will solve this problem. It only takes him one all-nighter to discover that Robert Stensland is actually still only the interim CEO of McKernon Motors and that he has to be officially voted in by the board in order to move the factory. Mike and Harvey just have to find the right man to replace Stensland.",
            {
                "title": "Suits",
                "ep_title": "Inside Track",
                "season_num": 1,
                "ep_num": 3
            }
        ],
        [
            "bdf60e70-1dce-11ee-b06f-52b307fec202",
            "At the office, Jessica tells Harvey to act humble during his senior partner initiation. During the meeting, an ongoing tradition is leading the new partner to believe that he must give his buy-in money of half a million dollars on the spot, to which Harvey acts surprised to hear before the partners laugh at their successful prank. After the conference, however, Harvey reveals to Jessica that he had the money all along and was merely trying to be humble.\nthumb|250px|The foodie and \"her view\"\nAlso, Louis tells Mike to organize the traditional \"rookie dinner\". During the conversation, Louis realizes that something more is going on with the McKernon Motors deal.",
            {
                "title": "Suits",
                "ep_title": "Inside Track",
                "season_num": 1,
                "ep_num": 3
            }
        ],
        [
            "bdf60e98-1dce-11ee-b06f-52b307fec202",
            "Mike then goes to both Harvey and Rachel to try and ask for their advice, but both provide him no help. Harvey, however, tells him to take the dinner seriously and believe that things like that matter if he wants to get ahead in the business. Mike realizes that he needs to get a better idea about what it means to be a lawyer and how to build up a strong work ethic.",
            {
                "title": "Suits",
                "ep_title": "Inside Track",
                "season_num": 1,
                "ep_num": 3
            }
        ],
        [
            "bdf60eb6-1dce-11ee-b06f-52b307fec202",
            "When Harvey hits a dead end with finding a replacement CEO, Mike suggests Dominic, the engineer. This, though, proves to be difficult for Harvey to accept since he and Dominic are not exactly on friendly terms.\nthumb|left|250px|\"You ditched us. Both.\"\nJenny then goes to Mike's apartment, furious at him for lying to her for years, and also for abandoning her and Trevor. He later visits his grandmother, Edith, and opens up to her about Trevor. Expecting her to tell him to be there for him, Mike is shocked when Edith tells Mike to cut Trevor loose, calling him the \"anchor\" that would keep Mike down.\nthumb|250px|\"You were also a junior partner until recently.\"",
            {
                "title": "Suits",
                "ep_title": "Inside Track",
                "season_num": 1,
                "ep_num": 3
            }
        ],
        [
            "bdf60ede-1dce-11ee-b06f-52b307fec202",
            "Meanwhile, Harvey was about to meet with Robert Stensland when he sees that Louis is in the restaurant as well and has also met with his client. He discovers that Louis was interfering with his plans by ensuring that Robert becomes CEO of the company, so he embarrasses Louis by telling Robert about the loophole of the bylaws he made years ago that may cause complications for him in the future if protocols aren't followed, which is that he has to be voted in by the board first. Robert agrees to delay his plans, and Harvey continues to embarrass Louis by pointing out that he was merely a junior partner and was not even supposed to be on the case.\nthumb|left|250px|\"These workers, they respect you.\"",
            {
                "title": "Suits",
                "ep_title": "Inside Track",
                "season_num": 1,
                "ep_num": 3
            }
        ],
        [
            "bdf60efc-1dce-11ee-b06f-52b307fec202",
            "Jessica then confronts Harvey about Robert Stensland, realizing that Harvey intends on getting him off McKernon Motors. Jessica tells him to drop it and just close the deal. Of course, Harvey does not listen and has Mike prepare a draft speech as he meets with their replacement CEO, Dominic Barone, to try and convince him, despite his own opinion now that they have no other choice. Dominic is initially reluctant, saying he has stayed underground to run the factory all this time and stayed away from his management rights because he hates boardroom politics.\nthumb|250px|Rachel helps Mike",
            {
                "title": "Suits",
                "ep_title": "Inside Track",
                "season_num": 1,
                "ep_num": 3
            }
        ],
        [
            "bdf60f24-1dce-11ee-b06f-52b307fec202",
            "When Devon and another co-worker makes fun of Mike about his plans for his rookie dinner, Mike intimidates them away but is obviously affected and even more frustrated by the predicament. Rachel sees this and feels sorry for Mike, so she arranges for dinner with him at a fancy restaurant. To not embarrass him further in front of the other associates, Rachel gives Mike a note and pretends that it is from Louis.",
            {
                "title": "Suits",
                "ep_title": "Inside Track",
                "season_num": 1,
                "ep_num": 3
            }
        ],
        [
            "bdf60f4c-1dce-11ee-b06f-52b307fec202",
            "Harvey and Mike prep Dominic for his speech at their conference room, but when Harvey and Dominic get into an argument, Harvey leaves Dominic with Mike, who then talks with Dominic about engines that leads to a pretty solid statement for Dominic's speech.",
            {
                "title": "Suits",
                "ep_title": "Inside Track",
                "season_num": 1,
                "ep_num": 3
            }
        ],
        [
            "bdf60f6a-1dce-11ee-b06f-52b307fec202",
            "Later that night, Mike and Rachel bond over dinner at the restaurant Rachel wants Mike conduct taste tests in to host his rookie dinner. They realize how different the worlds they came from were: Mike from a simple family with not much as he was growing up, and Rachel from a wealthy one. Rachel tells him that he should try more new experiences because it helps get his mind off work. Jenny then calls, but not wanting to ruin the night, he rejects the call.\nthumb|left|250px|\"Look, what matters is that you don't help me out, okay? I help you out.\"",
            {
                "title": "Suits",
                "ep_title": "Inside Track",
                "season_num": 1,
                "ep_num": 3
            }
        ],
        [
            "bdf60f88-1dce-11ee-b06f-52b307fec202",
            "On his way home, Mike receives a suspicious voice mail from Jenny about Trevor, so he visits Trevor to check up on him. Mike tells Trevor to stop dealing drugs and just stick with his computer business, and Trevor admits that he never actually had software clients. Mike offers him help and transition money, but Trevor, not knowing that Mike is now making a lot of money as a lawyer, does not accept it, saying that Mike should not be helping him because it should be the other way around. The confrontation leads to an argument about Jenny, and soon a brawl that ends their friendship.",
            {
                "title": "Suits",
                "ep_title": "Inside Track",
                "season_num": 1,
                "ep_num": 3
            }
        ],
        [
            "bdf60fb0-1dce-11ee-b06f-52b307fec202",
            "The next morning, it is time to introduce Dominic to the board as a contender for the position of CEO, but Harvey and Mike get their too late as Louis had already warned Stensland, who then moved the board meeting to an earlier time and was already voted in. The ratification of the sale of the company will be on the next day, and he also fires Pearson Hardman and Dominic.\nthumb|250px|\"If I win, I look great. If Louis wins, he looks great. Either way, you look great.\" \"You mean the firm looks great.\"",
            {
                "title": "Suits",
                "ep_title": "Inside Track",
                "season_num": 1,
                "ep_num": 3
            }
        ],
        [
            "bdf60fce-1dce-11ee-b06f-52b307fec202",
            "Back at the office, Harvey confronts Louis in front of Jessica about going to Stensland, but this time, Jessica sides with Louis. She chastises Harvey for trying to go after a client without telling her then gives Louis permission to go to Stensland to repair the relationship with the company and takes Harvey off the case. Harvey then realizes that Jessica sent Louis to Stensland in the first place and that Jessica would gain different advantages if either of their plans succeed. During the conversation, when Jessica reminds Harvey that he is now \"the firm\" because he has bought in, Harvey comes up with an idea. He has Mike get Dominic, saying it won't matter that Stensland is now CEO if they just buy the company.",
            {
                "title": "Suits",
                "ep_title": "Inside Track",
                "season_num": 1,
                "ep_num": 3
            }
        ],
        [
            "bdf60ff6-1dce-11ee-b06f-52b307fec202",
            "They later meet back at Javits Center with Laurence, and when Harvey tells him that the company is for sale, he seems more than eager, telling him what Harvey has been saying the whole time: that the asset of the company is not the name, but the engine quality. Harvey then introduces Laurence to Dominic to increase his interest.\nthumb|left|250px|\".. for way more goddamn money than the one in front of you right now.\"\nHarvey then proceeds to interrupt the board meeting Louis and Stensland has held, stating that Dominic can petition the board because he is an original employee and he was never fired because he was not given a three days notice (which was a lie Mike made up). Harvey, with Dominic's permission to his petition rights, then tells the board about the $250 million Laurence is offering for the purchase of the company, therefore beating out Stensland's deal.",
            {
                "title": "Suits",
                "ep_title": "Inside Track",
                "season_num": 1,
                "ep_num": 3
            }
        ],
        [
            "bdf61014-1dce-11ee-b06f-52b307fec202",
            "After Mike's good job on the case, Harvey was about to commend Mike when he apparently \"ruined it\" by commending himself. Mike's rookie dinner is then a success, and Harvey pays for his bill. Devon, who was previously making fun of Mike, commends him for the dinner, and Louis tells Mike to pay his bill, which would be quite high because Louis bought very expensive wines. Harvey then gives Jessica the good news, telling her that he did it for the firm, and he drives off in his Tesla with the saleswoman.\nthumb|250px|\"We're even.\"\nMeanwhile, Mike waits for Jenny outside her apartment. He apologizes to her and tells her Trevor is lying to her and that he is still dealing drugs, and that he has cut Trevor off. He tells her that he it is the last time he will rat anyone out, so she should not fall for anything similar ever again. They end up kissing, but Mike pulls away. This time, Rachel calls him and he rejects the call.",
            {
                "title": "Suits",
                "ep_title": "Inside Track",
                "season_num": 1,
                "ep_num": 3
            }
        ],
        [
            "bf11f094-1dce-11ee-b06f-52b307fec202",
            "Plot\nthumb|250px|left|\"The law is a very precise endeavor.\"\nLouis Litt and the associates play a Harvard trivia game after hours and Mike Ross is in the lead by one point against his rival, Seth Keller. During the double point round, Mike fails to answer the question about the Harvard Law dormitory tradition of getting square pizza from Pinocchio's. Seth then answers \"five\" when asked how many supreme court justices were from Harvard, and claims victory. Mike, however, points out that there are in fact six, including Ruth Bader Ginsberg who may have graduated from Columbia University but attended Harvard Law before then. Mike wins because he points out that Seth was not precise, just as Louis previously refuted Mike for not being precise. Having won, Mike receives a pro bono case of his own, but Mike is left uneasy about Louis and tells Harvey Specter that Louis may know his secret, which Harvey brushes off.\nthumb|250px",
            {
                "title": "Suits",
                "ep_title": "Dirty Little Secrets",
                "season_num": 1,
                "ep_num": 4
            }
        ],
        [
            "bf11f170-1dce-11ee-b06f-52b307fec202",
            "thumb|250px\nHarvey then sees Jessica Pearson and Quentin Sainz hugging in her office, immediately deducing that she has taken a case for him. Harvey warns Jessica about Quentin's case is a failure waiting to happen after hearing media coverage over the millions killed from the ALS drug that his company manufactured to the public. Jessica then shocks Harvey by revealing to him that Quentin is her ex-husband and then tells him that she wants him to take the case because Quentin's current girlfriend, Lisa Parker, does not want her on the case. Harvey has no interest in taking it because he fears that Jessica will interfere with his work.",
            {
                "title": "Suits",
                "ep_title": "Dirty Little Secrets",
                "season_num": 1,
                "ep_num": 4
            }
        ],
        [
            "bf11f1a2-1dce-11ee-b06f-52b307fec202",
            "Mike's case turns out to be a bedbug problem in a building owned by a Johnny Karinski who won't do anything about the problem. After filing a case to the housing department to take the situation to housing court, he visits his client, Frank, to inspect the apartment. They meet Karinski who threatens to kick Frank out for refusing to pay the rent, in which Mike states that it was legal if the apartment was inhabitable. However, he has yet to prove that in court.\n\nHarvey meets with Quentin and his girlfriend Lisa about the company's ALS death drug. Quentin explains that six terminal patients with other various health issues used his drug as a scapegoat for the other drug companies. He also claims that the drug was proven safe for eight years, and that the argument the media is putting out is baseless.",
            {
                "title": "Suits",
                "ep_title": "Dirty Little Secrets",
                "season_num": 1,
                "ep_num": 4
            }
        ],
        [
            "bf11f1c0-1dce-11ee-b06f-52b307fec202",
            "Harvey, Mike, and Quentin meet with Collin Church, a lawyer representing the legal dispute over the ALS drug. Collin refuses the settlement money, saying it should be much higher because his client was lied to by the company about the side affects and demands $250 million. When Quentin rejects the settlement, Collin reveals a poster with printed details of the side effects his clients had from using the ALS drug, threatening Quentin and Harvey that he intends to plaster them up. Harvey warns him that it's libel to do that, but Collin shows that he is willing to go lengths to receive the settlement he proposed. Harvey refuses to be extorted by Collins and leaves the room with Quentin, but Collins makes sure that Quentin knows that he must receive the $250 million in four days or he will take action. After hearing that Harvey refused the settlement offer, Jessica becomes angry at Harvey playing the \"bad lawyer\" and using dead patients as a small fraction to the millions that lived in",
            {
                "title": "Suits",
                "ep_title": "Dirty Little Secrets",
                "season_num": 1,
                "ep_num": 4
            }
        ],
        [
            "bf11f1de-1dce-11ee-b06f-52b307fec202",
            "that lived in court.",
            {
                "title": "Suits",
                "ep_title": "Dirty Little Secrets",
                "season_num": 1,
                "ep_num": 4
            }
        ],
        [
            "bf11f1f2-1dce-11ee-b06f-52b307fec202",
            "thumb|250px|left|\"I'm your first? Don't worry, I promise not to be gentle.\"\nMike's first case in housing court is against a professional lawyer, Vivien Tanaka. He loses miserably, leaving a bad first impression on the judge and failing to bring the required receipts for Frank's case. Louis lectures Mike, saying that the client he first brought in from the tennis courts helped save Mike's face from his loss in housing court and did little collateral damage to his reputation, but he had expected Mike to win.",
            {
                "title": "Suits",
                "ep_title": "Dirty Little Secrets",
                "season_num": 1,
                "ep_num": 4
            }
        ],
        [
            "bf11f210-1dce-11ee-b06f-52b307fec202",
            "Harvey and Mike takes the case to the court and reveal that Collin not only failed multiple lawsuits against pharmaceutical companies by threatening to publicize the case, leading to settlement agreements, but he also recycled his plaintiffs in order to win. Collin backfires by revealing Quentin's financial instability and bankruptcy prior to his drug's release stating that there was financial motive for advertising fraud. The judge then rules that the case will be taken to court. After Harvey's loss at court, Jessica takes the case herself, disapproving his lack of faith in Quentin.\nthumb|250px|\"My beautiful wife.\"\nMike and Rachel pose as a married couple looking for a luxurious home in an upscale neighborhood apartment building owned by Karinski to uncover some secrets. Instead of getting their information from the realtor, they ask to talk with the other inhabitants.",
            {
                "title": "Suits",
                "ep_title": "Dirty Little Secrets",
                "season_num": 1,
                "ep_num": 4
            }
        ],
        [
            "bf11f22e-1dce-11ee-b06f-52b307fec202",
            "Jessica and Quentin meet at Central Park to clear the air about their divorce. Jessica confronts him about his lies during the divorce and demands to know the rest of the secrets he has hidden from her in order for her to continue fighting for the lawsuit. She meets with Harvey later and they grab drinks. She reveals that Quentin is dying from ALS.\nthumb|250px|left|\"Like it or not... you're all in the same boat.\"",
            {
                "title": "Suits",
                "ep_title": "Dirty Little Secrets",
                "season_num": 1,
                "ep_num": 4
            }
        ],
        [
            "bf11f242-1dce-11ee-b06f-52b307fec202",
            "Harvey and Jessica meet with Lisa and made her confess that that she falsified drug trials to put it on the market to save Quentin. They then tell Quentin and give him options to make Lisa the scapegoat or fight with Collin and rebuild a new drug company. Instead, Harvey issues a conference with the six of the complainants and Collin to propose a compensation for the side effects Quentin was unaware about, showing them a video footage of Quentin suffering from ALS. The agreement is then made that these six ALS patients will have partial ownership of the drug company, which will then help save lives by conducting more research for the drugs that could help others like them.\nthumb|250px|\"Just get that carpet out of here!\"",
            {
                "title": "Suits",
                "ep_title": "Dirty Little Secrets",
                "season_num": 1,
                "ep_num": 4
            }
        ],
        [
            "bf11f260-1dce-11ee-b06f-52b307fec202",
            "Meanwhile, Mike recruits former tenants of Karinski's buildings to testify in court about the abuse they experienced living in his apartment building. He discovers from the photographs that the tenants gave him had similar carpets to that of Frank's. He and Harvey arrive at Karinski's home with a sample of Frank's apartment carpet. When Mike takes it out, Karinski flips out, knowing that the carpet was infested with bedbugs. Mike proceeds to reveal that Karinski actually created the bedbug problem in order to drive tenants out so he can remodel the apartment and rent it out for a much higher price. He reuses the bedbug carpet and installs it into other apartment buildings that he buys in order to create the same situation and profit. After Mike won the housing court case, fifteen other clients wanted to file similar complaints against Karinski and were willing to pay, surprising Louis.",
            {
                "title": "Suits",
                "ep_title": "Dirty Little Secrets",
                "season_num": 1,
                "ep_num": 4
            }
        ],
        [
            "bf11f27e-1dce-11ee-b06f-52b307fec202",
            "Towards the end, Mike and Rachel joke about their fake marriage status, and Mike takes a leap of faith and asks Rachel out on a date for their fake fifth anniversary. However, Rachel rejects him because she doesn't date anyone from the office.",
            {
                "title": "Suits",
                "ep_title": "Dirty Little Secrets",
                "season_num": 1,
                "ep_num": 4
            }
        ],
        [
            "bfefd9c2-1dce-11ee-b06f-52b307fec202",
            "Bail Out is the fifth episode of the first season of Suits and the fifth overall. It first aired on July 21, 2011.",
            {
                "title": "Suits",
                "ep_title": "Bail Out",
                "season_num": 1,
                "ep_num": 5
            }
        ],
        [
            "c0a2b8c6-1dce-11ee-b06f-52b307fec202",
            "Plot\nAt the Department of Justice's office, Harvey Specter is negotiating a deal with Becky, a judge Harvey has known since his job at the D.A.'s office, regarding his clients, Burt Kimball and Dean Morello, and the employee they think is responsible, Gabby Stone. Gabby is accused of insider trading, so they decide on a deal that will finally exonerate Harvey's clients that Gabby must agree to.",
            {
                "title": "Suits",
                "ep_title": "Tricks of the Trade",
                "season_num": 1,
                "ep_num": 6
            }
        ],
        [
            "c0a2b9c0-1dce-11ee-b06f-52b307fec202",
            "At the firm, Harvey tells Mike Ross that he is letting him sit in and observe the meeting with the client and the DOJ representatives when Mike nervously hides when Rachel Zane and a friend passes. Mike reveals that the woman is in fact one of his customers that he took the LSAT for, to which Harvey scoffs at, saying that she won't blow Mike's cover because if she does, then so will hers.\nthumb|right|250px|\"I get to sit in?\" \"With your head down and your mouth shut.\"",
            {
                "title": "Suits",
                "ep_title": "Tricks of the Trade",
                "season_num": 1,
                "ep_num": 6
            }
        ],
        [
            "c0a2b9fc-1dce-11ee-b06f-52b307fec202",
            "At the conference room, the full details of the case are revealed: Gabby Stone works as a trader for the company of Harvey's clients and one day, she apparently purchased $10 million worth of stocks in Lunardi pharmaceuticals just a day before their FDA approval, therefore tripling the money she receives. Although Harvey's clients claim that they had no involvement with her trade, Gabby and her lawyer insist that she purchased those stocks for Harvey's clients based on a tip sheet they gave her. Harvey then tells her that he managed to make a good deal with the DOJ for her which decreased her prison sentence from 7 years to 11 months and that she will be brought there personally without need for a perp walk. Knowing she has no chance if it goes on, she gives up and says she will sign the deal.\nthumb|left|250px|\"You here to make sure I don't change my mind about the deal?\"",
            {
                "title": "Suits",
                "ep_title": "Tricks of the Trade",
                "season_num": 1,
                "ep_num": 6
            }
        ],
        [
            "c0a2ba24-1dce-11ee-b06f-52b307fec202",
            "Morello and Kimball leave and Gabby's attorney asks Harvey to give her a minute so the two look over the papers in the office, leaving Mike to look after Gabby. Gabby tells Mike about the plans she had for her future, particularly teaching, which may no longer happen because of her conviction, and gets emotional. Mike then gets her a glass of water outside the conference room and gets sucked in a conversation with Rachel about her friend, Theresa, who was a former paralegal at Pearson Hardman and is now applying for a summer internship there. Mike gets nervous, and even more so when he finds that Gabby has escaped.",
            {
                "title": "Suits",
                "ep_title": "Tricks of the Trade",
                "season_num": 1,
                "ep_num": 6
            }
        ],
        [
            "c0a2ba42-1dce-11ee-b06f-52b307fec202",
            "Harvey and Mike visit Morello, and Mike takes mental notes of Gabby's colleagues. Later, he finds out that Morello's traders meet for drinks at a certain bar, and joins them, claiming to be an old friend of one of them, and encouraging them to drink and brag about their most successful trades. This way, he finds out about a number of possibly fraudulent trades, which he hands over to Harvey. In the end, Gabby is exonerated, thanks to Mike and Harvey.",
            {
                "title": "Suits",
                "ep_title": "Tricks of the Trade",
                "season_num": 1,
                "ep_num": 6
            }
        ],
        [
            "c18426f8-1dce-11ee-b06f-52b307fec202",
            "Plot\nThe scene opens with Mike almost running into Rachel on his bike. She tells that she isn’t going to tell that he cheated and that he doesn’t have to do that. They get into the office and no one is there. Rachel says that Mike forgets everything. Meanwhile, Harvey meets with Jones, his client. He says that he knows that he is trying to merge with Vega. Mike and Rachel go to find that they are doing a Mock Trial. Louis tells that they are going to get their roles. Kyle and Mike and are going against each other and Lewis says that Kyle was champion of Mock Trial several years in a row. Later, Harvey gives Mike an assignment and gives advice on the Mock Trial. He says that he needs to create a scenario that is going to make him win. Mike goes up to Kyle and says that he is not going to trial and wants to settle. Kyle says that he is more then happy to settle. They shake on it.",
            {
                "title": "Suits",
                "ep_title": "Play the Man",
                "season_num": 1,
                "ep_num": 7
            }
        ],
        [
            "c1842842-1dce-11ee-b06f-52b307fec202",
            "Harvey meets with Jones and Vega. He says that he doesn’t make a deal until his lawyer comes in. Dana Scott, Harvey’s old acquaintance, comes up and they go up to talk about the deal that is going to happen between Jones and Vega. Harvey and Dana exchange arguments and then they start to kiss and have sex. Later, the Mock Trial is underway and Mike says that they are going to settle. However, Kyle says that they are ready to move forward. Mike realizes that he was just blindsided. Harvey and Dana get back to paperwork and they talk about their two clients. Dana says that Vega has more properties and Jones says that he has more potential. She says that she isn’t going to show the private books until they have a signed deal. Harvey says that they don’t have a deal and Dana says that if they show her their books, she will show him theirs. Mike says that Kyle is not playing fair and Kyle says that he better watch his back in this case. They get back into trial and Mike calls the case a",
            {
                "title": "Suits",
                "ep_title": "Play the Man",
                "season_num": 1,
                "ep_num": 7
            }
        ],
        [
            "c1842a4a-1dce-11ee-b06f-52b307fec202",
            "calls the case a Defamation of Character. Jessica allows it and tells that they have until Friday to come up with their case.",
            {
                "title": "Suits",
                "ep_title": "Play the Man",
                "season_num": 1,
                "ep_num": 7
            }
        ],
        [
            "c1842b44-1dce-11ee-b06f-52b307fec202",
            "Harvey goes up to Donna and she asks if he came out on “top”. He asks why she didn’t tell that Dana was the lawyer. She says that she didn’t want him to get performance anxiety. Harvey says that he still got it and they are going to be able to see their books. Mike is in Harvey’s office and he says that Harvey gave him the worse advice. Harvey tells him that the real world is not going to allow for things to go his way. Mock Trial is to see what type of lawyer he is going to be. Mike goes out and walks up to Donna. She is crying and Mike says that Harvey can be really mean sometimes. However, it is an act so that Mike will call her as a witness. He says that she is in. Kyle comes up and is insulting. She tells Mike to go to a person who is willing to help him no matter what. Mike goes up to Jenny and she tells that she can’t believe that he has been living a lie and she says that is awesome. She asks if he can trust her and he says that he can. Later, Dana goes to Harvey’s place with",
            {
                "title": "Suits",
                "ep_title": "Play the Man",
                "season_num": 1,
                "ep_num": 7
            }
        ],
        [
            "c1842b80-1dce-11ee-b06f-52b307fec202",
            "Harvey’s place with the documents. Meanwhile, Mike gets pointers from Jenny and she tells him to be himself. They kiss and then get “busy”.",
            {
                "title": "Suits",
                "ep_title": "Play the Man",
                "season_num": 1,
                "ep_num": 7
            }
        ],
        [
            "c1842ba8-1dce-11ee-b06f-52b307fec202",
            "Back at Harvey’s, he recognizes from the kiss that he has been beaten. He gets up and tells that she is celebrating her win because she hid something in the negotiations. She denies it and leaves. At the firm, Mike says that they don’t want to merge, Vega wants to take over. Harvey says that they are going to put Jones’ hotels on the market to show that they are undesirable. The next day, Jenny gets to the office and asks for some water. Kyle comes up and says that the winner gets the girl. He says that he is not going to make a deal with him again. Harvey and Louis make a bet. Harvey goes up to Mike and asks how he is. Meanwhile, Rachel and Jenny talk. Harvey tells that Mike needs to use Kyle’s cockiness against him. Mike sees Rachel talking to Jenny and he is nervous. Later, the Mock Trial is underway and Donna is over-dramatic with her role and winks at Mike. Kyle tries to object but he is shut-down. Jenny takes the stand and they get a good role going. However, Kyle shuts it down.",
            {
                "title": "Suits",
                "ep_title": "Play the Man",
                "season_num": 1,
                "ep_num": 7
            }
        ],
        [
            "c1842bd0-1dce-11ee-b06f-52b307fec202",
            "Harvey stops Dana from leaving and says that she tricked him and that he is impressed. Harvey says that he has put three of Jones’ properties are for sale and he says that they will get anything to stop this. He tells that they are going to get the clients together and they are going to bring up the original deal. Back in the Mock Trial, Rachel is on the stand and Mike tells Donna that she is going to play the woman. He attacks her with the fact that she didn’t want to tell the truth and says that she can’t cut it. Rachel yells with emotion that she can cut it. Mike goes up to Kyle and begs for the settlement. However, Kyle says that he wants to see if he will break her. Mike says that he is not going to proceed and allows Kyle to beat him in the Mock Trial. Jessica asks Mike to come to her and she tells that he is naive and soft, two qualities that they are not looking for at Pearson and Hardman.",
            {
                "title": "Suits",
                "ep_title": "Play the Man",
                "season_num": 1,
                "ep_num": 7
            }
        ],
        [
            "c1842bee-1dce-11ee-b06f-52b307fec202",
            "Harvey and Dana sit down with Jones and Vega and Harvey says that they just want to make sure that everyone is happy. Dana tries to tell that Harvey just wants more hours, but Vega says that he wants to hear what he has to say. Harvey says that it is most important that both companies win and both men agree to go on the original deal. Mike gets into Harvey’s office and he asks what he is celebrating. Harvey says that he was worried about hurting his girlfriend and Harvey says that he doesn't have what it takes and Mike says that he is trying to be a good person as well. Harvey says that he calls it how he sees it. Harvey meets Dana at the bar and she says that she is fired from Vega and that her firm isn’t going to like it. Dana says that she is getting married and that she is going to do it. Harvey says that he sorry that he won and Dana says that he should never be sorry for that. Meanwhile, Mike goes over to Rachel and she thanks him for not attacking her. She says that she is",
            {
                "title": "Suits",
                "ep_title": "Play the Man",
                "season_num": 1,
                "ep_num": 7
            }
        ],
        [
            "c1842c16-1dce-11ee-b06f-52b307fec202",
            "says that she is sorry that she has been treating him bad and says that she just expects more from him and walks away.",
            {
                "title": "Suits",
                "ep_title": "Play the Man",
                "season_num": 1,
                "ep_num": 7
            }
        ],
        [
            "c292d71a-1dce-11ee-b06f-52b307fec202",
            "Never Have I Ever is an American comedy-drama series focusing on the life of an Indian-American teen who seeks popularity at her high school. It was released on April 27, 2020.\n\nJuly 1, 2020, it was announced that Netflix renewed the series for a second season.‘Never Have I Ever’ Renewed For Season 2 At Netflix It was released on July 15, 2021. On August 19, 2021, it was announced that Netflix has renewed the series for a third season.Mindy Kaling’s ‘Never Have I Ever’ Renewed For Season 3 By Netflix The season was released on August 12, 2022. The series' fourth and final season was confirmed to be renewed on March 8, 2022.Mindy Kaling’s ‘Never Have I Ever’ Renewed For Fourth & Final Season At Netflix It was released on June 8, 2023.",
            {
                "title": "Suits",
                "ep_title": "Identity Crisis",
                "season_num": 1,
                "ep_num": 8
            }
        ],
        [
            "c3593d9c-1dce-11ee-b06f-52b307fec202",
            "thumb|right|The main cast, from left to right: Rick Hoffman as Louis Litt, Gina Torres as Jessica Pearson, Gabriel Macht as Harvey Specter, Patrick J. Adams as Mike Ross, Meghan Markle as Rachel Zane, and Sarah Rafferty as Donna Paulsen",
            {
                "title": "Suits",
                "ep_title": "Undefeated",
                "season_num": 1,
                "ep_num": 9
            }
        ],
        [
            "c3593e28-1dce-11ee-b06f-52b307fec202",
            "Suits is an American legal drama, created by Aaron Korsh. It premiered on USA Network in June 2011. The series revolves around Harvey Specter (Gabriel Macht), a senior partner at a top law firm in Manhattan, and his recently hired associate attorney Mike Ross (Patrick J. Adams) as they hide the fact that Mike does not have a law degree. Each episode focuses on a single legal case and its challenges while examining the work environment of the firm, Mike's and Harvey's personal relationships, and problems stemming from Mike's lack of a degree. The rest of the starring cast portray other employees at the firm: Louis Litt (Rick Hoffman), a partner who manages the associates; Rachel Zane (Meghan Markle), a paralegal who develops feelings for Mike; Donna Paulsen (Sarah Rafferty), Harvey's long-time legal secretary, close friend, and confidante; and Jessica Pearson (Gina Torres), the co-founder and managing partner of the firm.",
            {
                "title": "Suits",
                "ep_title": "Undefeated",
                "season_num": 1,
                "ep_num": 9
            }
        ],
        [
            "b88da886-1dcd-11ee-8262-52b307fec202",
            "Kendall eventually does arrive in New Mexico and joins some locals on a cocaine and methamphetamine binge. Meanwhile, the rest of the therapy session also proves ineffectual, and Parfit is hospitalized after diving headfirst into a shallow pool and breaking several front teeth. Logan decides to give Roman more responsibilities by placing him in charge of overseeing a company satellite launch out of Japan. Roman, concerned for his brother's well-being, picks Kendall up from his relapse that night and takes him back to the ranch.",
            {
                "title": "Succession",
                "ep_title": "Austerlitz",
                "season_num": 1,
                "ep_num": 7
            }
        ],
        [
            "b88da912-1dcd-11ee-8262-52b307fec202",
            "Kendall returns to find the rest of the family in a heated argument. Logan demeans Tom and berates Shiv for meeting with his rival Eavis, causing her to leave crying. Logan also admits to planting stories in the tabloids of Kendall's drug use prior to his actual relapse. Still heavily intoxicated, Kendall accuses his father of resenting his children for the privilege in which he raised them, and nearly provokes a physical altercation when he flippantly dismisses the abuse Logan suffered at the hands of his uncle Noah. Marcia breaks up the argument, and Connor admits to Logan that he feels \"used\" by his father turning Austerlitz into merely another stage for waging his business-related conflicts.",
            {
                "title": "Succession",
                "ep_title": "Austerlitz",
                "season_num": 1,
                "ep_num": 7
            }
        ],
        [
            "b88da96c-1dcd-11ee-8262-52b307fec202",
            "The next morning, the rest of the Roy children leave Austerlitz, and Connor tells his escort girlfriend Willa that he wants to make their relationship exclusive, to which Willa half-heartedly agrees. Logan goes for a private swim with only Marcia present, revealing visible scars across his back, seemingly from his childhood abuse.",
            {
                "title": "Succession",
                "ep_title": "Austerlitz",
                "season_num": 1,
                "ep_num": 7
            }
        ],
        [
            "c4eea200-1dce-11ee-b06f-52b307fec202",
            "Jessica notifies Harvey and Louis that Malcolm Price, one of their clients, has passed away, and that he is leaving his estate and several of the companies he owned to his two daughters, Madison and Kelsey, who don't see eye to eye. Louis is tasked with getting Madison what she wants while Harvey and Mike are assigned to Kelsey. Louis bets that if he wins, he gets Mike as an associate, while Harvey asks for Louis' \"Nixon in China\" opera tickets so that Louis has to miss it. Madison hates Kelsey because she is her half-sister, and blames her for causing Malcolm Price to leave her mother and marry Kelsey's, and became jealous that Kelsey became her father's favorite. Since Malcolm and Kelsey worked on the \"Nothing but the Truth\" tabloid together, Madison wants Kelsey to not have it, while the tabloid is all that Kelsey wants.",
            {
                "title": "Suits",
                "ep_title": "Rules of the Game",
                "season_num": 1,
                "ep_num": 11
            }
        ],
        [
            "c4eea228-1dce-11ee-b06f-52b307fec202",
            "Mike asks Donna why she didn't tell him that Harvey used to work at the D.A.'s office. Donna doesn't wanna tell Mike because he doesn't want to uncover the truth to which will hurt Harvey's credibility as a lawyer - big time. Louis sets up ground rules for who wins the Malcolm Price fortune case including not going in each other's internal documents. Louis sets up a wager to which if Louis wins, he gets Mike's services and nothing in return if Harvey wins. Mike is surprised and confused why Harvey would agree to that but Harvey tells Mike that he's sure they would win.",
            {
                "title": "Suits",
                "ep_title": "Rules of the Game",
                "season_num": 1,
                "ep_num": 11
            }
        ],
        [
            "c4eea250-1dce-11ee-b06f-52b307fec202",
            "Harvey spots Alexandra Leeds a former colleague who now works for the attorney general and wants to talk about Cameron Dennis. Harvey is confused what is there to talk about him. Leeds tells Harvey that the attorney general is having Dennis investigated over allegations of tampering of evidence so he can win. Nobody from Dennis' firm want to testify since they all still work for Dennis. Leeds then had Harvey subpoena so he will testify in front of a grand jury since he used to work for Dennis. Harvey knows if they uncover the truth his reputation will be badly hurt and may be fired from the firm since some of the cases where Dennis tampered the evidence was Harvey's cases. Dennis reveals to Harvey the true reason of their date was that so he can assure that Harvey got his back during the trial. Harvey wants Dennis to settle however Dennis knows that during his time whatever may have happened, both of them put the real bad guys to jail.",
            {
                "title": "Suits",
                "ep_title": "Rules of the Game",
                "season_num": 1,
                "ep_num": 11
            }
        ],
        [
            "c4eea278-1dce-11ee-b06f-52b307fec202",
            "Harvey asks Donna what she will do if she was in Harvey's shoes since Donna used to work with Harvey as well at the DA office. Donna tells him he's tell him everything and watch him suffer in hell with pleasure. Mike comes in and tells Harvey that the tabloid that Malcolm Price had was a growing fortune and if Kelsey can have it, she is set for life. Harvey puts the whole case in Mike's shoulder and Mike isn't too proud of that. Harvey tells him if Louis loses he'll get the concert tickets Louis want to go to not because Harvey wants to go to the concert but so he can watch Louis cry.",
            {
                "title": "Suits",
                "ep_title": "Rules of the Game",
                "season_num": 1,
                "ep_num": 11
            }
        ],
        [
            "c4eea296-1dce-11ee-b06f-52b307fec202",
            "Harvey asks Rachel if she already has a date for their planned double date. Rachel insists she already has and is ready for the date. Mike goes to Louis' office to talk about division of assets between the two fighting sisters. Louis could not believe that Harvey put the case solely on Mike and is confident he can beat Mike. Mike talks about division of  the 10 companies that goes to Kelsey so a certain percentage goes to Madison. Louis refuses all alternative proposals telling Mike that his client only wants Kelsey to not get the tabloid. Louis tells Mike to get off Harvey's back and let him settle the case himself.",
            {
                "title": "Suits",
                "ep_title": "Rules of the Game",
                "season_num": 1,
                "ep_num": 11
            }
        ],
        [
            "c4eea2b4-1dce-11ee-b06f-52b307fec202",
            "A part of Harvey's past is told when he tells Jessica that he saw Dennis bury the key evidence that would let the defense walk. Jessica asks why he didn't report it. Harvey then says that Jessica put him there to be mentored and that was why he just left. Harvey absolutely does not want to expose Dennis of his actions because he was his mentor. Jessica says he will represent Harvey in the deposition and defend his credibility.",
            {
                "title": "Suits",
                "ep_title": "Rules of the Game",
                "season_num": 1,
                "ep_num": 11
            }
        ],
        [
            "c4eea2dc-1dce-11ee-b06f-52b307fec202",
            "Mike goes out with Jenny on a double date with Rachel and her date who is Kyle, Mike's rival associate at the firm. Mike asks Kyle how long he and Rachel have been dating and tells him that ever since he beat Mike at the mock trial, they \"bonded\" to which Mike knows Rachel does not like Kyle at all. Rachel asks Jenny how long she and Mike have been dating; Jenny tells her that it all started when she used to date Trevor but she and Mike were in love from the beginning. Mike tells Kyle to back off Rachel when he tries to put her hand on her and play with her, which annoys Jenny because she saw that Mike was looking at Rachel in the same way he was looking at Jenny when she was still with Trevor. Jenny then gives Mike a choice of whether he still wants to be with her or if he wishes to be with Rachel.",
            {
                "title": "Suits",
                "ep_title": "Rules of the Game",
                "season_num": 1,
                "ep_num": 11
            }
        ],
        [
            "c4eea2fa-1dce-11ee-b06f-52b307fec202",
            "Alexandra Leeds tries to grill Harvey during the deposition and begins by clarifying to him his tremendous record as assistant DA. She then asks Harvey about his relationship with Cameron Dennis. Harvey then says that wanted her to get the internship with Dennis so he could go to law school and ultimately land a job at Pearson Hardman. Alexander then grills Harvey about the said tampering of evidence and if he was in anyway involved which violated the code.\n\nHarvey and Jessica meet up with Alexandra Leeds and Alexandra hands Harvey the specific cases to which Cameron Dennis not only tampered the evidence but also got rid of witness testimony and falsifying DNA records. She tells Harvey that Dennis is a dirty public servant and need his help to get rid of him. Alexandra blackmails Harvey that if he doesn't help get rid of Dennis, she will have Harvey disbarred because of suspicions that Harvey helped with the tampering.",
            {
                "title": "Suits",
                "ep_title": "Rules of the Game",
                "season_num": 1,
                "ep_num": 11
            }
        ],
        [
            "c4eea322-1dce-11ee-b06f-52b307fec202",
            "Since all Kelsey wants is the paper, which Madison refuses to give up, Mike comes with the idea to allow Madison to keep the tabloid but allow all the employees to leave and form a new company under Kelsey. However, he faxes this proposal to Kelsey, and Louis breaks the ground rules he set with Harvey by accessing Mike's faxes. Louis proceeds to lock up employee contracts, preventing any of the tabloid employees to leave. Mike then decides to use Louis' fax ploy against him, by sending a letter of intent by United International to purchase the tabloid. Louis then convinces Madison to sell the tabloid to United so that Kelsey does not get it. However, Mike convinced Kelsey to purchase United International, and declares that she now owns the paper. With both sisters happy, Madison having prevented Kelsey from getting the tabloid and Kelsey owning it via United International, the matter is resolved. However, Louis admits that he knew that Kelsey bought United and thus convinced Madison",
            {
                "title": "Suits",
                "ep_title": "Rules of the Game",
                "season_num": 1,
                "ep_num": 11
            }
        ],
        [
            "c4eea340-1dce-11ee-b06f-52b307fec202",
            "convinced Madison to oversell the company to 50%, giving her more money while leaving her half-sister to drown in debt with the tabloid. Louis then gloats to Harvey that he won, but Harvey, still in turmoil over his past as the A.D.A., lashes out at Louis.",
            {
                "title": "Suits",
                "ep_title": "Rules of the Game",
                "season_num": 1,
                "ep_num": 11
            }
        ],
        [
            "c4eea368-1dce-11ee-b06f-52b307fec202",
            "Harvey goes to Cameron Dennis' house and convinces him to step down as DA instead of going to jail. Harvey reminds him of a specific case, Hector Avila, Harvey's own case to which Dennis tampered the key evidence. Harvey is sure that if found guilty, Harvey will be disbarred because of the Avila case. Dennis tells him that he did the right thing because all the men he put to jail were true murderers and rapists. Harvey then pushes Dennis to make a deal to step down so the trial does not push through and the men he put in jail will stay in jail.    \n\nDonna speaks to Jessica and believes that Harvey is the victim in the Cameron Dennis case and she feels sorry for him. She hands Jessica some documents that would help Harvey with the case.",
            {
                "title": "Suits",
                "ep_title": "Rules of the Game",
                "season_num": 1,
                "ep_num": 11
            }
        ],
        [
            "c4eea390-1dce-11ee-b06f-52b307fec202",
            "At the fax room, things got a little intimate when Rachel puts her hand on Mike's arm. Mike then tells her straight that he did everything he can to get Rachel's heart including faking a marriage for a client to which Mike masterminded so she can get Rachel in real life. Mike insists that Rachel is now flirting with him to which he says is too late because he was with Jenny now. Mike does not want any more playing between him and Rachel to which Rachel replies that if he doesn't want to be her friend, then he can just find another paralegal to help him and that their friendship is over.",
            {
                "title": "Suits",
                "ep_title": "Rules of the Game",
                "season_num": 1,
                "ep_num": 11
            }
        ],
        [
            "c4eea3ae-1dce-11ee-b06f-52b307fec202",
            "Jessica finds Dennis and tells him to cut a new deal with the attorney general for him to step down to which Dennis refuses at first as he will try to sell Harvey out along with him. Jessica then hands Dennis the documents that Donna gave her which were revealed to be the key evidence in which Dennis tried to bury and reveals to him that that wasn't even the original copy and that she still has it with even more evidence that he tried to tamper. Feeling threatened, Dennis then agrees to step down effective immediately.",
            {
                "title": "Suits",
                "ep_title": "Rules of the Game",
                "season_num": 1,
                "ep_num": 11
            }
        ],
        [
            "c4eea5b6-1dce-11ee-b06f-52b307fec202",
            "Jessica tells Harvey that he does not need to testify anymore as Dennis decided to step down. Harvey is however frustrated after he finds out that he put an 18 year old Clifford Danner to jail and Danner spent his entire adult life in jail even though he was innocent because Dennis buried the evidence that would clear his name. Jessica asks if Harvey has enough to overturn the conviction, and Harvey admits that he doesn't know; regardless, Harvey decides to get him out.",
            {
                "title": "Suits",
                "ep_title": "Rules of the Game",
                "season_num": 1,
                "ep_num": 11
            }
        ],
        [
            "c5e6aa0e-1dce-11ee-b06f-52b307fec202",
            "Dog Fight is the twelfth and final episode of the first season of Suits and the 12th overall. It first aired on September 8, 2011.",
            {
                "title": "Suits",
                "ep_title": "Dog Fight",
                "season_num": 1,
                "ep_num": 12
            }
        ],
        [
            "c69f2e4e-1dce-11ee-b06f-52b307fec202",
            "There are multiple media outlets which focus primarily on television soap operas and telenovelas. These publications and websites feature news, cast and crew interviews, plot summaries and previews, editorials and reviews, TV listings and video previews related to the genre.",
            {
                "title": "Suits",
                "ep_title": "She Knows",
                "season_num": 2,
                "ep_num": 1
            }
        ],
        [
            "c69f2ff2-1dce-11ee-b06f-52b307fec202",
            "Name Dates Country Notes+ List of soap opera media outlets All About Soap 1999–2016 United Kingdom Biweekly print magazine covering primetime soap operas Daytime Confidential 2007–present United States Website founded in 2007, under the Zap2it network from January 2012 through March 2014 Inside Soap 1992–present United Kingdom Weekly print magazine covering primetime and daytime soap operasInto Soap Magazine (IntoSoap) 2004 United Kingdom Short-lived print publication founded by actor Nicholas Cochrane of Coronation Street Michael Fairman TV 2008–present United States Established in 2008 as On-Air On-Soaps, the website was re-branded as Michael Fairman TV in May 2018. The site features news, interviews, reviews and previews by longtime soap opera journalist Michael Fairman, creator and executive producer of Sony's SoapCity. Serial Scoop 2013–present United States Covers \"daytime soap operas, primetime serials, novelas, TV movies, big screen features, web series, theater and every",
            {
                "title": "Suits",
                "ep_title": "She Knows",
                "season_num": 2,
                "ep_num": 1
            }
        ],
        [
            "c69f302e-1dce-11ee-b06f-52b307fec202",
            "theater and every form of serialized entertainment\" Soap Opera Digest 1975–present United States Weekly print magazine covering daytime and prime time soap operas Soap Opera Magazine ?–1999 United States Weekly print magazine covering daytime soap operas Soap Opera Network 2001–present United States News and features website Soap Opera Update 1988–2002 United States Weekly print magazine covering daytime soap operas Soap Opera Weekly 1989–2012 United States Weekly print magazine covering daytime soap operasSoap Hub2014-presentUnited StatesWebsite featuring soap opera news, spoilers, recaps, exclusive interviews, and more  Soap Central 1995–present United States Soap opera news and feature hub, originally a fansite known as  The AMC Pages and later Soap Opera Central SoapCities 2017–present United States Soap opera news blog founded by Shawn Brady and Akbi Khan in 2017. The site provides news and interviews. SoapCity 1999–? United States Sony Pictures' now-defunct official website for",
            {
                "title": "Suits",
                "ep_title": "She Knows",
                "season_num": 2,
                "ep_num": 1
            }
        ],
        [
            "c69f3056-1dce-11ee-b06f-52b307fec202",
            "website for the American daytime soap operas Days of Our Lives and The Young and the Restless, created and executive produced by longtime soap opera journalist Michael Fairman Soaplife 1999–2018 United Kingdom Biweekly (weekly in 2018) print magazine covering primetime soap operas ABC Soaps In Depth 1997–2020 United States Trio of print publications each focusing on the soaps of one of the three primary American networks. As of 2020, all print publications have ceased, although Soaps in Depth continues to operate as a digital-only publication. CBS Soaps In Depth 1997–2020 United States NBC Soaps In Depth 1997–1999 United States Soaps She Knows (Soaps.com) 2006–present United States Founded in June 2006 at Soaps.com, in January 2010 the site was mirrored at Soaps.SheKnows.com, and in April 2010 Soaps.com became a redirect to the new location. Thatsup 2015–present Canada Established in 2016, covers American soap operas. TVSource Magazine 2008–present United States Established in 2008 as",
            {
                "title": "Suits",
                "ep_title": "She Knows",
                "season_num": 2,
                "ep_num": 1
            }
        ],
        [
            "c69f307e-1dce-11ee-b06f-52b307fec202",
            "in 2008 as Soap Opera Source, the website was re-branded in 2012 as TVSource Magazine. The site focuses on the entertainment industry, television and pop culture. TVyNovelas 1982–present Mexico Print magazine and Televisa house publication covering telenovelas, with international editions in the US, Argentina, Chile and Colombia, and annual awards called the Premios TVyNovelas We Love Soaps 2007–present United States Originally a blog, founded by soap opera journalist Roger Newcomb",
            {
                "title": "Suits",
                "ep_title": "She Knows",
                "season_num": 2,
                "ep_num": 1
            }
        ],
        [
            "c7d17466-1dce-11ee-b06f-52b307fec202",
            "Plot\nThings aren't looking good for Mike after he is almost fired after Trevor spilled the beans to Jessica in the final episode of season 1. Mike is also well delighted to know that Rachel still harbors romantic feelings for him after finally hearing the message he missed because of Trevor.",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c7d17650-1dce-11ee-b06f-52b307fec202",
            "Jessica is surprised to see construction going around at the law firm without her permission and assumes it is all Daniel Hardman. Even her beloved tea set is being taken away from her office into the supposed new office. Louis walks in and wonders why the walls aren't taupe as this was Hardman's request. He wonders who he should now report to now that the founding partner is back and because Hardman asked him to summarize all the cases the law firm handled while he was gone. Jessica tells him it's still she who Louis answers to and that they work closely together when in the truth Jessica and Daniel will not be on the same page. Harvey asks why she hid the truth and tells him that \"you don't let the children know that mommy and daddy are fighting\".\n\nMike is excited to see Rachel and tell her that he finally got her message, but before Mike can tell her how he feels for her, Louis gets in the middle and demands that he needs Rachel. Just as she leaves Mike plants a long kiss on her.",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c7d17696-1dce-11ee-b06f-52b307fec202",
            "Jessica walks into Harvey's office to talk about how different departments feel about Harvey. Donna interrupts from her desk just as Jessica is about to ask about real estate saying that Harvey is horrible to the real estate people, as well as contracts, taxes, mergers and summarizes that all these people don't like Harvey because he thinks he is right all the time. She thinks they're barely known at bankruptcy though, as Jessica is assigning Harvey to a case of bankruptcy to Paul Porter's client. Mike is having a good time eating a pineapple flower from an omelet bar which Hardman brought for the associates. Harvey tells him to not trust Daniel because he doesn't know who he is yet: Hardman had embezzled funds from clients to support his mistress, while lying the money was for his wife's cancer treatments. Mike wants to side with Daniel instead of Jessica at first but when Harvey tells him his job will be in jeopardy if he goes to Daniel's side and that Jessica choose to keep him",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c7d176be-1dce-11ee-b06f-52b307fec202",
            "choose to keep him despite him being a fraud, he switches side. Harvey assigns something about Paul Porter to Mike.",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c7d176e6-1dce-11ee-b06f-52b307fec202",
            "Louis asks Donna what is really going on between Daniel and Jessica and even tries bribing her with tickets to a show she desperately wants to watch starring Meryl Streep and Glen Close if she tells him. Feeling used by Louis, Donna keeps her mouth shut but Louis lets her know if she's ready to talk, he'll give her a ticket. Mike flirts with Rachel and lets her know that he broke up with Jenny for her. They almost kiss when an executive walks by and Mike playfully switches to work. He asks her why she went out with Kyle during their double date when she doesn't even like him, then tells her to tell him about it on a date.\n\nHarvey meets with Paul on a golf course and they talk about the changes happening around the office. Harvey then promises to handle Tom, Paul's client to foreclose Madison 25 to save Paul's reputation. In exchange Harvey asks to support Jessica at the firm.",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c7d1770e-1dce-11ee-b06f-52b307fec202",
            "Harvey and Mike meet up with Tom Clapper and talk about foreclosing Madison 25. Tom doesn't want to declare bankruptcy, then Harvey throws out a football analogy that if Peyton Manning goes down and the team loses games, the team must move on and let go of some things in order to protect assets (that being letting go of Manning). Harvey tells Tom that he owes a quarter billion already and needs to let go to protect his own assets. Tom lets them know that is not about him or his future but is about his family name. Tom then comes up with his own football analogy that when team is about to lose, a quarterback throws a Hail Mary pass. Harvey counters that with the fact that a team does that if the team has nothing to lose; though in this case, Tom does. When almost all else fails and Tom makes his case, Mike comes up with an idea.",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c7d17736-1dce-11ee-b06f-52b307fec202",
            "Donna goes to Louis's office to ask if it is possible to have the 250 million loan debt extended for Tom, but when Donna tells him that the bank is National Metropolitan, Louis becomes doubtful. Louis asks for a detail in Daniel and Jessica's rift in exchange for the debt extension and Donna asks for the show tickets. Deal is done.\n\nHarvey and Mike talk to a bank representative about the foreclosure hold on Madison 25; that Tom will have the assets to make the bank a lot of money. But the bank tells them that what matters is the current assets the property has and that they will not be able to liquidate any of the property's assets as of now.",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c7d17754-1dce-11ee-b06f-52b307fec202",
            "Mike and Rachel try to set up some dating ground rules in the library when Louis walks in and remind Rachel about her assignment. Mike is not too pleased with it and reminds Louis that if he wants Rachel to summarize all the firm's cases, then he is going to have to wait. Mike then tries to make Louis jealous by telling him that Hardman invited all the associates to a Bruce Springsteen concert. Louis claims he doesn't care about it because he doesn't want to spend his evening with a bunch of associates.",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c7d1777c-1dce-11ee-b06f-52b307fec202",
            "Harvey finds Paul in his office and tells him why they did what they did with Madison 25 case, which Paul is not happy about because he is trying to protect Tom's future. Harvey tells him to trust him on this one; but Paul is not happy and forces Harvey to have Tom sign the bankruptcy papers. Harvey sees Mike deep in his research about the Madison 25 case and comes up with a new plan since Paul is not biting with their original plan. Mike informs Harvey that there are 8 projects in the 2-block radius of Madison 25 and were all built after Madison 25. He tells Harvey that this means that Madison 25 is the centerpiece of all this new properties. 6 of these properties are even backed by National metropolitan. This means that if Madison 25 closes then most of these new properties wont be doing good and that they need madison 25 to build up their own properties.",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c7d1779a-1dce-11ee-b06f-52b307fec202",
            "Mike and Harvey go to the bank again to see the rep and inform her that they would be pursuing maintaining Madison 25. They inform her that they found out the reason the bank is pursuing in leveraging the foreclosure of Madison 25; is to sell prime real estate cheaply in the other properties. They inform her that three of the properties surrounding Madison 25 are represented by Pearson Hardman and that if the bank forecloses Madison 25, they'll take their business elsewhere and even support the remaining properties. The bank rep then gives up on both men and approves a new loan.\n\nLouis is seen on a meeting with a Arnie Berenson, a headhunter at Berenson-O'Neill. Arnie tells Louis that there are plenty of other firms that would be happy to have him. Arnie gives Louis a choice and hands him his card.",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c7d177c2-1dce-11ee-b06f-52b307fec202",
            "While out on their first date, Rachel tells Mike that honesty is what he likes in a man after Mike confesses that Donna helped him in picking a good restaurant for their date. This doesn't go well with Mike as he is still conflicted about keeping the fact that he didn't graduate from Harvard from Rachel. They kiss and Mike waits for Rachel to leave in a cab.\n\nMike goes to Harvey's luxurious apartment to tell him that he needs to tell Rachel the complete truth. He tells Harvey that all the lies come back to haunt him and that he thinks telling Rachel will finally close the door on his past. Harvey doesn't approve and just as Mike is walking out the door Harvey tells him that if if Mike tells Rachel and it goes to Hardman -  he, Mike and even Jessica will be in big trouble. Harvey reminds him of what he had to go through to protect Mike and if he throws it all away, Harvey threatens him that he will be fired.",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c7d177ea-1dce-11ee-b06f-52b307fec202",
            "The next morning Jessica pays Harvey a visit at his apartment and is not thrilled at what Harvey did to threaten the bank. She says that she specifically told Harvey to do what Paul asks him to do and that Tom is not even Harvey's client. Harvey still sees the light at the end of the tunnel with his plan but Jessica orders him not to pitch his idea to the client and just do what Paul asks him to do.",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c7d17812-1dce-11ee-b06f-52b307fec202",
            "Rachel tells Donna about her date with Mike and boasts that the are very comfortable with each other. She tells her that they found a way to not let the firm know about their relationship. Donna advises Mike about his recent run-in with Harvey in his apartment. Mike thinks that Harvey doesn't care about Mike's happiness. Donna drags Mike into Harvey's office and tells him that Harvey had to fight tooth and nail to keep Mike on and even threatened Jessica that if Mike goes, he would go as well. Mike can't believe it. Donna tells him that if he cares so much about Rachel then he doesn't have a choice but to break up with her. A moment of emotion is seen as Donna tells Mike that the feelings go away after a break up and that it is still possible that they can work with each other because of Donna's experience with Harvey when they were still working at the DA office.",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c7d17830-1dce-11ee-b06f-52b307fec202",
            "Louis is waiting to speak with Jessica about something important when Paul Porter interrupts them. Jessica gives Louis a stern look, to which he replies begrudgingly \"it can wait\". Louis goes into his office and looks at the card he received from Arnie Berenson, when a messenger arrives and gives him a package. The package contains a gift from Daniel Hardman and when Louis opens it, he is delighted to see it is an audio recorder that Louis wanted. He then hides Arnie Berenson's card as if now he knows he can side with Daniel Hardman and stay with the firm.",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c7d1784e-1dce-11ee-b06f-52b307fec202",
            "Harvey tells Mike that Jessica rejected their deal with Tom and that bankruptcy should be the answer. Harvey is not pleased that he has to follow orders from Jessica and even Paul when there is a solution to the problem. Harvey tells Mike that he should also do the right thing in his conflict with Rachel. Harvey and Mike meet with Paul and Tom in the conference room to tell Tom about the deal. Harvey tells Tom that they were able to renegotiate the terms of the loan, and his payments would be further delayed. Harvey makes it clear that the decision means no bankruptcy nor foreclosure. Paul is not pleased and after Tom says that he will never forget what Harvey has done, he echos the same phrase, with much darker sentiment.",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c7d17876-1dce-11ee-b06f-52b307fec202",
            "Harvey meets with Jessica at the building's rooftop, and she explains that she feels betrayed by Harvey's actions. Harvey says that despite the situation he has created with the bankruptcy department, it will be great for her and the real estate department. She clarifies that she doesn't have a problem with real estate but it was Harvey they hated. She can't believe that Harvey would put himself in front of her and that Harvey just doesn't care. Jessica now feels betrayed and alone in her power struggle with Hardman.\n\nMike meets up with Rachel at a hotdog stand to break up with her. Rachel is confused. Mike reveals that he knows about Colin McCarthy, a first year associate Rachel used to date but when they broke up Colin's career went down the drain and he eventually got fired. Mike says that he will somehow screw up their relationship and have the same fate as Colin. Rachel believes that Mike thinks she's not good enough for him and storms off.",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c7d178a8-1dce-11ee-b06f-52b307fec202",
            "Jessica finds Louis in Hardman's office, and he makes several comments to the effect that he has been trying to make sure Harman's office is perfect for his return. She apologizes to him for blowing him off earlier, saying it was urgent, and offers to hear him out now giving him her full attention. After already choosing to side with Hardman, he tells Jessica curtly that he no longer needed to speak with her.\n\nHarvey finds Mike deep in research and checks in on him. Mike lets Harvey know that he did what he wanted him to do, it is obvious that he is upset with Harvey about it. Harvey lets Mike know that he knows he is right about dumping Rachel but Mike tells him that it doesn't make him a better man. As he leaves, Mike sees an unhappy Rachel heading into the elevator, salt in his open wound.\n\nIn the last scene of the episode, Harvey brings Jessica's tea set back into her office and lets her know that she is not alone with her endeavor with Daniel.",
            {
                "title": "Suits",
                "ep_title": "The Choice",
                "season_num": 2,
                "ep_num": 2
            }
        ],
        [
            "c8c31a0a-1dce-11ee-b06f-52b307fec202",
            "Plot\nPicking up exactly where the season 6 finale finished, Castiel (Misha Collins) proclaims himself to be the new God and tells Sam (Jared Padalecki), Dean (Jensen Ackles) and Bobby Singer (Jim Beaver) to bow and profess their love for him or be killed. When he sees that they only do it out of fear, he leaves to fix wrongs in the world. Sam begins to suffer hallucinations due to the torture he endured in Lucifer's Cage.\n\nCastiel goes to Heaven and kills all the angels that sided with Raphael, before starting to chastise false preachers and hear voices in his head. He goes to Crowley (Mark A. Sheppard) to make a trade, he will receive souls and he will reinstate Crowley's position as King of Hell. Seeing he can't refuse, Crowley accepts. In an attempt to stop Castiel, the Winchesters and Bobby summon Crowley to give them information to attempt to bind Death (Julian Richings) so he can kill Castiel.",
            {
                "title": "Suits",
                "ep_title": "Meet the New Boss",
                "season_num": 2,
                "ep_num": 3
            }
        ],
        [
            "c8c31b22-1dce-11ee-b06f-52b307fec202",
            "The ritual takes place and Death is bound. Castiel then appears, ready to kill them for their betrayal. Death then explains to Castiel that he consumed the Leviathans from the Purgatory, the first beasts created by God but locked in Purgatory as they were a threat to humanity. Castiel then disappears and while trying to punish a senator, the entities make him kill her entire staff. Death decides to help them stop Castiel, stating he will cause an eclipse to open a door to Purgatory so the souls can return.",
            {
                "title": "Suits",
                "ep_title": "Meet the New Boss",
                "season_num": 2,
                "ep_num": 3
            }
        ],
        [
            "c8c31b40-1dce-11ee-b06f-52b307fec202",
            "Realizing his powers are beyond his control, Castiel goes to Sam and Dean for help. While alone, Sam is taunted by Lucifer (Mark Pellegrino), who tries to convince Sam that he never left the Cage and he's currently giving him false hope through mental torture. Dean and Bobby open the door to the Purgatory as Castiel lets out the souls. Once the door closes, Castiel returns to normal, but the Leviathans are revealed to have remained inside his body. Castiel, now possessed by the Leviathans, attacks Dean and says, \"this is going to be so much fun\".",
            {
                "title": "Suits",
                "ep_title": "Meet the New Boss",
                "season_num": 2,
                "ep_num": 3
            }
        ],
        [
            "c9e04930-1dce-11ee-b06f-52b307fec202",
            "Plot\nAfter making fun of his records, Harvey loans Mike out to Louis for one case. Louis is working on a case for Liquid Water, who is being sued by Durham Foods for saying that their water increases the consumer's IQ. Harvey enlists Donna to help him go through files for a case that he worked on four years ago that is being reopened in light of new evidence. Mike begs Harvey to let him work on his case too. Mike and Donna are down in the files room when Harold comes in looking for a stapler for Rachel. Donna quickly musses her hair and loosens Mike's tie to give the appearance that they were having sex. Harold is so flustered that he doesn't notice the files they have been going though.",
            {
                "title": "Suits",
                "ep_title": "Discovery",
                "season_num": 2,
                "ep_num": 4
            }
        ],
        [
            "c9e04a52-1dce-11ee-b06f-52b307fec202",
            "Louis decides not to settle with Durham Foods, planning to bury them in paperwork. Harold delivers office supplies to Rachel. She tells him that his time is far too valuable and that he shouldn't be trying to help her when it's her job to help him. She takes the stapler that he has brought her, before opening a drawer full of staplers and tossing it inside.\n\nHarvey visits a woman who worked for Coastal Motors. She had known that the machinery was faulty. She tells him to get the hell off of her property and leave her alone. Travis Tanner is sitting on a car in front of the woman's house and threatens to tell the Bar that he's committing fraud now that he knows that the machinery was faulty.\n\nThe Vice-President of Market Research for Durham Foods, Kevin, and his lawyer are being interviewed by Louis and Mike. Louis connects with Kevin and gets him to admit that they are suing Liquid Water because their shares are dropping.",
            {
                "title": "Suits",
                "ep_title": "Discovery",
                "season_num": 2,
                "ep_num": 4
            }
        ],
        [
            "c9e04a7a-1dce-11ee-b06f-52b307fec202",
            "Harvey confronts a Lawerence Kemp in the parking lot of his building. Harvey tells him that he knows about Sarah Layton and pushes him into his car, making him feel guilty for the death of the man in the original case. Mike admits that he has really enjoyed working with Louis. He points out that Harvey hasn't poisoned the well, that Louis did it himself when he tried to sabotage his relationship with Jenny and blackmailed him with a fake drug test.\n\nLouis is waiting in Harvey's office when Harvey and Mike walk in. Louis says that he can help Harvey if he just trusts him, but Harvey tells him to go away. Mike tells him that he's being harsh and that all Louis wants is to be Harvey. Lawerence Kemp calls and tells Harvey to settle. Harvey asks where Donna is, Mike says that she's in the file room, and Harvey realizes that there is no document. The camera pans down to show that Louis has left his audio recorder under a sheet of paper in Harvey's office.",
            {
                "title": "Suits",
                "ep_title": "Discovery",
                "season_num": 2,
                "ep_num": 4
            }
        ],
        [
            "c9e04a8e-1dce-11ee-b06f-52b307fec202",
            "Harvey meets Travis Tanner and tells him that the document would never have held up in court anyway, because he forged it. Tanner says that he wanted a pound of flesh from CM and from Harvey. Louis is sitting in the conference room listening to the recording of Harvey and Mike's conversation of him. He is visibly upset. Daniel Pierce asks him if he has anything he wants to say. Harvey tells Jessica that they're still coming after him for fraud. Daniel storms in and demands to know when they were going to tell him that his firm was being sued. Donna finds the document that Harvey is being sued for fraud over, and it has her signature on it confirming that she received it.",
            {
                "title": "Suits",
                "ep_title": "Discovery",
                "season_num": 2,
                "ep_num": 4
            }
        ],
        [
            "cb19298e-1dce-11ee-b06f-52b307fec202",
            "Plot\nHarvey and Jeffrey meet up with a teenage tennis prodigy, Marco Mendoza, that Jeffrey wants to sign. Harvey then signs Mike the case and allows him to go to court. Marco is still under custody of his parents and they prohibit him from going pro. Marco then makes up a story about his father abusing him to file for emancipation. However, Mike realizes Marco lied and his father wasn't there the day the charges were made.\n\nDonna tries to shred the memo to protect Harvey, but Mike finds out. Harvey almost signs the affidavit that states that the firm never got the memo, but Mike interferes by spilling coffee over it. He then tells Harvey that signing the affidavit would be committing perjury and the destruction of evidence. Harvey consults Donna in the restroom and angrily lectures her. He says he'll kill her but won't fire her.",
            {
                "title": "Suits",
                "ep_title": "Break Point",
                "season_num": 2,
                "ep_num": 5
            }
        ],
        [
            "cb192af6-1dce-11ee-b06f-52b307fec202",
            "Louis brings his sick cat to work only to give Harold allergies. Later, after taking his cat to the dentist, finds out his cat had a system failure and had to be put down. Rachel consults Louis and tells him that he should show as much care to his associates as he showed his cat. She asks Mike for a signed ball from Marco and gives it to Louis, showing respect and care for her boss.\n\nJessica, Daniel, Allison and Harvey figure out a deal breaker. Allison wants a settlement but Harvey wants to win. Daniel and Jessica go out in a cold battle over the case and decide to protect Harvey, the firm, and Jessica's position by firing Donna. Jessica fires Donna and she packs her things. Mike and Rachel are shocked to see Donna go, fully believing that Harvey will do something to keep her at Pearson Hardman. Harvey, however, stood near the elevators waiting for Donna. He doesn't say anything but instead presses the elevator button. Harvey watches while Donna goes.",
            {
                "title": "Suits",
                "ep_title": "Break Point",
                "season_num": 2,
                "ep_num": 5
            }
        ],
        [
            "ccd73f54-1dce-11ee-b06f-52b307fec202",
            "Plot\nA phone begins to rings at the firm late one night, and Harvey puts down the call. He then calls Ray and tells him to bring him a tux and pick him up in his limo. Later, Mike is drinking while watching Diff'rent Strokes when Harvey knocks on his door. Harvey tells him to wear a tux because they have a \"situation\" in Atlantic City. When Mike tells Harvey he doesn't have one, Harvey reveals that he expected this, so he came prepared with an extra tux for Mike to wear.",
            {
                "title": "Suits",
                "ep_title": "All In",
                "season_num": 2,
                "ep_num": 6
            }
        ],
        [
            "ccd74030-1dce-11ee-b06f-52b307fec202",
            "Upon arrival at the casino, where Mike was actually banned in the past for counting cards, Harvey finds out that his friend, Keith Hoyt, is playing poker. This worries him since Keith is an alcoholic and a compulsive gambler. When they arrive at the table, Keith had just bet $3 million dollars, which he loses. He later reveals that he put up his company as collateral to Thomas Walsh for the money he borrowed and, since he lost, he also lost his company...with a contract signed on a napkin. While Harvey tries to talk to Tom and his lawyer, Mike explains to Keith that their napkin contract would be valid if it had the minimum requirements: an offer, acceptance, and consideration, all of which the napkin has.",
            {
                "title": "Suits",
                "ep_title": "All In",
                "season_num": 2,
                "ep_num": 6
            }
        ],
        [
            "ccd7404e-1dce-11ee-b06f-52b307fec202",
            "Meanwhile, at a ballet event at the Royal Hall, Louis and Rachel see each other. Realizing that they are both alone, since the grieving Donna had bailed on Rachel, Louis invites Rachel to the extra seat beside him that he always has reserved. They bond during the performance. As they leave the hall, they hear a man screaming insults, and when Louis assumes that he was insulting the ballet, he almost argues with the man, only to realize that the man was in fact Sergei Baskov, the renowned ballet dancer. He tells Louis and Rachel that two of his dancers had sprained their ankles in their rehearsal space, so Louis offers to help his legal case against the hall.",
            {
                "title": "Suits",
                "ep_title": "All In",
                "season_num": 2,
                "ep_num": 6
            }
        ],
        [
            "ccd74062-1dce-11ee-b06f-52b307fec202",
            "The next day, Jessica is worried about Harvey playing poker, saying that he is reeling from the release of Donna. When Harvey tells Jessica that Donna is irreplaceable, Jessica decides to assign a temp to be Harvey's assistant. Jessica then finds out that the judge working on Harvey's fraud case had just denied the motion to seal. When she finds out that the judge is in fact an old classmate and rival, Ella Follman, on whom Jessica had once played a very dirty prank on to get rid of her as competition for a position they had both wanted, she realizes that the attack might be very personal, seeing as Follman has never really moved on from the prank.",
            {
                "title": "Suits",
                "ep_title": "All In",
                "season_num": 2,
                "ep_num": 6
            }
        ],
        [
            "ccd7406c-1dce-11ee-b06f-52b307fec202",
            "Harvey then retrieves the security tapes from a woman he was flirting with at the hotel and has Mike review the security footage to count how many drinks Keith had before he signed the contract with Tom. When both parties finally bring the case to a judge, Harvey argues that since his client was drunk, he was not in a competent state of mind to make a decision, which Tom abused. Tom's lawyer, however, counters that while Keith was not, Harvey was sober when he offered them the money owed to him in exchange for the nullification of the napkin contract, so the judge moves that the case be brought to court.\n\nLouis, on the other hand, assigns Rachel, despite her being a paralegal and not an associate, to help him with the case when he realizes that Harold Gunderson is clueless and ignorant about ballet.",
            {
                "title": "Suits",
                "ep_title": "All In",
                "season_num": 2,
                "ep_num": 6
            }
        ],
        [
            "ccd74080-1dce-11ee-b06f-52b307fec202",
            "At the office, Harvey meets his new temporary assistant, Cameron, and he ends up peeved when he realized that Cameron had gone to great lengths to try and impress him. He is, however, particularly annoyed that Cameron touched Donna's filing system but says nothing about it.\n\nThe current agendas at Pearson Hardman have been going very well: Harvey realizes that in order to win back the company, Keith should get interim control of the company while the trial is ongoing, and then asks Mike to find out more about Tommy; Rachel and Louis, who bond over the case, discover that the defective air conditioning system in the Royal Hall resulted in a toxic environment for the space; and Jessica tries to buy Follman out of Harvey's case by contributing to Follman's re-election campaign to imply a conflict of interest.",
            {
                "title": "Suits",
                "ep_title": "All In",
                "season_num": 2,
                "ep_num": 6
            }
        ],
        [
            "ccd74094-1dce-11ee-b06f-52b307fec202",
            "That is, until, setbacks occur for all parties: Tommy has had experience of running companies by hiring experts in fields he has no knowledge of, so the judge grants him interim control of the company; Sergei has apparently not paid his required share for the maintenance repairs of their ballet rehearsal space for more than a year, so the hall decides to take legal action against him and evict them; and Follman is still bitter towards Jessica and tries to refuse her donation, so Jessica resorts to blackmailing her about possibly looking like Follman had accepted the money as bribe but chickened out about it.",
            {
                "title": "Suits",
                "ep_title": "All In",
                "season_num": 2,
                "ep_num": 6
            }
        ],
        [
            "ccd7409e-1dce-11ee-b06f-52b307fec202",
            "Just when Harvey was about to give up, saying that Tommy and his lawyer have \"a better hand,\" after some pep talk from Mike, Harvey decides to use Keith's knowledge of the company's flaws to threaten the company's future in Tommy's hands. He tells them that he would rather see the company become worth nothing than let them have it. He then offers them three choices: they go on with the suit and both suffer losses; Keith/Harvey give back the $3.5 million Keith owes Tommy; or they can play poker for it, wherein the loser gets nothing, much to Mike's surprise and disapproval.",
            {
                "title": "Suits",
                "ep_title": "All In",
                "season_num": 2,
                "ep_num": 6
            }
        ],
        [
            "ccd740b2-1dce-11ee-b06f-52b307fec202",
            "When Louis finds out that Sergei had lied to him about his financials and paying the hall, Louis is heartbroken that the man he idolized and trusted would take advantage of him. He opens up to Rachel, who reminds him that he is Louis, and that despite of Sergei's status, the ballet is bigger than Sergei and should not let that stop him. Louis then goes on and pays for Sergei's debts to the Royal Hall through Sergei's salary, which they would receive because Louis was able to convince the board to fire Sergei. He does, however, give Sergei the opportunity to leave gracefully on his own to avoid scandal.",
            {
                "title": "Suits",
                "ep_title": "All In",
                "season_num": 2,
                "ep_num": 6
            }
        ],
        [
            "ccd740bc-1dce-11ee-b06f-52b307fec202",
            "As for Jessica's dilemma, Ella Follman herself summoned for Jessica to her office to confront her about her lies regarding the prank Jessica had played on her in law school. She tells her that she knew Jessica targeted her because they were in competition for a position, and the classroom Jessica had left her naked in was the classroom of the professor conducting the interviews. Although Jessica initially denies this, she admits to it when Ella says she will recuse herself from Harvey's case if Jessica does.",
            {
                "title": "Suits",
                "ep_title": "All In",
                "season_num": 2,
                "ep_num": 6
            }
        ],
        [
            "ccd740d0-1dce-11ee-b06f-52b307fec202",
            "In Rachel's office, she tells Mike that she finds herself liking Louis, to which he replies that he's \"been there\" (referring to their short-lived camaraderie in \"Discovery\"), and she will get over it. When he sees Louis' Dictaphone with Rachel, he decides to play some of the recordings, much to Rachel's horror and amusement. However, the fun stops when Mike plays a recording of him and Harvey talking about Travis Tanner's lawsuit against them, realizing that Louis had used the record to tell Daniel Hardman.",
            {
                "title": "Suits",
                "ep_title": "All In",
                "season_num": 2,
                "ep_num": 6
            }
        ],
        [
            "ccd740e4-1dce-11ee-b06f-52b307fec202",
            "Mike offers to play the poker game for Harvey, who refuses, saying Harvey could do it because \"[he doesn't] play the odds, [he] play[s] the man.\" Also, he tells Harvey about Louis bugging his office and lets him hear the recording, infuriating Harvey enough to make him focus. At the poker game, Harvey talks a nervous Tommy into folding by going all in on his first move and taunting Tommy about his past and lack of expertise with anything. Tom folds, thinking Harvey was convincing him to call because he has a good hand. Harvey then reveals that he was bluffing and had a bad hand. After that, Tommy was nerved the rest of the game and never recovered, thus winning back Keith's company.",
            {
                "title": "Suits",
                "ep_title": "All In",
                "season_num": 2,
                "ep_num": 6
            }
        ],
        [
            "ccd740f8-1dce-11ee-b06f-52b307fec202",
            "That evening, Jessica chastises Harvey for his irresponsibility, pointing out that it began getting worse after Donna's release. In a fit of anger, Harvey then goes to Louis' office, where Louis was practicing ballet, and confronts him about the recording on his Dictaphone, which Harvey had taken from Mike earlier. He then approaches Louis, and from inches away, Harvey threatens Louis, saying that Louis owes Harvey for letting that incident pass, and that someday, when Harvey needs something, Louis will deliver.",
            {
                "title": "Suits",
                "ep_title": "All In",
                "season_num": 2,
                "ep_num": 6
            }
        ],
        [
            "cdfae9bc-1dce-11ee-b06f-52b307fec202",
            "thumb|right|The main cast, from left to right: Rick Hoffman as Louis Litt, Gina Torres as Jessica Pearson, Gabriel Macht as Harvey Specter, Patrick J. Adams as Mike Ross, Meghan Markle as Rachel Zane, and Sarah Rafferty as Donna Paulsen",
            {
                "title": "Suits",
                "ep_title": "Sucker Punch",
                "season_num": 2,
                "ep_num": 7
            }
        ],
        [
            "cdfaea84-1dce-11ee-b06f-52b307fec202",
            "Suits is an American legal drama, created by Aaron Korsh. It premiered on USA Network in June 2011. The series revolves around Harvey Specter (Gabriel Macht), a senior partner at a top law firm in Manhattan, and his recently hired associate attorney Mike Ross (Patrick J. Adams) as they hide the fact that Mike does not have a law degree. Each episode focuses on a single legal case and its challenges while examining the work environment of the firm, Mike's and Harvey's personal relationships, and problems stemming from Mike's lack of a degree. The rest of the starring cast portray other employees at the firm: Louis Litt (Rick Hoffman), a partner who manages the associates; Rachel Zane (Meghan Markle), a paralegal who develops feelings for Mike; Donna Paulsen (Sarah Rafferty), Harvey's long-time legal secretary, close friend, and confidante; and Jessica Pearson (Gina Torres), the co-founder and managing partner of the firm.",
            {
                "title": "Suits",
                "ep_title": "Sucker Punch",
                "season_num": 2,
                "ep_num": 7
            }
        ],
        [
            "cee48676-1dce-11ee-b06f-52b307fec202",
            "Plot \n\nThe plot focuses around the fact that aliens are invading the plant and all the main heroes have been captured.  The children of the heroes are kept in an underground facility to be safe, but do to the fact that one of them can predict the future they know they will not be safe and escape to train.\n\nThe movie opens on Mr. Miracle and this other guy investigating a issue in space.  When Mr. Miracle goes to investigate he lose communication as he has been knocked out by an alien drone and is falling back to Earth.",
            {
                "title": "Suits",
                "ep_title": "Rewind",
                "season_num": 2,
                "ep_num": 8
            }
        ],
        [
            "cee4875c-1dce-11ee-b06f-52b307fec202",
            "We see Missy Moreno waking up in bed then proceeding to choose between two shirts for the day.  Going with the black shirt over the pink one stating that she picked it so that no one would talk to her.   She walks into the kitchen where her father is cracking an usually large amount of eggs and mixing up the egg shells with the yokes.  He obviously is very engulfed by the TV coverage of Mr. Miracle being knocked out.  When Missy questions him about the event he brushes it off as simply being a training exercise. \n\nAuthors Note:  There are many spelling and grammatical errors as well as details being left out.  Revisions of the current draft is advised and appreciated.",
            {
                "title": "Suits",
                "ep_title": "Rewind",
                "season_num": 2,
                "ep_num": 8
            }
        ],
        [
            "cfc01b96-1dce-11ee-b06f-52b307fec202",
            "Asterisk is the ninth episode of the second season of Suits and the 21st overall. It first aired on August 16, 2012.",
            {
                "title": "Suits",
                "ep_title": "Asterisk",
                "season_num": 2,
                "ep_num": 9
            }
        ],
        [
            "d09f5266-1dce-11ee-b06f-52b307fec202",
            "Plot\nIn Hadleyville, a small town in New Mexico Territory, in 1898, Marshal Will Kane, newly married to Amy Fowler, prepares to retire. The happy couple will soon depart for a new life: to raise a family and run a store in another town. However, word arrives that Frank Miller, a vicious outlaw whom Kane sent to prison, has been released and will arrive by the noon train, one day ahead of the new marshal. Miller's gang—his younger brother Ben, Jack Colby, and Jim Pierce—await his arrival at the train station.\n\nthumb|left|Will Kane and Amy Fowler argue in the Marshal's office\n\nFor Amy, a devout Quaker and pacifist, the solution is simple—leave town before Miller arrives—but Kane's sense of duty and honor make him stay. Besides, he says, Miller and his gang would hunt him down anyway. Amy gives Kane an ultimatum: she is leaving on the noon train, with or without him.",
            {
                "title": "Suits",
                "ep_title": "High Noon",
                "season_num": 2,
                "ep_num": 10
            }
        ],
        [
            "d09f5356-1dce-11ee-b06f-52b307fec202",
            "Kane visits a series of old friends and allies, but none can or will help: Judge Percy Mettrick, who sentenced Miller, flees on horseback, and urges Kane to do the same. Harvey Pell, Kane's young deputy, is bitter that Kane did not recommend him as his successor; he says he will stand with Kane only if Kane goes to the city fathers and \"puts the word in\" for him. When Kane refuses, Pell turns in his badge and pistol. Kane's efforts to round up a posse at Ramírez's Saloon, and then the church, are met with fear and hostility. Some townspeople, worried that a gunfight would damage the town's reputation, urge Kane to avoid the confrontation entirely. Some are Miller's friends, but others resent that Kane cleaned up the town in the first place. Others are of the opinion that their tax money goes to support local law enforcement, and that the fight is not a posse's responsibility. Sam Fuller hides in his house, sending his wife Mildred to the door to tell Kane he is not home. Jimmy offers",
            {
                "title": "Suits",
                "ep_title": "High Noon",
                "season_num": 2,
                "ep_num": 10
            }
        ],
        [
            "d09f5374-1dce-11ee-b06f-52b307fec202",
            "home. Jimmy offers to help, but he is blind in one eye, sweating, and unsteady. Kane tells him he will call him and gives him money for a drink. The mayor encourages Kane to just leave town. Martin Howe, Kane's predecessor, is too old and arthritic. Herb Baker agrees to be deputized, but backs out when he realizes he is the only volunteer. A final offer of aid comes from 14-year-old Johnny. Kane admires the boy's courage, but refuses his help.",
            {
                "title": "Suits",
                "ep_title": "High Noon",
                "season_num": 2,
                "ep_num": 10
            }
        ],
        [
            "d09f5388-1dce-11ee-b06f-52b307fec202",
            "thumb|The film's trailer\nWhile waiting at the hotel for the train, Amy confronts Helen Ramírez, who was once Miller's lover, then Kane's, then Pell's. Amy believes the reason Kane refuses to leave town is because he wants to protect her, but Helen reveals there is no lingering attachment on Kane's part and she, too, is leaving. When Helen questions why Amy will not stay with Kane, she explains that both her brother and father were gunned down by criminals, a tragedy that compelled her to become a Quaker in the first place. Helen nonetheless chides Amy for not standing by her husband in his hour of need, saying that if she was in Amy's place, she would take up a gun and fight alongside Kane.",
            {
                "title": "Suits",
                "ep_title": "High Noon",
                "season_num": 2,
                "ep_num": 10
            }
        ],
        [
            "d09f539c-1dce-11ee-b06f-52b307fec202",
            "At the stables, Pell saddles a horse and tries to persuade Kane to take it. They end up in a fist fight. After knocking his former deputy senseless, Kane returns to his office to write out his will. As the clock ticks toward noon, Kane goes into the street to face Miller and his gang. Amy and Ramirez ride by on a wagon with their luggage, bound for the train station. The train arrives, and Miller steps off. He is given a gun by his gang.",
            {
                "title": "Suits",
                "ep_title": "High Noon",
                "season_num": 2,
                "ep_num": 10
            }
        ],
        [
            "d09f53b0-1dce-11ee-b06f-52b307fec202",
            "The gunfight begins. Kane walks down the town's deserted main street alone as Miller's gang advance from the train station. Kane manages to ambush them and kill Ben Miller and Colby. Just before the train departs, Amy hears the gunfire, leaps off, and runs back to town. Kane takes refuge in a stable, but Miller sets fire to the structure. Kane frees the horses and tries to escape on one, only to be shot off and cornered. Choosing her husband's life over her religious beliefs, Amy picks up Pell's pistol and shoots Pierce from behind, leaving only Frank Miller, who grabs Amy as a human shield to force Kane into the open. When Amy claws Miller's face, he pushes her to the ground, and Kane shoots him dead.\n\nKane helps his bride to her feet and they embrace. As the townspeople cluster around him, Kane throws his marshal's star in the dirt and departs with Amy on their wagon.",
            {
                "title": "Suits",
                "ep_title": "High Noon",
                "season_num": 2,
                "ep_num": 10
            }
        ],
        [
            "d18bfb02-1dce-11ee-b06f-52b307fec202",
            "Plot\nthumb|left|250px|Mike smoking in his apartment\nMike Ross is smoking in his apartment when he is approached by Tess, who is wrapped in just a sheet. She informs him that they are out of pizza, before being handed the cigarette by Mike. She asks whether his smoking indicates he isn't going back to Pearson Hardman the next day, and whether he is scared to do so, but Mike replies that he is looking forward to going back, and that he is simply celebrating. Tess asks whether the reason he is looking forward to going back is to talk to Rachel Zane; Mike becomes defensive, saying that Rachel is just a friend, but Tess is not convinced.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfc24-1dce-11ee-b06f-52b307fec202",
            "The next day, at Pearson Hardman, Harvey Specter enters his office, only to find Donna waiting for him in his chair. She gives him some messages regarding ongoing cases, before revealing that he received a message from Zoe Lawford. Donna asks Harvey why Zoe would be calling, and after some pressuring, he reveals that he called her to ask her on a date. Their conservation is interrupted by Louis Litt, who begins to discuss one of the onasgoing cases with Harvey, but Harvey cuts him off, saying that he \"[doesn't] give a shit what [Louis] needs\". Louis confronts Harvey regarding his animosity towards him, saying that what happened with Daniel Hardman was over a week ago, and Harvey should \"get over it\", but Harvey angrily asks him to leave. Louis responds that he wasn't the only senior partner to support Hardman, and that in the end he supported Harvey, but Harvey still isn't swayed.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfc42-1dce-11ee-b06f-52b307fec202",
            "Mike goes to see Rachel, and he attempts to apologize for his actions. However, Rachel is still upset, and questions Mike on whether he told Tess what happened between them before he slept with her. Mike responds by telling her that Tess is married, to which Rachel is speechless. Harvey enters the office and asks Mike if he is ready to start working again, but Mike asks him to give Rachel and himself a minute; Harvey responds by informing Mike that they have a new case which cannot wait, and the two of them leave.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfc56-1dce-11ee-b06f-52b307fec202",
            "Harvey and Mike go to see an Gillian Colson, an old client of Harvey's, who needs their assistance with a problem regarding her son, Liam. He informs them that he was involved in an accident, to which Mike begins interrogating him on whether he had been drinking. Liam states that he hadn't, but then reveals that he drove away from the accident, and doesn't know what happened to the person he hit. As they leave, Harvey questions Mike on his directness when questioning Liam, and suggests that it would be better if he was to sit the case out. Mike attempts to defend his actions, but Harvey interrupts him, saying that he understands why this case would be hard for Mike after what happened with his parents, but he cannot have Mike getting emotional on this case. Mike replies that he said he was on board, and Harvey relents, allowing him to stay.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfc74-1dce-11ee-b06f-52b307fec202",
            "Harvey goes to inspect the damage to the car Liam was driving, and states that the minimal damage and position will help them, as it corroborates Liam's story that he didn't see the other person. Mike approaches them and reveals the identity of the other person as Albert Chung, who was rushed to hospital the previous night after a 911 call; Liam then confirms that he was the one to make the call, which Harvey says he should have told them. Mike informs them that despite sustaining some injuries, including a concussion, Albert is stable. Harvey informs Liam that he has to turn himself in, despite the fact that it was an accident, as it will put then in a better position.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfc88-1dce-11ee-b06f-52b307fec202",
            "Liam makes the decision to turn himself in, and is escorted to the police station by Mike, who assures him that he will not be sent to jail. Liam asks Mike how he can be sure, and Mike tells him that he knows Harvey. Liam is still nervous, so Mike reveals to him his own history, and how he was arrested for possession when he was sixteen. He promises Liam that he will be home by the end of the day.\n\nLouis is having lunch with Sheila Sazs, and the two of them flirt with one another regarding Louis' recent promotion. He informs Shelia that, as senior partner, he is allowed to hire an associate as his own, and requests that she line up interviews with the best possible graduates, which she agrees to do. After some further flirtation, Shelia suggests that Louis visit her at her hotel the following evening, before leaving.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfc9c-1dce-11ee-b06f-52b307fec202",
            "Harvey and Mike go and see Katrina Bennett, the Assistant District Attorney; they present their case to her, stating that since it is only a minor offence, and Liam turned himself in to the police, they are willing to accept maximum community service and a fine, but nothing more. Katrina, however, asks whether they are willing to pay funeral costs, revealing that Albert Chung died from his injuries, despite initially appearing to be stable. Such a felony would normally be 12–15 years in jail, but Katrina offers them 10 years, despite Mike's objections that it was an accident, before leaving.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfcb0-1dce-11ee-b06f-52b307fec202",
            "At Pearson Hardman, Louis is conducting interviews for the position as his new associate. He lists the many achievements of his interviewee, Maria Monroe, before stating that such achievements do not impress him, and gives her five minutes to prove why she \"is the one\". She responds by saying that she doesn't need five minutes, as she is the one, and already has offers from the top three firms in New York. Louis counters by saying that Pearson Hardman is a top three firm, but Maria suggests otherwise given that they haven't offered her an interview until now, and states that he should submit a formal offer by the next day if he wants her to even consider working at the firm. Louis interrupts her and steps out of his office, dismissing the other four interviewees waiting there, saying that the position has been filled. He then offers to give Maria a tour of the firm, but she declines.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfcc4-1dce-11ee-b06f-52b307fec202",
            "In Harvey's office, Mike informs his superior that Albert Chung was wearing entirely black when he was knocked down, as he was tagging a wall with graffiti just prior to the accident and did not wish to be seen. Mike asks if Harvey intends to use this information to \"stick it to Katrina\", but he replies that Mike will do so instead, as given that Katrina's agenda is to beat him, Mike will be able to obtain a better deal going alone. Mike goes to see Katrina, and presenting her with the evidence they have, she agrees to accept the deal they proposed. She states that her desire is to work at Pearson Hardman, and asks that in return for her accepting Mike's deal, he put in a good word for her with Harvey.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfcce-1dce-11ee-b06f-52b307fec202",
            "Mike goes to see Harvey, and informs him of what Katrina asked him to do. Harvey, however, is unworried, as since Katrina signed the plea deal, she cannot renege on their deal if he refuses to interview her, which he is under no obligation to do. He then informs Mike that they need to settle with Albert Chung's family; Mike is hesitant about going to see them so soon after Albert's death, and relays to Harvey his own memories of when he and his grandmother were visited by a lawyer, Nick Rinaldi, after his parents died. He requests that Harvey let him be the one to talk to them, and though Harvey is skeptical of whether he can handle it, he agrees.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfce2-1dce-11ee-b06f-52b307fec202",
            "At Pearson Hardman, Mike finds Rachel in the file room, and requests that she not tell anyone else what he revealed to her about Tess. Mike confronts her regarding her supposed judgmental attitude towards him, saying that he isn't \"little miss perfect\" like her. Rachel, however, reveals that she too once had an affair, and chastises Mike for being the one to now judge her. As she leaves, she remarks to him that his affair with Tess will only end badly.\n\nMike goes to see Albert Chung's family, and informs them how devastated Liam is by what happened. Albert's sister informs Mike that all they want is enough money to cover Albert's debts and funeral costs, which amounts to $20,000. Mike in turn offers them $100,000, the maximum amount that Harvey said Mike could offer them, and Albert's family gratefully accept.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfcf6-1dce-11ee-b06f-52b307fec202",
            "Louis arrives at Sheila's hotel suite and finds her already waiting for him, wearing very little. She interrupts him as he approaches her, and asks who the front-runner is for the associate position. He immediately replies that it is Maria Monroe, to which Sheila states that she already knows, but that she wasn't going to just \"serve up [her] best candidate on a silver platter\". Louis informs Sheila that he will need her help in closing Maria, to which she eagerly agrees. Sheila then asks Louis if he requires a safe word, which he declines, and the two of them proceed to have intercourse.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfd0a-1dce-11ee-b06f-52b307fec202",
            "Harvey knocks on the door to Zoe's house, and it opens to reveal a young girl named Olivia. She asks Harvey where his flowers are, saying that \"if [he wants] a date, [he is] supposed to bring flowers\". Zoe then approaches the two of them, and requests that Olivia go up stairs. Harvey inquires whether Zoe perhaps forget to tell him something, and after initially joking that Olivia is Harvey's daughter, Zoe informs him that Olivia is her niece, and that she is looking after her for her brother. Harvey offers to join the two of them, and Zoe agrees.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfd1e-1dce-11ee-b06f-52b307fec202",
            "Tess returns to Mike's apartment only to find him having already begun smoking, to which Mike states that he just \"couldn't wait\". He tells her about the great day he had, and how he managed to negotiate the settlement with the Chung family. He gets a call from Harvey, who informs him that Liam's plea deal has come through, and requests that Mike visit Liam so they can wrap up the deal. Tess questions whether Mike should do so given that he is high, but Mike is undeterred.\n\nBack at Zoe's house, Zoe informs Harvey that Olivia has asked for him to kiss her good night. Harvey gladly agrees to do so, despite Zoe stating that it is not necessary. She requests that he kiss her good night afterwards, but Harvey kisses her there and then, taking Zoe by surprise.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfd32-1dce-11ee-b06f-52b307fec202",
            "Mike visits Liam, and takes him through the deal he arranged with Katrina. He assures Liam that there will be no more problems after he has signed the deal, and Liam does so, though he comments on the fact that he is only getting community service and a fine. Mike states that Liam seems disappointed; Liam subsequently thanks Mike for his efforts in breaking the deal, but points out that it could have been a lot worse, and chastises himself for his actions. Mike attempts to comfort him by stating that the Chung family doesn't blame Liam for what happened, but Liam reveals that whilst he wasn't drunk when the accident occurred, he was high. Mike berates him for not telling them sooner, and lies to Liam when he asks whether it is still a done deal.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfd46-1dce-11ee-b06f-52b307fec202",
            "The next day at Pearson Hardman, Harvey arrives at his office to find Mike waiting for him. Mike informs him that they can no longer submit the deal they brokered with Katrina, as Liam was on drugs when he crashed, and thus it was not an accident. Harvey responds by saying that nothing has changed, as they did not know Liam was high when they submitted the deal, and that the knowledge is privileged information. Mike questions his superior's decision not to act, as the Chung family believe their son was to blame, and states that if he doesn't tell them he is no better Nick Rinaldi. Harvey, however, does not believe that to be so, and reveals that he knows Mike offered the Chung family more than they requested. He requests that Mike let it go, but Mike storms out of the office in anger.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfe4a-1dce-11ee-b06f-52b307fec202",
            "Louis finds Maria Monroe waiting for him, and she informs him that she accepts his offer of employment at Pearson Hardman. Their discussion is overhead by Donna, and Louis proceeds to introduce the two of them. He informs her that Maria is \"a machine\", and will \"run circles around Mike Ross\". As he leaves to get them some cake, Maria asks Donna who Mike Ross is, and questions whether he is a first year from Harvard. Donna replies he is, but Maria reveals that she was secretary of her class, and there was no one named Mike Ross in her year. Donna lies and says that Mike clerked for three years, and thus not in her class, and Maria replies that she \"look[s] forward to meeting him\".\nthumb|right|250px|Nick Rinaldi",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfe9a-1dce-11ee-b06f-52b307fec202",
            "Mike visits Nick Rinaldi's office, and pretends that he accidentally killed someone driving whilst drunk. He requests Nick's assistance, but Nick declines, stating that he no longer takes cases like that. Mike becomes angry and asks whether he remembers taking the case of the drunk driver that killed his parents. Nick states he has no recollection of the case, and Mike attempts to remind him by relaying his own memory of when Nick visited himself and his grandmother, and how Nick subsequently screwed them over. Nick doesn't deny it may have occurred, but that it happened so many times he doesn't remember that specific case. He asks what Mike wants from him, and Mike responds by questioning how he lives with himself with some of the things he has done. Nick replies that even though he does not recall the case, he still regrets what he did to Mike. However, his statement does little to console Mike, and he angrily states that if he ever sees Nick again, he had better remember his",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfeae-1dce-11ee-b06f-52b307fec202",
            "better remember his parents' names.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfec2-1dce-11ee-b06f-52b307fec202",
            "Back at Pearson Hardman, Harvey approaches Jessica and asks whether she was aware Louis had hired a new associate for himself. Jessica replies that he is entitled to do so, but Harvey states that she has to stop him. She responds by requesting that he let go of the animosity he has towards to Louis. Harvey pulls her into the conference room, and informs her that Maria was secretary of Mike's \"class\" at Harvard, and could expose him as a fraud. Jessica is sceptical that Maria would remember everyone in the class, but Harvey states that she does. Jessica voices her annoyance that Mike's lie is again going to cause her problems. She requests Louis visit her in her office, and reveals to him that he will have to rescind the offer he made to Maria, as after the firm's recent turmoil, she has decided to impose a hiring freeze. Louis, however, suggests that Jessica is merely punishing him for voting against her, but Jessica is undeterred, and orders him to find a way to rescind the offer,",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfed6-1dce-11ee-b06f-52b307fec202",
            "rescind the offer, before dismissing him.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfeea-1dce-11ee-b06f-52b307fec202",
            "Mike is in the courtroom waiting for his case to begin, and as Katrina arrives, he informs her that he wants to help her win the case. He reveals to her that Liam was high when he hit Albert Chung, and though he is unwilling to tell her how he came to know such information, she thanks him for it. As the case begins, Katrina stands and informs the judge that they entered into a plea deal the previous day, and after a brief moment, the judge announces that the case is closed. Mike confronts Katrina on why she didn't use what he told her, and she reveals that she knows what he told her was privileged information. Mike questions whether she cares that Liam was driving under the influence, but Katrina responds by stating that she cannot prove that to be the case. Mike asks her how she will be able to sleep at night, but Katrina turns the question back on him, and asks how he will be able to sleep knowing he tried to \"sell out a 20asyear old kid\". Mike questions her integrity given that she",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bfefe-1dce-11ee-b06f-52b307fec202",
            "given that she was supposedly willing to bribe him to gain a position at Pearson Hardman, but Katrina is unfazed, and suggests Mike is the one lacking in integrity given that he was willing to break privilege, before leaving.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bff12-1dce-11ee-b06f-52b307fec202",
            "In Harvey's office, Donna informs her superior that Katrina Bennett called, and that \"the deal is done\". She questions what Harvey did, to which Harvey responds that he \"did what [he] had to do\". Donna continues to question whether he wants Katrina to be the second person he hires, but Harvey rebuffs her concerns.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bff1c-1dce-11ee-b06f-52b307fec202",
            "Louis goes to see Sheila in her hotel suite again, and presents with a bottle of wine. He informs her that he has had to rescind the offer to Maria Monroe, to which she states her disappointment. Louis defends himself by stating that he was forced to do so by Jessica, but Sheila questions whether he is the \"strong, powerful senior partner\" she believed him to be. Louis states that he is, but Sheila is unconvinced given what has happened with Maria, and requests that he leave. Louis is unwilling to do so, but Sheila angrily states that she put her reputation on the line to help him close Maria. Louis again states that his hands are tied given that Jessica has implemented a hiring freeze, but Sheila counters by informing Louis that Harvey hired a new associate that day, leaving Louis speechless.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bff3a-1dce-11ee-b06f-52b307fec202",
            "Mike confronts Harvey in his office, and questions his decision to hire Katrina. Harvey replies that after looking into her, he found she was a \"stellar candidate\", but Mike isn't fooled, and states that he bribed her. Harvey refutes Mike's suggestion, stating that \"she put the deal through, then [he] offered her a job\", adding that he could see that Mike was going to inform Katrina of what Liam told him. Mike states again that he bribed her, and Harvey angrily agrees, adding that he did so to protect Mike, as if it was found out that Mike broke attorneyasclient privilege, his secret would soon be revealed. Mike is unwilling to accept Harvey's statement, stating that \"there is such thing as right and wrong, and [they were] wrong\". Harvey states that he won't think twice about sending Mike packing if a similar situation occurs again, and after telling Mike to get his act together, he leaves.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bff4e-1dce-11ee-b06f-52b307fec202",
            "Mike informs Liam that the deal is done, but interrupts him before Liam can thank him, saying that he has to live with the fact that Liam killed someone. Liam replies by saying that he too has to live with it, and that what happened makes him sick. Mike tells him that he doesn't deserve what he has been given, and he should find a way to make up for Albert Chung's death.\nthumb|left|250px|Harvey visiting Zoe",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bff62-1dce-11ee-b06f-52b307fec202",
            "Harvey goes to see Zoe again, and she is surprised to find that he has brought a bouquet of flowers. However, he states that the flowers are for Olivia, and asks her whether she wishes to come with him for a weekend away. Zoe reluctantly informs Harvey that she cannot go away with him, as her brother has terminal cancer, and she has to take care of Olivia. Harvey asks Zoe why she didn’t tell him sooner, to which she replies that she didn't expect him to stay when he found out Olivia was staying with her, but that she was happy that he chose to do so. She informs him that she will be leaving soon, and Harvey goes to console her.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d18bff6c-1dce-11ee-b06f-52b307fec202",
            "Mike arrives at his apartment to find Tess waiting for him, wearing only her underwear. She inquires how the case he was working on went, but he brushes her off. She invites him to join her on the bed, but Mike states that he can no longer continue their affair. He asks Tess whether she loves her husband, and after she replies that she doesn't know, he states that what they are doing is wrong, and he no longer wishes to be a part of what they are doing. Tess asks Mike what he would do if she wasn't married, but he asks her to leave, and she does so.",
            {
                "title": "Suits",
                "ep_title": "Blind-Sided",
                "season_num": 2,
                "ep_num": 11
            }
        ],
        [
            "d2bb1210-1dce-11ee-b06f-52b307fec202",
            "Plot\nthumb|right|250px|\"That's it? No fun banter? No witty repartee?\"\nMike Ross finally decides to get rid of his stash of weed by vacuuming it and throwing it out with a bag of other things. At the office, Donna Paulsen waits for Harvey Specterto arrive to give him urgent news. But first, they discuss the change of name of Pearson Hardman; Harvey comments that \"Pearson\" does not have the same ring to it, and Donna suggests \"Pearson Paulsen\". She then changes the topic and asks about his weekend with Zoe Lawford before realizing through Harvey's odd behavior that the weekend never happened.",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb12f6-1dce-11ee-b06f-52b307fec202",
            "Moving onto business, Donna tells Harvey that he needs to meet with one of his clients, Trent Devon. He then asks for Mike and becomes furious when he finds out that Mike hasn't come in to work yet. During his meeting with Trent, Trent tells Harvey about his concerns about the changes at the firm and the effect it may have on his company and is even considering leaving Pearson Hardman for another firm.\nthumb|250px|left|\"Today is day one of the Louis Litt rehabilitation program.\"\nMeanwhile, Jessica Pearson also approaches Louis Litt about another client, Bernie Carillo, threatening to leave. Louis then confronts Jessica about not letting him hire Maria Monroe while she let Harvey hire a fifth-year. Jessica then retorts, reminding him that she had warned him about voting for Hardman against her, and she is willing to put that behind her if Louis contributes to the firm and does something about the leaving clients. Louis then finds Harold Gunderson and chastises him about the client.",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb131e-1dce-11ee-b06f-52b307fec202",
            "When Mike finally comes in, he brings Donna her very precisely blended latte and does not listen when Donna tries to warn him about Harvey's mood. Harvey then starts reprimanding Mike and threatens to fire him if he does not \"get his shit together\", which Mike was doing that caused Mike to be late in the first place.",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb1332-1dce-11ee-b06f-52b307fec202",
            "That night, Donna tells Harvey that he might have gone too far with Mike. She then quotes him telling Mike earlier that \"People don't leave [him],\" realizing that he might actually be referring to Zoe. He finally tells her that it is Zoe, and that she is leaving to take care of her niece whose father is dying. She then tells him that he shouldn't be taking out his frustrations on Mike.\nthumb|250px|right|\"Here's to the wonderful world of being an associate.\"",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb1350-1dce-11ee-b06f-52b307fec202",
            "Elsewhere, Mike is drinking alone at a bar when Jimmy Kirkwood appears and sits with him, saying he owes him one for making him quit Pearson Hardman, which then led him to work at Bratton Gould. He then tells him that working at that firm is great and then invites Mike to work with him. Mike refuses but finds out the names of two of the associates who will be transferring: Clarke and Owens. He then goes immediately to Harvey's apartment to tell him, and they realize that the firm must also be poaching their clients, particularly Trent Devon. Harvey then immediately thinks of Allison Holt and Daniel Hardman, speculating their involvement and their grudge against Pearson Hardman.\nthumb|250px|left|\"Pearson Hardman is falling apart, and I'm telling you, the avalanche has already started.\"",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb1364-1dce-11ee-b06f-52b307fec202",
            "The next day, Jessica and Harvey has a meeting with Allison Holt in their under construction building. When asked about it, Allison denies any involvement with Daniel, and they then tell her about the tortious interference claim they are filing against them for using privileged information to target their clients. Allison just scoffs at it and goes on to taunt them about more possible future attacks on the firm, saying everyone knows about the civil war the firm had gone through.\nthumb|250px|right|\"You can't fire Mike!\"",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb1378-1dce-11ee-b06f-52b307fec202",
            "At the firm, Louis goes to Rachel Zane for an update about the Carillo contracts and finds out that they have lost the client. He then goes straight to Harold, despite Rachel's objections, and fires him in front of the other associates, warning them that they cannot afford incompetence at a time like that. Later, as Harold packs up his things, he tells Mike about how good he is and even shows him his record at Harvard which then impresses Mike enough to try to talk Louis out of firing him. Louis then lists some of the big mistakes Harold has made over his years at the firm. After getting Louis to agree, however, he set conditions that Mike will be responsible for Harold when he stays, which Mike does not agree to, given his already full load with Harvey's assignments.\nthumb|250px|left|\"No one is leaving you.\"",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb138c-1dce-11ee-b06f-52b307fec202",
            "Harvey and Donna then go over the clients and decide on tactics to woo them to keep them. Then, through his recent discovery from Harold, Mike comes in and tells them that two other fifth-year associates: McKinney and Kline, and that all four of these fifth-year associates are in fact the best ones under Louis.\nthumb|250px|right|\"You and I... we're done.\"\nHarvey then goes to confront Louis, assuming that Louis has been telling Allison Holt who to hire, which Louis denies. In a fit of anger, Harvey trashes Louis' desk and tells him that he is now unwanted in the firm.",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb13aa-1dce-11ee-b06f-52b307fec202",
            "Louis then sets up a meeting with Allison and offers to transfer to Bratton Gould. He asks her why they have been going after his associates but not him, and Allison replies that despite being aware of his very impressive record, his loyalties apparently waver according to Daniel Hardman. Louis then tells her that he is leaving Pearson Hardman because he is no longer wanted there, and when Allison points out the non-compete clause in his contract, he reveals that Jessica will waive the clause if he does not take clients with him. Because of this information, Allison gets away with only offering him a junior partnership which Louis questions but agrees to anyway.\nthumb|250px|left|\"But you also said you've always trusted me, and I'm telling you, trust me one more time.\"",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb13be-1dce-11ee-b06f-52b307fec202",
            "Harvey's clients are all secure except for Trent Devon. Mike finds out what deal Bratton Gould may have made with Trent. Mike finds out that a company, Flash-Start, has recently spoken about its interest in Trent's work, and apparently, Allison represents a hedge fund that's about to buy controlling interest. This deal will offer him a lot of money and he gets to run both companies. Harvey realizes that the deal is too good to be true, so he goes to Trent and tells him that he wants to check the terms of the agreement and will let him go if that is what he really wants.",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb13d2-1dce-11ee-b06f-52b307fec202",
            "Back at the office, Louis approaches Jessica and asks her to waive his non-compete contract terms so he could take a position at another firm. Jessica realizes that Allison had gotten to her, but Louis says he was the one who approached Allison, saying he got Harvey's message that he was no longer welcome at Pearson Hardman. Louis also tells her that he was not the one tipping off Allison about the good associates, and Jessica tells him that he was willing to give him one more chance because she knows what it was liked to be played by Daniel Hardman. Jessica, having no clue about what Harvey has done, tells Louis that she sees his worth and wants him to stay but waives his non-compete anyway.",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb13e6-1dce-11ee-b06f-52b307fec202",
            "Harvey later drops Mike off at the firm so he could find out what's too good about the deal, but not before Mike questions his real intentions at \"helping\" Trent. Before he could get into the building though, a man revealed to be Tess' husband jumps him. Mike recognizes him and apologizes, but Tess' husband continues to beat him up anyway, warning him to stay away from Tess.\nthumb|right|250px|\"Let's just say that actions have consequences.\"",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb13fa-1dce-11ee-b06f-52b307fec202",
            "Louis, close to tears, leaves his resignation letter on Jessica's desk, packs his things and begins to leave when he sees a bleeding Mike stumbling from the elevator. Louis, who has experience with first aid kits because his cat often got into fights before, takes care of his wounds. Mike then asks him why he was about to leave when he saw him, and Louis tells him about Harvey no longer wanting him there. When Mike tells him that he should not quit for Harvey's sake, Louis tells him that his rivalry with Harvey was not always like this: that it was once healthy and was strictly in the office only, and once office hours are over, they \"punched out\", and so did their spiteful relationship. But now, apparently, Harvey never punches out anymore, and he cannot take any more of it any longer. Mike then suggests redeeming himself through action as well, starting with helping him on Trent's case.",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb1418-1dce-11ee-b06f-52b307fec202",
            "The next day, Jessica tells Harvey that Louis is quitting because of him and rebukes him for it, saying he is off his game. Mike then walks in on them, and when Jessica sees his bruised face, he tries to explain himself but to no avail. Harvey then demands to know what happened to him, intent on kicking whoever beat him's ass, but Mike refuses to answer, telling Harvey that he does not want to because of the story he had told him about his parents in \"High Noon\". Harvey stops asking and tells him that he got off easy\n\nMike then tells him that the deal Trent will make with Allison will screw him over, that after the deal, they are just going to sell Trent's company and that the firm only wanted to take Trent away from Pearson Hardman as their client. Harvey realizes that Mike had help from Louis, and Mike tells him that he is now certain Louis didn't betray them.",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb142c-1dce-11ee-b06f-52b307fec202",
            "Harvey later meets with Allison to tell her the bad news for Bratton Gould: Trent is letting go of Allison's deal and staying with Pearson Hardman, and that their hedge fund client, Edelson Investments, will also be moving to Pearson Hardman. Allison is apparently not disappointed. Allison then offers Harvey to come work at Bratton Gould. Harvey, of course, declines, and Allison questions his position and future at the firm. She then warns Harvey that the battle is just beginning for them, saying other firms now know that Pearson Hardman is vulnerable.",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb1440-1dce-11ee-b06f-52b307fec202",
            "Meanwhile, Mike meets with Jimmy again. Jimmy is more than enthusiastic to recruit Mike, saying he will look good for bringing a good lawyer like Mike in, so he is disappointed when he finds out that Mike wanted him to hire Harold for him instead. He is, however, impressed by the grade Harold has on his resume and still owes Mike a favor, so he agrees.\nthumb|left|250px|\"One day, what he is isn't going to be enough to make up for what he isn't.\" - Jessica talking about Mike",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb1454-1dce-11ee-b06f-52b307fec202",
            "Harvey reports to Jessica his successes of the day, and Jessica commends him for it. Harvey then tells her that he and Mike were offered positions at Bratton Gould. When Harvey tells Jessica that he wants to be a name partner, though, she blows him off. Harvey insists that getting rid of the Hardman name of the firm will send out a message to the attacking firms that they are recovered, but Jessica counters that she will not rush a decision that big. She then compares Mike's lack of a degree to Harvey's lack of discretion.",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d2bb1468-1dce-11ee-b06f-52b307fec202",
            "Mike then talks to Rachel, telling her that Harold now has a job. Rachel, seeing Mike's shiner, then asks if her husband found out. She then tells him that she no longer cares, even after Mike tells her that he has ended things with Tess.\n\nHarvey then goes to Louis with his resignation paper and tears it up in front of him, telling him without words that he does not want him to quit.",
            {
                "title": "Suits",
                "ep_title": "Blood in the Water",
                "season_num": 2,
                "ep_num": 12
            }
        ],
        [
            "d3b2816c-1dce-11ee-b06f-52b307fec202",
            "Plot\nHarvey Specter and Mike Ross are messing around in Harvey's office, throwing balls of paper into a bin. Mike is one shot away from losing, but just as he throws, Jessica Pearson walks in and catches his shot. The two of them protest her interrupting their game, but Jessica is unconcerned, and promptly requests that Mike leave. She proceeds to inform Harvey of the death of Derek Portis, to which Harvey shows little sympathy, asking \"what took him so long?\". However, Jessica reminds Harvey that Derek had convinced Folsom Foods to settle in their case with Pearson Hardman, to the tune of $10 million. Harvey states that the deal only needs signing, but Jessica replies that it will not be so simple, and Harvey asks who is to replace him?",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b282ac-1dce-11ee-b06f-52b307fec202",
            "Rachel Zane is having a birthday lunch with her father, Robert Zane, and he informs her that he is due to represent Folsom Foods in a case against Pearson Hardman. Rachel responds that she is aware of the case, and Robert states that he is telling her to give her a chance to get off of the case if she so wishes. He remarks that he knows she tries to keep a low profile at the firm, and states that he wished she didn't keep secret that he is her father. Rachel responds that she doesn't broadcast the fact since people tend to treat her differently when they find out. Robert asks whether she feels people judge her for being a paralegal, but Rachel becomes defensive, replying that only he judges her in that way, and that she doesn't intend to be a paralegal forever. When Robert states that he knows, Rachel questions his sincerity, and whether he truly believes she has what it takes. He replies that she could do whatever she wanted, and that after five years as a paralegal, she might",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b282e8-1dce-11ee-b06f-52b307fec202",
            "she might consider doing something else. Rachel angrily scolds her father for telling her that she \"won't amount to anything\", and abruptly leaves.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b28310-1dce-11ee-b06f-52b307fec202",
            "Katrina Bennett enters her new office at Pearson Hardman, only to find Louis Litt waiting for her there, cutting his nails. She points out to him that he is in the wrong office, but he states otherwise, and reveals he is aware of her position as Harvey's new associate. Katrina responds by asking who he is, to which Louis cryptically replies that \"that's [their] problem right there\", before clarifying by asking why she hadn't yet come to see him. Louis informs Katrina that he oversees all first and second year associates, but Katrina counters by asking why, if that is the case, he is in a fifth year associate's office. Louis is undeterred, and turns to use Katrina's computer. Katrina points out that it is password protected, but Louis reveals he has already guessed her password, and is unconcerned when Katrina states it to be a violation of her privacy. After briefly reading over her current case, he suggests her defense to be weak, despite Katrina's objections, and states that he",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b2832e-1dce-11ee-b06f-52b307fec202",
            "and states that he \"will be forced to supervise [her]\". Katrina again objects, saying that she doesn't \"need a babysitter\", but Louis remains unsympathetic, and sarcastically welcomes her to Pearson Hardman, before leaving.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b2834c-1dce-11ee-b06f-52b307fec202",
            "Rachel goes to see Mike in his cubicle, and requests that he put her as the paralegal on the Folsom Foods case. Mike refuses, saying that he doesn't believe it would be a good idea, but Rachel replies that the new opposing counsel is her father. Mike is surprised to find out that Robert Zane is her father, but is still reluctant to put her on the case. He asks Rachel whether she considers them working together a good idea, but after Rachel questions whether Mike is in a position to ask her what constitutes a good idea, Mike agrees.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b28374-1dce-11ee-b06f-52b307fec202",
            "Harvey and Mike are in a meeting with Robert Zane in Harvey's office. Harvey offers Robert his condolences regarding Derek Portis, but Robert agrees with Harvey's earlier assertion that \"Derek was a dick\". Harvey informs Robert that their deal only needs signing, and Mike courteously offers him the deal, but Robert counters by saying that \"[he] didn't come over … to sign, [he] came to negotiate\". Harvey states that his attempt to renegotiate is bad faith, but Robert replies that the settlement Derek negotiated was too much, and offers them $2 million in return. Harvey refuses Robert's offer, to which Robert asks when they wish to arrange the deposition of Sloan Moseley. Mike states that she had already been deposed, but Harvey interrupts his associate and states that Robert is within his right to do so, and Robert informs them that \"when [he gets] done with her, she is going to jump at the $2 million\". As Robert leaves, Harvey confronts Mike regarding his overly respectful attitude",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b28388-1dce-11ee-b06f-52b307fec202",
            "respectful attitude towards Robert, and reveals that he is aware of Mike putting Rachel on the Folsom Foods case. Mike replies that Rachel requested to be put on the case, but Harvey again warns Mike about telling Rachel his secret.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b283a6-1dce-11ee-b06f-52b307fec202",
            "Katrina confronts Donna Paulsen as she exits the elevator, and is surprised to discover that Donna already knows who she is, to which Donna replies that she \"know[s] who everybody is\". Katrina asks Donna for a minute of her time, attempting to bribe her with home-made butterscotch cookies, and after some initial hesitation, Donna relents. Katrina immediately asks her \"who the hell is Louis Litt?\", to which Donna responds that it \"might take more than a minute\". Katrina voices her frustration with Louis, and asks whether Harvey would stand in her way in getting even, to which Donna replies that he would not, but warns her that if she is going up against Louis, she'd \"better be prepared to go the distance\".",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b283c4-1dce-11ee-b06f-52b307fec202",
            "Robert visits Jessica in her office, and requests that she settle the Folsom Foods case. Jessica responds that she thought they were already settling in the case, but Robert informs her that he changed the settlement offer from the one Derek proposed. Jessica in turn informs Robert that she already knows Harvey rejected the offer Robert made, but Robert counters by saying that with Pearson Hardman losing employees and clients, she needs a high profile win, no matter \"how ugly\".\n\nJessica finds Harvey, and informs him of her meeting with Robert. She relays to him how Robert feels they are weak after what happened with Alison, and is attempting to force her to settle at his lower offer. Harvey berates Robert's actions, calling them \"below the belt\", and when Jessica asks what she does to people like that, Harvey replies \"cut them off at the knees\", before leaving.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b283e2-1dce-11ee-b06f-52b307fec202",
            "In the break room, Katrina approaches Louis as he is making a smoothie. She attempts to start a conversation, but he quickly interrupts her, and forces her to wait until he is done. When he is finally finished, Katrina apologizes for her previous attitude, and informs Louis that after looking up his record, she realized he is a \"white collar genius\", and begs for his help with her case. Louis encourages her to continue, and Katrina relays to him that her motion to dismiss is on Wednesday, but that she is hesitant since she has never been able to connect with Judge McIntyre, who is residing over her case. Louis tells her that the judge is a stickler for the rules, and provided she abide by them, she should be fine. Katrina requests that Louis sign onto her case as first chair, to which he agrees.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b28400-1dce-11ee-b06f-52b307fec202",
            "Rachel enters Harvey's office, and confirms whether Harvey wished to see her. Harvey replies that he did, but informs her that the usual protocol is to let Donna know first. Rachel points out that Donna is not at her desk, but Harvey responds that that is not by accident, and asks Rachel whether she knows why he wished to see her, and why Donna is not at her desk. Rachel replies that he wished to see her \"because [her] last name is Zane\", and Donna isn't there because Harvey wishes to ask her to do something Donna would advise her against doing. Harvey enquires whether she knows what that is, to which Rachel replies that he wants to know if she wishes to be on the Folsom Foods deposition, to which Rachel adds that she does. Harvey asks her whether she feels her presence will rattle her father, to which she replies that she feels he wouldn't care, which Harvey states to be good. Rachel enquires why that would be the case, and Harvey informs her that if that is how she feels, then her",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b2859a-1dce-11ee-b06f-52b307fec202",
            "she feels, then her relationship with her father is worse than she thinks, and that her father cares about her more than she believes. Rachel is left surprised by Harvey's statement, and leaves.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b28694-1dce-11ee-b06f-52b307fec202",
            "The next day, Robert walks with Harvey to the deposition room, only to find his daughter in there preparing files. He asks Harvey whether what he is doing is supposed to be a joke, telling him that Rachel doesn't need to be there. He informs Harvey that her being there won't stop him from doing his job, but Harvey counters by asking Robert what his daughter will think of him after he has attacked their client. Robert accuses Harvey of being cruel, but Harvey states that it is his own fault after he pulled their deal. As Robert enters the room, Mike arrives, and seeing Rachel, asks Harvey what he did, to which Harvey replies \"my job\".",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b286d0-1dce-11ee-b06f-52b307fec202",
            "Robert begins his deposition of Sloan Moseley, and questions her on why she chose to work in the food industry. She replies that she has a love of food, but Robert counters by asking whether such a thing is necessary in an executive position. Sloan responds that she felt her love of food was a perfect fit with the company, to which Robert asks why she was looking for employment elsewhere if Folsom Foods was such a good fit. She states that she had worked at Folsom Foods for nine years, but had been passed over multiple times for promotion \"in favour of less qualified men\". Robert suggests that she is blaming his client because she is unwilling to work out what it takes to succeed in her industry, to which Mike asks whether Robert has a question for Sloan. In response, Robert asks Sloan why she didn't simply focus on one particular job rather than several, but Sloan replies that doing so would have required a step backward. Robert however, suggests that such employment was the only",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b286ee-1dce-11ee-b06f-52b307fec202",
            "was the only thing she was capable of finding, as \"no-one thought [she was] any good at the job [she] had\". Sloan denies his accusation, but Robert states he has sworn testimony from a head-hunter that \"no-one wanted [her]\". Mike confronts Robert over his badgering, but Robert continues, calling Sloan \"untalented\" and \"pathetic\" and that she was \"blaming other people because [she doesn't] have the skills or the fortitude or anything else to make it in [her] chosen field\", a statement that leaves Rachel taken aback. Robert states he has several more questions to ask, but Mike interrupts him, stating that the deposition is over.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b2870c-1dce-11ee-b06f-52b307fec202",
            "Rachel confronts Mike in the men's room, and berates him for trying to protect her during the deposition. Mike, however, states that he wasn't even watching Rachel during the deposition, and that he ended the deposition to protect the client. He suggests that she wanted to be put on the case to make it about herself versus her father, which Rachel denies, but Mike continues, reminding her that the case is about Folsom Foods and their client.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b2872a-1dce-11ee-b06f-52b307fec202",
            "Louis bursts into Katrina's office, and angrily informs her that he received a fine from Judge McIntyre for missing his court date, as she lied to him about when the hearing was. She denies his accusation, stating that the correct court date was in the documents she gave him. Walking up to her, Louis states to Katrina that she doesn't want to pick a fight with him, but Katrina replies that she wasn't the one that picked the fight. Louis suggests otherwise, and tells him that she will pay his fine, in addition to writing a letter to the judge to apologize. Katrina bluntly refuses, and asks him who he is going to tell that she lied about the date.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b28748-1dce-11ee-b06f-52b307fec202",
            "Mike finds Harvey, and suggests that he made things personal with Robert Zane by putting Rachel on the Folsom Foods case. Harvey states that Robert was the one that made things personal when he threatened the firm and attacked Sloan Moseley during the deposition. Mike states that it didn't appear to have any effect on Robert, and questions whether Harvey thought about the effect his actions would have on Sloan Moseley, or on Rachel. Jessica interrupts their conversation, and berates Harvey for not going far enough in his actions against Robert, stating that Sloan called to accept Robert's $2 million offer.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b28770-1dce-11ee-b06f-52b307fec202",
            "Harvey goes to see Robert on the golf course, but Robert rejects Harvey's assertion that he is there to negotiate. He reveals to Harvey that he is aware Sloan wishes to accept his offer, but informs Harvey that his offer has dropped to $1 million. Harvey attempts to discuss the issue, but Robert drops his offer again, and then twice more, finally offering Harvey a $100 dollar note. He criticizes Harvey for putting Rachel in the deposition so she could see him attack Sloan Moseley, adding that he did so because it is his job. Harvey counters that he was attempting to protect his client, because that is his job, but Robert states that his client is \"scared shitless\", suggesting that he \"did [his] job a lot better than [Harvey] did [his]\". He informs Harvey that the settlement offer is gone, and that he will have to take what he wants at trial.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b2878e-1dce-11ee-b06f-52b307fec202",
            "Rachel approaches Harvey as he is buying a bagel, and asks him what he needs to take down her father. Harvey rejects the necessity of such a drastic action, but Rachel responds that Mike informed her that her father pulled the settlement, and that \"[they] can't let that happen\". Harvey questions her including herself in the case, but Rachel responds that she works at Pearson Hardman as well. Harvey states that he now understands, making Rachel think he is talking about her wanting to get her own back on her father, but Harvey corrects her, saying that he realizes why Donna likes her so much, leaving Rachel somewhat stunned as her unnecessary outburst. She begins to apologize, but Harvey interrupts her, stating that he was intending to give in and drop the case, but now she has \"accosted [him] during [his] me time\", he has changed his mind. Rachel realizes that he is joking, and intended to continue fighting anyway. Harvey sarcastically asks Rachel if she wants to eat his bagel as",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b287ac-1dce-11ee-b06f-52b307fec202",
            "to eat his bagel as well, but Rachel thanks him and takes it from him, before realizing again that he was joking,. She apologizes profusely, before leaving.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b287ca-1dce-11ee-b06f-52b307fec202",
            "At the hearing for Katrina's client, Louis enters the courtroom holding a folder containing a large number of files. He approaches Katrina, who questions his appearance at her hearing, but Louis apologizes for his previous actions, saying that it is her case, and he is no longer first chair. She quickly thanks him, but requests that he leave. However, Louis informs her that he cam to give her back her files; Katrina refuses the files, saying that she \"wasn't born yesterday\", and she already has her files in front of her. Louis tries again to give her the files, but she rejects them again. The judge begins the hearing, asking whether Katrina has something she wishes to give him. Katrina confirms she does, and opens the folder in front of her, only to find it filled with pictures of Louis photo-shopped as former American presidents. Louis offers a hollow apology, and states that the files she is looking for are in the folder he brought with him. Katrina goes to grab them, but Louis",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "c412d842-1dce-11ee-b06f-52b307fec202",
            "The Shelf Life is the tenth episode of the first season of Suits and the tenth overall. It first aired on August 25, 2011.",
            {
                "title": "Suits",
                "ep_title": "The Shelf Life",
                "season_num": 1,
                "ep_num": 10
            }
        ],
        [
            "d3b28806-1dce-11ee-b06f-52b307fec202",
            "Donna enters Louis' office, and requests that he let go of his feud with Katrina. Louis refuses, stating that won't \"let anything go until that women kneels before Zod\". Donna asks him what he wants from Katrina, but Louis refuses to answer. Donna realises that Louis is really angry at Harvey for hiring Katrina when he wasn't allowed to hire Maria Monroe. Louis denies it is about Maria, stating that it is about him getting respect from a new employee. Donna acknowledges that Louis beat Katrina, but informs him that the best way to earn her respect would be to make up with her and leave her alone. Louis questions her statement, asking her whether she and Harvey leaving him alone after what happened with Daniel was them showing him respect. Donna reminds him that Harvey welcomed him back, but Louis questions whether it was truly meant given that Harvey never said a word. He informs Donna that he always considered the practical jokes they played on him to be a mark of respect, but that",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b28824-1dce-11ee-b06f-52b307fec202",
            "respect, but that she has barely spoken to him since he backed Hardman, and instructs her to inform Katrina that he isn't \"in a forgiving mood\".",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b28842-1dce-11ee-b06f-52b307fec202",
            "Mike approaches Harvey as he is buying lunch, and tells him that he has an idea regarding Folsom Foods. He informs Harvey that he checked a review of every promotion over the past five years, and that the company uses similar phrasing every time they do not promote a woman, something which is not evident for the men. He indicates that Folsom Foods deliberately shielded themselves from any one woman being able to claim discrimination, treating each woman in the same way. Harvey takes this information to Robert, revealing to him that 113 women in total were denied promotions because of their gender, not because they were \"untalented or pathetic, or lack the fortitude to excel in their chosen field\". Robert calls their evidence \"a crock of shit\", but Harvey states that with the vast number of clients, they will \"be lucky to settle for $200 million\".",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b28856-1dce-11ee-b06f-52b307fec202",
            "Louis arrives at the court house in a good mood, but his mood is somewhat reduced when he is pulled over by a security guard after passing through the metal detector. Louis informs the guard that he merely forgot to remove his belt, but the guard proceeds to sweep him with a hand held detector, and discovers Louis' nail clippers in his breast pocket. The guard states that the clippers could be used as a weapon, but Louis defends himself, saying that he doesn't know how the clippers came to be in his pocket. He goes to take them back, but the guard grabs him and pins him against a table, arresting him for carrying a concealed weapon and assault. Katrina appears, and refers to the security guard by name. The guard in turn states that it is \"nice to see [her] again\", and Louis proclaims that it was Katrina. The guard, however, informs Louis that he is aware Katrina set him up.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b28874-1dce-11ee-b06f-52b307fec202",
            "Rachel is waiting for her father in his office, looking at a picture of herself framed on his desk. Robert enters, and noticing the picture in her hand, states that he always loved that picture of her. Rachel asks to talk about the deposition, but Robert replies that they cannot talk about the case. Rachel states again that she only wishes to talk about the deposition, as she doesn't \"give a shit about the case\", prompting Robert to ask why she wished to be put on the case in the first place. Rachel replies that she did so because, during her birthday lunch, he suggested she sit the case out because she couldn't handle it. Pointing to the picture Rachel had in her hand, depicting Rachel at the auditions for a school play, Robert asks her whether she knows why he likes that picture so much. Rachel replies \"because [she was] still [his] little girl\", but Robert informs her it is because she was happy then, reminding her that it killed her to not get the part she auditioned for. Rachel",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b28892-1dce-11ee-b06f-52b307fec202",
            "for. Rachel defends herself by saying that she was just a child, but Robert states that most children would have let it go, but Rachel never did. Rachel responds that she did other things, to which Robert asks why she isn't doing other things now. Rachel informs her father that she took the LSATs, and scored a 172. Robert asks his daughter why she has taken so long to tell him, and Rachel replies that she \"didn’t want to hear some joke about [his] 177\". She adds that, even though he was talking to Sloan Moseley during the deposition, it felt like he was aiming his attacks at her, and tells her father that he needs to \"toughen up, as [she isn't] that little girl anymore\", before leaving.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b288b0-1dce-11ee-b06f-52b307fec202",
            "Katrina visits Louis in jail, and mockingly asks him \"who's going to kneel before Zod now\". Louis, looking somewhat dishevelled, states he won't kneel before anyone, particularly after Katrina framed him. Katrina counters that Louis humiliated her with Judge McIntyre, and considers what he did to her far greater than what she did to him. She informs him that she put away all sorts of people during her time in the DA's office, and those people will spend \"the rest of their lives realising [she] wasn't just a pretty face\". Louis responds that their feud has nothing to do with her being a woman, but because she took a job from someone that deserved it more, namely Maria Monroe. Katrina informs Louis that she went to resubmit her motion to dismiss, but that the judge had already received it from Louis. Katrina asks him if he is ready to call a truce, to which Louis agrees.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b288ce-1dce-11ee-b06f-52b307fec202",
            "Jessica finds Robert waiting for her as she arrives the courthouse, and he compliments Harvey on his tenaciousness. She asks him whether he is there to give her a cheque, but instead he hands her a file, indicating that they intend to split their class of cases, as after his discussion with Rachel, he realised that \"not all women are the same\". Jessica contests that they will be able to have all one 113 cases tried separately, to which Robert suggests they will be able to split it into at least 45, all of which will bleed dry Pearson Hardman's available resources.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b288ec-1dce-11ee-b06f-52b307fec202",
            "Jessica informs Harvey what Robert told her, which Harvey finds laughable. Jessica cuts him off however, and informs him that Robert has proposed a merger. Harvey refuses to accept such a move, stating that they \"didn't fight off Hardman to end up [there]\". Jessica counters that it was Harvey's actions that put them in that position, and that if he was going to \"cut him off at the knees\" he should have made sure he wasn't going to get back up. Harvey tells his superior that they can only take the hits for so long, and after some deliberation, Jessica states that they will fight until the end.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b2890a-1dce-11ee-b06f-52b307fec202",
            "The next day, Jessica meets with Robert, and promptly rejects his merger proposal. She hands him a press release, indicating that she intends to fight every one of the 45 gender discrimination cases. Robert claims it to be rubbish, but Jessica reiterates her seriousness, stating that she would rather lose her firm than \"get married staring down the barrel of a shotgun\". Robert points out that she won't be able to have attend all 45 depositions, but Jessica simply replies that he will end up paying 45 times the amount he could settle for there and then. She admits that the first case may be difficult, but that after that, the cases will fall like dominoes, and she will be left standing at the end holding \"a big, fat cheque\".",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b28932-1dce-11ee-b06f-52b307fec202",
            "Louis walks into his office, only to find his police mug shot pasted on every one of his office windows, with unflattering captions underneath each image. He asks who did it, and angrily sits down at his desk. Donna enters, and states that Louis \"[does] look kinda hot as a bad boy\". Louis asks her whether Katrina was the one who put up the pictures, citing the truce they decided upon, but Donna corrects him, stating that it was Harvey who put up the pictures. As she leaves, Louis stands to ask her to stay, only for his pants to rip as he does so, revealing his underwear.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d3b28946-1dce-11ee-b06f-52b307fec202",
            "Robert enters Rachel's office, and informs her that he has decided to drop the Folsom Foods case. Rachel asks why, and he states that he never should have taken it in the first place, and he was wrong to say what he said. Rachel reminds her father that they never finished their lunch, and they agree to do so the next day. After Robert leaves, Mike enters, and asks Rachel whether she has made up with her father; Rachel proclaims that it was a start. He hands her a framed copy of her LSAT score as a belated birthday gift, which she thanks him for.\n\nIn Jessica's office, Harvey asks his superior whether she dealt with Robert Zane. Robert interrupts their discussion, and Jessica assumes that his appearance in her office is because he wishes to settle. Robert, however, informs the two of them that, due to a conflict of interest, his firm has decided to farm out their case, to Daniel Hardman.",
            {
                "title": "Suits",
                "ep_title": "Zane vs. Zane",
                "season_num": 2,
                "ep_num": 13
            }
        ],
        [
            "d4d962b8-1dce-11ee-b06f-52b307fec202",
            "Plot\nSince Robert Zane has dropped out of the gender discrimination suit against Pearson Hardman, Folsom Foods has hired Daniel Hardman to defend them. And not only that, but Monica Eton is filing her own wrongful termination suit against Jessica Pearson, with Hardman as her lawyer. And since Pearson Hardman is bound by the confidentiality agreement Jessica signed with Daniel, they cannot use Daniel's affair with Monica as a reason for her Monica's termination years ago.\n\nDaniel then makes Mike guilty by making Mike think it was his idea that made Daniel and Monica pursue the lawsuit. He also tries to pit Harvey against Jessica by convincing Harvey that Jessica does not trust him.\n\nMeanwhile, Rachel is busy filling out her application form to Harvard and is tense about writing her essay. Rachel is determined to get into Harvard enough to not have a back-up law school, so she can work at Pearson Hardman.",
            {
                "title": "Suits",
                "ep_title": "He's Back",
                "season_num": 2,
                "ep_num": 14
            }
        ],
        [
            "d4d96434-1dce-11ee-b06f-52b307fec202",
            "Both Louis and Donna are still bitter about Daniel's betrayal, which included sabotaging and using both of them. Louis wants in on the case, but Donna is sure that Harvey won't let him. Louis states that he still feels guilty for betraying them to Hardman, but Donna reassures him that their issues are a thing of the past.",
            {
                "title": "Suits",
                "ep_title": "He's Back",
                "season_num": 2,
                "ep_num": 14
            }
        ],
        [
            "d5c318d6-1dce-11ee-b06f-52b307fec202",
            "Plot\nHarvey Specter and Mike Ross are watching an advertisement featuring Hanley Folsom, the CEO of Folsom Foods, in which he states his objections to the recent gender discrimination allegations that his company is facing. Harvey pauses the video, and asks Mike to find something that will incriminate Hanley. Mike responds that he has already looked and cannot find anything, but Harvey persists, and requests that he do whatever it takes to catch Folsom out. Mike informs his superior that his request to hire an investigator was denied, but Harvey encourages Mike to \"do it anyway\", and that he will \"take care of it\".",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c319d0-1dce-11ee-b06f-52b307fec202",
            "Harvey enters Jessica Pearson's office, and states that they need to discuss the distribution of resources. Jessica agrees, informing Harvey that she has heard that several clients haven't had their calls returned. Harvey reminds her that due to Daniel Hardman's actions, they have seven cases which need immediate attention, at the expense of the others, but Jessica states that they cannot simply give up on their other clients. Harvey replies that he will deal with the situation, but requests additional resources to continue their fight. Jessica replies that they do not have the available funds to cover the additional resources, after the hit they took from settling with Monica Eton. Harvey suggests she use their line of credit with the bank, but Jessica informs him that she has already tried, and that the line is gone. Harvey is shocked at her statement, and asks Jessica how she proposes he continue fighting their cases.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c319ee-1dce-11ee-b06f-52b307fec202",
            "Mike is working with Rachel Zane in the Pearson Hardman library on the Folsom Foods case. He requests some documents from her, but she is daydreaming and doesn't hear him. He eventually gets her attention, and asks her what she is doing. Rachel replies that she is working, but after looking at her computer, Mike discovers that she is actually looking at a map of Boston, perusing possible locations for where she could live when she attends Harvard. Mike becomes annoyed when he discovers she has been procrastinating for the past 45 minutes, but Rachel counters by saying that she is not good at waiting. Mike consoles her that she did everything she could to get into Harvard, before being called away by Harvey. He informs Mike that Jessica has approved the resources they need, but only on one case. Mike objects, stating that they have to fight every case, but Harvey cautions his associate that rather than fighting every case, they will put everything into one attack. He asks Mike what",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31a02-1dce-11ee-b06f-52b307fec202",
            "He asks Mike what would be the best case to choose, to which Mike immediately replies Bakersfield, as it has the \"lowest percentage of female promotions\" but the \"highest percentage of female applicants\", and is run by Hanley Folsom's brother-in-law.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31a16-1dce-11ee-b06f-52b307fec202",
            "Donna Paulsen enters Harvey's office, and presents him with a coffee. Harvey states that he doesn't require any coffee, but Donna suggests otherwise, before fussing with his suit. Harvey attempts to dissuade her, stating that he is only meeting with clients, but Donna informs him that there has been a slight change of plans, adding that he \"will understand when [he] get[s] there\". She begins to tidy Harvey's hair, and after some hesitation, he allows her to do so.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31a2a-1dce-11ee-b06f-52b307fec202",
            "Harvey enters the conference room, only to find Dana Scott waiting for him there. He asks her how married life is, but she informs him that she never got married. Harvey looks at her suggestively, but she brushes off his implication that it was because of him. She informs him that she has come to see him about Bakersfield, but Harvey states that he will not let her steal his clients. Dana reveals that she and her firm already have, stating that \"Bakersfield is everything\", and suggests Harvey allow her to do so or she will take more of his clients. Harvey implies that her being there is personal, but Dana denies his accusation, saying that it is \"just business\". Harvey is unconvinced, and bluntly refuses Dana's request.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31a3e-1dce-11ee-b06f-52b307fec202",
            "Harvey informs Jessica of Dana's actions, and reveals that it is her intention to take ten more of their clients. Jessica voices her admiration of Dana, and reveals that she had considered hiring Dana in the past, as \"she was the best on paper\", but chose to hire Harvey instead. Harvey states that he intends to turn their financial troubles into a strength, suggesting that they join forces with Dana's firm who can help them fund their assault. Jessica is skeptical, and points out that joining forces will mean sharing all 45 cases, rather than giving up 10. Harvey counters that since Dana's firm is based in London, Pearson Hardman will be the ones running point. Jessica is still not convinced, since it would mean giving up a share of the winnings, but Harvey responds that joining forces is the best way to defeat Hardman. Jessica agrees, but cautions Harvey as he leaves that he had better not lose.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31a52-1dce-11ee-b06f-52b307fec202",
            "Mike enters the conference room with a box of files, only to find Katrina Bennett already there. As he approaches her, she begins to divide the work between the two of them, but Mike promptly interrupts her. Katrina continues, stating that they don't have all day to work on the Bakersfield case. Mike replies that he didn't realize she was on the Bakersfield case, but Katrina simply responds that she is, before ordering Mike to start working. Mike stops her again, stating that he is the lead on the case, and they will not be working on what Katrina is proposing until they have some up-to-date statistics to show Harvey. Katrina proceeds to list the relevant statistics, which she states she checked with a statistician. Mike informs her that the statistician is wrong, stating that he did not make the necessary adjustments; Katrina begins to state the adjusted figure, only for Mike to interrupt her and state the figure himself. Katrina asks him how he knew the relevant figure, to which",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31a66-1dce-11ee-b06f-52b307fec202",
            "figure, to which Mike replies that he \"did it in [his] head\". He reiterates that he is the lead on the case, but Katrina is undeterred, and tells Mike that using the original figure \"skews the results in [their] favor\". Mike sarcastically voices his shock that Katrina wishes to sacrifice their credibility by skewing the results, stating again that they will not do so. Katrina attempts to pull rank, but Mike counters that he works for Harvey. Katrina informs Mike that Jessica was the one that put her on the case, and that if he has a problem, he should \"go talk to her\".",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31a7a-1dce-11ee-b06f-52b307fec202",
            "Mike finds Harvey, and informs him that he doesn't want to work with Katrina, stating that she \"acts like everything is her idea\". Harvey reveals that he has a similar problem, as he doesn't want to work with Dana. Mike voices his surprise that they are working with Dana, though Harvey informs him that only he is working with Dana, revealing that she stole Bakersfield from them. Mike becomes nervous, and extending Harvey's metaphor that Bakersfield is akin to the Battle of Normandy, states that they will \"lose World War II\".",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31a8e-1dce-11ee-b06f-52b307fec202",
            "Dana is waiting for Harvey in his office, when Donna enters, asking her if she wants something to drink. Dana politely refuses, to which Donna voices her distrust of \"a woman who wants nothing.\" Dana counters Donna's statement by asking \"who said [she] want[s] nothing\", but Donna replies that no-one has ever said that about her. Dana asks what they have said, specifically what Donna has said about her. Donna questions whether her opinion matters to Dana, who responds that her opinion matters to Harvey. Donna replies that she has \"only ever said good things about\" her, but Dana asks her what she has thought. Donna avoids the question, telling Dana not to screw with Harvey, to which Dana asks \"don't screw with him, or don't screw him?\" Their discussion is interrupted when Harvey enters his office, and Donna uses his arrival as an excuse to leave. Dana asks Harvey whether he is going to take her up on her offer, or if he intends to fight her, but Harvey asks her what she thinks. Dana",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31aa2-1dce-11ee-b06f-52b307fec202",
            "she thinks. Dana responds that she thinks he wishes for them to try the cases together, with her firm providing the necessary financing. Harvey states that she always wanted them to try the cases together, a fact which Dana confirms. She states that they will begin with Bakersfield, but Harvey asks her why she couldn't have just directly told him what she wanted. Dana replies that Harvey doesn't \"respond to the direct approach\", and that he likes to \"feel [he] can come to things on [his] own\". Harvey informs Dana that they will not be starting with Bakersfield, despite it being the clear choice, and instead they will be going to Parkville. Dana points out that Parkville is the one division with a female manager, and the highest ratio of women executives, but Harvey states that they will be starting there because it is the \"one division where Hardman will never think to find [them]\". Dana states that Parkville is the \"dumbest place to start, and the hardest place to win\", but Harvey",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31ab6-1dce-11ee-b06f-52b307fec202",
            "to win\", but Harvey replies that after they win at Parkville, \"all the others will surrender\". Dana is unsurprised Harvey wishes to take the difficult approach, to which Harvey states his own lack of surprise that Dana is looking for the shortcut. Dana asks Harvey why he is so sure Hardman won't find out they aren't going to Bakersfield, but Harvey replies that they will create the illusion they are. Dana states his plan is not worthy of her firms money, and if he really wants to overwhelm Hardman, they should go to all 45 cities. Harvey smiles at her statement, and Dana realizes that that had been Harvey's plan all along.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31aca-1dce-11ee-b06f-52b307fec202",
            "Mike returns to the conference room, and apologizes to Katrina for his previous actions, stating that she should take the lead on Bakersfield. Katrina asks Mike what he will be working on, but he simply replies that he has \"other things\". Jessica interrupts the two of them, and states that there have been a change of plans. Mike informs her that he is aware of the changes, but Jessica informs him that she isn't talking about Parkville, and instead that she will be deposing Hanley Folsom, and needs to \"know more about him than his mistress does\" before he arrives. Katrina questions whether Folsom actually has a mistress; Jessica states that it would help their case if he did, but adds that Katrina should already know if it is true since she asked to be on the case, before leaving. Mike immediately confronts Katrina over her lying to him about Jessica assigning her to the case; Katrina counters that she asked to be on the case, and then Jessica assigned her. Mike accuses Katrina of",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31ad4-1dce-11ee-b06f-52b307fec202",
            "accuses Katrina of deliberately attempting to conceal the truth from him, but Katrina states that he did the same by not specifically informing her that the focus of their case had moved. She reveals she doesn't have a problem with what Mike did, but suggests Mike has a problem with her; Mike informs her that he has a problem with how she got her job at Pearson Hardman, to which Katrina replies that her problem with Mike is also how she got her job at Pearson Hardman. Mike is unsure what she is referring to, and Katrina clarifies that she initially felt she had received the offer on merit, but after Mike \"showed up offering to break privilege\", she realized that Harvey was hiring her to protect Mike. Mike points out to Katrina that even after she knew the truth, she still took the job, but Katrina reveals that she did so because she had already handed in her notice, urging Mike to \"stop taking everything so personally\".",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31ae8-1dce-11ee-b06f-52b307fec202",
            "Dana is flying with Harvey on her firm's private jet, and she proceeds to mock that Pearson Hardman does not have a jet of their own. Harvey casually brushes off her slight, pointing out that it is \"hard to park them in Manhattan\". Dana continues taunting Harvey, referring to the fact they only have one office in one city, but Harvey defends him firm by pointing out they have one office in the city. Dana looks at Harvey playfully, and he correctly guesses that she has realized there are certain advantages to working together. She starts to undo the buttons on Harvey's jacket, and after some initial hesitation due to his wish to keep things professional between them, Harvey acquiesces and proceeds to undo Dana's dress. He pauses however, when he realizes they have yet to decide who will take the lead on the deposition, but Dana grabs Harvey and pushes him onto the couch, and suggests they play rock-paper-scissors to decide. Harvey, however, suggests another way to decide, based upon",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31afc-1dce-11ee-b06f-52b307fec202",
            "decide, based upon their current situation. Dana asks how they will know who won, to which Harvey pushes Dana onto the couch much as she had done, and proceeds to kiss her, stating that they will know.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31b10-1dce-11ee-b06f-52b307fec202",
            "Rachel is in her office, reading a letter with a dejected look on her face. Donna enters, and upon seeing the look on Rachel's face, asks her what is wrong. Rachel doesn't reply, but Donna looks down and sees that her letter is from Harvard, and realizes she didn't get in. Rachel informs Donna she doesn't wish to talk about it, when Mike enters asking for her help. Rachel takes a second to compose herself, before informing Mike that she is \"ready to work\". Donna offers her assistance to Rachel in dealing with her situation if she needs it, before excusing herself. Mike relays to Rachel his frustration in dealing with Katrina, before asking Rachel what she feels is Hanley Folsom's personal opinion on hiring women. Rachel states she feels he doesn't believe they are good enough, but points out that he would never admit as such. Mike agrees with Rachel that he would never say as such at work, and reveals he needs access to Hanley's personal correspondence. Rachel states that it is",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31b1a-1dce-11ee-b06f-52b307fec202",
            "states that it is outside the scope of their investigation, but Mike states that he has 62 boxes of documents to find a way to put in within the scope, and only 12 hours in which to find it. Rachel readily agrees to assist him as a distraction from her current predicament, and the two of them leave.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31b2e-1dce-11ee-b06f-52b307fec202",
            "Dana and Harvey arrive at the Folsom Foods factory in Parkville, arguing over whether Harvey allowed Dana to win their competition. Harvey suggests he did, but Dana counters that he has \"never let anyone win anything [his] whole life\". Harvey does not disagree with her, and merely states that he can now demand a rematch. Their discussion is interrupted by the arrival of Hardman, who sarcastically professes his surprise at finding the two of them at Parkville. Harvey quickly recovers to offer his own sarcastic welcome to Hardman, to which Daniel states that he very nearly didn't make it, as he had intended to fly to Bakersfield, where Harvey was scheduled to fly, only to discover that Dana was flying to Parkville. Dana reveals to Hardman that they have sent people to all the other cities as well, and quickly brushes off his supposed pleasure at meeting her. Hardman directs them to the deposition, but Harvey excuses himself as he receives a call from Mike, who reveals that he knows why",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31b42-1dce-11ee-b06f-52b307fec202",
            "that he knows why they promoted Cathleen Mitchell, the manager at the Parkville factory.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31b56-1dce-11ee-b06f-52b307fec202",
            "Dana takes the lead in the deposition of Cathleen Mitchell, and questions her on Folsom Foods' hiring policy, and their unwillingness to promote women into positions of power. Cathleen retorts that the policy is to hire the best applicant, and that she herself is in a position of power. Harvey interrupts her, however, stating that she is \"not exactly like other women\". Dana questions Harvey on his approach, but Harvey continues, noting that Cathleen applied multiple times for a management position, but was repeatedly rejected for being too \"aggressive, hostile, and overly-ambitious\", and then suddenly, she was \"dedicated, hard-working, and a team-player\". Hardman interrupts Harvey's statement to note that people change, and that \"the last [he] checked, you have to ask a question\". Harvey takes Hardman's prompt, and asks Cathleen whether she was previously diagnosed with uterine cancer. Hardman queries the relevance of Harvey's question, but Harvey continues, asking Cathleen about her",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31b60-1dce-11ee-b06f-52b307fec202",
            "Cathleen about her marriage status, and the possibility of her having children, to which Cathleen replies no. Hardman again berates Harvey for his line of questioning, but Harvey counters by mentioning Hardman's previous deposition of Jessica, and directly asks Cathleen whether she \"[had] a hysterectomy that rendered [her] unable to have children, nine months before [she was] promoted\". Hardman states that his client will not answer Harvey's question, but Harvey is undeterred, stating that it will become part of the record that \"Hanley Folsom only promotes women whose attention to home and family isn't in question\". Cathleen interrupts Harvey to inform him that Folsom was unaware of her circumstances, but Harvey questions whether that was truly the case. Cathleen reiterates her statement once again, stating that it was her business only, but Harvey states that Folsom found out, and that was the reason she was promoted. Dana warns Harvey that he has gone far enough, and Hardman notes",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31b74-1dce-11ee-b06f-52b307fec202",
            "and Hardman notes that \"even Ms. Scott understands that being childless and unmarried doesn't make you damaged goods\", and sarcastically wishes him good luck on the rest of the cases.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31b88-1dce-11ee-b06f-52b307fec202",
            "Leaving the factory, Dana chastises Harvey for not informing her of the fact Cathleen had had a hysterectomy, but Harvey defends himself by saying that he only learnt it himself just before entering the room. Dana asks again why he could not have taken the time to fill her in, but Harvey responds that he didn't tell her because he \"wasn't sure [she] could play good cop\", but Dana suggests instead that it was because Harvey still wanted to win, even though they are on the same side. Harvey defends himself again, noting that Dana's anger at him will help her to establish a rapport with Cathleen, but Dana is still unconvinced and storms away angrily. Harvey follows her, and suggests that she is the one still trying to win, admonishing himself for not having realized sooner that there was something else. He requests Dana tell him the whole story, and she responds that since he beat her last time, her boss hasn't thought her worthy of being a named partner, and that if she delivers a huge",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31b9c-1dce-11ee-b06f-52b307fec202",
            "she delivers a huge win, she \"get[s] [her] name on the door\". Harvey asks Dana why she wasn't truthful with him sooner, and she informs Harvey that he \"respond[s] to strength, not weakness\". Harvey commends Dana for fooling him, and playfully tells her that if he had known she was that good of a performer, he would have \"let [her] be bad cop\".",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31bb0-1dce-11ee-b06f-52b307fec202",
            "Rachel is in the Pearson Hardman library going through several boxes of documents for Jessica's deposition of Hanley Folsom, but is distracted by her rejection letter from Harvard. She hurriedly hides the letter as Mike approaches her, and presents to him the work he requested from her. Mike goes to pick up the information, before realizing that the information from several boxes is missing. He points out to Rachel that the boxes are only several feet away, admonishing her for her lack of focus, when Jessica enters and asks Mike for his work. Mike informs Jessica that he has most of the work finished, but Jessica is less than impressed, stating that \"if [she] can't count on [him] for the effort, how the hell [is she] supposed to count on [him] for the results\". Rachel begins to speak out, but Mike interrupts her to accept the blame, promising Jessica that he will get the work finished. Jessica informs him, however, that it is too late, and that she will have to call Hardman to",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31bba-1dce-11ee-b06f-52b307fec202",
            "to call Hardman to postpone the deposition until the next day, before storming off. Rachel tearfully attempts to apologize to Mike, but he cuts her off before she can finish, and asks her to get the work finished, before leaving.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31bce-1dce-11ee-b06f-52b307fec202",
            "Acting on Mike's request, Rachel continues working through the documents in front of her, when she is approached by Katrina, who promptly introduces herself. Rachel accepts her introduction, but informs Katrina that she is already aware who she is. Katrina tells Rachel that she heard from Louis that she is the \"best paralegal around\", a compliment Rachel somewhat rigidly accepts, before asking her to make forty copies of every document in a box she is carrying. Katrina begins to leave, but Rachel calls her back, and apologizes that she cannot carry out the tasks Katrina has requested, as she is too busy with her current work. Katrina asks Rachel what she is working on, and she replies that she is trying to \"find a door into Folsom's personal correspondence\" for Mike. Katrina is skeptical that she will find anything, but tells Rachel that Jessica asked her to do something, and she didn't tell her she was to busy to do it. Rachel replies that her work is also for Jessica, but Katrina",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31c46-1dce-11ee-b06f-52b307fec202",
            "but Katrina counters that Mike asked for the information, not Jessica. Katrina informs Rachel that she is aware she took the LSATs, but that she is not yet a lawyer, she is paralegal, and should do her job by helping her.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31caa-1dce-11ee-b06f-52b307fec202",
            "Rachel begrudgingly agrees to assist Katrina, and begins photocopying the documents as requested. Louis approaches her, and asks Rachel to pause what she is doing, but she refuses, stating that she is \"busy doing [her] job\". Louis voices his surprise at her response, but Rachel is unfazed, asking whether he is going to \"fire [her] like [he] fired Harold\", stating that she couldn't care either way. After thinking for a second, Louis starts laughing, stating that he knows \"about the Harvard thing\" and thinks it is great. Rachel, believing Louis is talking about her rejection letter, is left stunned, but Louis subsequently reveals he is unaware she was rejected, stating that he has \"100% faith in [her]\". Rachel tearfully reveals to Louis that she didn't get in, adding that she doesn't know why, when everything, including her interview with Sheila Sazs, went okay. Upon learning that Sheila was the person that interviewed her, Louis informs Rachel that he believes she was wronged, and that",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31cc8-1dce-11ee-b06f-52b307fec202",
            "wronged, and that he will rectify the situation.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31cdc-1dce-11ee-b06f-52b307fec202",
            "Arriving back at Pearson Hardman, Harvey and Dana are met by Donna as they walk to Harvey's office. Donna suggests that their trip went well, to which Harvey states otherwise, although Dana confirms that \"the plane ride was fun\". As the two of them enter Harvey's office, Donna informs them that Jessica has asked to see the both of them. Dana questions why Jessica would want to see her, to which Donna clarifies that it is actually her boss that wants to see her.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31cf0-1dce-11ee-b06f-52b307fec202",
            "Jessica is talking with Dana's boss, Edward Darby, in her office, when Dana and Harvey enter. Edward introduces himself to Harvey, who sarcastically states to Dana that Edward \"doesn't seem stodgy at all\". Jessica informs Harvey and Dana that Edward stopped by to assess the state of his investment, and asks the two of them how the case is going; Harvey responds that they are right on schedule, and after Jessica and Edward look slightly skeptical, Dana confirms that they have \"dropped a grenade, [they're] just waiting for it to go off\". Edward takes from Dana's response that the \"grenade\" hasn't yet gone off, but Dana defends herself by pointing out that \"Rome wasn't built in a day\". Edward sarcastically states that if that is the case, he needn't have \"crossed the pond\", to which Harvey points out that he did anyway. After a slight hesitation, Edward informs Harvey and Dana that he had an ulterior motive in their \"little venture\", regarding Hardman. Edward states that he has had the",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31d04-1dce-11ee-b06f-52b307fec202",
            "that he has had the \"distinct displeasure\", and Jessica informs them that, with Edward's assistance, she has stepped up their attack on Daniel. Harvey is impressed after reading over the proposal Jessica hands him, but Edward merely states it \"was the least [he] could do\". He then takes his leave, stating to Dana and Harvey that he will be \"waiting for that detonation\", noting to Dana in particular that he trusts it will happen.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31d18-1dce-11ee-b06f-52b307fec202",
            "Upon Rachel's request, Mike goes to see her in her office. Rachel begins to apologize for her earlier behavior, but Mike cuts her off before she can, and informs that he over-reacted. Rachel accepts Mike's offer, and instead informs him that she found what he needs to access Hanley Folsom's personal correspondence. Mike is delighted to hear it, stating that it \"couldn't have come at a better time\". Rachel informs him that she would have gotten it to him sooner, but she had a job to do for Katrina first. Mike asks Rachel why she didn't tell Katrina she was working for him, to which Rachel states that she did, and Mike realizes that Katrina did to Rachel what she did to him before. Opening the document Rachel have him, Mike asks what she found, and Rachel replies that what she found is enough for him to write a motion.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31d2c-1dce-11ee-b06f-52b307fec202",
            "Walking back to his office with Dana, Harvey comments to her that Edward seemed nice, but Dana retorts that he was actually annoyed. Harvey is left surprise, sarcastically asking her what \"happy look[s] like\", to which Dana responds \"he's British, pretty much the same thing\". Harvey asks her seriously how she knew Edward was annoyed, and Dana questions whether Harvey wouldn't be annoyed too given the state of their case. Harvey states that he is annoyed since they still haven't convinced Cathleen Mitchell to help them, adding that Dana's good cop failed, but Dana counters that it is Harvey's move that failed. Dana states to Harvey that Jessica seemed to take their news well, but Harvey responds that it was only because she had company, and that he will \"hear about it later\". Harvey asks Dana whether Edward has a habit of suddenly visiting; Dana responds that Edward has £12 million invested in their case, but Harvey suggests to her that she wasn't expecting him to visit. Dana confirms",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31d40-1dce-11ee-b06f-52b307fec202",
            "Dana confirms Harvey's statement, but adds that it is a big investment for him; Harvey counters that for Edward, it is only money, but for him, it is his whole firm. Katrina enters to interrupt their conversation, and asks to speak to Harvey.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31d54-1dce-11ee-b06f-52b307fec202",
            "Harvey goes to see Mike at his cubicle, but before he can say anything, Mike informs his superior that he has found a way to get them access to Hanley Folsom's personal correspondence. However, Harvey recites the exact evidence that Mike has found, informing him that Katrina already gave him the subpoena. Mike is left dumbstruck, and Harvey states that \"it's a good thing Jessica put her on the case after all\". As Harvey leaves, Mike angrily screws up the document he had intended to give to him.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31d68-1dce-11ee-b06f-52b307fec202",
            "Mike storms into Katrina's office, and slamming a document onto her desk, informs her that he takes it personally when people steal from him. Katrina glances down at the document and asks Mike whether he is subpoenaing her, but Mike states that she diverted Rachel, and then pursued his idea herself. Katrina questions whether it was his idea, but Mike responds by asking whether she is denying his allegation. Katrina defends herself by pointing out that Mike stated they \"needed to fly\", so she \"built an aeroplane\". Mike is still incensed, stating that she \"flew\" he aeroplane right into Harvey's office just in time to take credit. Katrina notes that she offered Mike a chance to work together, but he refused her offer. Mike turns to leave, stating as he does that Katrina has \"always got an answer\", but Katrina counters that Mike has \"always got an accusation\", and suggests he get to work preparing for Jessica's deposition of Folsom.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31d7c-1dce-11ee-b06f-52b307fec202",
            "Louis angrily confronts Sheila at her hotel room; opening the door, Sheila voices her surprise at seeing Louis there, asking him where her interviewee is. Louis informs her that he dismissed him, which Sheila states as being unacceptable. Storming into Sheila's hotel, Louis states that she is the one that is unacceptable, and that she has behaved unprofessionally. Sheila denies Louis' accusations, stating that she never behaves unprofessionally. Louis is unconvinced, noting Sheila's unconventional requests during their previous sexual encounters. Sheila counters that those instances were personal, but Louis replies that she \"let the personal, colour the professional\", and that Rachel \"will not be a casualty of [Sheila's] misplaced anger\". Sheila is offended at Louis' use of the phrase \"misplaced anger\", stating that he made her look like a fool. Louis counters that he was the one made to look a fool, and that Sheila was merely collateral damage, which wasn't his fault, and certainly",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31d90-1dce-11ee-b06f-52b307fec202",
            "and certainly not Rachel's fault. Sheila sarcastically asks Louis whether he is there to be Rachel's \"knight in shining armour\", but Louis replies that he is there to right a wrong. Sheila's attitude softens, noting that Louis' action is very noble. After a slight pause, Louis agrees that it is, adding that Sheila is going to undo what she has done. Sheila, however, undoes her blouse, and when Louis informs her that that isn't what he meant, Sheila replies that \"it's what [he's] caused\". Louis steps closer to Sheila, informing her that he will not be denied, but after some flirting from Sheila, he grabs her and takes her into her bedroom, shutting the doors behind him.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31da4-1dce-11ee-b06f-52b307fec202",
            "Mike storms into Rachel's office, and tells her that they need to get to the evidence in Hanley Folsom's correspondence before Katrina, but Rachel informs Mike that Katrina has already found the evidence, leaving him exasperated. She continues that Katrina gave the evidence to Missy Dietler to make copies, and Jessica likely already has it, but this gives Mike an idea, noting that Missy will take numerous coffee breaks before finishing the job, and the evidence is probably still waiting to be copied. Rachel questions whether Missy would leave the evidence in the copy machine, which Mike admits is true, but adds that she has probably already scanned it into the machine, and that they simply need her code. Rachel is not convinced, stating in hushed tones that Mike is \"talking about stealing someone's work\", but Mike points out to Rachel that Katrina already lied to her, stole their work, and made them both look like fools. He adds that, in the end, they are all the same team, and that",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31db8-1dce-11ee-b06f-52b307fec202",
            "same team, and that the faster the work gets done the better for everyone. Rachel asks Mike whether he is sure he wants to continue what he has suggested, and after Mike readily agrees, she undoes the top button of her blouse. Mike questions what Rachel is doing, and she informs him that she can easily get Missy's code by flirting with Manningham, one of the IT employees. Mike is unconvinced that Rachel's plan will work in time, stating that they \"need a sure thing\", but Rachel flirtatiously whispers in his ear that she is a sure thing. Mike is left dazed for several seconds, and when he finally regains his senses, agrees to let Rachel proceed with her plan.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31dcc-1dce-11ee-b06f-52b307fec202",
            "Back at Sheila's hotel room, Louis and Sheila compliment one another on their sexual encounter. Sheila playfully calls Louis \"a knight\", to which Louis responds rather more seriously that \"it is time to right what is wrong\". When Sheila doesn't respond, Louis continues that whilst he is flattered by her actions, what she did isn't fair and cannot stand. Taking a more serious tone, Sheila asks Louis to pull an application from a stack on her desk and read. Louis does so a number of times, finding all of them to be highly exceptional. Louis begins to say that he gets what Sheila means, but Sheila proceeds to inform him that those applications are from her reject pile. Responding to Louis' earlier accusation, Sheila states that she is a professional, and that she would never he let her feelings for Louis sway her against a candidate. Louis asks her to let her feelings sway her for a candidate, but Sheila blankly refuses to do so. Louis continues his argument, stating that Rachel \"is the",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31de0-1dce-11ee-b06f-52b307fec202",
            "that Rachel \"is the best paralegal, in the best law firm in New York\", and \"is relied upon by the best lawyers, who have graduated from the best university\", to which Sheila asks Louis who she should kick out. Louis doesn't answer, but states to Sheila that he made Rachel a promise. Sheila informs Louis that she liked Rachel, but that he will have to tell her that \"sometimes good isn't good enough\".",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31dea-1dce-11ee-b06f-52b307fec202",
            "At Pearson Hardman, Jessica asks Harvey how their \"detonation is coming\". Harvey replies that it has a \"long fuse\", to which Jessica asks whether that means \"it's never going off\". Harvey states somewhat angrily that if it doesn't, she could always have \"James Bond\", i.e. Edward, take care of it instead. Jessica continues Harvey's joke, asking him how things are going with Dana, referring to her as \"Pussy Galore\". Mike enters to interrupt their discussion, and at Jessica's inquiry of why he is there, informs the two of them that they can win Parkville. Harvey and Jessica both look over the information Mike hands them, with Harvey commenting that it is \"the key to everything\".",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31dfe-1dce-11ee-b06f-52b307fec202",
            "Daniel Hardman exits the lift at Pearson Hardman with Hanley Folsom, the two of them discussing their strategy during the deposition. However, as they turn the corner, they find Jessica, Harvey, and Mike waiting for them, with Daniel referring to the trio as \"The Three Stooges\". Jessica asks Hardman and Folsom to accompany them to the conference room, where Dana is waiting with Cathleen Mitchell. Hardman asks why Cathleen is there, and Mike informs them that she is reading an email written by Folsom regarding the circumstances surrounding her being promoted. Jessica then adds that they will then show her the attachment to that email, which was originally missing from their own copy. Hardman states that they will need time to review the new evidence, but Harvey counters that Folsom was the one who wrote the email, and as it shows, knew Cathleen was unable to have children, and thus the reason he changed her review and subsequently promoted her. Jessica then states that after she has",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31e12-1dce-11ee-b06f-52b307fec202",
            "that after she has read the email, she will join their lawsuit against Folsom Foods, and they \"won't stand a chance\". Hardman counters that the email doesn't prove a pattern, to which Harvey states that it proves what Folsom did to her. Hardman is undeterred, stating that it is only one case, and that they will see them at the next 44. He adds that they won't participate in the deposition unless Harvey puts Cathleen on a plane back to Parkville, and he and Folsom take their leave.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31e26-1dce-11ee-b06f-52b307fec202",
            "Walking together along the corridors of Pearson Hardman, Rachel asks Mike how it went with Daniel; Mike replies that the case isn't over yet, but confirms Rachel's subsequent suggestion that he is \"out of the dog house with Jessica\". As they are walking, Mike starts to chuckle, and when Rachel inquires why, he states that she never told him how it went with Manningham. Rachel laughingly replies that she never will, but their conversation comes to halt as they reach Rachel's office, and discover Katrina waiting for them. Rachel asks Katrina what she is doing in her office, to which Katrina replies that after what she did, she didn't think Rachel cared about people using her property. Mike steps in, stating to Katrina that her problem isn't with Rachel, but with him. Katrina accepts Mike's suggestion, telling him angrily that he \"stole her discovery\". Mike asks her whether she is referring to the piece of paper he turned into a strategy, or quoting Katrina's earlier metaphor, \"an",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31e3a-1dce-11ee-b06f-52b307fec202",
            "metaphor, \"an airplane\". Katrina agrees that she may have \"put [her] toe over the line\", but adds that Mike obliterated the line with his actions. Mike sarcastically apologizes to her, adding that he was merely taking Katrina's advice on right and wrong. Katrina asks Mike on what side of right and wrong sleeping with the paralegals falls on, but Rachel immediately tells Katrina to \"get the hell out of [her] office\". Katrina starts to leave, stating as she does that it is none of her business, but adds as she does so that it is a good thing Rachel is going to law school, because \"they may sleep with the paralegals, but they end up with the lawyers\".",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31e4e-1dce-11ee-b06f-52b307fec202",
            "Edward enters Jessica's office, bemoaning the lateness of the hour. Jessica informs Edward that she is willing to consider taking him up on his offer, and hands Edward Pearson Hardman's books for the past five years, stating that if they are going to do it, she wants him \"to know exactly what it is [he is] getting [himself] into\". She encourages him to start at the beginning, saying it is \"a great read\". Edward states to Jessica that she is an impressive woman, and Jessica merely replies that he doesn't know the half of it. The two of them say their goodbyes, as Harvey looks on from outside.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31e58-1dce-11ee-b06f-52b307fec202",
            "Harvey meets Dana at a posh restaurant, and brushing aside Dana's observation that he is late, states that he knows Jessica and Edward are considering a merger. Dana states that it isn't \"what it looks like\", but Harvey counters that after checking Edward's flight, he discovered that Edward flew in the same day Dana did, and didn't just \"pop in\" as Dana suggested. Dana replies that Edward wasn't meant to do that, but Harvey continues, stating that Dana wants her name on his door. Dana corrects him, stating that she wants to see \"[their] names, on the same door\". Harvey reiterates his previous statement that Dana is always trying to hide something, but Dana counters that she wanted to tell Harvey herself, but Edward wouldn't let her until he had decided. Harvey points out to Dana that Edward decided without her; Dana admits that Edward jumped the gun, but informs Harvey that she has Edward's promise that if they merge, he will name Dana as partner, and notes that Jessica's only choice",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31e6c-1dce-11ee-b06f-52b307fec202",
            "only choice will be him. Harvey replies that he doesn't need Dana's help to get his name on the door, just as he didn't need her help to win the case. Dana points out that he has been out-gunned ever since Hardman left, and that she is \"bringing the guns\". She adds that being partner is what he has always wanted, and he should get over his pride, but Harvey refuses to do so, stating that the merger will never happen, before leaving.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31e80-1dce-11ee-b06f-52b307fec202",
            "Jessica and Edward go to see Hardman at his office; Daniel exchanges pleasantries with Edward, but Jessica brushes off his friendliness, stating that they are not friendly adversaries, and that Daniel is about to lose. Hardman points out that Folsom already said no, but Edward replies that Folsom might not listen to Daniel any longer when he informs him of Daniel's prior embezzlement. Hardman turns to Jessica, and asks her whether she told Edward about his embezzlement. Jessica replies that she didn't, and Edward adds that he find it on his own. Jessica reveals that she and Edward are merging, and she was legally required to show him Pearson Hardman's books, noting that unlike Hardman, she doesn't break the law. Edward suggests to Daniel that Hanley Folsom could be made aware of his past indiscretions; Hardman counters that failing to report embezzlement is in itself a crime, but Jessica merely suggests that he bring it up at his sentencing hearing. Hardman is still undeterred,",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31e94-1dce-11ee-b06f-52b307fec202",
            "still undeterred, stating that he could sue her, but Jessica replies that he still doesn't have proof she told Edward, and Daniel doesn't even have a firm. Jessica bids him goodbye, instructing Daniel as she leaves to get Folsom to sign the papers.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d5c31ea8-1dce-11ee-b06f-52b307fec202",
            "Louis stares at Rachel in her office, building up the confidence to enter. When he finally does, he informs Rachel that he has \"a hard truth\" to tell her. Rachel guesses that she isn't going to Harvard, which Louis confirms. Rachel states that she understands why, as she has never been good enough, but Louis replies that that isn't the hard truth, stating that she is an amazing candidate, and the reason she didn't get in is because he let her down. Rachel asks what he means, and Louis informs her that he and Sheila had a previous relationship, and that he hurt her. Rachel asks Louis whether Sheila is taking it out on her, but Louis doesn't reply, stating instead that he will write her a recommendation for any law school, but it just won't be Harvard. Rachel tries to contain her emotions, and as Louis leaves, he tells Rachel that he is sorry for what happened. Rachel continues to try to hold back her emotions, but eventually fails, and starts to cry over her desk.",
            {
                "title": "Suits",
                "ep_title": "Normandy",
                "season_num": 2,
                "ep_num": 15
            }
        ],
        [
            "d7db81bc-1dce-11ee-b06f-52b307fec202",
            "World War I or the First World War (28 July 1914 – 11 November 1918), often abbreviated as WWI, was one of the deadliest global conflicts in history. It was fought between two coalitions, the Allies and the Central Powers. Fighting took place throughout Europe, the Middle East, Africa, the Pacific, and parts of Asia, especially East Asia. An estimated 9 million soldiers were killed in combat, plus another 23 million wounded, while 5 million civilians died as a result of military action, hunger, and disease. Millions more died as a result of genocide, while the 1918 Spanish flu pandemic was exacerbated by the movement of combatants during the war.",
            {
                "title": "Suits",
                "ep_title": "War",
                "season_num": 2,
                "ep_num": 16
            }
        ],
        [
            "d7db8338-1dce-11ee-b06f-52b307fec202",
            "The first decade of the 20th century saw increasing diplomatic tension between the European great powers. This reached a breaking point on 28 June 1914, when a Bosnian Serb named Gavrilo Princip assassinated Archduke Franz Ferdinand, heir to the Austro-Hungarian throne. Austria-Hungary held Serbia responsible, and declared war on 28 July. Russia came to Serbia's defence, and by 4 August, defensive alliances had drawn in Germany, France, and Britain, with the Ottoman Empire joining the war in November.",
            {
                "title": "Suits",
                "ep_title": "War",
                "season_num": 2,
                "ep_num": 16
            }
        ],
        [
            "d7db8388-1dce-11ee-b06f-52b307fec202",
            "German strategy in 1914, known as the Schlieffen Plan, was to first defeat France and bypass their fortifications by moving through Belgium, then attack Russia. However, this manoeuvre failed due to heavy French and Belgian resistance, and British reinforcements. By the end of 1914, the Western Front consisted of a continuous line of trenches stretching from the English Channel to Switzerland. The Eastern Front was more fluid, but neither side could gain a decisive advantage, despite a series of costly offensives. Fighting expanded onto secondary fronts as Bulgaria, Romania, Greece, and most notably Italy, and others entered the war between 1915 and 1916.",
            {
                "title": "Suits",
                "ep_title": "War",
                "season_num": 2,
                "ep_num": 16
            }
        ],
        [
            "d7db83ba-1dce-11ee-b06f-52b307fec202",
            "The United States entered the war on the side of the Allies in April 1917, while the Bolsheviks seized power in the Russian October Revolution, and made peace with the Central Powers in early 1918. Freed from the Eastern Front, Germany launched an offensive in the west on March 1918, hoping to achieve a decisive victory before American troops arrived in significant numbers. Failure left the German Imperial Army exhausted and demoralised, and when the Allies took the offensive in August 1918, German forces could not stop the advance.",
            {
                "title": "Suits",
                "ep_title": "War",
                "season_num": 2,
                "ep_num": 16
            }
        ],
        [
            "d7db83e2-1dce-11ee-b06f-52b307fec202",
            "Between 29 September and 3 November 1918, Bulgaria, the Ottoman Empire, and Austria-Hungary agreed to armistices with the Allies, leaving Germany isolated. Facing revolution at home and with his army on the verge of mutiny, Kaiser Wilhelm II abdicated on 9 November. The Armistice of 11 November 1918 three days later brought the fighting to a close, while the Paris Peace Conference imposed various settlements on the defeated powers, the best-known being the Treaty of Versailles. The dissolution of the Russian, German, Austro-Hungarian, and Ottoman Empires resulted in the creation of new independent states, among them Poland, Czechoslovakia, and Yugoslavia. Failure to manage the instability that resulted from this upheaval during the interwar period, as well as hyperinflation in Germany and Austria due to crippling war debts, contributed to the outbreak of World War II in September 1939.",
            {
                "title": "Suits",
                "ep_title": "War",
                "season_num": 2,
                "ep_num": 16
            }
        ],
        [
            "d8fe33b4-1dce-11ee-b06f-52b307fec202",
            "Plot\nThe episode begins with Mike being called into Harvey's office in the middle of the night. Harvey explains that they are having an essential partners only meeting to discuss the merger, and Mike has been promoted to partner for his help in making this happen. Harvey also tells Mike that he has decided to accept his loss to Jessica and forgiven Mike for what he did, since he had no choice. In the meeting, Darby and Jessica begin making their speech, which is interrupted by Rachel. Mike tells Harvey that he told her the truth, when Louis asks what the truth is, Rachel replies that Mike is a fraud and she will not let him get away with it. Mike asks how could she do this to him, to which Rachel replies that he did it to himself and is arrested. Mike then wakes up in a cold sweat and realizes it was a dream.",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe3530-1dce-11ee-b06f-52b307fec202",
            "Harvey is examining an offer in his office as Donna enters and tells him Darby needs an answer as to which branch he wants Scottie to work. Harvey pauses before telling her that he decided to send her to London, refusing to talk about his decision and instead asks to have Ray bring him to Brooklyn. Harvey arrives at a sports executive office to negotiate the contract of his client Deron Williams, before returning to his apartment to find Jessica. She asks why he is closing a deal behind their client's back, especially since the offer he used as leverage in closing the deal was a bluff and could have backfired. She accuses him of wanting the deal to backfire so that she will fire him, but he insists that this is how he operates and what she used to value him for.",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe3558-1dce-11ee-b06f-52b307fec202",
            "Mike goes to see Rachel to talk about their situation. She insists that they will not be sleeping together, to which he asks if that refusal is for \"now or ever?\" to which Rachel angrily tells him that she asked for time to process his secret as Mike interrupts her to tell her about his nightmare. She insists that she would never betray him, as he replies he realized after waking up the real nightmare wasn't that she might turn him in, but that she wouldn't want to be with him: something he wanted since he first saw her. While Rachel wishes that he never told her the truth, they both agree that they are happy with what happened afterwards. Rachel then asks if he isn't afraid that he will be exposed, and as he confirms that he is, Rachel tells him that he could quit to prevent that from happening.",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe3576-1dce-11ee-b06f-52b307fec202",
            "Mike arrives at the office reliving his nightmare, and attempts to approach Harvey who gives him a glare before turning away. Mike then attempts to talk to Jessica, who presents him with his own office for his efforts in the merger and in fooling Hardman. Mike comments that the road to where he is doesn't usually involve stabbing someone in the back, as Jessica relates his situation to how she was given a car when her parents got separated. She hated that car since it represented her parent's separation, but then began to saw the car as what she used to get to Harvard and eventually to her current position. Mike can similarly see his new office as either a reminder of his betrayal to Harvey, or a symbol of the greater things he could accomplish at the firm. He asks if her parents ever got back together, to which she replies that they didn't. As she leaves, she smiles while seeing the new sign of the firm: Pearson Darby.",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe359e-1dce-11ee-b06f-52b307fec202",
            "Jessica and Darby discuss how despite the latter's bigger control of the firm, her name is still placed first as a gesture by Darby to signify that their partnership is equal. Darby then informs Jessica how he plans to have Harvey represent Ava Hessington in her trial against the US government, something which she will not have a say in, causing her to realize that their partnership is not truly equal. Jessica then approaches Harvey and tells him that Darby was furious about how he handled his deal with Deron Williams, but she fought to give him a chance to prove his worth by taking on the Hessington case. She tells him this is a chance for them to make up, which he agrees.",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe35b2-1dce-11ee-b06f-52b307fec202",
            "Rachel sees Mike's new office and tells him how it is convenient that while he was earlier afraid of being exposed, he now has a brand new office. Mike tells her that Jessica offered him this office before he could talk about his retirement, and they begin to argue. While arguing, Rachel comments that while she has been trying to earn one as long as she can remember, he didn't do a thing to deserve it. When he insists that she has no idea what he did for it, she replies that she actually doesn't know anything about him anymore.",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe35d0-1dce-11ee-b06f-52b307fec202",
            "The next day, Harvey confronts Darby and reveals that he is aware of Jessica's deception. He agrees to work on the Hessington case only if Darby will tear up his non complete and allow him to leave afterwards. When Darby asks if he hates the merger that much, he replies that since the merger Jessica has accused him of trying to get fired, and then lying to him about fighting to get him on this case. Darby comments on the irony that her believing Harvey wanted to be fired led him to genuinely wanting to be fired now, but agrees to Harvey's terms.",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe35e4-1dce-11ee-b06f-52b307fec202",
            "Mike then meets Louis in the copier room, who sees the former was making copies of his letter of resignation. Mike explains that Harvey no longer wants anything to do with him, and he has no idea how to fix their relationship. Louis tells Mike about how when he and Harvey were both associates, Harvey seemed unstoppable, like Superman. When Hardman decided to give him an assignment that had undoable workload and was ultimately unwinnable to humble him, Louis thought this could be an opportunity to offer his help and become friends. Instead, Harvey glared at him as though to say \"How dare you?\" Mike assumes the morale of the story is that Harvey has and always will be a lone wolf, but Louis replies that it is in fact the opposite: Harvey is no longer Superman, but Batman, who needs his Robin. Since Harvey prioritizes winning above all else, Mike just needs to remind him of how he is needed by helping him win. To do so, he would need to access Harvey's hard drive and proceeds to ask",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe3602-1dce-11ee-b06f-52b307fec202",
            "and proceeds to ask Benjamin for help. Benjamin asks why he would want to help Mike, when for the past ten months he has been tracking Mike's internet movement to seek revenge for the last time Mike outsmarted him. Mike replies that Benjamin for the foreseeable future will help him with whatever he asks, as he has recorded Benjamin admitting that he has hacked Mike's personal computer.",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe3620-1dce-11ee-b06f-52b307fec202",
            "Harvey is working on a huge pile of documents from the Hessington case, which is only a fifth of what they have. Donna suggests Mike enlist help with the case, but when he refuses to ask Mike for help, she insists that he ask Scottie instead. While initially upset that Harvey sent her to the London office, Harvey asks if she could help him now that he is genuinely asking, as she was willing to help before without him doing so. He tells her how the first time he saw her, the sight of her stopped him in his tracks, and the second time when she answered a question in class, made him realize her looks were only her second greatest asset. Harvey tells her how she has always meant something to him, moving her and changing her mind.",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe363e-1dce-11ee-b06f-52b307fec202",
            "Harvey approaches Ava Hessington to convince her to be a client. Both of them have checked up on the other, and are aware of the morally grey things they have done. She admits the bribery charges she is being accused of are true, and Harvey acknowledges this before leaving the office as her official attorney. Harvey enters the lobby of the firm to find Mike waiting for him, with information that could aid in the Hessington case. All the information Mike has however, is already in Harvey's hands and was discussed with Ava Hessington earlier. Harvey tells Mike that he isn't replaceable: he was working as a lawyer before he met Mike and he will be doing so long after he has forgotten him. Mike then tells Harvey to just hurt him however he wants, since it will lead to his forgiveness, but he needs Harvey to listen to the information he has. Harvey then angrily tells him that a time when he would have listened to Mike was before he was betrayed by him, and that even though Jessica",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe3652-1dce-11ee-b06f-52b307fec202",
            "even though Jessica threatened him, Mike should have came to Harvey as no matter who threatens him he should have still remained loyal. Emotional, Mike rushes to Rachel's apartment and promises to tell her everything but at the end of the night they will either be done with each other or sleep together. The next morning they wake up in bed together, and he has told her everything.",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe3670-1dce-11ee-b06f-52b307fec202",
            "Harvey and Ava sit before Richard Jenson, arguing how although men in Ava's position would typically be let off with a fine, she is instead being threatened with jail time. Jenson insists that this case is not about her gender, prompting Harvey to ask her to leave the room. Harvey asks how much Ava needs to give him to be let off, however Jenson insists that he needs someone to go to prison as he is planning to run for politics. Harvey proposes making an example out of more serious offenders instead, but Jenson remains adamant that he cannot afford to make any deals regarding this case.",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe3684-1dce-11ee-b06f-52b307fec202",
            "At the firm, Rachel distracts Donna by claiming Richard Gere is in the lobby to allow Mike to sneak into Harvey's office and place the information he found on Harvey's desk. Donna later enters Mike's office to ask for his help, but is in fact a segue into her commenting that he seems to like doing things for others who neither asked, wanted, nor needed him to do, before handing him the file he left on Harvey's desk. Donna tells him Harvey valued Mike not for his usefulness, but his loyalty which he has lost and cannot regain. Mike tells Donna he also hid multiple copies of the file in Harvey's office, as whether he is forgiven or not, Harvey will need this information. Donna tells Mike that this won't lead to Harvey's forgiveness. Mike asks Donna if she can keep their own relationship separate from his and Harvey's, to which Donna replies that she feels betrayed too, since she has been looking out for Mike since his first day. Mike asks if she remembers when he had her back last year",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe36a2-1dce-11ee-b06f-52b307fec202",
            "her back last year but she ignored him and almost cost Harvey his license, as she rebuts that what she did was for Harvey and not herself and in the end she didn't get a new office like Mike did but instead got fired.",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe36b6-1dce-11ee-b06f-52b307fec202",
            "The next day, Mike asks for a favor from Benjamin, but first makes a gesture by allowing him to delete the recording, as while he has enough enemies, he would prefer to have him as a friend. Mike asks Benjamin to cryptically build him a \"time machine\" to fix a mistake he made. Jessica is called into Mike's office where he holds a copy of the letter to the district attorney she threatened him with. After confirming that he is not recording their conversation, Mike tells her that this copy was from her hard drive and has her computer's data signature: proving its authenticity and date, meaning that if she sends this letter in future she will also be complicit. Jessica asks what he wants, to which he asks if she would trade the car she received for her parents being together. When she confirms she would, Mike says that he has that chance now: he wants to give back the office, as it may be a step towards Harvey's forgiveness.",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe36ca-1dce-11ee-b06f-52b307fec202",
            "Harvey tells Donna how he was unable to change Jenson's mind as Donna hands him the file Mike gave her, which reveals how Jenson lied to him. Harvey realizes that the file was from Mike, but both he and Donna agree that although the information is useful, he doesn't have to forgive Mike. Harvey confronts Jenson on how his main campaign contributor is also Hessington Oil's main competitor: Jenson doesn't want Ava to be imprisoned, he wants a trial that will cause their stock to plummet. Harvey tells Jenson to cut a deal for Ava and to look for a new campaign contributor or he will reveal this conflict of interest. As Harvey returns to the firm, he finds Cameron Dennis waiting: Jenson appointed Dennis as a special prosecutor to the case to avoid a conflict of interest. Jessica asks Darby into her office to confirm why Ava Hessington is so important to him: her father was also his former lover. Jessica warns Darby that if Harvey finds out how important she is, he may use it as leverage",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe36e8-1dce-11ee-b06f-52b307fec202",
            "use it as leverage to leave. Darby however replies that he does not believe Harvey is truly intending to leave.  Harvey meets with Darby as they discuss the new involvement of Cameron Dennis. Harvey tells Darby he knows how important Ava is, and that now the terms of him winning the case will be that Darby will support Harvey's attempt to replace Jessica as managing partner of the firm.",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe36fc-1dce-11ee-b06f-52b307fec202",
            "Meanwhile, Donna checks in on Louis who is exclaiming in annoyance. Since the merger, the new quartermaster, Barbara L. Tottingham, will not buy any Uniball pens, instead purchasing pens that keep breaking in Louis' hand. Louis believes that the new quartermaster has a vendetta against him, as Donna tricks him into applying the spilled ink on his hand onto his face in the shape of Hitler's moustache and to do an impression of a Nazi salute, which he believes to be a rotator cuff exercise. Louis makes a note to Norma on his Dictaphone on how he needs Barbara L. Tottingham's number, before relaying to another secretary to tell Norma to purchase him Uniball pens or he will cancel her vacation. Louis tries to get a Bran bar from the pantry, only to find that they are all gone. He finds Nesbitt standing behind him, who is in fact the real quartermaster: Barbara L. Tottingham was in fact a convoluted reference linking to a BLT sandwich, and eventually the Count of Monte Cristo, a story",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe371a-1dce-11ee-b06f-52b307fec202",
            "Cristo, a story about revenge from the assumed dead. Nesbitt tells him that he is taking his revenge on Louis by not only refusing to purchase Bran bars for the pantry but by outright banning them from being consumed in the firm. Louis tells Donna about the situation, and he believes that Nigel's revenge has only begun unless he is stopped, something which Donna says Louis can only do by removing him as quartermaster.",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "d8fe3738-1dce-11ee-b06f-52b307fec202",
            "Louis waits for Darby in his temporary office, surprising him with the latter's favorite tea, food and even choice of pen and ink, all to make the point that he is the best choice to become the new quartermaster. Nesbitt brings Louis some Bran bars and Uniball pens in an attempt to ask that he is allowed to keep his position as quarter master. When Louis refuses, Nesbitt reveals this was his true plan as Darby International's bylaws prohibit someone from being in charge of both personnel and logistics at the same time: Louis will no longer be in charge of the associates. If Louis asks Darby to undo his new position he would lose his credibility, meaning there is nothing Louis can do to reclaim his position.",
            {
                "title": "Suits",
                "ep_title": "The Arrangement",
                "season_num": 3,
                "ep_num": 1
            }
        ],
        [
            "da32dce4-1dce-11ee-b06f-52b307fec202",
            "Plot",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32de60-1dce-11ee-b06f-52b307fec202",
            "Donna reacts to Harvey's plan of overthrowing Jessica as managing partner with shock, but nonetheless tells him that she will still support him in his plan if he is sure about his decision. Mike enters and tells Harvey and Donna that he has made sure Jessica can no longer blackmail him into doing anything, but is still met with contempt from them as Harvey tells him Jessica should have never been able to blackmail him anyway if he were loyal, and tells him to shut the door on his way out. Mike enters the bullpen with Rachel to see Louis giving his goodbye speech to the associates as he steps down from being head of the associates, with Louis leaving in tears after Mike helps complete his facsimile of the emotional complex from \"Dead Poet's Society\". As Louis returns to his office, he finds Jessica waiting for him. Jessica expresses her apologies that she does not have the means to reinstate his position, but comforts him by giving him a choice to mentor any associate of his choosing.",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32dea6-1dce-11ee-b06f-52b307fec202",
            "of his choosing. Excited, Louis goes to see Donna to see if Harvey would be okay with Mike being his new associate. After an amusing conversation regarding Louis' senior prom, Harvey tells Louis that he can make Mike his new associate and promises will not regret giving him permission.",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32dece-1dce-11ee-b06f-52b307fec202",
            "Jessica goes to see Cameron Davis to clarify that in their previous encounter, she was the one who went against him and Harvey didn't betray him. When Cameron is still upset about the matter, Jessica realizes he wasn't upset that Harvey might have betrayed him, but that ultimately when Harvey left the DA's office he chose Jessica over him. Cameron tells her that he resents that Harvey chose what Jessica stands for, someone who lets \"bad guys do whatever they want\" as opposes to him who puts them away. He then reaches for a disc which he hands to Jessica, claiming that it holds proof of Ava Hessington's guilt.",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32deec-1dce-11ee-b06f-52b307fec202",
            "In his endeavor to convince Mike to become his new associate, Louis has taken him to a restaurant with amazing food and introduces him to the owner as a client. Louis explains to Mike that the restaurant is currently in the middle of an eminent domain case, and if they lose, this restaurant will be converted into a shopping center. Mike points out that eminent domain cases are infamously unwinnable, as Louis replies in the affirmative and expresses his view that this is an opportunity for them to rewrite the law, which Mike expresses his interest in.",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32df14-1dce-11ee-b06f-52b307fec202",
            "Jessica returns to the firm and is met with Harvey who is infuriated that she went to see Cameron Dennis, as it painted the picture that Harvey cannot face Cameron by himself. Jessica clarifies that he is fighting Cameron WITH him and not for him, as the two agree to work together on the case. Jessica hands him the disk that Cameron gave to review. Together with Ava, they watch the footage on the disc, which shows Ava's second in charge showing a colonel a briefcase full of cash. As there is no audio on the disk, they clarify that if the audio did exist, it would not show either party explicitly mentioning anything about a bribe. Since this would not be enough evidence for Cameron to use, Harvey wonders if the colonel in the video would testify, but Jessica refutes this as the colonel is still a foreign leader and cannot be deposed. This leads them to the conclusion that Cameron instead has convinced Nick, Ava's second in charge and protégé to testify against her instead, confirmed",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32df32-1dce-11ee-b06f-52b307fec202",
            "instead, confirmed when Nick refuses to answer Ava's call. Ava is furious at her protege's betrayal, and Harvey tells her he empathizes with her situation after Mike's betrayal. Ava suggests bribing Nick into not testifying, making Harvey realize that this was Cameron's endgame: he wants to catch them in the act of attempting to bribe Nick. Harvey goes to see Nick, who claims he did not initially want to testify, but believes he has no choice. After confirming that Nick does care about Ava, Harvey tells him that without his testimony Cameron does not have a case and that going through with betraying her would prove to be the biggest regret of his life.",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32df5a-1dce-11ee-b06f-52b307fec202",
            "Mike finds Louis in the library, who has been researching eminent domain cases since they returned. Several hours later, Mike is still researching for the case, as Rachel tells him it is possible that Louis is attempting to recruit him to become his new associate. As Mike expresses disbelief, Louis enters with a trolley of lavish food items, prompting Rachel to smile as it confirms her suspicions. Mike asks Louis how he managed to obtain all this food in the middle of the night, as Louis tells him that he is the firm's quartermaster and has the means to do so. Mike tells Louis of an idea he had from Money Ball that could be used in the case, although he fears it is outside the scope of the case. Louis is confident that Mike's idea can be used however, as long as they can trick the opposing counsel to bring it into the scope first. The next day they attempt to do so, but is still unable to overrule the judge's ruling. Undaunted, Louis tells Mike that this is not the time to be sorry,",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32df78-1dce-11ee-b06f-52b307fec202",
            "time to be sorry, and takes Mike to his mudding treatment. Although uncomfortable, Mike obliges and is forced to enter his own tub of mud nude as Louis pointed out wearing his undergarments into the mud would mean not having them later. After settling into his tub, Mike asks Louis why he did not simply ask him to become his associate if he wanted him to. Louis replies that he is aware of how others see him, and wanted to remind him of the good that comes with working with him. Mike assures him that he remembers the good times he had with Louis, but unfortunately also the bad times, particularly when Louis fired someone in front of him on his first day just to scare him. Louis reassures Mike that since then, Mike has helped him change and want to become a better person. Their conversation inspires Mike of an idea on how to win the case, prompting Louis to stand up abruptly from his tub of mud while nude, as he refuses to \"mix mudding with pleasure\". They call for a meeting before the",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32dfa0-1dce-11ee-b06f-52b307fec202",
            "meeting before the judge to point out that after a revised valuation, the restaurant is worth potentially 100 million dollars. The opposing counsel argues that this value cannot be guaranteed, but Louis points out that the opposing counsel's argument relies on a similar hypothetical, as the judge decides to give a ruling the next day. The following night, Louis goes to Mike's apartment to tell him the judge ruled in their favor, and tells Mike the difference between him and Harvey is that Harvey is only a lawyer as he likes to win, while Louis himself loves the law. Mike tells him he loves the law himself, but also loves wining, prompting Louis say he believes that Mike is half Harvey and also half like Louis, now that he has spent time as Harvey's associate it could now be time for Mike to see what it is like to be Louis' associate.",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32dfbe-1dce-11ee-b06f-52b307fec202",
            "Meanwhile, Rachel attempts to warn Donna that Louis is attempting to have Mike become his new associate but she is already aware, and so is Harvey. Rachel asks if Donna would be willing to convince Harvey to change his mind, but Donna refuses as she is also of the opinion that Mike betrayed Harvey and should not be forgiven. Rachel tells Mike of their argument, prompting Mike to be upset as by asking Donna to help him with Harvey, it gives off the impression that he is weak, especially if it comes from Rachel. When she asks why it would be especially bad coming from her, Mike confesses that Harvey did not approve of their relationship. After further prompting, he also confesses that it was the initial reason they did not get together initially, as Mike did not want to have a relationship with Rachel without telling her the truth, something which Harvey forbid him form doing. Infuriated, Rachel expresses her contempt for Harvey, and after Mike attempts to defend him, she tells him",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32dfe6-1dce-11ee-b06f-52b307fec202",
            "him, she tells him Harvey is aware of Louis wanting Mike to become his new associate and gave his approval. Upset, Mike asks Harvey what it would take to be forgiven, but Harvey instead points out the numerous wrongdoings that Mike did while working for him and asks why he told Rachel. Mike tells him this was after Harvey fired him, and Rachel was the only person who was there for him. Thinking Harvey sent him to work with Louis as punishment, Mike tells him that he actually enjoys working with Louis and is considering becoming his accomplice. Harvey insists that he is in fact indifferent to Mike's situation, and could not care about Mike anymore as their relationship is now over.",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32e004-1dce-11ee-b06f-52b307fec202",
            "Harvey goes to the roof to have a drink, as Jessica attempts to approach him. Realizing he is still resentful, Jessica gives him an analogy of how in every rift, both sides will be convinced that the other side started the problem. The two begin to argue about who began this rift between them, as Harvey asks her to tell the truth, to which she complies and admits that she didn't fight to get him on the Hessington case, Darby did, but she used it as an opportunity to reconcile with Harvey. He asks her if she would do it all again, as she changes the subject to the deposition with Cameron tomorrow. The next day, the two arrive with Ava at Cameron's office, as Cameron tells them that Ava's competitor has footage of her bribing the colonel, who in turn gave it to her shareholders who want to file a lawsuit against her. Cameron tells them Harvey's attempt to appeal to Nick sentimentally failed, and asks Jessica what she did to the person he mentored in the DA's office. Harvey comes to",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32e022-1dce-11ee-b06f-52b307fec202",
            "Harvey comes to Jessica's defense that Cameron was never his mentor: only Jessica was. During the deposition, Nick gives his testimony on how he and Ava bribed a colonel. Harvey and Jessica instead, put in a new perspective: that Nick alone was responsible for bribing the colonel, and now that it has come to light, he is attempting to pass the blame to Ava. Cameron tells them this is irrelevant to the deposition, to which Harvey tells him this is a taste of what would happen in court if Nick were to testify, especially since Nick is unable to look at Ava without an expression of guilt. Later that night, Cameron goes to Harvey to tell him he will still manage to win in trial, before Harvey calls his bluff and Cameron admits that he is under orders to make a deal. Harvey tells him the only deal they will accept if it is only a fine with no admission of guilt, which Cameron reveals was the deal he was told to make with one adjustment at his prompting: Ava is to admit to being guilty of",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32e04a-1dce-11ee-b06f-52b307fec202",
            "to being guilty of bribery, making it official that Cameron has still beaten Harvey. In Jessica's office, Harvey tells her he refuses to take the deal, something which Jessica suggests they do since it is practically the same deal with only a single technical change, something which Darby would consider to be acceptable. Harvey still refuses to take the deal, prompting Jessica to answer his earlier question: she would indeed do everything she has done again, even though it caused a rift between them. She also tells him they have already accepted the deal, behind his back.",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32e41e-1dce-11ee-b06f-52b307fec202",
            "Rachel confronts Donna about Harvey forbidding Mike from telling her, as Donna tries to explain it was for Rachel's protection as well. Rachel expresses disbelief, since Harvey hardly knows who she is as if he did, he would know she would never tell anyone Mike's secret. Donna then tells her that if she wanted to be angry at Harvey for his decision, she should be mad at her too since she also told Mike the same thing: specifically that Mike should have gotten over Rachel, even after Rachel had told her then about her feelings for Mike. Rachel accuses Donna of choosing Harvey over her, which she confirms, but insists that it is part of her job, prompting Rachel to comment how everyone cares about their job but have no life, something she implies is inclusive of Donna, prompting the latter to walk out of the room. Later that night, Mike goes to Rachel's apartment where they both apologize for their earlier argument. Mike tells her that Louis has asked him to become his new associate,",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32e478-1dce-11ee-b06f-52b307fec202",
            "his new associate, and they spend the night together.",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32e4aa-1dce-11ee-b06f-52b307fec202",
            "The next day, Ava signs the deal as Harvey assures her that this is a good deal. She tells him she is aware it is, her only hesitation being that she will be returning to London without her protégé . When Harvey points out that Nick betrayed her, she points out however that Nick did not do so for personal gain, but because he had no other choice. As Harvey insists a betrayal is still a betrayal, she replies that regardless of his betrayal, she will still miss her protégé. After she leaves, Donna enters to confirm if Harvey is still going through with overthrowing Jessica, something which he replies in the affirmative since she confirmed that she does not regret her actions. Donna then suggests that since the entire blame is on Jessica, perhaps they should consider forgiving Mike.",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "da32e4d2-1dce-11ee-b06f-52b307fec202",
            "Mike enters Louis' office to accept his offer of becoming his new associate, and the two begin quoting from the Jerry Maguire movie. Louis excitedly tells him that he has already prepared something to celebrate this and rushes out of his office. After Louis leaves, Harvey enters and quotes the movie with Mike as well, to show he has forgiven him. As Mike tells him he cannot go back on his word to Louis, Harvey tells him it would not be going back on his word, just going back to where he belongs: as Harvey's associate. Harvey tells Mike to take the night off to celebrate with Rachel, unaware that Louis is outside the office holding a cake. Realizing that Mike will not be his associate, Louis quietly leaves and throws the cake into the trash, the cake revealed to have icing which reads: Welcome to Team Litt.",
            {
                "title": "Suits",
                "ep_title": "I Want You to Want Me",
                "season_num": 3,
                "ep_num": 2
            }
        ],
        [
            "db4ac060-1dce-11ee-b06f-52b307fec202",
            "Plot\nRachel and Mike are discussing their dating plans in the pantry, when Louis walks in and throws a bran bar Mike reached for into the trash, and coldly says as the new quarter master he has forbidden all first year associates to consume the bran bars. Mike attempts to apologize to Louis for agreeing to be his associate but then going back to Harvey, but the latter is still upset with him. Louis returns to his office to find Harvey waiting for him, and without Harvey saying anything, Louis tells him he does not accept any apology that Harvey has prepared for going back on his word that he would allow Louis to make Mike his associate. Harvey insists he is only here to give Louis files regarding Hessington Oil, since Louis would be the best person to tackle their legal issues with Tony Gisnopoloud orchestrating a takeover, something which Harvey openly admits to please Louis.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac13c-1dce-11ee-b06f-52b307fec202",
            "In a further effort to console Louis, Harvey suggests that the former take on a \"rebound\" associate, something he claims he had done after previously firing Mike. Louis insists however that he is not looking for a temporary superficial relationship, but someone he can truly mentor and would accompany him to activities such as going to the gun range, mudding or an origami festival, prompting an amused Harvey to respond that he will meet the right person to mentor. In the copier room, Rachel and Donna reconcile after their fight in the previous episode. Donna assures Rachel that she has forgiven Mike as well, although has not told him so that Mike will continue to secretly buy her favorite beverages.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac15a-1dce-11ee-b06f-52b307fec202",
            "In his office, Louis leaves a message on his Dictaphone for Norma, as Katrina Bennett enters his office to give him a file to help him with the Hessington Oil case. After Louis asks how does she qualify to be his personal associate, Katrina clarifies that she has no interest in being anyone's personal associate as she is a fifth year associate. However she knows Louis is good at his job, and believes instead they could be useful to each other, as Louis compares her proposed arrangement to being like a symbiotic relationship. Louis turns her down however, commenting that he has had enough of being used.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac164-1dce-11ee-b06f-52b307fec202",
            "Harvey meets with Ava Hessington to discuss how Louis will be handling the takeover attempt on her firm. Ava offers Harvey an opportunity to leave the firm and work for her instead, as she believes he would be an excellent replacement for her former protégé and second in command. As Harvey turns down the opportunity, Cameron enters and to their shock, arrests Ava for a conspiracy to commit murder. In Cameron's office, he explains to Harvey that the colonel Ava confessed to bribing was found to have ordered the death of six civilians who were in the way of Ava developing her pipeline. Harvey accuses Cameron of making this case purely to cause trouble for him, something which Cameron admits but also points out that Harvey walked into his trap by getting Ava to confess to bribery.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac178-1dce-11ee-b06f-52b307fec202",
            "Leaving Cameron's office, Harvey tells Mike to prepare do whatever he has to in order to bail Ava out, as Mike expresses his excitement that they are a team again. Mike questions Ava on her level of involvement in the murders of the civilians, as she replies that every death reported in that country is described as a military accident, and she had paid no heed to it. As Mike leaves the room, Ava asks Harvey if he thinks she did order those murders. Harvey replies that it is irrelevant, as the important thing is that he will clear her of the charges. Upon leaving the building, Harvey asks Mike to return to the firm to continue working on securing Ava's bail, jokingly promise to have a long talk with him after the whole thing is settled.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac182-1dce-11ee-b06f-52b307fec202",
            "Mike returns to find Katrina Bennett leaving Harvey a file in his office. Mike tells her that Harvey is no longer looking for an associate anymore, and that he handles all of Harvey's cases. Katrina questions Mike's usefulness to Harvey, and says they will see who Harvey values more, before turning to face Donna who admonishes Katrina for entering Harvey's office while she is away, and tells her to accept that Mike speaks for Harvey completely. Mike thanks Donna for her help, as she comments that she will still be expecting free beverages in the future.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac196-1dce-11ee-b06f-52b307fec202",
            "Jessica and Harvey discuss how Cameron tricked them into Ava confessing to bribery which linked her to murder. Harvey also tells her that he and Mike are now working together again, and she assures both Mike and Harvey that she holds no grudges against Mike previously threatening her. During the bail hearing, Harvey and Mike bring up how Cameron has never denied bailed for a defendant before, and accuses him of only doing so as part of personal vendetta against Harvey, to the point of hiding a witness and negotiating the previous settlement in bad faith. The judge calls them into her chambers, and Harvey brings up how Cameron confessed to him previously that he only accepted the case to cause trouble for him, and that Cameron leaked the details of the case to Tony Gianapolous. The judge declines Harvey's request to dismiss the case, but sets the bail to a single dollar, and warns Cameron that he better have concrete evidence tying Ava to the murders.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac1aa-1dce-11ee-b06f-52b307fec202",
            "In the firm, a mysterious suave gentleman arrives and is about to enter Harvey's office. As Donna stops him from entering, the two begin to flirt playfully and the man introduces himself as Stephen Huntley. Harvey enters and is aware of Stephen's role as Darby's fixer, and dismisses him. Stephen realizes that Donna was secretly texting Harvey when they were flirting and appears impressed. Stephen enters Harvey's office and tells him that he is here to oversee \"cultural integration\", something which Harvey implies he does not believe and Stephen concludes that his best course of action is to stay out of Harvey's way to stay on his good side.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac1b4-1dce-11ee-b06f-52b307fec202",
            "Jessica tells Harvey that Stephen brought with him the first dividend from the merger, and hands Harvey his share of a half a million dollars, although she herself received one and a half million dollars. They both discuss how they don't believe why Stephen claimed to be here, and Jessica instructs him to look into Harvey. Donna tells him that Stephen booked a suite for a month, which is longer than \"cultural integration\" should be, something which Harvey notes but also comments that Donna was looking into him even before Jessica ordered him to, suggesting that she is indeed interested in Stephen.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac1c8-1dce-11ee-b06f-52b307fec202",
            "Katrina attempts to make peace with Mike while he is working on the case in the law library, but he turns her down and admonishes her for how she has treated everyone in the firm. Katrina asks if this is because of how she treated his \"girlfriend\", as Mike insists that it is about more than Rachel, while Katrina comments that he already knew who she was talking about. Katrina then mysteriously leaves the library with a smile.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac1d2-1dce-11ee-b06f-52b307fec202",
            "Harvey goes to meet Stephen for lunch, and tells him that he already checked Stephen out of his room. Harvey asks him why he is really here, and Stephen admits he is really here to help Darby deliver on his promise of backing Harvey in taking over the firm from Jessica. Stephen jokingly tells him that in return, Harvey could race him using two luxury cars from his car club. Cameron approaches their table, and tells them he has secured 5 witnesses that confirm the colonel Ava bribed was at the scene of the murders and walks away smiling. Harvey still refuses Stephen's offer to help, even after the latter pointed out this is a request from Darby, merely replying that Darby himself was not here.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac1e6-1dce-11ee-b06f-52b307fec202",
            "In Rachel's office, Rachel tells Mike that Donna told her that she has already forgiven Mike, and Mike relates to her the previous incident where Donna admonishes Katrina in his defense. They also discuss how Katrina referred to Rachel as Mike's girlfriend, something they realized they never officially established. Mike proceeds to covertly get down on a knee and asks Rachel to officially become his girlfriend, which she accepts. Just then, a video mocking Mike is shown across every computer in the firm, with the dialogue being from Mike's earlier conversation with Katrina. In Louis' office, Katrina tells him that after she has done this, no one will think Louis is a fool but instead Mike will be mocked by the entire firm. She also tells him that she gains nothing from this, and that without Louis' support and protection, her career in the firm will be over.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac1f0-1dce-11ee-b06f-52b307fec202",
            "Mike and Harvey meet with Ava, and discuss how 3 of the witnesses can be discredited, and they can argue the deaths were part of a military incident, just as it was originally reported to Ava. Instead however, she proposes that the witnesses be bribed so that they will refuse to testify in the first place, and fires them after they refuse to do so. Mike and Rachel attempt to retaliate against Katrina, as Harvey walks in and tells Mike to continue working on Ava's case, since it is unlikely Cameron will just drop the case, asking him to think of how to bribe the witnesses legally. He also tells Mike not to retaliate against Katrina.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac204-1dce-11ee-b06f-52b307fec202",
            "After assuring Jessica that they will regain Ava as a client, Harvey walks into Katrina's office and warns her that she is now done at this firm. Katrina argues that Harvey left her out to dry after hiring her, and he replies that she only got into the firm by extorting him and Mike, anything else she expects at the firm has nothing to do with him. He also clarifies that when he told her she was done, he meant that her career will never be more than it is at the moment, but if she ever tries to go after Mike again he will fire her regardless of whatever deal they have. Rachel observes the entire affair quietly from outside the office, and tells Mike, as the two began to joke about the matter, which gives Mike an idea. Mike suggests to Harvey that the witnesses can file a suit against Ava for emotional duress from witnessing the murders, and they can legally provide a settlement fee. Mike also thanks Harvey for defending him against Katrina, something Harvey admits that he himself was",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac20e-1dce-11ee-b06f-52b307fec202",
            "that he himself was not planning to be involved in.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac222-1dce-11ee-b06f-52b307fec202",
            "Just then, Harvey spots Stephen accompanying Ava out of the firm. After she leaves in her car, he demands to know if Stephen is now Ava's new lawyer. Instead however, Stephen reveals that Ava asked him if he was willing to bribe the witnesses, something that while he confirmed, he also insisted that Harvey was right as Cameron would merely use the bribe as further evidence. Stephen suggested to Ava instead that she return to Harvey as her lawyer, since he would best manage it, convincing Harvey that Stephen is indeed here to help. Stephen tells Harvey that even if he does not trust him, Darby trusts him, and since Darby wants Ava to be cleared of charges, Harvey can trust that Stephen will help with that.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac22c-1dce-11ee-b06f-52b307fec202",
            "In Ava's office, Mike presents Ava with their solution, and she asks if Harvey trusts him, which Mike replies is something he likes to think so. Ava asks if Harvey thinks she is guilty, and Mike replies that Harvey is only interested in the evidence and how they can clear Ava. As she continues to press him for an answer, Mike replies that he has no idea what Harvey thinks, but if he did he would never discuss it with anyone since Harvey would not want him to. Ava compliments him as being a good second in command to Harvey and asks if he himself thinks she is guilty, and he replies that its his job to represent her to the best of his ability but to say anything more would also be a betrayal to Harvey.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac240-1dce-11ee-b06f-52b307fec202",
            "Outside the firm, Stephen pulls up alongside Donna on the pavement in a luxury car, and tells her that he lost the race. He asks her out and tells her that he let Harvey win, since if Harvey thinks he is better than him, he won't be jealous when Donna goes out with him. She turns him down, and he reveals that he was planning to take her to see Macbeth, portrayed by Daniel Day Lewis and drives off, leaving an impressed Donna behind.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "db4ac24a-1dce-11ee-b06f-52b307fec202",
            "Back at the firm, Louis gives Katrina his files on Tony Gianopoulous and welcomes her as his new protégé. In Harvey's office, Mike tells Harvey that the settlements have been finished, with the lawyer handling the cases of the witnesses being Harold Gunderson. Harvey asks Mike what he told Ava when she asked if he thought she was guilty, and Mike replies that he told her it was none of her concern. The two of them confirm however, that they both believe Ava did indeed order the murders. Harvey pours Mike a drink, and tells him that he made a deal with Darby to take over the firm from Jessica.",
            {
                "title": "Suits",
                "ep_title": "Unfinished Business",
                "season_num": 3,
                "ep_num": 3
            }
        ],
        [
            "dc7ade3e-1dce-11ee-b06f-52b307fec202",
            "A conflict of interest (COI) is a situation in which a person or organization is involved in multiple interests, financial or otherwise, and serving one interest could involve working against another. Typically, this relates to situations in which the personal interest of an individual or organization might adversely affect a duty owed to make decisions for the benefit of a third party.\n\nAn \"interest\" is a commitment, obligation, duty or goal associated with a particular social role or practice. By definition, a \"conflict of interest\" occurs if, within a particular decision-making context, an individual is subject to two coexisting interests that are in direct conflict with each other. Such a matter is of importance because under such circumstances the decision-making process can be disrupted or compromised in a manner that affects the integrity or the reliability of the outcomes.",
            {
                "title": "Suits",
                "ep_title": "Conflict of Interest",
                "season_num": 3,
                "ep_num": 4
            }
        ],
        [
            "dc7adf7e-1dce-11ee-b06f-52b307fec202",
            "Typically, a conflict of interest arises when an individual finds themselves occupying two social roles simultaneously which generate opposing benefits or loyalties. The interests involved can be pecuniary or non-pecuniary. The existence of such conflicts is an objective fact, not a state of mind, and does not in itself indicate any lapse or moral error. However, especially where a decision is being taken in a fiduciary context, it is important that the contending interests be clearly identified and the process for separating them is rigorously established. Typically, this will involve the conflicted individual either giving up one of the conflicting roles or else recusing themselves from the particular decision-making process in question.",
            {
                "title": "Suits",
                "ep_title": "Conflict of Interest",
                "season_num": 3,
                "ep_num": 4
            }
        ],
        [
            "dc7adfc4-1dce-11ee-b06f-52b307fec202",
            "The presence of a conflict of interest is independent of the occurrence of inappropriateness. Therefore, a conflict of interest can be discovered and voluntarily defused before any corruption occurs. A conflict of interest exists if the circumstances are reasonably believed (on the basis of past experience and objective evidence) to create a risk that a decision may be unduly influenced by other, secondary interests, and not on whether a particular individual is actually influenced by a secondary interest.",
            {
                "title": "Suits",
                "ep_title": "Conflict of Interest",
                "season_num": 3,
                "ep_num": 4
            }
        ],
        [
            "dc7adff6-1dce-11ee-b06f-52b307fec202",
            "A widely used definition is: \"A conflict of interest is a set of circumstances that creates a risk that professional judgement or actions regarding a primary interest will be unduly influenced by a secondary interest.\"Lo and Field (2009). The definition originally appeared in Thompson (1993). Primary interest refers to the principal goals of the profession or activity, such as the protection of clients, the health of patients, the integrity of research, and the duties of public officers. Secondary interest includes personal benefit and is not limited to only financial gain but also such motives as the desire for professional advancement, or the wish to do favours for family and friends. These secondary interests are not treated as wrong in and of themselves, but become objectionable when they are believed to have greater weight than the primary interests. Conflict of interest rules in the public sphere mainly focus on financial relationships since they are relatively more objective,",
            {
                "title": "Suits",
                "ep_title": "Conflict of Interest",
                "season_num": 3,
                "ep_num": 4
            }
        ],
        [
            "dc7ae01e-1dce-11ee-b06f-52b307fec202",
            "more objective, fungible, and quantifiable, and usually involve the political, legal, and medical fields.",
            {
                "title": "Suits",
                "ep_title": "Conflict of Interest",
                "season_num": 3,
                "ep_num": 4
            }
        ],
        [
            "dd4436e4-1dce-11ee-b06f-52b307fec202",
            "Shadow of a Doubt is the fifth episode of the third season of Suits and the 33rd overall. It first aired on August 13, 2013.",
            {
                "title": "Suits",
                "ep_title": "Shadow of a Doubt",
                "season_num": 3,
                "ep_num": 5
            }
        ],
        [
            "0f369bf6-1dcf-11ee-b06f-52b307fec202",
            "The painting's global fame and popularity stem from its 1911 theft by Vincenzo Peruggia, who attributed his actions to Italian patriotism—a belief it should belong to Italy. The theft and subsequent recovery in 1914 generated unprecedented publicity for an art theft, and led to the publication of many cultural depictions such as the 1915 opera Mona Lisa, two early 1930s films (The Theft of the Mona Lisa and Arsène Lupin) and the song Mona Lisa recorded by Nat King Cole—one of the most successful songs of the 1950s.\n\nThe Mona Lisa is one of the most valuable paintings in the world. It holds the Guinness World Record for the highest known painting insurance valuation in history at US$100 million in 1962, equivalent to $1 billion .",
            {
                "title": "Suits",
                "ep_title": "The Painting",
                "season_num": 6,
                "ep_num": 12
            }
        ],
        [
            "100f444c-1dcf-11ee-b06f-52b307fec202",
            "The sixth season of the American legal drama Suits was ordered on July 1, 2015, and began airing on USA Network in the United States July 13, 2016. The season is produced by Hypnotic Films & Television and Universal Cable Productions, and the executive producers are Doug Liman, David Bartis, and series creator Aaron Korsh. The season has six series regulars playing employees at the fictional Pearson Specter Litt law firm in Manhattan: Gabriel Macht, Patrick J. Adams, Rick Hoffman, Meghan Markle, Sarah Rafferty, and Gina Torres. \n\nGina Torres left the show following the summer season due to her contract being up, and she starred in ABC's The Catch. She returned for the season finale and was still credited as main cast for the episode. She further went on to star in the Suits spinoff, Pearson.",
            {
                "title": "Suits",
                "ep_title": "Teeth, Nose, Teeth",
                "season_num": 6,
                "ep_num": 13
            }
        ],
        [
            "10cb3dc8-1dcf-11ee-b06f-52b307fec202",
            "Admission of Guilt is the fourteenth episode of the sixth season of Suits and the 90th overall. It first aired on February 15, 2017.",
            {
                "title": "Suits",
                "ep_title": "Admission of Guilt",
                "season_num": 6,
                "ep_num": 14
            }
        ],
        [
            "df355154-1dce-11ee-b06f-52b307fec202",
            "She's Mine is the seventh episode of the third season of Suits and the 35th overall. It first aired on August 27, 2013.",
            {
                "title": "Suits",
                "ep_title": "She's Mine",
                "season_num": 3,
                "ep_num": 7
            }
        ],
        [
            "e040247a-1dce-11ee-b06f-52b307fec202",
            "Plot \n\nIn 2018, twenty-three days after Thanos erased half of all life in the universe, Carol Danvers rescues Tony Stark and Nebula from deep space and they reunite with the remaining Avengers—Bruce Banner, Steve Rogers, Thor, Natasha Romanoff, and James Rhodes—and Rocket on Earth. Locating Thanos on an uninhabited planet, they plan to use the Infinity Stones to reverse his actions, but discover Thanos has already destroyed them to prevent further use. Enraged, Thor decapitates Thanos.",
            {
                "title": "Suits",
                "ep_title": "Endgame",
                "season_num": 3,
                "ep_num": 8
            }
        ],
        [
            "e04025ce-1dce-11ee-b06f-52b307fec202",
            "Five years later, Scott Lang escapes from the Quantum Realm. Reaching the Avengers Compound, he explains that he experienced only five hours while trapped. Theorizing that the Quantum Realm allows time travel, they ask a reluctant Stark to help them retrieve the Stones from the past to reverse the actions of Thanos in the present. Stark, Rocket, and Banner, who has since merged his intelligence with the Hulk's strength, build a time machine. Banner notes that altering the past does not affect their present; any changes create alternate realities. Banner and Rocket travel to Norway, where they visit the Asgardian refugees' settlement New Asgard and recruit an overweight and despondent Thor. In Tokyo, Romanoff recruits Clint Barton, who became a vigilante after his family was erased during the execution of Thanos' plan.",
            {
                "title": "Suits",
                "ep_title": "Endgame",
                "season_num": 3,
                "ep_num": 8
            }
        ],
        [
            "e040261e-1dce-11ee-b06f-52b307fec202",
            "Banner, Lang, Rogers, and Stark time-travel to New York City during Loki's attack in 2012. At the Sanctum Sanctorum, Banner convinces the Ancient One to give him the Time Stone after promising to return the various Stones to their proper points in time. At Stark Tower, Rogers retrieves the Mind Stone from Hydra sleeper agents, but Stark and Lang's attempt to steal the Space Stone fails, allowing 2012-Loki to escape with it. Rogers and Stark travel to Camp Lehigh in 1970, where Stark obtains an earlier version of the Space Stone and encounters his father, Howard. Rogers steals Pym Particles from Hank Pym to return to the present and spies his lost love, Peggy Carter.",
            {
                "title": "Suits",
                "ep_title": "Endgame",
                "season_num": 3,
                "ep_num": 8
            }
        ],
        [
            "e0402650-1dce-11ee-b06f-52b307fec202",
            "Meanwhile, Rocket and Thor travel to Asgard in 2013; Rocket extracts the Reality Stone from Jane Foster, while Thor gets encouragement from his mother, Frigga, and retrieves his old hammer, Mjolnir. Barton, Romanoff, Nebula, and Rhodes travel to 2014; Nebula and Rhodes go to Morag and steal the Power Stone before Peter Quill can, while Barton and Romanoff travel to Vormir. The Soul Stone's keeper, Red Skull, reveals it can only be acquired by sacrificing a loved one. Romanoff sacrifices herself, allowing Barton to get the Stone. Rhodes and Nebula attempt to return to their own time, but Nebula is incapacitated when her cybernetic implants link with her past self, allowing 2014-Thanos to learn of his future self's success and the Avengers' attempt to undo it. 2014-Thanos sends 2014-Nebula forward in time to prepare for his arrival.",
            {
                "title": "Suits",
                "ep_title": "Endgame",
                "season_num": 3,
                "ep_num": 8
            }
        ],
        [
            "e0402678-1dce-11ee-b06f-52b307fec202",
            "Reuniting in the present, the Avengers place the Stones into a gauntlet that Stark, Banner, and Rocket have built. Having the most resistance to their radiation, Banner wields the gauntlet and reverses Thanos's disintegrations. Meanwhile, 2014-Nebula, impersonating her future self, uses the time machine to transport 2014-Thanos and his warship to the present, which he then uses to destroy the Avengers Compound. Present-day Nebula convinces 2014-Gamora to betray Thanos, but is unable to convince 2014-Nebula and kills her. Thanos overpowers Stark, Thor, and a Mjolnir-wielding Rogers and summons his army to retrieve the Stones, intent on using them to destroy the universe and create a new one. A restored Stephen Strange arrives with other sorcerers, the restored Avengers and Guardians of the Galaxy, the Ravagers, and the armies of Wakanda and Asgard to fight Thanos's army. Danvers also arrives and destroys Thanos's warship, but Thanos overpowers her and seizes the gauntlet. Stark steals",
            {
                "title": "Suits",
                "ep_title": "Endgame",
                "season_num": 3,
                "ep_num": 8
            }
        ],
        [
            "e04026aa-1dce-11ee-b06f-52b307fec202",
            "Stark steals the Stones and uses them to disintegrate Thanos and his army, at the cost of his life.",
            {
                "title": "Suits",
                "ep_title": "Endgame",
                "season_num": 3,
                "ep_num": 8
            }
        ],
        [
            "e04026d2-1dce-11ee-b06f-52b307fec202",
            "Following Stark's funeral, Thor appoints Valkyrie as the new king of New Asgard and joins the Guardians. Rogers returns the Stones and Mjolnir to their proper timelines and remains in the past to live with Carter. In the present, an elderly Rogers passes his shield to Sam Wilson.",
            {
                "title": "Suits",
                "ep_title": "Endgame",
                "season_num": 3,
                "ep_num": 8
            }
        ],
        [
            "e149b908-1dce-11ee-b06f-52b307fec202",
            "Bad Faith is the ninth episode of the third season of Suits and the 37th overall. It first aired on September 10, 2013.",
            {
                "title": "Suits",
                "ep_title": "Bad Faith",
                "season_num": 3,
                "ep_num": 9
            }
        ],
        [
            "e2750378-1dce-11ee-b06f-52b307fec202",
            "Plot\nAva's attorney for her malpractice suit is Travis Tanner, whose strategy is to get Harvey to settle by attacking Scottie both personally and professionally. He gets Stephen to sign an affidavit claiming that she was complicit in the murders, but Donna is able to neutralize this. She visits Stephen in prison with Mike, then asks Mike to leave the room and gets Stephen to admit that he lied, unaware that he was being recorded. Later Harvey interrupts Ava's deposition to speak with her directly, apologizing for his failings but insisting that everything he did was part of a zealous defense of her interests. She agrees to withdraw the suit. Harvey tells Scottie that he wants not only to work with her, but to have her in his life.",
            {
                "title": "Suits",
                "ep_title": "Stay",
                "season_num": 3,
                "ep_num": 10
            }
        ],
        [
            "e27504c2-1dce-11ee-b06f-52b307fec202",
            "Jessica learns of Mike and Rachel's relationship, and is concerned about Robert learning the firm's business, and tells Mike she will fire him unless he gets Rachel to sign an affidavit saying that she knew of Mike's fraud. Rachel visits Jessica and signs it, but asks her in return to waive the \"Harvard rule\" in her case so that she could apply for an associate's position there on her graduation. After initially threatening to break up with her if she goes to Stanford, Mike is again supportive of Rachel, and she decides to go to Columbia in spite of her rational analysis in favor of Stanford.\n\nLouis again gets romantically involved with Sheila Sazs while attempting to lure a top Harvard Law candidate for an open associate position, and he later declares he wants to be \"exclusive\" with Sheila. She briefly leaves Louis alone in a room which contains the records of everyone who ever attended Harvard Law School; he is surprised to find no folder for Mike.",
            {
                "title": "Suits",
                "ep_title": "Stay",
                "season_num": 3,
                "ep_num": 10
            }
        ],
        [
            "e35a267e-1dce-11ee-b06f-52b307fec202",
            "The 39 Clues is a series of adventure novels written by a collaboration of authors, including Rick Riordan, Gordon Korman, Peter Lerangis, Jude Watson, Patrick Carman, Linda Sue Park, Margaret Peterson Haddix, Roland Smith, David Baldacci, Jeff Hirsch, Natalie Standiford, C. Alexander London, Sarwat Chadda and Jenny Goebel. It consists of five series, The Clue Hunt, Cahills vs. Vespers, Unstoppable, Doublecross, and Superspecial.  They chronicle the adventures of two siblings, Amy and Dan Cahill, who discover that their family has been, and still is, the most influential family in history.",
            {
                "title": "Suits",
                "ep_title": "Buried Secrets",
                "season_num": 3,
                "ep_num": 11
            }
        ],
        [
            "e35a27dc-1dce-11ee-b06f-52b307fec202",
            "The first story arc concerns Dan and Amy's quest to find the 39 Clues, which are ingredients to a serum that can create the most powerful person on Earth. This series' primary audience is age 9–14. Since the release of the first novel, The Maze of Bones, on September 9, 2008, the books have gained popularity, positive reception, and commercial success. , the book series has about 8.5 million copies in print and has been translated into 24 languages. \n\nThe publisher of the books is Scholastic Press in the United States. Steven Spielberg acquired film rights to the series in June 2008, and a film based on the books was set to be released in 2016, but, as of March 2023, production has not yet started. The series also originated tie-in merchandise, including collectible cards and an interactive Internet game.",
            {
                "title": "Suits",
                "ep_title": "Buried Secrets",
                "season_num": 3,
                "ep_num": 11
            }
        ],
        [
            "e40d43ee-1dce-11ee-b06f-52b307fec202",
            "Yesterday's Gone is the twelfth episode of the third season of Suits and the 40th overall. It firat aired on March 6, 2014.",
            {
                "title": "Suits",
                "ep_title": "Yesterday's Gone",
                "season_num": 3,
                "ep_num": 12
            }
        ],
        [
            "e4c66c16-1dce-11ee-b06f-52b307fec202",
            "Moot Point is the thirteenth episode of the third season of Suits and the 41st overall. It first aired on March 20, 2014.",
            {
                "title": "Suits",
                "ep_title": "Moot Point",
                "season_num": 3,
                "ep_num": 13
            }
        ],
        [
            "e56db8ae-1dce-11ee-b06f-52b307fec202",
            "Heartburn is the fourteenth episode of the third season of Suits and the 42nd overall. It first aired on March 27, 2014.",
            {
                "title": "Suits",
                "ep_title": "Heartburn",
                "season_num": 3,
                "ep_num": 14
            }
        ],
        [
            "e61ee50c-1dce-11ee-b06f-52b307fec202",
            "Plot\n\nThis season saw the departure of Marcy's husband Steve Rhoades. Marcy remained single for the remainder of the season. This was also the first season where the audience would applaud when a major character would enter a scene for the first time in the episode, the first time that Buck \"speaks\", as well as a Bundyesque of the classic film It's a Wonderful Life.  In the episode \"It's a Bundyful Life (Part 2),\" Ted McGinley makes a guest appearance as Norman Jablonsky before reappearing as a regular cast member in the next season as Jefferson D'arcy. Also, Michael Faustino makes his third guest appearance.\n\nDavid Garrison missed two episodes this season. Amanda Bearse also missed one episode.\n\nThis would also be the final season for writers Marcy Vosburgh & Sandy Sprung.",
            {
                "title": "Suits",
                "ep_title": "Know When to Fold 'Em",
                "season_num": 3,
                "ep_num": 15
            }
        ],
        [
            "e6eea2a6-1dce-11ee-b06f-52b307fec202",
            "No Way Out is the sixteenth and final episode of the third season of Suits and the 44th overall. It first aired on April 10, 2014.",
            {
                "title": "Suits",
                "ep_title": "No Way Out",
                "season_num": 3,
                "ep_num": 16
            }
        ],
        [
            "e7bf51bc-1dce-11ee-b06f-52b307fec202",
            "Plot\nMike, Rachel, Harvey and Jessica are all beginning a new day, all appearing to have spent the night with someone. Rachel is revealed to now be attending Columbia Law School part time and also working as Harvey's new associate. Harvey is distracted by the woman he met the previous night, and is subsequently late to work - apparently now a regular occurrence. Meanwhile, Mike, now an investment banker, goes to strong-arm Walter Gillis into selling him part of his business, which he successfully does. He gets back to his new office at Sidwell Investment Group, meeting his 'Donna', Amy, only to find that Sidwell is waiting for him, demanding he come up with an investment that makes 50% profit or else he is out.",
            {
                "title": "Suits",
                "ep_title": "One-Two-Three Go...",
                "season_num": 4,
                "ep_num": 1
            }
        ],
        [
            "e873b47c-1dce-11ee-b06f-52b307fec202",
            "Breakfast, Lunch and Dinner is the second episode of the fourth season of Suits and the 46th overall. It first aired on June 18, 2014.",
            {
                "title": "Suits",
                "ep_title": "Breakfast, Lunch and Dinner",
                "season_num": 4,
                "ep_num": 2
            }
        ],
        [
            "e93194ce-1dce-11ee-b06f-52b307fec202",
            "Two in the Knees is the third episode of the fourth season of Suits and the 47th overall. It first aired on June 25, 2014.",
            {
                "title": "Suits",
                "ep_title": "Two in the Knees",
                "season_num": 4,
                "ep_num": 3
            }
        ],
        [
            "ea0c0456-1dce-11ee-b06f-52b307fec202",
            "Leveraged is the fourth episode of the fourth season of Suits and the 48th overall. It first aired on July 9, 2014.",
            {
                "title": "Suits",
                "ep_title": "Leveraged",
                "season_num": 4,
                "ep_num": 4
            }
        ],
        [
            "eac77d12-1dce-11ee-b06f-52b307fec202",
            "Pound of Flesh is the fifth episode of the fourth season of Suits and the 49th overall. It first aired on July 16, 2014.",
            {
                "title": "Suits",
                "ep_title": "Pound of Flesh",
                "season_num": 4,
                "ep_num": 5
            }
        ],
        [
            "eb994d38-1dce-11ee-b06f-52b307fec202",
            "The fourth season of the American legal comedy-drama Suits was ordered on October 22, 2013. The fourth season originally aired on USA Network in the United States between June 11, 2014 and March 4, 2015. The season was produced by Hypnotic Films & Television and Universal Cable Productions, and the executive producers were Doug Liman, David Bartis and series creator Aaron Korsh. The season had six series regulars playing employees at the fictional Pearson Specter, later Pearson Specter Litt, law firm in Manhattan: Gabriel Macht, Patrick J. Adams, Rick Hoffman, Meghan Markle, Sarah Rafferty, and Gina Torres. Both Gabriel Macht and Patrick J. Adams made their director debut this season, with Macht directing the eleventh episode while Adams directed the 14th episode.",
            {
                "title": "Suits",
                "ep_title": "Litt the Hell Up",
                "season_num": 4,
                "ep_num": 6
            }
        ],
        [
            "ec50d728-1dce-11ee-b06f-52b307fec202",
            "We're Done is the seventh episode of the fourth season of Suits and the 51st overall. It first aired on July 30, 2014.",
            {
                "title": "Suits",
                "ep_title": "We're Done",
                "season_num": 4,
                "ep_num": 7
            }
        ],
        [
            "ed76a556-1dce-11ee-b06f-52b307fec202",
            "Plot\nIntro\nIn a dystopian future, Earth suffers from a planetary wide drought. The world’s rivers and oceans have receded, causing the world to dessertify. As humanity struggles to survive, water quotas were imposed, causing civil unrest. In the backdrop of this, the Song Sisters (Song Ji-An and Song Wong-Kyung) would dream to see the ocean one day.",
            {
                "title": "Suits",
                "ep_title": "Exposure",
                "season_num": 4,
                "ep_num": 8
            }
        ],
        [
            "ed76a65a-1dce-11ee-b06f-52b307fec202",
            "Prologue",
            {
                "title": "Suits",
                "ep_title": "Exposure",
                "season_num": 4,
                "ep_num": 8
            }
        ],
        [
            "ed76a68c-1dce-11ee-b06f-52b307fec202",
            "Five years prior, the Republic of Korea’s Space and Aeronautics Division (SAA) built the Balhae Lunar Research Station on the moon for scientific research. Unknown to the world, the scientists of Balhae discovered Lunar Water, an extraterrestrial type of water that multiplies like a virus when exposed to living bio-material. Unfortunately, when exposed to humans, the lunar water can aggressively overwhelm the host and drown them from the inside-out. Viewed as a potential means of saving the world from planetary drought, Chief Scientist Dr. Song Wong-Kyung (Ji-An’s sister) led the research and looked for a means to solve the deadly side effects of lunar water to make it safe for human consumption. Through experimenting with marine life, they realized fish can naturally survive exposure to lunar water. With the privacy of the station and far from other world governments knowing, they began human cloning and genetic experimentation. Using the genetic material of a girl, they created the",
            {
                "title": "Suits",
                "ep_title": "Exposure",
                "season_num": 4,
                "ep_num": 8
            }
        ],
        [
            "ed76a6b4-1dce-11ee-b06f-52b307fec202",
            "they created the Lunar clone series, each with different characteristics in hopes one of them will adapt to the water. After 72 failures, Luna 073 was their greatest success as her genetic enhancements allowed her to process lunar water. She has enhanced speed, strength, healing factor (when exposed to lunar water), and fish gills to breathe through water. Unfortunately, the lunar water began infecting the scientists within the station. To contain the situation, Director Choi (of SAA) locked all the scientists within the station; all 117 crew members would die from drowning through lunar water. To cover up this debacle, the public was told that all hands were lost at Balhae due to a fatal radiation leak. It was only after the news reported (the cover story) what happened to Balhae that Ji-An realized her sister died on the moon. This would lead Ji-An to a life-long desire to understand what happened to her sister. Unknown to all, Luna 073 survived on Balhae all this time.",
            {
                "title": "Suits",
                "ep_title": "Exposure",
                "season_num": 4,
                "ep_num": 8
            }
        ],
        [
            "ed76a6d2-1dce-11ee-b06f-52b307fec202",
            "Recovery Mission at Balhae Station\nFive years after the demise of the Balhae crew, Director Choi wants to covertly recover the lunar water back to Earth. She recruits Captain Han Yunjae, a man desperate to save his ill daughter. Han Yunjae agreed to the mission in order to increase his water privileges to help heal his daughter. Astrobiologist Dr. Song Jian was recruited for her scientific knowhow and ties with Wong-Kyung. Along with Ryu Tae-Suk, Dr. Hong Ga-Young, Chief Gong Soo-Hyuk, Kim Sun, Song Soo-Chan, Co-Pilot Lee Gi-Su, Hwang, and two other astronauts, they were instructed and informed to simply go recover mysterious sealed canisters for scientific research; only the captain knew about the lunar water and their true mission. Their recovery mission to the silent sea will not be a smooth journey.",
            {
                "title": "Suits",
                "ep_title": "Exposure",
                "season_num": 4,
                "ep_num": 8
            }
        ],
        [
            "ed76a6f0-1dce-11ee-b06f-52b307fec202",
            "Shortly after leaving Earth, the mission’s spacecraft malfunctions enroute and they crash on the moon’s surface. The ship was dangling on a cliff and Hwang suffered internal injuries. The crew quickly exited the ship and watched it fall into the bottom of the moon cliff. They traveled the rest of the way by foot with depleting oxygen. Unfortunately, Hwang’s injuries were severe and he died of his internal injuries before making it to Balhae. The surviving crew just made it within minutes before losing all oxygen and restored their tanks. Inside the research station, they were surprised to find Balhae mostly functional and with no signs of radiation. As they explored the station, they found corpses and were confused how none seemed to have died from radiation but from acute drowning. Once the crew restored life support and overall systems on Balhae, the crew searched the station for viable samples but all were emptied or unsalvageable. It was during their search that Song’s team",
            {
                "title": "Suits",
                "ep_title": "Exposure",
                "season_num": 4,
                "ep_num": 8
            }
        ],
        [
            "ed76a70e-1dce-11ee-b06f-52b307fec202",
            "that Song’s team detected a foreign presence moving around the station (Luna). Crewmember Soochan touched a dead body to recover a canister, which released water droplets that entered Soo-Chan’s eyes. Unknown to him, he’s contaminated and going to die.",
            {
                "title": "Suits",
                "ep_title": "Exposure",
                "season_num": 4,
                "ep_num": 8
            }
        ],
        [
            "ed76a72c-1dce-11ee-b06f-52b307fec202",
            "Strongly curious about the station, Ji-An wanted to learn more about the cause of death from the drowned station crew. However, Captain Han Yun-Jae denied her from further investigation. It was while exploring the corridors of the station that Gi-Su found a single viable capsule. Just as he left the door, he was dragged back into the laboratory by Luna. Ji-An found him dragged and hung to the ceiling of the station and dropped, killing him from physical trauma. Captain Han investigates Gi-Su’s death and confirms that the intruder travels in the vents and can access an area that is not in the station’s plans. Song theorizes that the intruder is a human survivor of the original Balhae crew. Soochan soon falls ill and vomits unnatural amounts of water from his body until he dies from drowning.",
            {
                "title": "Suits",
                "ep_title": "Exposure",
                "season_num": 4,
                "ep_num": 8
            }
        ],
        [
            "ed76a740-1dce-11ee-b06f-52b307fec202",
            "The crew struggled to restore communications, but managed to regain communication with Earth, and Director Choi orders them to get the capsule from the intruder before they can be rescued. Song and medical officer Hong analyzed the water in Soo-Chan’s blood and realized that it multiplied (in volume) rapidly when in contact with living tissue. They confronted Han and he admits that he knew that the sample they are collecting is lunar water. Their fortunes would change after Han and Song discover a deep hollow basement full of plants.",
            {
                "title": "Suits",
                "ep_title": "Exposure",
                "season_num": 4,
                "ep_num": 8
            }
        ],
        [
            "ed76a75e-1dce-11ee-b06f-52b307fec202",
            "The crew finds a hidden laboratory that is not in the station’s blueprints, which contains hundreds of capsule samples in good condition. The crew obtained a few samples before being attacked by Luna. Choi insists they kill the child to prevent others from finding other capsules. Song searches for the station’s research data, but it has been erased. Tae-Suk is revealed to be a corporate spy who plans to take the lunar water himself and eliminate all opposition for his escape.",
            {
                "title": "Suits",
                "ep_title": "Exposure",
                "season_num": 4,
                "ep_num": 8
            }
        ],
        [
            "ed76a894-1dce-11ee-b06f-52b307fec202",
            "In a confrontation between the girl and the crew, Luna held a canister of luna water and it exploded after a bullet destroyed the sample. To their surprise, the water healed her wounds and allowed her to escape. Song theorizes that the girl has a condition that makes her compatible with the water and that she may be the key to making lunar water viable for consumption. The crew set a trap for Luna and Song manages to interact with Luna. She bites Dr. Song but allows Song to follow her to her room. While examining her room, she realizes it was Wong-Kyung’s quarters. Tae-Suk takes the crew’s remaining capsules, kills another crewmember to cover his tracks, and seals all doors to trap the remaining crewmembers.",
            {
                "title": "Suits",
                "ep_title": "Exposure",
                "season_num": 4,
                "ep_num": 8
            }
        ],
        [
            "ed76a920-1dce-11ee-b06f-52b307fec202",
            "Song finds the station’s research data in her sister’s room, which includes details of SAA’s experiments of lunar water and the origins of Luna 073. In between, Tae-Suk confronts Kim Sun for the samples’ whereabouts. He would expose Kim Sun to lunar water and kill him from drowning. Tae-Suk programs the station to be flooded with lunar water to kill the others, but his escape is delayed when Han catches him. Tae-Suk manages to flee, but is exposed to lunar water. Song is also exposed to lunar water and begins to vomit water. The crew thought she was done for but her body managed to survive the experience. Dr. Song theorizes that Luna’s bite transferred antibodies to her to help Song survive the multiplication process.",
            {
                "title": "Suits",
                "ep_title": "Exposure",
                "season_num": 4,
                "ep_num": 8
            }
        ],
        [
            "ed76a948-1dce-11ee-b06f-52b307fec202",
            "The remaining crew agree that though lunar water is dangerous, it could be the salvation of humanity, but if they take Luna to Earth she will be treated as an experiment forever. Song suggests that they take her to the International Institute of Space Biology, an international space station and neutral territory, to ensure Luna's safety and that the benefits of lunar water will be shared with everyone. The station starts to collapse from lunar water flooding. Several decks are overwhelmed with water and the environmental systems have all frozen. Han and Gong sacrificed themselves so that Song, Luna and Hong can make it out safely. Once outside the station, it is revealed that Luna can survive exposure to the moon’s atmosphere without a space suit. A rescue team successfully picks up the surviving crew and samples.",
            {
                "title": "Suits",
                "ep_title": "Exposure",
                "season_num": 4,
                "ep_num": 8
            }
        ],
        [
            "eea910da-1dce-11ee-b06f-52b307fec202",
            "Plot\nthumb|Scarlett and Rhett at the charity dance",
            {
                "title": "Suits",
                "ep_title": "Gone",
                "season_num": 4,
                "ep_num": 9
            }
        ],
        [
            "eea91256-1dce-11ee-b06f-52b307fec202",
            "In 1861, on the eve of the American Civil War, Scarlett O'Hara lives at Tara, her family's cotton plantation in Georgia, with her parents, two sisters, and their many black slaves. Scarlett is deeply attracted to Ashley Wilkes and learns he is to be married to his cousin, Melanie Hamilton. At an engagement party the next day at Ashley's home, Twelve Oaks, a nearby plantation, Scarlett makes an advance on Ashley but is rebuffed; however, she catches the attention of another guest, Rhett Butler. The party is disrupted by news of President Lincoln's call for volunteers to fight the South, and the Southern men rush to enlist. Scarlett marries Melanie's younger brother Charles to arouse jealousy in Ashley before he leaves to fight. Following Charles's death while serving in the Confederate States Army, Scarlett's mother sends her to the Hamilton home in Atlanta. She creates a scene by attending a charity bazaar in mourning attire and waltzing with Rhett, now a blockade runner for the",
            {
                "title": "Suits",
                "ep_title": "Gone",
                "season_num": 4,
                "ep_num": 9
            }
        ],
        [
            "eea912a6-1dce-11ee-b06f-52b307fec202",
            "runner for the Confederacy.",
            {
                "title": "Suits",
                "ep_title": "Gone",
                "season_num": 4,
                "ep_num": 9
            }
        ],
        [
            "eea912ce-1dce-11ee-b06f-52b307fec202",
            "The tide of war turns against the Confederacy after the Battle of Gettysburg. Many of the men of Scarlett's town are killed. Eight months later, as the Union Army besieges the city in the Atlanta campaign, Melanie gives birth with Scarlett's aid, and Rhett helps them flee the city. Rhett chooses to go off to fight, leaving Scarlett to make her own way back to Tara. She finds Tara deserted, except for her father, sisters, and former slaves, Mammy and Pork. Scarlett learns that her mother has just died of typhoid fever, and her father has lost his mind. With Tara pillaged by Union troops and the fields untended, Scarlett vows to ensure her and her family's survival.",
            {
                "title": "Suits",
                "ep_title": "Gone",
                "season_num": 4,
                "ep_num": 9
            }
        ],
        [
            "eea91300-1dce-11ee-b06f-52b307fec202",
            "With the defeat of the Confederacy, the O'Haras toil in the cotton fields. Ashley returns but finds he is of little help to Tara. When Scarlett begs him to run away with her, he confesses his desire for her and kisses her passionately but says he cannot leave Melanie. Scarlett's father attempts to chase away a carpetbagger from his land but is thrown from his horse and killed.  Unable to pay the Reconstructionist taxes imposed on Tara, Scarlett unsuccessfully appeals to Rhett, then dupes her younger sister Suellen's fiancé, the middle-aged and wealthy general store owner Frank Kennedy, into marrying her. Frank, Ashley, Rhett, and several other accomplices make a night raid on a shanty town after Scarlett is attacked while driving through it alone, resulting in Frank's death. Shortly after Frank's funeral, Rhett proposes to Scarlett, and she accepts.",
            {
                "title": "Suits",
                "ep_title": "Gone",
                "season_num": 4,
                "ep_num": 9
            }
        ],
        [
            "eea91328-1dce-11ee-b06f-52b307fec202",
            "Rhett and Scarlett have a daughter whom Rhett names Bonnie Blue, but Scarlett still pines for Ashley and, chagrined at the perceived ruin of her figure, refuses to have any more children or share a bed with Rhett. One day at Frank's mill, Ashley's sister, India, sees Scarlett and Ashley embracing. Harboring an intense dislike of Scarlett, India eagerly spreads rumors. Later that evening, Rhett, having heard the rumors, forces Scarlett to attend a birthday party for Ashley. Melanie, however, stands by Scarlett. After returning home, Scarlett finds Rhett downstairs drunk, and they argue about Ashley. Rhett kisses Scarlett against her will, stating his intent to have sex with her that night, and carries the struggling Scarlett to the bedroom.",
            {
                "title": "Suits",
                "ep_title": "Gone",
                "season_num": 4,
                "ep_num": 9
            }
        ],
        [
            "eea91350-1dce-11ee-b06f-52b307fec202",
            "The next day, Rhett apologizes for his behavior and offers Scarlett a divorce, which she rejects, saying it would be a disgrace. When Rhett returns from an extended trip to London, England, Scarlett informs him that she is pregnant, but an argument ensues, resulting in her falling down a flight of stairs and suffering a miscarriage. While recovering, tragedy strikes again when Bonnie dies while attempting to jump a fence with her pony. Scarlett and Rhett visit Melanie, who has suffered complications from a new pregnancy, on her deathbed. As Scarlett consoles Ashley, Rhett prepares to leave Atlanta. Having realized that it was him, and not Ashley, she truly loved all along, Scarlett pleads with Rhett to stay, but he rebuffs her and walks away into the morning fog. A distraught Scarlett resolves to return home to Tara, vowing to one day win Rhett back.",
            {
                "title": "Suits",
                "ep_title": "Gone",
                "season_num": 4,
                "ep_num": 9
            }
        ],
        [
            "efe93182-1dce-11ee-b06f-52b307fec202",
            "The Baháʼí Faith is a religion founded in the 19th century that teaches the essential worth of all religions and the unity of all people. Established by Baháʼu'lláh, it initially developed in Iran and parts of the Middle East, where it has faced ongoing persecution since its inception. The religion is estimated to have five to eight million adherents, known as Baháʼís, spread throughout most of the world's countries and territories.",
            {
                "title": "Suits",
                "ep_title": "Faith",
                "season_num": 4,
                "ep_num": 10
            }
        ],
        [
            "efe932e0-1dce-11ee-b06f-52b307fec202",
            "The Baháʼí Faith has three central figures: the Báb (1819–1850), considered a herald who taught his followers that God would soon send a prophet who would be similar to Jesus or Muhammad and who was executed by the Iranian authorities in 1850; Baháʼu'lláh (1817–1892), who claimed to be that prophet in 1863 and faced exile and imprisonment for most of his life; and his son, ʻAbdu'l-Bahá (1844–1921), who was released from confinement in 1908 and made teaching trips to Europe and the United States. After ʻAbdu'l-Bahá's death in 1921, the leadership of the religion fell to his grandson Shoghi Effendi (1897–1957). Baháʼís annually elect local, regional, and national Spiritual Assemblies that govern the religion's affairs, and every five years an election is held for the Universal House of Justice, the nine-member governing institution of the worldwide Baháʼí community that is located in Haifa, Israel, near the Shrine of the Báb.",
            {
                "title": "Suits",
                "ep_title": "Faith",
                "season_num": 4,
                "ep_num": 10
            }
        ],
        [
            "efe93330-1dce-11ee-b06f-52b307fec202",
            "According to Baháʼí teachings, religion is revealed in an orderly and progressive way by a single God through Manifestations of God, who are the founders of major world religions throughout human history; Buddha, Jesus, and Muhammad are noted as the most recent of these before the Báb and Baháʼu'lláh. Baháʼís regard the world's major religions as fundamentally unified in purpose, but diverging in terms of social practices and interpretations. The Baháʼí Faith stresses the unity of all people as its core teaching and explicitly rejects notions of racism, sexism, and nationalism. At the heart of Baháʼí teachings is the goal of a unified world order that ensures the prosperity of all nations, races, creeds, and classes.",
            {
                "title": "Suits",
                "ep_title": "Faith",
                "season_num": 4,
                "ep_num": 10
            }
        ],
        [
            "efe93362-1dce-11ee-b06f-52b307fec202",
            "Letters and epistles by Baháʼu'lláh, along with writings and talks by his son ʻAbdu'l-Bahá, have been collected and assembled into a canon of Baháʼí scriptures. This collection includes works by the Báb, who is regarded as Baháʼu'lláh's forerunner. Prominent among the works of Baháʼí literature are the Kitáb-i-Aqdas, the Kitáb-i-Íqán, Some Answered Questions, and The Dawn-Breakers.",
            {
                "title": "Suits",
                "ep_title": "Faith",
                "season_num": 4,
                "ep_num": 10
            }
        ],
        [
            "f0cfcce6-1dce-11ee-b06f-52b307fec202",
            "Plot",
            {
                "title": "Suits",
                "ep_title": "Enough Is Enough",
                "season_num": 4,
                "ep_num": 11
            }
        ],
        [
            "f0cfcdf4-1dce-11ee-b06f-52b307fec202",
            "The episode starts with Harvey Specter driving down to the offices of Pearson Specter due to an emergency call from Jessica Pearson. As he walks in demanding why she summoned him at such an hour, she curtly replies \"He knows\" and glances aside at Louis Litt, who is standing right there, to Harvey's surprise. Louis tells Harvey that the reason he didn't hear about this before is because he told Donna Paulsen not to warn him as his first official act as name partner. Harvey believes he must be joking, but Jessica tells him that he isn't, and that Louis will be name partner soon. Louis demands to be name partner instantly but Harvey brings up the fact that the senior partners will know something is up due to the fact that Louis just resigned and Jessica wants to take her time easing them in. Louis warns her that if she takes too much time, he will reveal their secret. Harvey returns to his office where he sees Donna crying. Donna tries to apologize, claiming Louis broke her, but Harvey",
            {
                "title": "Suits",
                "ep_title": "Enough Is Enough",
                "season_num": 4,
                "ep_num": 11
            }
        ],
        [
            "f0cfce1c-1dce-11ee-b06f-52b307fec202",
            "her, but Harvey reassures that Louis didn't break her down, and that the only reason he confronted her is because he already knew the truth about Mike Ross. Donna tells Harvey that they need to tell Mike, but Harvey wishes to let Mike have the night and to tell him in the morning.",
            {
                "title": "Suits",
                "ep_title": "Enough Is Enough",
                "season_num": 4,
                "ep_num": 11
            }
        ],
        [
            "f0cfce30-1dce-11ee-b06f-52b307fec202",
            "However, Louis arrives at Mike's house that night and lets Mike know that he knows his secret. He tells Mike to resign, but Mike lets him know that he won't quit and that he can't be fired by him either, to which Louis replies that he will break Mike. Rachel Zane walks in, but Louis dismisses her as a liar too and this causes Rachel to realize that Louis now knows.",
            {
                "title": "Suits",
                "ep_title": "Enough Is Enough",
                "season_num": 4,
                "ep_num": 11
            }
        ],
        [
            "f0cfce4e-1dce-11ee-b06f-52b307fec202",
            "Despite Louis being told by Jessica to keep the name partner promotion a secret, he tells Katrina Bennett, who wonders how he got it. When Louis tells her that he can't explain why and this it's supposed to be a secret, she deduces that he has something on Jessica, and tells Louis that Jessica is pulling the strings to make him look like a fool. No longer deciding to listen to Jessica, Louis lets Robert Zane, who was going to hire him, that he no longer needs the job since he is now a name partner. Zane, who was promised a favor by Harvey if he hired Louis, calls in Harvey for the favor anyways. Although Harvey states that the favor is now void due to Louis never being hired by his firm, Zane tells Harvey that since Louis just resigned before Jessica could fire him only for him to return as a name partner, that means that something is not right at Pearson Specter, and tells Harvey that if he doesn't do this favor then he (Zane) may \"open (his) big mouth and talk about it\".",
            {
                "title": "Suits",
                "ep_title": "Enough Is Enough",
                "season_num": 4,
                "ep_num": 11
            }
        ],
        [
            "f0cfce62-1dce-11ee-b06f-52b307fec202",
            "The favor happens to be regarding a case between Zane's firm and Scottie's new firm. Scottie's firm is about to win the case, and Zane wants to settle instead, so he asks Harvey to settle it for him. Harvey calls up Scottie and tells her that she needs to settle so that Mike Ross' secret doesn't get him into trouble. Scottie agrees, but tells him that this is the last time she will do such a thing, and that she never wants to hear of Mike Ross and his secret again.",
            {
                "title": "Suits",
                "ep_title": "Enough Is Enough",
                "season_num": 4,
                "ep_num": 11
            }
        ],
        [
            "f0cfce80-1dce-11ee-b06f-52b307fec202",
            "Meanwhile at the firm, Louis gives a ton of paralegal work to Mike, telling him that since he didn't go to law school or have a law degree, that's the only thing he can do. Louis believes that burying Mike under all that work will break him, but Mike gets Rachel to help him out. Louis, who is also angry at Rachel for lying to him about Mike's secret, gives her paralegal work too, telling her that although she's in law school, she will never be a good enough lawyer, that she wasn't even able to get into Harvard, and that even though Mike doesn't have a degree, he is a better lawyer than she ever would be, and also brings up her father, which breaks her down. Mike sees her crying and confronts Louis, who tells him that Rachel is Mike's weak point, and that pushing and constantly hammering down on her would break not only her, but Mike as well.",
            {
                "title": "Suits",
                "ep_title": "Enough Is Enough",
                "season_num": 4,
                "ep_num": 11
            }
        ],
        [
            "f0cfce94-1dce-11ee-b06f-52b307fec202",
            "Jessica comes to Louis' office to discuss why he's told Robert Zane, but Louis is rude to her, asking her if she had asked Norma (his secretary) before entering, something Jessica does not take kindly to. Louis demands to be made senior partner right away, and since he's already been going around telling everybody that he is, Jessica gathers all the senior partners up and both she and Harvey give a speech, with Harvey adding that he made a mistake firing Louis since Louis got him out of a jam a few times and is an excellent attorney and thus deserves the title of name partner. Louis, however, coldly adds that he feels that he has always been up there with Harvey and that he will be a name partner for a very long time. After the meeting, Jeff Malone goes to Jessica's office, aware that since Louis resigned right before being fired for committing a crime and is now suddenly back as name partner, that must mean he has something over her, and so he asks what it is. Jessica, however, tells",
            {
                "title": "Suits",
                "ep_title": "Enough Is Enough",
                "season_num": 4,
                "ep_num": 11
            }
        ],
        [
            "f0cfcea8-1dce-11ee-b06f-52b307fec202",
            "however, tells him that she doesn't want to lie to him so she'd rather not say anything. Jeff tells her that while he can accept that at the moment, he won't forever.",
            {
                "title": "Suits",
                "ep_title": "Enough Is Enough",
                "season_num": 4,
                "ep_num": 11
            }
        ],
        [
            "f0cfcec6-1dce-11ee-b06f-52b307fec202",
            "That night, Jessica goes to Mike's office and tells him that he has to stay there and draft Louis' partnership agreement, not only because that it is not billable but because Louis only became a partner because of his dirty little secret. Mike, however, tells Jessica that she could have fired him when she found out, but she didn't. Instead, she used his secret to get rid of Daniel Hardman and get back her power, then she used it again to keep Harvey, then again to beat Harvey. Mike asks her at what point she would accept that it is also her dirty little secret.",
            {
                "title": "Suits",
                "ep_title": "Enough Is Enough",
                "season_num": 4,
                "ep_num": 11
            }
        ],
        [
            "f0cfceda-1dce-11ee-b06f-52b307fec202",
            "Later on, Louis is seen near the elevators, staring at the wall which now reads Pearson Specter Litt. However, Louis wonders if people walking in tomorrow will actually notice the sign, and so demands that Jessica have a little ceremony at 4pm, despite her having a meeting at the time, which will celebrate Louis Litt as the new name partner. Jessica refuses to reschedule her meeting, but Louis says that as a name partner, the event will be held and that she must be there, as well as Harvey, to which she replies that as partners, they both will be there.",
            {
                "title": "Suits",
                "ep_title": "Enough Is Enough",
                "season_num": 4,
                "ep_num": 11
            }
        ],
        [
            "f0cfcef8-1dce-11ee-b06f-52b307fec202",
            "Harvey comes to the library to see Mike, who has been up all night memorizing Louis' cases, a punishment inflicted by Louis himself, as well as drafting Louis' partnership agreement. Harvey tells Mike that they need to go to Louis' ceremony, but Mike refuses to, telling him that Louis is an asshole who is hammering down on Rachel to get to him, which pisses off Harvey as well. Both Harvey and Mike go to Louis' office but before a fight or argument can be had, Jessica walks in. She tells Mike that she added a little something to Mike's draft, which states that Louis is a co-conspirator to hiring a fraud. Louis refuses to sign such a thing, and tells her that he can call the cops, but Jessica tells him that he wouldn't do such a thing, because not only did he use Mike's secret to make himself a name partner, he also went around telling everyone and also demanded that an event be held for him, for which partners were lined up outside to celebrate his new promotion. Louis begrudgingly",
            {
                "title": "Suits",
                "ep_title": "Enough Is Enough",
                "season_num": 4,
                "ep_num": 11
            }
        ],
        [
            "f0cfcf16-1dce-11ee-b06f-52b307fec202",
            "Louis begrudgingly signs the agreement, which now means Louis cannot use Mike's secret against them without bring himself down as well.",
            {
                "title": "Suits",
                "ep_title": "Enough Is Enough",
                "season_num": 4,
                "ep_num": 11
            }
        ],
        [
            "f0cfcf34-1dce-11ee-b06f-52b307fec202",
            "While everyone is in front of the new name on the wall to celebrate Louis' promotion, Jessica gives a speech about how with a new name, they can wipe the slate clean. Harvey privately asks Jessica when she planned on making Louis sign such an agreement, to which she replies that she thought up of it 15 seconds after Donna told her Louis confronted her. Harvey asks why she never told him, and Jessica tells him that Louis needed to see Harvey suffer and that since he isn't a good actor, it was best not to tell him. Harvey apologizes to Jessica, telling her that this is all his fault since he brought Mike to the firm, but she tells him that his dirty little secret is theirs as well, and that now they need to fight like hell to protect it.",
            {
                "title": "Suits",
                "ep_title": "Enough Is Enough",
                "season_num": 4,
                "ep_num": 11
            }
        ],
        [
            "f0cfcf48-1dce-11ee-b06f-52b307fec202",
            "Jessica goes to Jeff's office, knowing that since Jeff will always be wondering what Louis has on her, she should tell him the \"truth\". However, she tells him a half-truth - she tells him that years ago, Daniel Hardman embezzled money from the firm and that when she found out, she hid it from the cops and from the other partners and hid the crime up. She tells Jeff that while she did make Daniel pay the money back, she did alter the books to hide the crime and that Louis found out, and used that to come back and leverage himself as name partner. Jeff wonders why she never trusted him with that information before, and she tells him that she didn't know how he'd react and that she didn't want to lose everything. Jeff hugs her and tells her that her secret is safe with him.",
            {
                "title": "Suits",
                "ep_title": "Enough Is Enough",
                "season_num": 4,
                "ep_num": 11
            }
        ],
        [
            "f0cfcf5c-1dce-11ee-b06f-52b307fec202",
            "Donna arrives at Louis' office with a piece of cake that reads 'Litt', asking to wipe the slate clean, despite Louis telling her that they weren't friends and she was dead to him. Louis is mad at Donna for lying to him about Mike and from keeping his secret, but she tells him that her loyalty to Harvey is greater than their friendship, and also tells him that not only did she never plan to tell him Mike's secret, but she never planned or told Jessica or Rachel either. Louis is taken aback at this, but asks her a very personal question - if she had ever slept with Harvey. He tells her that unless she answers this, he can't even begin to think of trusting her again. She tells him that she slept with him once, and now that she has divulged this very private information, maybe they can wipe the slate clean.",
            {
                "title": "Suits",
                "ep_title": "Enough Is Enough",
                "season_num": 4,
                "ep_num": 11
            }
        ],
        [
            "f21758e4-1dce-11ee-b06f-52b307fec202",
            "Respect is the twelfth episode of the fourth season of Suits and the 56th overall. It first aired on February 4, 2015.",
            {
                "title": "Suits",
                "ep_title": "Respect",
                "season_num": 4,
                "ep_num": 12
            }
        ],
        [
            "f2d38c1c-1dce-11ee-b06f-52b307fec202",
            "Fork in the Road is the thirteenth episode of the fourth season of Suits and the 57th overall. It first aired on February 11, 2015.",
            {
                "title": "Suits",
                "ep_title": "Fork in the Road",
                "season_num": 4,
                "ep_num": 13
            }
        ],
        [
            "f3cdf120-1dce-11ee-b06f-52b307fec202",
            "This is an incomplete chronological list of railway accidents and incidents in India.\n\nRailway accidents may be classified by their effects (e.g.: head-on collisions, rear-end collisions, side collisions, derailments, fires, explosions, etc.), or by cause (e.g.: driver and signalman error; mechanical failure of rolling stock, tracks and bridges; vandalism, sabotage and terrorism; level crossing misuse and trespassing; natural causes such as flooding and fog; hazards of dangerous goods carried; effectiveness of brakes; and adequacy of operating rules).",
            {
                "title": "Suits",
                "ep_title": "Derailed",
                "season_num": 4,
                "ep_num": 14
            }
        ],
        [
            "f3cdf1fc-1dce-11ee-b06f-52b307fec202",
            "India's deadliest rail accident was the 1981 Bihar train derailment (750+ killed), followed by the 1995 Firozabad rail disaster (358 killed), the 2023 Odisha train collision (294 killed), the 1999 Gaisal train disaster (285 killed), the 1998 Khanna rail disaster (212 killed), the 2002 Rafiganj train wreck (200 killed), the 1964 Rameswaram cyclone causing Pamban Bridge accident (150+ killed) and the 2010 Jnaneswari Express train derailment (148 killed). followed by 2023 Odisha Railway Accident (Killed 300)",
            {
                "title": "Suits",
                "ep_title": "Derailed",
                "season_num": 4,
                "ep_num": 14
            }
        ],
        [
            "f4ef49d2-1dce-11ee-b06f-52b307fec202",
            "Intent is the fifteenth episode of the fourth season of Suits and the 59th overall. It first aired on February 25, 2015.",
            {
                "title": "Suits",
                "ep_title": "Intent",
                "season_num": 4,
                "ep_num": 15
            }
        ],
        [
            "f5d32198-1dce-11ee-b06f-52b307fec202",
            "Not Just a Pretty Face is the sixteenth and final episode of the fourth season of Suits and the 60th overall. It first aired on March 4, 2015.",
            {
                "title": "Suits",
                "ep_title": "Not Just a Pretty Face",
                "season_num": 4,
                "ep_num": 16
            }
        ],
        [
            "f6dd5aa4-1dce-11ee-b06f-52b307fec202",
            "Holocaust denial is an antisemitic conspiracy theory that asserts that the Nazi genocide of Jews, known as the Holocaust, is a myth, fabrication, or exaggeration. Holocaust denial involves making one or more of the following false statements:\nNazi Germany's \"Final Solution\" was aimed only at deporting Jews from the territory of the Third Reich and did not include their extermination.\nNazi authorities did not use extermination camps and gas chambers for the mass murder of Jews.\nThe actual number of Jews murdered is significantly lower than the accepted figure of approximately 6 million.\nThe Holocaust is a hoax perpetrated by the Allies, Jews, and/or the Soviet Union.",
            {
                "title": "Suits",
                "ep_title": "Denial",
                "season_num": 5,
                "ep_num": 1
            }
        ],
        [
            "f6dd5bda-1dce-11ee-b06f-52b307fec202",
            "The methodologies of Holocaust deniers are based on a predetermined conclusion that ignores overwhelming historical evidence to the contrary. Scholars use the term denial to describe the views and methodology of Holocaust deniers in order to distinguish them from legitimate historical revisionists, who challenge orthodox interpretations of history using established historical methodologies. Holocaust deniers generally do not accept denial as an appropriate description of their activities and use the euphemism revisionism instead. In some former Eastern Bloc countries, Holocaust deniers do not deny the mass murder of Jews but deny the participation of their own nationals in the Holocaust.\n\nHolocaust denial is considered a serious societal problem in many places where it occurs, and it is illegal in Israel and many European countries.",
            {
                "title": "Suits",
                "ep_title": "Denial",
                "season_num": 5,
                "ep_num": 1
            }
        ],
        [
            "f7e0b55e-1dce-11ee-b06f-52b307fec202",
            "ReMastered: The Lion's Share is an American documentary film directed by Sam Cullman and written by Jeff Zimbalist and Michael Zimbalist that was released on Netflix on May 17, 2019. This film documents the search by Rian Malan, a South African journalist, for the original writers of the legendary song \"The Lion Sleeps Tonight\".",
            {
                "title": "Suits",
                "ep_title": "Compensation",
                "season_num": 5,
                "ep_num": 2
            }
        ],
        [
            "f89a680a-1dce-11ee-b06f-52b307fec202",
            "No Refills is the third episode of the fifth season of Suits and the 63rd overall. It first aired on July 8, 2015.",
            {
                "title": "Suits",
                "ep_title": "No Refills",
                "season_num": 5,
                "ep_num": 3
            }
        ],
        [
            "f95cf6cc-1dce-11ee-b06f-52b307fec202",
            "The fifth season of the American legal comedy-drama Suits was ordered on August 11, 2014. The fifth season originally aired on USA Network in the United States between June 24, 2015 and March 2, 2016. The season was produced by Hypnotic Films & Television and Universal Cable Productions, and the executive producers were Doug Liman, David Bartis and series creator Aaron Korsh. The season had six series regulars playing employees at the fictional Pearson Specter Litt law firm in Manhattan: Gabriel Macht, Patrick J. Adams, Rick Hoffman, Meghan Markle, Sarah Rafferty, and Gina Torres.",
            {
                "title": "Suits",
                "ep_title": "No Puedo Hacerlo",
                "season_num": 5,
                "ep_num": 4
            }
        ],
        [
            "fa4a3522-1dce-11ee-b06f-52b307fec202",
            "Narcoworld: Dope Stories is an American true crime documentary series that was released on Netflix on November 22, 2019. This series explores the global drug trade, told from both the drug trade and law enforcement side.",
            {
                "title": "Suits",
                "ep_title": "Toe to Toe",
                "season_num": 5,
                "ep_num": 5
            }
        ],
        [
            "fb2ffcec-1dce-11ee-b06f-52b307fec202",
            "White privilege, or white skin privilege, is the societal privilege that benefits white people over non-white people in some societies, particularly if they are otherwise under the same social, political, or economic circumstances. With roots in European colonialism and imperialism, and the Atlantic slave trade, white privilege has developed in circumstances that have broadly sought to protect white racial privileges, various national citizenships, and other rights or special benefits.",
            {
                "title": "Suits",
                "ep_title": "Privilege",
                "season_num": 5,
                "ep_num": 6
            }
        ],
        [
            "fb2ffe86-1dce-11ee-b06f-52b307fec202",
            "In the study of white privilege and its broader field of whiteness studies, both pioneered in the United States, academic perspectives such as critical race theory use the concept to analyze how racism and racialized societies affect the lives of white or white-skinned people. For example, American academic Peggy McIntosh described the advantages that whites in Western societies enjoy and non-whites do not experience as \"an invisible package of unearned assets\". White privilege denotes both obvious and less obvious passive advantages that white people may not recognize they have, which distinguishes it from overt bias or prejudice. These include cultural affirmations of one's own worth; presumed greater social status; and freedom to move, buy, work, play, and speak freely. The effects can be seen in professional, educational, and personal contexts. The concept of white privilege also implies the right to assume the universality of one's own experiences, marking others as different or",
            {
                "title": "Suits",
                "ep_title": "Privilege",
                "season_num": 5,
                "ep_num": 6
            }
        ],
        [
            "fb2ffed6-1dce-11ee-b06f-52b307fec202",
            "as different or exceptional while perceiving oneself as normal.",
            {
                "title": "Suits",
                "ep_title": "Privilege",
                "season_num": 5,
                "ep_num": 6
            }
        ],
        [
            "fb2fff08-1dce-11ee-b06f-52b307fec202",
            "Some scholars say that the term uses the concept of \"whiteness\" as a substitute for class or other social privilege or as a distraction from deeper underlying problems of inequality.Hartigan, Odd Tribes (2005), pp. 1–2. Others state that it is not that whiteness is a substitute but that many other social privileges are interconnected with it, requiring complex and careful analysis to identify how whiteness contributes to privilege. Other commentators propose alternative definitions of whiteness and exceptions to or limits of white identity, arguing that the concept of white privilege ignores important differences between white subpopulations and individuals and suggesting that the notion of whiteness cannot be inclusive of all white people. They note the problem of acknowledging the diversity of people of color and ethnicity within these groups.",
            {
                "title": "Suits",
                "ep_title": "Privilege",
                "season_num": 5,
                "ep_num": 6
            }
        ],
        [
            "fb2fff3a-1dce-11ee-b06f-52b307fec202",
            "Some commentators have observed that the \"academic-sounding concept of white privilege\" sometimes elicits defensiveness and misunderstanding among white people, in part due to how the concept of white privilege was rapidly brought into the mainstream spotlight through social media campaigns such as Black Lives Matter. As an academic concept that was only recently brought into the mainstream, the concept of white privilege is frequently misinterpreted by non-academics; some academics, having studied white privilege undisturbed for decades, have been surprised by the recent opposition from right-wing critics since approximately 2014.",
            {
                "title": "Suits",
                "ep_title": "Privilege",
                "season_num": 5,
                "ep_num": 6
            }
        ],
        [
            "fbf8cae6-1dce-11ee-b06f-52b307fec202",
            "Plot",
            {
                "title": "Suits",
                "ep_title": "Hitting Home",
                "season_num": 5,
                "ep_num": 7
            }
        ],
        [
            "fbf8cc30-1dce-11ee-b06f-52b307fec202",
            "Jack Soloff tries to make peace with Mike Ross, which Mike shuns at first. On the direct order of Jessica Pearson, Mike starts working with Jack. In his pursuit on a case with Jack, Mike first finds it difficult to work with Jack and shows a great distrust of him. Despite their differences, Mike and Jack manage to bluff their way through their case, which Jack recognizes as brilliant legal work, and nominates Mike for a junior partner promotion. When Jessica reveals this to Mike, she insists that he find a believable way to decline the offer in order to avoid drawing public attention. Meanwhile, Daniel Hardman approaches Jack to collude with him on a case by pouring poison in his ears about Jessica and Harvey, but Jack denies Daniel's offer. Jack tells Daniel that he has earned Jessica's trust. At the same time, Louis's sister, Esther, comes to Harvey for help on a lawsuit against her company. Harvey declines and sends Esther to Louis, as he no longer wants to sleep with her behind",
            {
                "title": "Suits",
                "ep_title": "Hitting Home",
                "season_num": 5,
                "ep_num": 7
            }
        ],
        [
            "fbf8cc76-1dce-11ee-b06f-52b307fec202",
            "with her behind Louis's back. At the end of the episode, Louis finds out about Harvey and his sister sleeping together. Louis gets in to a fight with Harvey and brings up Harvey's family problems, causing Harvey to punch Louis in the face and then throw him onto a glass table, which breaks apart. Jessica comes in Harvey's office and gets Harvey out of his office to help Louis.",
            {
                "title": "Suits",
                "ep_title": "Hitting Home",
                "season_num": 5,
                "ep_num": 7
            }
        ],
        [
            "fcef9c54-1dce-11ee-b06f-52b307fec202",
            "Plot\nThe fallout from Harvey punching Louis begins. Jessica wants to send Harvey on a two-week vacation to allow heads to cool, but Louis pushes for a three-month suspension without pay. Harvey meets with Louis to sincerely apologize. He confesses that he's been seeing a therapist because of panic attacks, and that old family issues are part of the reason for his attacks. Louis accepts the apology, but then turns on Harvey in a partners meeting and pushes for the suspension, citing company by-laws. Jack steps in and, also citing by-laws, says there is a required 48-hour review period before the partners can vote.",
            {
                "title": "Suits",
                "ep_title": "Mea Culpa",
                "season_num": 5,
                "ep_num": 8
            }
        ],
        [
            "fcef9d26-1dce-11ee-b06f-52b307fec202",
            "Elsewhere, Mike tries to come up with some ways to decline his junior partnership that would sound plausible, but is then surprised when Jessica has already decided to quietly make him a junior partner, and offers him his first case in that role. Mike asks Rachel to be his associate on the case. When the client shows up, however, Mike sees it is Claire Bowden, the woman he once lied to about being a Columbia Law student. Mike runs and hides, telling Rachel to handle the client and make up some excuse why he can't be there. Claire asks about Rachel's boss on the case, saying if it's the Mike Ross she knows, \"he's really turned his life around.\" Rachel says it must be a different Mike Ross. She then comes up with some creative ways to handle Claire's case, but they backfire. Rachel mistakenly leads them to another client who is in a defense contract and will want to check all the background of the people on the case. This leads Rachel to change the paperwork to remove Mike's name but",
            {
                "title": "Suits",
                "ep_title": "Mea Culpa",
                "season_num": 5,
                "ep_num": 8
            }
        ],
        [
            "fcef9d44-1dce-11ee-b06f-52b307fec202",
            "Mike's name but Claire suspects something is wrong and threatens to call the DA's office if Rachel doesn't come clean. She pressures Rachel to finally admit it's the same Mike Ross, and that she's engaged to him.",
            {
                "title": "Suits",
                "ep_title": "Mea Culpa",
                "season_num": 5,
                "ep_num": 8
            }
        ],
        [
            "fcef9d58-1dce-11ee-b06f-52b307fec202",
            "Back in the office, Jack meets with Harvey to discuss the suspension vote and try and make peace. However, upon returning to his office, Jack finds two packages from Daniel Hardman – one for Jack to use on Jessica, and one that Hardman will use on Jack. Louis tries to convince Jessica that he wants to cancel the vote in to suspend Harvey, but Jessica tells Louis that they all have to live with the consequences of Louis starting this in the first place and leaves. Mike meets Claire outside her office and asks Claire why she won't tell and she says it's because she can see how much Rachel loves him. But she also advises Rachel to not marry Mike, saying Mike's secret will eventually ruin their relationship.",
            {
                "title": "Suits",
                "ep_title": "Mea Culpa",
                "season_num": 5,
                "ep_num": 8
            }
        ],
        [
            "fde16372-1dce-11ee-b06f-52b307fec202",
            "Plot\nThe voting for Harvey's suspension begins and Harvey starts off by saying that he admits he hit Louis and apologizes. He humbles himself in front of the partners by reducing his compensation to the median amount, with the remainder going to all partners to share. The vote ends 8-8, hence the motion doesn't carry. Daniel Hardman returns to Pearson Specter Litt to bring in a huge amount of business to the firm, but only if Jessica takes him back. If she declines, he will begin takeovers of PSL clients. Jack Soloff brings it up in a partners meeting, but Harvey and Jessica shoot him down. Hardman tells Jessica that the client he was willing to share was going to make numerous acquisitions, but now that she's said no, he will begin targeting PSL's clients, starting with one \"that's gonna hit you right where it hurts.\"",
            {
                "title": "Suits",
                "ep_title": "Uninvited Guests",
                "season_num": 5,
                "ep_num": 9
            }
        ],
        [
            "fde1641c-1dce-11ee-b06f-52b307fec202",
            "Meanwhile, Rachel and her mother meet at the Plaza Hotel, and Mom tells her about her grandiose wedding plans, and her plan to put the wedding announcement in the New York Times. This leads Rachel to fear that Mike may get too much attention and get caught, and she shocks her mother by saying she wants a small, private wedding. Mike figures out who Hardman's first target will be: McKernan Motors. Mike and Harvey attempt to make McKernan Motors private, protecting it from a hostile takeover. Louis tries to convince Jack to get out of bed with Hardman, telling him what kind of a person Hardman is. Jack says he knows who Hardman is but is siding with him anyway, leading Louis to surmise Hardman has something on Jack. Louis suggests to Jessica that they make Soloff a name partner, which is what Hardman had promised him, but Jessica instead asks Louis to find out what Hardman may have on Jack.",
            {
                "title": "Suits",
                "ep_title": "Uninvited Guests",
                "season_num": 5,
                "ep_num": 9
            }
        ],
        [
            "fde1643a-1dce-11ee-b06f-52b307fec202",
            "Mike and Harvey go to Tony Gianopoulos and Jonathan Sidwell and pit them against each other to take McKernan Motors private. This results in them getting a 20 percent better offer for McKernan than Hardman's client, and Mike and Harvey go to Hardman's office to cheerfully tell him his plot has failed. But Hardman later comes to Jessica to tell her that his offer is now 20 percent more than the private offer Mike and Harvey negotiated, saying he has a Japanese investor and the Dollar took a dive against the Yen.",
            {
                "title": "Suits",
                "ep_title": "Uninvited Guests",
                "season_num": 5,
                "ep_num": 9
            }
        ],
        [
            "fde16444-1dce-11ee-b06f-52b307fec202",
            "Louis is frustrated since he cannot find any dirt or a single case where Soloff crossed the line, and he takes it out on Donna. Jessica tells Harvey about Hardman's Japanese client. Harvey informs the dollar dropped against the yen two weeks ago, which makes them realize that Hardman was playing them. They now know there is only one person who would offer such a ridiculous sum to steal a PSL client: Charles Forstman. Harvey visits Forstman in prison, and Charles says his only profit comes from seeing Harvey's life destroyed. He wants Harvey to quit now, or he will see PSL's clients picked off by Hardman, one by one.",
            {
                "title": "Suits",
                "ep_title": "Uninvited Guests",
                "season_num": 5,
                "ep_num": 9
            }
        ],
        [
            "fde16458-1dce-11ee-b06f-52b307fec202",
            "Rachel's mother talks to Mike, fooling him by saying Rachel would be there, too. The conversation leaves Mike wondering whether forcing Rachel to sacrifice so much for him is worth it. Jessica asks Jack what Hardman has on him, but Jack refuses to tell her. She then asks him to resign immediately, which he won't do. Mike calls Trevor, since he is the only \"family\" he has left, and wants him to attend his wedding. Trevor, who appears to have turned his life around, refuses to attend, saying he promised his wife that he would leave his previous life behind. Trevor says Mike is breaking the law every day, and should quit as a lawyer. Trevor reveals Mike's secret is still safe, but that he did go see someone about it. Mike asks who, and Trevor replies, \"You know who.\"",
            {
                "title": "Suits",
                "ep_title": "Uninvited Guests",
                "season_num": 5,
                "ep_num": 9
            }
        ],
        [
            "ff2882ce-1dce-11ee-b06f-52b307fec202",
            "The Baháʼí Faith is a religion founded in the 19th century that teaches the essential worth of all religions and the unity of all people. Established by Baháʼu'lláh, it initially developed in Iran and parts of the Middle East, where it has faced ongoing persecution since its inception. The religion is estimated to have five to eight million adherents, known as Baháʼís, spread throughout most of the world's countries and territories.",
            {
                "title": "Suits",
                "ep_title": "Faith",
                "season_num": 5,
                "ep_num": 10
            }
        ],
        [
            "ff288490-1dce-11ee-b06f-52b307fec202",
            "The Baháʼí Faith has three central figures: the Báb (1819–1850), considered a herald who taught his followers that God would soon send a prophet who would be similar to Jesus or Muhammad and who was executed by the Iranian authorities in 1850; Baháʼu'lláh (1817–1892), who claimed to be that prophet in 1863 and faced exile and imprisonment for most of his life; and his son, ʻAbdu'l-Bahá (1844–1921), who was released from confinement in 1908 and made teaching trips to Europe and the United States. After ʻAbdu'l-Bahá's death in 1921, the leadership of the religion fell to his grandson Shoghi Effendi (1897–1957). Baháʼís annually elect local, regional, and national Spiritual Assemblies that govern the religion's affairs, and every five years an election is held for the Universal House of Justice, the nine-member governing institution of the worldwide Baháʼí community that is located in Haifa, Israel, near the Shrine of the Báb.",
            {
                "title": "Suits",
                "ep_title": "Faith",
                "season_num": 5,
                "ep_num": 10
            }
        ],
        [
            "ff2884ea-1dce-11ee-b06f-52b307fec202",
            "According to Baháʼí teachings, religion is revealed in an orderly and progressive way by a single God through Manifestations of God, who are the founders of major world religions throughout human history; Buddha, Jesus, and Muhammad are noted as the most recent of these before the Báb and Baháʼu'lláh. Baháʼís regard the world's major religions as fundamentally unified in purpose, but diverging in terms of social practices and interpretations. The Baháʼí Faith stresses the unity of all people as its core teaching and explicitly rejects notions of racism, sexism, and nationalism. At the heart of Baháʼí teachings is the goal of a unified world order that ensures the prosperity of all nations, races, creeds, and classes.",
            {
                "title": "Suits",
                "ep_title": "Faith",
                "season_num": 5,
                "ep_num": 10
            }
        ],
        [
            "ff288526-1dce-11ee-b06f-52b307fec202",
            "Letters and epistles by Baháʼu'lláh, along with writings and talks by his son ʻAbdu'l-Bahá, have been collected and assembled into a canon of Baháʼí scriptures. This collection includes works by the Báb, who is regarded as Baháʼu'lláh's forerunner. Prominent among the works of Baháʼí literature are the Kitáb-i-Aqdas, the Kitáb-i-Íqán, Some Answered Questions, and The Dawn-Breakers.",
            {
                "title": "Suits",
                "ep_title": "Faith",
                "season_num": 5,
                "ep_num": 10
            }
        ],
        [
            "00164ffe-1dcf-11ee-b06f-52b307fec202",
            "1983 is a Polish crime drama TV series co-created by Maciej Musiał, written by Joshua Long and released on Netflix on November 30, 2018. This series is set in an alternate timeline in which the fall of the communist Polish People's Republic never happened and the Iron Curtain is still in place.",
            {
                "title": "Suits",
                "ep_title": "Blowback",
                "season_num": 5,
                "ep_num": 11
            }
        ],
        [
            "00de00f8-1dcf-11ee-b06f-52b307fec202",
            "Live to Fight is the twelfth episode of the fifth season of Suits and the 72nd overall. It first aired on February 3, 2016.",
            {
                "title": "Suits",
                "ep_title": "Live to Fight...",
                "season_num": 5,
                "ep_num": 12
            }
        ],
        [
            "018dca1a-1dcf-11ee-b06f-52b307fec202",
            "God's Green Earth is the thirteenth episode of the fifth season of Suits and the 73rd overall. It first aired on February 10, 2016.",
            {
                "title": "Suits",
                "ep_title": "God's Green Earth",
                "season_num": 5,
                "ep_num": 13
            }
        ],
        [
            "0288c8fc-1dcf-11ee-b06f-52b307fec202",
            "Self Defense is the fourteenth episode of the fifth season of Suits and the 74th overall. It first aired on February 17, 2016.",
            {
                "title": "Suits",
                "ep_title": "Self Defense",
                "season_num": 5,
                "ep_num": 14
            }
        ],
        [
            "0369cb22-1dcf-11ee-b06f-52b307fec202",
            "Plot\nTime is running out for Mike Ross. As Mike's trial speeds along, it's time for him and Harvey to pull out all the stops. In these final moments before the clock runs out and the jury returns with a verdict.\n\nAfter convincing the judge to let Mike represent himself, which involves agreeing to not move for a mistrial because of it, Mike calls Clifford Danner's mother to stand. She tells the court she wishes Mike had been her son's lawyer from day one and wouldn’t have cared if he was a fraud because Mike was \"the only lawyer I ran into who gave a damn about my son.\"",
            {
                "title": "Suits",
                "ep_title": "Tick Tock",
                "season_num": 5,
                "ep_num": 15
            }
        ],
        [
            "0369ccbc-1dcf-11ee-b06f-52b307fec202",
            "With that tear-filled testimony, Mike works on his closing argument. At this point, Jessica has accepted that Mike is defending himself. If only the same could be said of Louis, who is freaking out about it and believes it's a sign that Harvey doesn’t think he can win, and if Harvey thinks they’ll lose, then they will lose. \"It’s him growing up and realizing he is not the one to bring this home,\" Jessica argues. While Louis doesn’t buy that, it seems to be confirmed in the next scene when Harvey tells Donna that Mike doesn’t need his help with his closing because it’s his story and he’s got it handled.\n\nWhen it comes time to present his closer, Mike decides to go off script in order to deliver what he believes is a more sincere argument. “The truth is I am guilty of being a fraud,” he says, explaining he wanted to be a lawyer to help people. \"But instead, all I've done as a lawyer is work night and day to put money into the hands of rich people.\"",
            {
                "title": "Suits",
                "ep_title": "Tick Tock",
                "season_num": 5,
                "ep_num": 15
            }
        ],
        [
            "0369cd0c-1dcf-11ee-b06f-52b307fec202",
            "As Gibbs delivers her closing statement, Mike starts zoning out, and her voice fades into the background as he imagines the jury saying guilty. Part of him clearly believes he doesn’t deserve to be found guilty. Once she's done talking and the jury heads off to deliberate, he melodramatically decides that he’s not going to leave the courtroom until they return with a verdict.\n\nJessica isn’t comfortable leaving her firm's fate up to a jury, so she orders Harvey to go and get a mistrial by any means necessary. First, Harvey asks Donna if her friend in the U.S. Attorney’s Office would give him the jury names, but she refuses because she doesn’t want anyone breaking the law for this. So Harvey decides to blackmail David Green into buying one of the jurors a coffee. \"This is atonement,\" Harvey tells David. \"This is the day you face the music.:. But David doesn't fall for that nonsense and doesn't come through.",
            {
                "title": "Suits",
                "ep_title": "Tick Tock",
                "season_num": 5,
                "ep_num": 15
            }
        ],
        [
            "0369cd3e-1dcf-11ee-b06f-52b307fec202",
            "While Mike’s awaiting the verdict in the empty courtroom, he overhears a prosecutor trying to railroad a defendant. So, Mike steps in to defend the man whose own lawyer didn’t show up for his petty theft trial. Even while his life is on the line, Mike can’t not help someone out in need. It’s an admirable characteristic, but it’s also frustrating for Rachel, who rightfully gets angry when she finds out what he’s doing. Instead of spending time with her in what might he last few hours of freedom, he’s doing this.\n\nScared for his life and dreading prison, Louis visits Gibbs to make a deal, but she says she can’t help him without any hard proof that Harvey did something. So, Louis decides to go get that proof. He confronts Harvey in the lobby of the firm’s building and secretly records Harvey admitting that he hired a fraud. But Louis ends up deleting the audio when Jessica refuses to consider turning on Harvey.",
            {
                "title": "Suits",
                "ep_title": "Tick Tock",
                "season_num": 5,
                "ep_num": 15
            }
        ],
        [
            "0369cd66-1dcf-11ee-b06f-52b307fec202",
            "Later that night, Gibbs shows up at Mike’s apartment with two deals: Deal No. 1:  If he pleads guilty and does two years, she won’t go after his friends; and Deal No. 2, he pleads guilty, gets no jail time, but has to give her some kind of evidence to prosecute his friends. Rachel overhears the offers, and she wants Mike to take the second option. However, her real problem is that she thinks Mike doesn’t have enough faith in himself that he could win on the strength of his performance in court, even though she does.\n\nThe case Mike is working on turns into a very obvious allegory. The prosecutor offers his client a deal: No jail if he turns on his accomplices. Despite Mike pleading with him to not betray his friends, his client agrees to the deal because, as he puts it, his friends are going to jail either way.",
            {
                "title": "Suits",
                "ep_title": "Tick Tock",
                "season_num": 5,
                "ep_num": 15
            }
        ],
        [
            "0369cda2-1dcf-11ee-b06f-52b307fec202",
            "Harvey shows up at the courthouse to sit with Mike and because the jury has finally returned with a verdict, but, Mike isn’t anywhere to be found. Harvey knows where he is and takes off running to the U.S. Attorney’s Office, where Mike is in Gibbs’ office and says he’s ready to take the deal.",
            {
                "title": "Suits",
                "ep_title": "Tick Tock",
                "season_num": 5,
                "ep_num": 15
            }
        ],
        [
            "04839560-1dcf-11ee-b06f-52b307fec202",
            "Plot\nA car pulls up on a New York City street, which Monty Brogan exits with his friend Kostya to look at an injured dog lying in the road. Monty intends to perform a mercy kill and shoot him, but changes his mind after he looks it in the eye; he takes the dog to a nearby clinic instead.\n\nA few years later, Monty is about to begin serving a seven-year prison sentence for dealing drugs. He sits in a park with Doyle, the dog he rescued, on his last day of freedom. He plans to meet childhood friends Frank, a boorish Wall Street trader, and Jacob, an introverted high school teacher with a crush on his student Mary, at a club with his girlfriend Naturelle.",
            {
                "title": "Suits",
                "ep_title": "25th Hour",
                "season_num": 5,
                "ep_num": 16
            }
        ],
        [
            "048396c8-1dcf-11ee-b06f-52b307fec202",
            "Monty visits his father, James, a former firefighter and recovering alcoholic at his bar, to confirm their plans to drive to the prison the following morning. James was able to establish the bar with Monty’s drug money, and remorsefully sneaks a drink when Monty goes to the bathroom. Facing himself in the mirror, Monty lashes out in his mind against everyone in New York before finally turning on himself, angry for becoming greedy and not giving up drug dealing before he was caught.",
            {
                "title": "Suits",
                "ep_title": "25th Hour",
                "season_num": 5,
                "ep_num": 16
            }
        ],
        [
            "04839718-1dcf-11ee-b06f-52b307fec202",
            "In a flashback, Monty remembers the night he was arrested: DEA agents raided Monty's apartment and quickly found the drugs he was selling for Uncle Nikolai, a Russian mobster. Kostya tries to persuade Monty it was Naturelle who betrayed him, since she knew where he hid his drugs and money. Monty refused to turn state's evidence against Nikolai, but is unsure about Nikolai’s actions. Monty remembers how he met Naturelle hanging around his old school, and how happy they were. He then asks Frank to find out if it was Naturelle who betrayed him.",
            {
                "title": "Suits",
                "ep_title": "25th Hour",
                "season_num": 5,
                "ep_num": 16
            }
        ],
        [
            "04839844-1dcf-11ee-b06f-52b307fec202",
            "Jacob sees Mary outside the club, and Monty invites her inside with them. Discussing what kind of a future Monty can have after prison, Frank says they can open a bar together, even though he told Jacob that he believes Monty deserves his sentence for dealing drugs. Frank accuses Naturelle of living high on Monty's money despite knowing its origins, but she retorts that Frank also knew but said nothing. The argument culminates with Frank insulting Naturelle's ethnicity, followed by her slapping Frank and leaving. Jacob, meanwhile, finds the courage to kiss Mary, but both are shocked afterwards and go their separate ways.",
            {
                "title": "Suits",
                "ep_title": "25th Hour",
                "season_num": 5,
                "ep_num": 16
            }
        ],
        [
            "04839e84-1dcf-11ee-b06f-52b307fec202",
            "Monty and Kostya go to see Nikolai, who gives Monty advice on surviving in prison. Nikolai then reveals it was Kostya who betrayed Monty, and offers him a chance to kill Kostya in exchange for protecting his father's bar. Monty refuses, reminding Nikolai that he was the one who told Monty to trust Kostya in the first place. Monty walks out, leaving Kostya to be killed by the Russian mobsters.\n\nMonty returns to his apartment and apologizes to Naturelle for mistrusting her. He then hands Doyle over to Jacob in the park. He admits that he is terrified of being raped in prison, whereupon he asks Frank to beat him, believing that he might have a chance at survival if he enters the prison ugly. Frank refuses, and Monty goads Frank into taking out his frustrations, leaving Monty bruised and bloody, with a broken nose.",
            {
                "title": "Suits",
                "ep_title": "25th Hour",
                "season_num": 5,
                "ep_num": 16
            }
        ],
        [
            "04839f1a-1dcf-11ee-b06f-52b307fec202",
            "Naturelle tries to comfort him as Monty's father arrives to take him to Federal Correctional Institution, Otisville. On the drive to prison, Monty once again sees a parade of faces from the streets of the city. As they drive up the turnpike, James suggests they take the George Washington Bridge to go west, into hiding, and gives Monty a vision of a future where he avoids imprisonment, reunites with Naturelle, starts a family, and grows old. When the vision stops, they are past the bridge, still driving towards prison.",
            {
                "title": "Suits",
                "ep_title": "25th Hour",
                "season_num": 5,
                "ep_num": 16
            }
        ],
        [
            "05598e90-1dcf-11ee-b06f-52b307fec202",
            "Plot\nMike enters the Danbury Federal Penitentiary in Connecticut to face his two-year jail sentence for fraud. Rachel and Harvey struggle to cope personally, while Louis, Jessica, and Donna don't know how to deal with an office empty of employees. It doesn't take long before the firm is sued in a $100 million class-action lawsuit for every case Mike touched. When they learn that all their client files were also stolen, the three name partners agree to go all in for the sake of the firm. In jail, Mike discovers a new enemy in Frank Gallo, an inmate who has a great deal of influence with the guards. Gallo tricks Mike into giving him Rachel's phone number, and promises trouble for Mike in his vendetta against Harvey.",
            {
                "title": "Suits",
                "ep_title": "To Trouble",
                "season_num": 6,
                "ep_num": 1
            }
        ],
        [
            "060fd380-1dcf-11ee-b06f-52b307fec202",
            "Plot\nMike meets his actual cellmate, Kevin Miller, and is wary of being tricked a second time. Donna obtained visitation rights for Rachel, but Mike gets into a fight with Frank Gallo that leads to his visitation rights being revoked for two weeks. When Harvey visits Mike in prison as his lawyer and learns about Gallo, he reveals that he put the man behind bars for racketeering for 15 years, three times the usual sentence. Rachel keeps receiving text messages from Gallo posing as Mike and learns the situation from Harvey, who hopes Sean Cahill can help. As the cost for allowing the settlement of the class-action lawsuit to move forward, A. Elliott Stemple demands Harvey's duck painting, a prized possession painted by his mother. In the midst of the firm's money problems, Jack Soloff demands his buy-in back. Jessica refuses but helps him by negotiating for his buy-in with Robert Zane's firm. Kevin earns some goodwill with Mike by opposing Gallo.",
            {
                "title": "Suits",
                "ep_title": "Accounts Payable",
                "season_num": 6,
                "ep_num": 2
            }
        ],
        [
            "06d9d874-1dcf-11ee-b06f-52b307fec202",
            "Plot",
            {
                "title": "Suits",
                "ep_title": "Back on the Map",
                "season_num": 6,
                "ep_num": 3
            }
        ],
        [
            "06d9da7c-1dcf-11ee-b06f-52b307fec202",
            "Mike tries to stay out of trouble to please Julius Rowe, the prison psychologist, but Kevin gets attacked. Sean Cahill informs Harvey that Gallo is an informant and will not be transferred. Through Mike, Harvey informs Gallo that he'll be eligible for parole in six weeks. Jessica forces Harvey to meet with William Sutter as a potential client; Harvey refuses to do business with a shady businessman, but Jessica demands a high-profile client for the firm's future. When Harvey tries to sign Nathan Byrnes instead, Sutter interferes. Louis regretfully books an office tenant to pay the bills and clashes with Stu Buzzini, head of an investment company, as soon as they move in, but Harvey makes a deal with the investor to stave off Sutter, cementing them as new neighbors and gaining Byrnes as a client. Now in law school, Rachel engages in a debate with a classmate and uses the skills learned from her work experience to win. Cahill informs Harvey that he can get Mike released from prison if",
            {
                "title": "Suits",
                "ep_title": "Back on the Map",
                "season_num": 6,
                "ep_num": 3
            }
        ],
        [
            "06d9dab8-1dcf-11ee-b06f-52b307fec202",
            "from prison if Mike informs on Kevin Miller.",
            {
                "title": "Suits",
                "ep_title": "Back on the Map",
                "season_num": 6,
                "ep_num": 3
            }
        ],
        [
            "07e009fa-1dcf-11ee-b06f-52b307fec202",
            "Turn Up Charlie is a British comedy miniseries created by Idris Elba and Gary Reich, and directed by Tristram Shapeero and Matt Lipsey. It was released on March 15, 2019. This series revolves around a DJ planning to rebuild his music career while taking care of his best friend's wild pre-teen daughter.",
            {
                "title": "Suits",
                "ep_title": "Turn",
                "season_num": 6,
                "ep_num": 4
            }
        ],
        [
            "08d847dc-1dcf-11ee-b06f-52b307fec202",
            "is an American crime documentary film directed by Luke Sewell. It was released on Netflix on March 30, 2022. This film is about group of investors who decided to, after his death, take the missing $250 million that belonged to the cryptocurrency multimillionaire Gerry Cotten, who they believe Cotten stole from them.",
            {
                "title": "Suits",
                "ep_title": "Trust",
                "season_num": 6,
                "ep_num": 5
            }
        ],
        [
            "09facc20-1dcf-11ee-b06f-52b307fec202",
            "Spain (, ), or the Kingdom of Spain (), is a country primarily located in Southwestern Europe, with parts of its territory in the Atlantic Ocean and across the Mediterranean Sea. The largest part of Spain is situated on the Iberian Peninsula; its territory also includes the Canary Islands in the Atlantic Ocean, the Balearic Islands in the Mediterranean Sea, and the autonomous cities of Ceuta and Melilla in Africa. The country's mainland is bordered to the north by France, Andorra, and the Bay of Biscay; to the east and south by the Mediterranean Sea and Gibraltar; and to the west by Portugal and the Atlantic Ocean. It is the largest country in Southern Europe and the second-largest and fourth-most populous in the European Union. Spain's capital and largest city is Madrid; other major urban areas include Barcelona, Valencia, Zaragoza, Seville, Málaga, Murcia, Palma de Mallorca, Las Palmas de Gran Canaria, and Bilbao.",
            {
                "title": "Suits",
                "ep_title": "Spain",
                "season_num": 6,
                "ep_num": 6
            }
        ],
        [
            "09face1e-1dcf-11ee-b06f-52b307fec202",
            "Anatomically modern humans first arrived on the Iberian Peninsula around 42,000 years ago. The ancient Iberian and Celtic tribes, along with other local pre-Roman peoples, inhabited the territory, maintaining contacts with foreign Mediterranean cultures. The Roman conquest and colonization of the peninsula (Hispania) ensued, bringing about the Romanization of the population. Receding of Western Roman imperial authority ushered in the invasion into Iberia of tribes from Central and Northern Europe, with the Visigoths as the dominant power in the peninsula by the fifth century. In the early eighth century, most of the peninsula was conquered by the Umayyad Caliphate, and during early Islamic rule, Al-Andalus became a dominant peninsular power centered in Córdoba. Several Christian kingdoms emerged in Northern Iberia, chief among them León, Castile, Aragon, Portugal, and Navarre; made an intermittent southward military expansion, known as the Reconquista, repelling Islamic rule in",
            {
                "title": "Suits",
                "ep_title": "Spain",
                "season_num": 6,
                "ep_num": 6
            }
        ],
        [
            "09face64-1dcf-11ee-b06f-52b307fec202",
            "Islamic rule in Iberia, which culminated with the Christian seizure of the Emirate of Granada in 1492. The dynastic union of the Crown of Castile and the Crown of Aragon in 1479, often considered the formation of Spain as a country, was followed by the annexation of Navarre and the incorporation of Portugal during the Iberian Union. The Crown of Spain, through the Spanish Inquisition, forced the Jewish and Muslim minorities to choose between conversion to Catholicism or expulsion, and eventually most of the converts were expelled from Iberia through different royal decrees.",
            {
                "title": "Suits",
                "ep_title": "Spain",
                "season_num": 6,
                "ep_num": 6
            }
        ],
        [
            "09face96-1dcf-11ee-b06f-52b307fec202",
            "A major country of the Age of Discovery, Spain began the conquest of the New World in 1492, giving rise to the Spanish Empire. Controlling vast portions of the Americas, parts of Africa, various territories in Asia and Oceania, as well as territory in other parts of Europe, the Spanish Empire became, in conjunction with the Portuguese, the first empire to achieve a global scale and one of the largest empires in history. The empire's need for financing and the transatlantic trade underpinned the rise of a global trading system fueled primarily by precious metals. Centralisation and further state-building in mainland Spain ensued in the 18th century with the Bourbon reforms. In the 19th century, the Crown saw the independence of most of its American colonies as a result of cumulative crises and political divisions after the Peninsular War. Political instability reached its peak in the 20th century with the Spanish Civil War, giving rise to the Francoist dictatorship that lasted until",
            {
                "title": "Suits",
                "ep_title": "Spain",
                "season_num": 6,
                "ep_num": 6
            }
        ],
        [
            "09facebe-1dcf-11ee-b06f-52b307fec202",
            "that lasted until 1975. With the restoration of democracy under the Constitution of Spain and its entry into the European Union, the country experienced an economic boom that profoundly transformed it socially and politically.",
            {
                "title": "Suits",
                "ep_title": "Spain",
                "season_num": 6,
                "ep_num": 6
            }
        ],
        [
            "09facefa-1dcf-11ee-b06f-52b307fec202",
            "Spain is a secular parliamentary democracy and a constitutional monarchy, with King Felipe VI as head of state. It is a major capitalist advanced economy, with the world's sixteenth-largest economy by nominal GDP (fourth of the European Union) and the sixteenth-largest by PPP. Spain has a very high Human Development Index (HDI) and quality of life standard, with one of the highest life expectancies in the world. Spain is a member of the United Nations, the European Union, the Eurozone, the Council of Europe (CoE), de facto member of the G20, the Organization of Ibero-American States (OEI), the Union for the Mediterranean, the North Atlantic Treaty Organization (NATO), the Organisation for Economic Co-operation and Development (OECD), the Organization for Security and Co-operation in Europe (OSCE), the World Trade Organization (WTO), and many other international organisations. Since the so-called Siglo de Oro, a period of flourishing in arts and literature in Spain coinciding with the",
            {
                "title": "Suits",
                "ep_title": "Spain",
                "season_num": 6,
                "ep_num": 6
            }
        ],
        [
            "09facf22-1dcf-11ee-b06f-52b307fec202",
            "coinciding with the political rise of the Spanish Empire under the Catholic Monarchs and the Spanish Habsburgs, Spanish art, architecture, music, literature, and cuisine have been influential worldwide, particularly in Western Europe and the Americas. As such, Spain is considered a regionalSpain is ranked between the Top 10 Soft Powers. https://img1.wsimg.com/blobby/go/905bb114-a609-4bd0-a33b-dabe335781b0/downloads/ISSF_s%20World%20Soft%20Power%20Index%202022.pdf?ver=1660547924817\"Spain, main reference for world's Hispanic heritage\". ABC.es (Madrid). 2014-07-03. http://www.abc.es/cultura/20140703/abci-espana-patrimonio-inmaterial-humanidad-201407011734.html. Retrieved 2016-06-08.\"From Seville to Brussels: The Architecture of Global Presence\". International Relations and Security Network. October 28, 2015. http://www.isn.ethz.ch/Digital-Library/Articles/Detail/?lng=en&id=194365. Retrieved December 9, 2015. and cultural",
            {
                "title": "Suits",
                "ep_title": "Spain",
                "season_num": 6,
                "ep_num": 6
            }
        ],
        [
            "09facf4a-1dcf-11ee-b06f-52b307fec202",
            "2015. and cultural superpower.https://explora.globalpresence.realinstitutoelcano.org/en/country/iepg/global/ES/ES/2021https://www.lamoncloa.gob.es/consejodeministros/resumenes/Documents/2021/270421-foreigh_action_strategy_2021-2024.pdfhttps://brandfinance.com/events/global-soft-power-summit-2021 As a reflection of its large cultural wealth, Spain has one of the world's largest numbers of World Heritage Sites, It's the world's second-most visited country and the most popular destination for Erasmus students.Spain is crowned the champion of foreign students. This is thanks to universities such as those in Barcelona, Valencia, Madrid, Granada and Salamanca. Although nowhere near as popular as Spain, we find Germany in second place. It is a country that also has a large number of prestigious universities spread out across many cities. The fact that Germany is an economic powerhouse makes it an attractive destination for those searching for employment after studying. France, the United",
            {
                "title": "Suits",
                "ep_title": "Spain",
                "season_num": 6,
                "ep_num": 6
            }
        ],
        [
            "09facf7c-1dcf-11ee-b06f-52b307fec202",
            "France, the United Kingdom and Italy appear in third, fourth and fifth position. The rest of countries rank behind at a considerable distance. https://www.wimdu.co.uk/blog/discover-popular-erasmus-destinations Its cultural influence extends to over 570 million Hispanophones, making Spanish the world's second-most spoken native language and the world's most widely spoken Romance language.",
            {
                "title": "Suits",
                "ep_title": "Spain",
                "season_num": 6,
                "ep_num": 6
            }
        ],
        [
            "0ad851ee-1dcf-11ee-b06f-52b307fec202",
            "The sixth season of the American legal drama Suits was ordered on July 1, 2015, and began airing on USA Network in the United States July 13, 2016. The season is produced by Hypnotic Films & Television and Universal Cable Productions, and the executive producers are Doug Liman, David Bartis, and series creator Aaron Korsh. The season has six series regulars playing employees at the fictional Pearson Specter Litt law firm in Manhattan: Gabriel Macht, Patrick J. Adams, Rick Hoffman, Meghan Markle, Sarah Rafferty, and Gina Torres. \n\nGina Torres left the show following the summer season due to her contract being up, and she starred in ABC's The Catch. She returned for the season finale and was still credited as main cast for the episode. She further went on to star in the Suits spinoff, Pearson.",
            {
                "title": "Suits",
                "ep_title": "Shake the Trees",
                "season_num": 6,
                "ep_num": 7
            }
        ],
        [
            "0b8f2612-1dcf-11ee-b06f-52b307fec202",
            "Plot\nIn the Old West, a sheriff and his young son are traveling on a wagon trail. The sheriff gives his son his own pocket watch and his hat for good luck. During their trek, their stagecoach is attacked by bandits. While the sheriff attempts to fend off their attackers, the son drives the wagon, but loses control when it collides with a rock, breaking a wagon wheel, and causing the sheriff to be flung over a nearby cliff's edge. The son recovers, and observes the damage. As he looks around, he finds his father hanging on to a lower rock ledge. Attempting to reach his father with his hand, he isn't able to reach him; subsequently, the sheriff hands his son his rifle for additional leverage, and the son begins to pull him up. Before the son can pull his father to the top of the cliff, he puts his finger inside the trigger guard and accidentally fires the rifle, killing his father by mistake, leaving the young son traumatized.",
            {
                "title": "Suits",
                "ep_title": "Borrowed Time",
                "season_num": 6,
                "ep_num": 8
            }
        ],
        [
            "0b8f2766-1dcf-11ee-b06f-52b307fec202",
            "Many years later, the son has risen to the office of the sheriff, and visits the cliff where his father died. Reliving the events of that day, he contemplates suicide, unable to cope with the guilt. He allows himself to slip off the cliff's edge, but when he sees the pocket watch his father gave him, he attempts to climb back onto the cliff, almost falling off in the process. He manages to get back up and retrieves the pocket watch, then breaks down crying. He cradles the watch in his hands and breathes deeply in a short moment of solace. He holds the watch close to his heart, and it starts ticking.",
            {
                "title": "Suits",
                "ep_title": "Borrowed Time",
                "season_num": 6,
                "ep_num": 8
            }
        ],
        [
            "0c58b6e4-1dcf-11ee-b06f-52b307fec202",
            "Henry Jones Fairlie (13 January 1924, in London, England – 25 February 1990, in Washington, D.C.) was a British political journalist and social critic, known for popularizing the term \"the Establishment\", an analysis of how \"all the right people\" came to run Britain largely through social connections. He spent 36 years as a prominent freelance writer on both sides of the Atlantic, appearing in The Spectator, The New Republic, The Washington Post, The New Yorker, and many other papers and magazines. He was also the author of five books, most notably The Kennedy Promise, an early revisionist critique of the US presidency of John F. Kennedy.\n\nIn 2009, Yale University Press published Bite the Hand That Feeds You: Essays and Provocations (), an anthology of his work edited by Newsweek correspondent Jeremy McCarter.",
            {
                "title": "Suits",
                "ep_title": "The Hand That Feeds You",
                "season_num": 6,
                "ep_num": 9
            }
        ],
        [
            "0d1dabc0-1dcf-11ee-b06f-52b307fec202",
            "P.S.L. is the tenth episode of the sixth season of Suits and the 86th overall. It first aired on September 14, 2016.",
            {
                "title": "Suits",
                "ep_title": "P.S.L.",
                "season_num": 6,
                "ep_num": 10
            }
        ],
        [
            "0dda400a-1dcf-11ee-b06f-52b307fec202",
            "She's Gone is the eleventh episode of the sixth season of Suits and the 87th overall. It first aired on January 25, 2017.",
            {
                "title": "Suits",
                "ep_title": "She's Gone",
                "season_num": 6,
                "ep_num": 11
            }
        ],
        [
            "0f369ade-1dcf-11ee-b06f-52b307fec202",
            "The Mona Lisa ( ;   or  ;  ) is a half-length portrait painting by Italian artist Leonardo da Vinci.\n\nConsidered an archetypal masterpiece of the Italian Renaissance, it has been described as \"the best known, the most visited, the most written about, the most sung about, [and] the most parodied work of art in the world\". The painting's novel qualities include the subject's enigmatic expression, monumentality of the composition, the subtle modelling of forms, and the atmospheric illusionism.",
            {
                "title": "Suits",
                "ep_title": "The Painting",
                "season_num": 6,
                "ep_num": 12
            }
        ],
        [
            "0f369bce-1dcf-11ee-b06f-52b307fec202",
            "The painting has been definitively identified to depict Italian noblewoman Lisa del Giocondo. It is painted in oil on a white Lombardy poplar panel. Leonardo never gave the painting to the Giocondo family, and it is believed he later left it in his will to his favored apprentice Salaì. It was believed to have been painted between 1503 and 1506; however, Leonardo may have continued working on it as late as 1517. It was acquired by King Francis I of France and is now the property of the French Republic. It has been on permanent display at the Louvre in Paris since 1797.",
            {
                "title": "Suits",
                "ep_title": "The Painting",
                "season_num": 6,
                "ep_num": 12
            }
        ],
        [
            "de775884-1dce-11ee-b06f-52b307fec202",
            "Plot\nDonna and Louis share an elevator while he mentions his previous night with his cat, Mikado. Quickly noticing, Donna points out the 'Specter' in the newly added 'Pearson Darby Specter'. Looking surprised, she enters Harvey's office, indirectly pointing out that he should've made her aware of his latest accomplishments. However, Harvey argues back stating, she isn't focused, due to her current circumstances regarding Stephen Huntley.\nthumb|right|250px|Flashback to the past.\nIn a flashback taking place ten years prior, at the District Attorney's office, Donna notices the several spots Harvey had missed shaving, however she swiftly realizes this was due to his poker game the previous night. As they continue to 'play footsie' Cameron Dennis ensures he focuses on his work. Now, it takes us to Mike and Trevor's story. As Mike enters their apartment, Trevor shows him a letter from Harvard, explaining of his successful transfer application from Harvard.",
            {
                "title": "Suits",
                "ep_title": "The Other Time",
                "season_num": 3,
                "ep_num": 6
            }
        ],
        [
            "de775a28-1dce-11ee-b06f-52b307fec202",
            "Meanwhile, in the present day, Mike points out that Cameron has another witness, heavily protected by U.S. Marshals. Harvey realizes Cameron's case is becoming solid and will stop at nothing. Meanwhile, in the middle of packing for her visit to Law schools, Rachel and Mike engage in an argument.",
            {
                "title": "Suits",
                "ep_title": "The Other Time",
                "season_num": 3,
                "ep_num": 6
            }
        ],
        [
            "b88da6ba-1dcd-11ee-8262-52b307fec202",
            "Plot\nKendall has cut off communications with the rest of his family and is suing Logan for firing him from Waystar. Tabloids suggest that Kendall, a recovering drug addict, has relapsed, but Kendall unconvincingly insists to Rava that he has not. Meanwhile, in an effort to fix his public image after the failed no-confidence vote, Logan agrees to a weekend-long family therapy session at Austerlitz, Connor's ranch in New Mexico, which Kendall chooses not to attend.\n\nThe first therapy session, conducted by celebrity psychologist Dr. Alon Parfit, proves fruitless. Shiv leaves Austerlitz to meet U.S. Senator and presidential candidate Gil Eavis, a staunch leftist who vehemently opposes Logan and his company. Nate has been attempting to persuade Shiv to work alongside him for Eavis's campaign. Shiv considers the idea more seriously after meeting Eavis, and has a sexual encounter with Nate in his car.",
            {
                "title": "Succession",
                "ep_title": "Austerlitz",
                "season_num": 1,
                "ep_num": 7
            }
        ]
    ]
}

def hash_dict(d: dict):
    return hashlib.sha256(json.dumps(d, sort_keys=True).encode()).hexdigest()

def abs_ep_num(db_data, title, season_num, ep_num):
    #print(db_data, title, season_num, ep_num)
    prev_ep_count = 0

    for n in range(1, season_num):
        all_season_eps = list(filter(lambda x: x[2]['season_num'] == n and x[2]['title'] == title, db_data["data"]))
        all_season_info = list(map(lambda x: hash_dict(x[2]), all_season_eps))
        prev_ep_count += len(set(all_season_info))

        #Temporary fix due to the fact that we don't have all episodes added
        

    return prev_ep_count + ep_num