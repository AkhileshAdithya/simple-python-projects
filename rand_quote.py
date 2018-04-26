import random

quotes = [
'"Creativity is discontent translated into arts. -Eric Hoffer"',
' "The music is not in the notes, but in the silence between." ~Wolfgang Amadeus Mozart',
' "Courage is what it takes to stand up and speak; courage is also what it takes to sit down and listen." ~Winston Churchill',
' "If I decide to be an idiot, then I’ll be an idiot on my own accord." ~Johann Sebastian Bach',
' "Not everyone is capable of madness; and of those lucky enough to be capable, not many have the courage for it." ~August Strindberg',
' "People understand contests. You take a bunch of kids throwing rocks at random and people look askance, but if you go and hold a rock-throwing contest - people understand that." Don Murray ',
' "Artificial Intelligence is no match for natural stupidity."  ',
' "Santa Claus has the right idea ... visit people only once a year." ',
' "Only to the extent that we expose ourselves over and over to annihilation can that which is indestructible in us be found." ~ Pema Chodron',
' "The only ones who should kill are those who are prepared to be killed!" - Lelouch Lamperouge ',
' "You cant change the world without getting your hands dirty” - Lelouch Lamperouge ' ,
' "False tears bring pain to others. A false smile brings pain to yourself." - C.C. ',
' "Books are not something that you just read words in. They’re also a tool to adjust your senses.” – Shogo Makishima ' ,
' "A perfect plan doesn’t mean having everything go within expectations. A perfect plan is achieved when it has the plasticity needed to flexibly deal with troubles.” – Shogo Makishima ' ,
' "Charisma has three points. The nature of a hero or prophet, the ability to simply make you feel good when you’re around them, and the intelligence to eloquently talk about all sorts of things," ' ,
' "Theres nothing special about being born. Not a thing. Most of the universe is just death, nothing more. In this universe of ours, the birth of a new life on some corner of our planet is nothing but a tiny, insignificant flash. Death is a normal thing. So why live? " ~ Johann Liebert  ',
]
cont = 1
while cont == 1:
    print(random.choice(quotes))
    print('\n')
    a = int(input("Type 1 to exit || Type 2 for another quote  "))
    if a == 1:
        cont = 0




