# -*- coding: UTF8 -*-

import time,datetime
import telepot
from telepot.loop import MessageLoop

#Libraries------------------------------------------------------------------------------
#Libraries
#Libraries
 
now = datetime.datetime.now()                                                       


#Libraries
#Libraries
#Libraries------------------------------------------------------------------------------



#function handle + Object---------------------------------------------------------------
#function handle + Object
#function handle + Object


def handle(msg):                                                                    
    chat_id = msg['chat']['id']
    command = msg['text']
    

    print 'Received: %s'% command 


    


#Various test commands-------------------------------------------------------
#Various test commands
#Various test commands


    if command == 'Hi':                                                             
        bot.sendMessage (chat_id, str("Hi! How are you?"))

    elif command == 'I am fine':
        bot.sendMessage(chat_id, str("That's good."))
        

    elif command == 'What time is it?':
        bot.sendMessage(chat_id, str(now.hour)+str(":")+str(now.minute))        


    #elif command == '':
        #bot.sendMessage(chat_id, str(""))


#Various test commands
#Various test commands
#Various test commands-------------------------------------------------------------------

    
#Country---------------------------------------------------------------------------------
#Country
#Country

        
    elif command == 'Germany':
        bot.sendMessage(chat_id, str("https://t.me/AGIGermany"))


    elif command == 'Spain':
        bot.sendMessage(chat_id, str("https://t.me/AGISpain"))


    elif command == 'Russia':
       bot.sendMessage(chat_id, str("https://t.me/SingularityNET_Rus"))


    elif command == 'Holland':
       bot.sendMessage(chat_id, str("https://t.me/AGIHolland"))


    elif command == 'Dutch':
       bot.sendMessage(chat_id, str("https://t.me/AGIHolland"))

       
    elif command == 'China':
       bot.sendMessage(chat_id, str("https://t.me/AGIChina"))


    elif command == 'Portugal':
       bot.sendMessage(chat_id, str("https://t.me/AGIPortugal"))


    elif command == 'France':
       bot.sendMessage(chat_id, str("https://t.me/AGIFrancais"))


    elif command == 'Deutschland':
       bot.sendMessage(chat_id, str("https://t.me/AGIDeutschlandTechnologie"))


    elif command == 'Japan':
       bot.sendMessage(chat_id, str("https://t.me/AGIJapan"))


    elif command == 'Korea':
        bot.sendMessage(chat_id, str("싱귤레리티넷 SingularityNet/Sophia https://t.me/SingularityNet_Kor"))


    #elif command == '':
        #bot.sendMessage(chat_id, str(""))


#Country
#Country
#Country---------------------------------------------------------------------------------


#Official--------------------------------------------------------------------------------
#Official
#Official


    elif command == 'Website':
        bot.sendMessage(chat_id, str("https://singularitynet.io"))


    elif command == 'website':
        bot.sendMessage(chat_id, str("https://singularitynet.io"))
       

    elif command == 'Main':
       bot.sendMessage(chat_id, str("https://t.me/singularitynet"))


    elif command == 'Ofc':
       bot.sendMessage(chat_id, str("https://t.me/singularitynet"))
       

    elif command == 'Announcements':
       bot.sendMessage(chat_id, str("https://t.me/snetann"))


    elif command == 'Announcement':
       bot.sendMessage(chat_id, str("https://t.me/snetann"))


    elif command == 'News':
       bot.sendMessage(chat_id, str("https://blog.singularitynet.io/singularitynet-partners-with-deepbrain-chain-to-towards-an-open-and-democratic-ai-future-49db584f62ad"))


    elif command == 'news':
       bot.sendMessage(chat_id, str("https://blog.singularitynet.io/singularitynet-partners-with-deepbrain-chain-to-towards-an-open-and-democratic-ai-future-49db584f62ad"))
       

    elif command == 'Dev':
       bot.sendMessage(chat_id, str("https://t.me/AGIDevelopers"))


    elif command == 'Philosophy':
     bot.sendMessage(chat_id, str("https://t.me/AGIPhilosophy"))


    elif command == 'Reddit':
       bot.sendMessage(chat_id, str("https://www.reddit.com/r/SingularityNet"))


    elif command == 'reddit':
       bot.sendMessage(chat_id, str("https://www.reddit.com/r/SingularityNet"))

       
    elif command == 'Twitter':
       bot.sendMessage(chat_id, str("https://mobile.twitter.com/singularity_net"))

    elif command == 'Whitepaper':
       bot.sendMessage(chat_id, str("https://public.singularitynet.io/whitepaper.pdf"))


    elif command == 'Medium':
        bot.sendMessage(chat_id, str("https://medium.com/singularitynet"))


    elif command == 'Forum':
        bot.sendMessage(chat_id, str("https://community.singularitynet.io/"))


    elif command == 'forum':
        bot.sendMessage(chat_id, str("https://community.singularitynet.io/"))


    elif command == 'FAQ':
        bot.sendMessage(chat_id, str("https://community.singularitynet.io/c/qa"))


    elif command == 'Roadmap':
        bot.sendMessage(chat_id, str("https://singularitynet.io/platform-roadmap/"))

        

    elif command == 'Services':
        bot.sendMessage(chat_id, str("https://singularitynet.io/services-roadmap/"))


    elif command == 'Research':
        bot.sendMessage(chat_id, str("https://singularitynet.io/research-initiatives/"))


    elif command == 'Platform':
        bot.sendMessage(chat_id, str("https://singularitynet.io/platform-roadmap/\nhttps://singularitynet.io/services-roadmap/\nhttps://singularitynet.io/research-initiatives/"))   


    #elif command == '':
        #bot.sendMessage(chat_id, str(""))


    #Text various


    elif command == 'Steemit':
        bot.sendMessage(chat_id, str("https://steemit.com/blockchain/@aigents/proof-of-reputation-as-liquid-democracy-for-blockchain"))

    elif command == 'Aigents':
        bot.sendMessage(chat_id, str("https://steemit.com/blockchain/@aigents/proof-of-reputation-as-liquid-democracy-for-blockchain"))        
        

    elif command == 'Social':
        bot.sendMessage(chat_id, str("https://blog.singularitynet.io/singularitynet-moves-toward-social-computing-with-proof-of-reputation-14df7c6618f"))


    elif command == 'Sophia':
      bot.sendMessage(chat_id, str("http://goertzel.org/sophias-ai-some-comments/"))


    elif command == 'Face recognition':
        bot.sendMessage(chat_id, str("https://blog.singularitynet.io/building-calling-face-services-through-singularitynet-8b1c7a142e45"))


    elif command == 'face recognition':
        bot.sendMessage(chat_id, str("https://blog.singularitynet.io/building-calling-face-services-through-singularitynet-8b1c7a142e45"))


    elif command == 'Face':
        bot.sendMessage(chat_id, str("https://blog.singularitynet.io/building-calling-face-services-through-singularitynet-8b1c7a142e45"))


    elif command == 'face':
        bot.sendMessage(chat_id, str("https://blog.singularitynet.io/building-calling-face-services-through-singularitynet-8b1c7a142e45"))


    #elif command == '':
        #bot.sendMessage(chat_id, str(""))


     #Text various


#Official
#Official
#Official--------------------------------------------------------------------------------


    

    #elif command == '':
        #bot.sendMessage(chat_id, str(""))

#Partner---------------------------------------------------------------------------------
#Partner
#Partner


    elif command == 'Deepbrainchain':
        bot.sendMessage(chat_id, str("https://t.me/deepbrainchain"))


    elif command == 'DeepBrainChain':
        bot.sendMessage(chat_id, str("https://t.me/deepbrainchain"))

        
    elif command == 'deepbrainchain':
        bot.sendMessage(chat_id, str("https://t.me/deepbrainchain"))


    elif command == 'Deepbrainchain Website':
        bot.sendMessage(chat_id, str("http://www.deepbrainchain.org"))


    elif command == 'Deepbrainchain website':
        bot.sendMessage(chat_id, str("http://www.deepbrainchain.org"))


    elif command == 'deepbrainchain website':
        bot.sendMessage(chat_id, str("http://www.deepbrainchain.org"))


    elif command == 'DBC Website':
        bot.sendMessage(chat_id, str("http://www.deepbrainchain.org"))
        

    elif command == 'DBC website':
        bot.sendMessage(chat_id, str("http://www.deepbrainchain.org"))


    elif command == 'dbc website':
        bot.sendMessage(chat_id, str("http://www.deepbrainchain.org"))


    elif command == 'OceanProtocol News':
        bot.sendMessage(chat_id, str("https://t.me/OceanProtocol"))


    elif command == 'OceanProtocol news':
        bot.sendMessage(chat_id, str("https://t.me/OceanProtocol"))


    elif command == 'Oceanprotocol News':
        bot.sendMessage(chat_id, str("https://t.me/OceanProtocol"))


    elif command == 'Oceanprotocol news':
        bot.sendMessage(chat_id, str("https://t.me/OceanProtocol"))

    elif command == 'oceanprotocol news':
        bot.sendMessage(chat_id, str("https://t.me/OceanProtocol"))

    elif command == 'OceanProtocol':
        bot.sendMessage(chat_id, str("https://t.me/joinchat/GUyxrE0Hi154D0NrlOqLFg"))


    elif command == 'Oceanprotocol':
        bot.sendMessage(chat_id, str("https://t.me/joinchat/GUyxrE0Hi154D0NrlOqLFg"))


    elif command == 'oceanprotocol':
        bot.sendMessage(chat_id, str("https://t.me/joinchat/GUyxrE0Hi154D0NrlOqLFg"))


    elif command == 'Fundrequest Announcement':
        bot.sendMessage(chat_id, str("https://t.me/fundrequestannouncement"))


    elif command == 'fundrequest announcement':
        bot.sendMessage(chat_id, str("https://t.me/fundrequestannouncement"))


    elif command == 'fundrequest':
        bot.sendMessage(chat_id, str("https://t.me/fundrequestannouncement"))


    elif command == 'Fundrequest':
        bot.sendMessage(chat_id, str("https://t.me/fundrequestannouncement"))


    elif command == 'Hacken':
        bot.sendMessage(chat_id, str("https://t.me/hacken_en"))


    elif command == 'hacken':
        bot.sendMessage(chat_id, str("https://t.me/hacken_en"))


    elif command == 'Bitspace':
        bot.sendMessage(chat_id, str("https://t.me/BitSpaceNetwork"))


    elif command == 'bitspace':
        bot.sendMessage(chat_id, str("https://t.me/BitSpaceNetwork"))


    elif command == 'Bitspace Network':
        bot.sendMessage(chat_id, str("https://t.me/BitSpaceNetwork"))


    elif command == 'bitspace network':
        bot.sendMessage(chat_id, str("https://t.me/BitSpaceNetwork"))


    elif command == 'Bitdegree':
        bot.sendMessage(chat_id, str("https://t.me/bitdegree"))


    elif command == 'bitdegree':
        bot.sendMessage(chat_id, str("https://t.me/bitdegree"))


    elif command == 'bitdegree news':
        bot.sendMessage(chat_id, str("@bitdegree_ann"))
        

    elif command == 'Bitdegree News':
        bot.sendMessage(chat_id, str("@bitdegree_ann"))


    elif command == 'Bitdegree news':
        bot.sendMessage(chat_id, str("@bitdegree_ann"))

        
    #elif command == '':
        #bot.sendMessage(chat_id, str(""))



#Partner
#Partner
#Partner---------------------------------------------------------------------------------        

#Forumuserlinks--------------------------------------------------------------------------
#Forumuserlinks
#Forumuserlinks


    elif command == 'Decentralized':
       bot.sendMessage(chat_id, str(" https://community.singularitynet.io/t/decentralised-personal-agent"))


    elif command == 'decentralized':
       bot.sendMessage(chat_id, str(" https://community.singularitynet.io/t/decentralised-personal-agent"))


    elif command == 'Virtual':
       bot.sendMessage(chat_id, str("https://community.singularitynet.io/t/singularitynet-and-vr-meetings-events-and-collaboration/253"))


    elif command == 'virtual':
       bot.sendMessage(chat_id, str("https://community.singularitynet.io/t/singularitynet-and-vr-meetings-events-and-collaboration/253"))


    #elif command == '':
        #bot.sendMessage(chat_id, str(""))


#Forumuserlinks
#Forumuserlinks
#Forumuserlinks--------------------------------------------------------------------------


#Unofficial Telegram groups--------------------------------------------------------------
#Unofficial Telegram groups
#Unofficial Telegram groups
       
       
    elif command == 'Vr':
       bot.sendMessage(chat_id, str("https://t.me/joinchat/Gops-UtKqHNEYBMbStVBzg"))  
       

    elif command == 'Ar':
       bot.sendMessage(chat_id, str("https://t.me/joinchat/Gops-UtKqHNEYBMbStVBzg"))   


    elif command == 'Price':
       bot.sendMessage(chat_id, str("AGI Price Talk (unofficial) Here you can talk AGI price and Singularitynet growth. It is not allowed in the main Community Channel anymore. We thank you for your understanding    https://t.me/joinchat/Gops-Q0JmTFXNM0K88sISw"))


    elif command == 'price':
       bot.sendMessage(chat_id, str("https://t.me/joinchat/Gops-Q0JmTFXNM0K88sISw"))

      
    elif command == 'Truth':
       bot.sendMessage(chat_id, str("https://t.me/snettruthers"))


    elif command == 'truth':
       bot.sendMessage(chat_id, str("https://t.me/snettruthers"))


    elif command == 'botcontrol':
        bot.sendMessage(chat_id, str("https://t.me/joinchat/Gops-U-HT3IIoBrjjNwNSg"))


    elif command == 'Botcontrol':
        bot.sendMessage(chat_id, str("https://t.me/joinchat/Gops-U-HT3IIoBrjjNwNSg"))

    elif command == 'Admins Volunteers Unofficial':
        bot.sendMessage(chat_id, str("https://t.me/joinchat/Gops-USbfBEF8nXN6ZZ02w"))


    elif command == 'usecases':
        bot.sendMessage(chat_id, str("https://t.me/joinchat/G-U0kUmUVKyu3wzRJbHaZg"))


    elif command == 'Usecases':
        bot.sendMessage(chat_id, str("https://t.me/joinchat/G-U0kUmUVKyu3wzRJbHaZg"))


    elif command == 'usecase':
        bot.sendMessage(chat_id, str("https://t.me/joinchat/G-U0kUmUVKyu3wzRJbHaZg"))


    elif command == 'Usecase':
        bot.sendMessage(chat_id, str("https://t.me/joinchat/G-U0kUmUVKyu3wzRJbHaZg"))


    #elif command == '':
        #bot.sendMessage(chat_id, str(""))


#Unofficial Telegram groups
#Unofficial Telegram groups
#Unofficial Telegram groups--------------------------------------------------------------


#interacting bots------------------------------------------------------------------------
#interacting bots + other feeds
#interacting bots
       

    elif command == 'Numbers':
        bot.sendMessage(chat_id, str("https://tinyurl.com/y7tgzbtl"))


    elif command == 'numbers':
        bot.sendMessage(chat_id, str("https://tinyurl.com/y7tgzbtl"))


    elif command == 'Number':
        bot.sendMessage(chat_id, str("https://tinyurl.com/y7tgzbtl"))


    elif command == 'number':
        bot.sendMessage(chat_id, str("https://tinyurl.com/y7tgzbtl"))

    elif command == 'Google trends':
        bot.sendMessage(chat_id, str("https://trends.google.com/trends/explore?q=singularityNET"))


    elif command == 'Markets':
        bot.sendMessage(chat_id, str("https://coinmarketcap.com/currencies/singularitynet/#markets"))


    #elif command == '':
        #bot.sendMessage(chat_id, str(""))


#interacting bots
#interacting bots + other feeds
#interacting bots------------------------------------------------------------------------


#Articles-------------------------------------------------------------------------------------
#Articles
#Articles

        
    elif command == 'Trend':
        bot.sendMessage(chat_id, str("https://blockchainflashnews.com/cftc-commissioner-cryptocurrencies-are-here-to-stay-and-they-will-transform-the-economic-landscape"))
    

    elif command == 'trend':
        bot.sendMessage(chat_id, str("https://blockchainflashnews.com/cftc-commissioner-cryptocurrencies-are-here-to-stay-and-they-will-transform-the-economic-landscape"))


    elif command == 'trends':
        bot.sendMessage(chat_id, str("https://blockchainflashnews.com/cftc-commissioner-cryptocurrencies-are-here-to-stay-and-they-will-transform-the-economic-landscape"))


    elif command == 'trend':
        bot.sendMessage(chat_id, str("https://blockchainflashnews.com/cftc-commissioner-cryptocurrencies-are-here-to-stay-and-they-will-transform-the-economic-landscape"))

    elif command == 'Datasheets':
        bot.sendMessage(chat_id, str("https://venturebeat.com/2018/05/02/datasheets-could-be-the-solution-to-biased-ai/"))


    elif command == 'DAIA':
        bot.sendMessage(chat_id, str("Snet launches 100 million http://www.the-blockchain.com/2018/05/25/singularitynet-launches-100-million-industry-initiative-to-fund-and-support-ai-blockchain-projects/?utm_content=buffer94578&utm_medium=social&utm_source=facebook.com&utm_campaign=buffer"))


    elif command == 'Generative Twitter':
        bot.sendMessage(chat_id, str("https://twitter.com/bengoertzel/status/1008175639734579201?s=19"))


    elif command == 'Generative':
        bot.sendMessage(chat_id, str("https://blog.singularitynet.io/singularitynets-ai-team-experiments-with-generative-capsule-networks-c48ebc3fb2e1"))


    elif command == 'Digital kitties':
        bot.sendMessage(chat_id, str("http://badcryptopodcast.com/2018/06/02/benny-giang-simone-giacomelli-134/"))


    elif command == 'Digital Kitties':
        bot.sendMessage(chat_id, str("http://badcryptopodcast.com/2018/06/02/benny-giang-simone-giacomelli-134/"))


    #elif command == '':
        #bot.sendMessage(chat_id, str(""))


#Articles
#Articles
#Articles-------------------------------------------------------------------------------------


#Comments-------------------------------------------------------------------------------------
#Comments
#Comments

        
    elif command == 'Concern':
        bot.sendMessage(chat_id, str("This is such a great cause for concern.Google is apparently trying to monopolize AI by patenting stuff they didn't even invent themselves. https://ipkitten.blogspot.com/2018/06/deepmind-first-major-ai-patent-filings.html?m=1"))

    elif command == 'DBC':
        bot.sendMessage(chat_id, str("Ben Goertzel- Yeah, the DBC partnership should be a valuable one -- and we can use that to prototype interoperation btw SingularityNET and other AI networks ... fleshing out a technical approach that can then be used for interoperation w/ many other AI networks- Ben Goertzel"))

    elif command == 'Latest':
        bot.sendMessage(chat_id, str("Ben Goertzel - @streondj along with our core AI algorithms, we are building example useful services in biomedical AI (genomics) and social media analytics, as well as social robots (together w/ Hanson Robotics) ... a few examples to showcase the platform, and then indeed the broader community will need to carry the platform into the full variety of vertical markets...- Ben Goertzel"))


    elif command == 'Comment':
        bot.sendMessage(chat_id, str("Ben Goertzel- We are going to organize a bunch of SingularityNET developer workshops this fall though, as a student maybe you can help by organizing one at your campus, as a start...- Ben Goertzel"))

    
    elif command == 'Vitalik':
        bot.sendMessage(chat_id, str("https://www.reddit.com/r/SingularityNet/comments/7t3yzi/my_analysis_of_singularitynet/?utm_source=reddit-android"))


    elif command == 'Comments1':
        bot.sendMessage(chat_id, str("Emre- we talk about ai, and ai is the revolution and revolution is not avoidable, you can't stop changing. if we able to stop , we couldn't talk from here, neither phone or anything. Technology is not stopable!- Emre"))


    elif command == 'Comments2':
        bot.sendMessage(chat_id, str("Haitian Trader- rasad imagines a future where Alexa can hold human-like conversations, chatting about topics like movies, news, and sports, and answering questions about the details that humans care about — not just the questions machines can answer. It’s the difference between asking “Who won the NBA finals?” and “How did LeBron James do last night?” A more talkative Alexa would become more personable, which is an entity users could relate to “as a friend, as a companion,” says Prasad. @not_un -Haitian Trader"))



    elif command == 'Oligopoly':
        bot.sendMessage(chat_id, str("Ben Goertzel- Today we face an AI oligopoly, where data and frameworks are largely owned by a handful of corporations. With DAIA, we aim to leverage blockchain and related technologies to create a democratically-governed AI community that will benefit the broader society, rather than a few powerful companies -Ben Goertzel"))


    #elif command == '':
        #bot.sendMessage(chat_id, str(""))


#Comments
#Comments
#Comments-------------------------------------------------------------------------------------


#Youtubelinks---------------------------------------------------------------------------------
#Youtubelinks
#Youtubelinks

    #elif command == 'Lecture':
    #    bot.sendMessage(chat_id, str("https://youtu.be/KoEL_4KGvtg"))



    #elif command == 'lecture':
    #    bot.sendMessage(chat_id, str("https://youtu.be/KoEt_4KGvtgg"))


    elif command == 'Rise':
        bot.sendMessage(chat_id, str("https://youtu.be/Dk7h22mRYHQ"))


    elif command == 'Nasdaq':
        bot.sendMessage(chat_id, str("https://youtu.be/VWPM4mqL0z8"))


    elif command == 'CNBC':
        bot.sendMessage(chat_id, str("https://youtu.be/7fnCQC7bLs0"))


    elif command == 'Telepathy':
        bot.sendMessage(chat_id, str("https://youtu.be/6Tp79rv2Keg"))

    elif command == 'BEF':
        bot.sendMessage(chat_id, str("https://youtu.be/HUPvUfgNJkE"))


    elif command == 'Youtube community':
        bot.sendMessage(chat_id, str("https://www.youtube.com/channel/UCxf7KLrbusMC6-NQEGgLwSw"))

    #elif command == '':
        #bot.sendMessage(chat_id, str(""))


#Youtubelinks
#Youtubelinks
#Youtubelinks---------------------------------------------------------------------------------



#altvrlinks-----------------------------------------------------------------------------------
#altvrlinks
#altvrlinks
        

    elif command == 'meetup':
       bot.sendMessage(chat_id, str("https://account.altvr.com/events/965383221179056837"))


    elif command == 'Meetup':
       bot.sendMessage(chat_id, str("https://account.altvr.com/events/965383221179056837")) 


    #Text Tim

        
    elif command == 'reminder':
        bot.sendMessage(chat_id, str("Reminder!!!          Second Virtual Reality Event in AltspaceVR, where I delivered the first part of a four part lecture, centred on Human advancements using technology from the dawn of man through to the Singularity and Beyond.          The next event where we will focus on how do we get to the Singularity from here?, which is scheduled to occur on Monday the 18th of June at 19:00 UTC          Please feel free to DM me and I can help you.https://t.me/joinchat/Gops-UtKqHNEYBMbStVBzg"))


    elif command == 'Reminder':
        bot.sendMessage(chat_id, str("Reminder!!!          Second Virtual Reality Event in AltspaceVR, where I delivered the first part of a four part lecture, centred on Human advancements using technology from the dawn of man through to the Singularity and Beyond.          The next event where we will focus on how do we get to the Singularity from here?, which is scheduled to occur on Monday the 18th of June at 19:00 UTC          Please feel free to DM me and I can help you.https://t.me/joinchat/Gops-UtKqHNEYBMbStVBzg"))


    elif command == 'stake':
       bot.sendMessage(chat_id, str("You can stake your AGI against an ai agent responsible for a service to increase its reputation.               This will generate a bonus depending on the use and success of the agent.           The bonus earned diminishes the more AGI are staked.            AGI that are staked are locked and so if they do not generate a bonus you will forfeit them.            The bonus earned diminishes the more AGI staked against that AI agent."))


    elif command == 'Telegram keywords':
       bot.sendMessage(chat_id, str("Hi; I am fine; Germany; Spain; Russia; Holland; Dutch; China; Portugal; France; Deutschland; Japan; Korea; Website; Main; Ofc; Announcement; News; Dev; Philosophy; Reddit; Twitter; Whitepaper; Medium; Forum; FAQ; Steemit; Aigents; Social; Sophia; Face; Face recognition; Decentralized; Virtual; Vr; Ar; Price; Truth; Numbers; Google trends; Trend; Datasheets; DAIA; Generative Twitter; Generative; Digital kitties; Concern; DBC; Latest; Comment; Vitalik; Comments1; Comments2; Oligopoly; Rise; Nasdaq; CNBC; Telepathy; BEF; Meetup; Reminder; stake; Latoken; Event; Deepbrainchain website; DBC website; OceanProtocol news; OceanProtocol; Fundrequest; Hacken; Bitspace; Bitdegree; Bitdegree news; Botcontrol; Usecases; Filthy; send the xyz; Telegram keywords"))


    #Text Tim 

  
#altvrlinks
#altvrlinks
#altvrlinks-----------------------------------------------------------------------------------  
    

#Events---------------------------------------------------------------------------------------
#Events
#Events
       
       
    elif command == 'Latoken':
        bot.sendMessage(chat_id, str("http://bef.latoken.com/"))
     

    elif command == 'Event':                                                                            #jpg Event send
        bot.sendPhoto(chat_id, photo=open('/home/pi/Pictures/Sophia17.06SanFrancisco.jpg'))


    elif command == 'Events':                                                                           #jpg Events send
        bot.sendPhoto(chat_id, photo=open('/home/pi/Pictures/Sophia17.06SanFrancisco.jpg'))


    elif command == 'event':                                                                            #jpg event send
        bot.sendPhoto(chat_id, photo=open('/home/pi/Pictures/Sophia17.06SanFrancisco.jpg'))


    elif command == 'events':                                                                           #jpg events send
        bot.sendPhoto(chat_id, photo=open('/home/pi/Pictures/Sophia17.06SanFrancisco.jpg'))


#various-------------------------------------------------------------------------------------
#various Documents + resources
#various

        
    elif command == 'Filthy':
        bot.sendPhoto(chat_id, photo=open('/home/pi/Pictures/Filthy.jpg'))

        
    #various


    #elif command == 'send the ***png.':
    #    bot.sendPhoto(chat_id, photo=open('/home/pi/Pictures/***.png'))


    #elif command == 'send the code':                                                
        #bot.sendDocument(chat_id, document=open('/home/pi/Documents/***.py'))


    #Documents


    elif command == 'send the xyz' :                                           
        bot.sendDocument(chat_id, document=open('/home/pi/Documents/keywords/keywords 18.06.2018.odt'))


    #Documents


    #elif command == 'send the LibroOOp' :                                           
    #    bot.sendAudio(chat_id, audio=open('/home/pi/Music/***.mp3'))

    
#various
#various Documents + resources
#various-------------------------------------------------------------------------------------


#Token AGI community bot

bot = telepot.Bot('XXX')                  

MessageLoop(bot, handle).run_as_thread()
print ('I am Listening...')


 
    
