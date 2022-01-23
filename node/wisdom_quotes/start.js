"use strict";
const messages = [
    "All of the great geniuses of the world were inspired and driven by their desire to enrich the lives of others.",
    "If you wish success in life, make perseverance your bosom friend, experience your wise counselor, caution your elder brother and hope your guardian genius.",
    "We all have genius within us, never doubt that fact.",
    "Anyone who seems to experience a heightened attention to detail can be encouraged to channel that ability to create their own highly successful outcomes and to exhibit their own sparks of genius.",
    "Genius I met the other day\
    He looked at me and walked away\
    What did he see, thought I with frown,\
    Fellow genius or happy clown?",
    "When defining genius, it's also important to realize this is a status that is never fully reached. Instead, it is something to aspire to.",
    "Although genius always commands admiration, character most secures respect. The former is more the product of brain-power, the latter of heart-power; and in the long run it is the heart that rules in life.",
    "I don't want to be a genius-I have enough problems just trying to be a man.",
    "You might not need to be a money genius to raise one, but there's no need to rub your bad money habits in your kid's face.",
    "That is the true genius of America, a faith in the simple dreams of its people; the insistence on small miracles.",
    "An average person with average talents and ambition and average education, can outstrip the most brilliant genius in our society, if that person has clear, focused goals.",
    "Genius is talent set on fire by courage."
];
const randomPosition = Math.floor(Math.random() * messages.length);
const randomMessage = messages[randomPosition];
console.log(randomMessage);
