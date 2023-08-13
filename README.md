# Eth_Munich_2023
Is it possible to keep track of a specific public key whenever and wherever it had participated/applied in an event? :O
A real person can have many public keys, not only one.
Does this mean that tracking a public key behaviour, achivements, fines, ghosting in events is useless?
The fact that whenever a specific public key is blacklisted and can not participate in a specific activity, does that mean that the person behind that public key will be also blacklisted? or this person can easily create a new one and with that escape the sanctions.
Is there a way to force a person to have one and only public key? :{
Technically it is not possible. Its like creating a social media account, it has no real limit number.
But when a person really finds himself attached to a specific public key, so, even if he is sancionned from doing something he will still use the same address?
in social media that happens if the person has a huge ammount of follwers(income, fame) or if he has a lot of publications and memories that he/she/.. can not afford to lose.
information such as:
a public key attented an event, participated with a project, wins, loses, did something valuable, or cheated can really affect the decision of accepting this person in the next events or no.
I honnestly think that all these challenges can not be solved in a hackaton. That's why i will try to keep this as simple as possible.

*****Project Description*****

This is a web app that give to any event creator the chance to track and manage the state of the people that registred, were accepted to participate, attended the event, submitted a project or no.
And maybe accept to share their data with other event organizers that are planning to use this platform so they have more insghts about who to accept and who to reject.
So, i am trying to put my ideas together.
The blacklisting/whitelisting process will be done using molecule protocole. Why?
Simply because, every event after it finished, after their approval we ask them to create a blacklist and a whitelist of the participants of that specific event. And then we create a MoleculeLogic.sol for that specific event.
Whenever a new event is being organised, we provide this event organisers these MoleculeLogic.sol contracts and then they can decide which logic ids to choose when creating an nft for tha person that was accepted to attend that event. 
As an example:
a football match event happend when some fans invaded the pitch, the orgonizer blacklisted these persons,
this information can be valueble for another football match organizer however, its not valuable at all for a concert organizer.  

I highly recoomand adding event type field to the event form.
regarding the type of event we can use chainlink to give the event owner more information about the molecule logics that are related to his type of event so he can have more insights about which guests to accept regarding their public key.