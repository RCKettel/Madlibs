#Entering a second list of inputs to find out if I can
#create multiple inputs and stories to choose from.

def News_Story():

    TV_host = input(["Please enter your name: "])
    channel = input(["Please enter your favorite TV channel: "])
    noun1 = input(["Please enter a noun: "])
    verb1 = input(["Please enter a verb: "])
    ing_verb1 = input(["Please enter a verb ending in -ing: "])
    polit_party = input(["Please enter a political affiliation: "])
    plur_noun1 = input(["Please enter a plural noun: "])
    forn_country = input(["Please enter the name of a foreign country: "])
    plur_noun2 = input(["Please enter a plural noun: "])
    adjective = input(["Please enter an adjective: "])
    noun2 = input(["Please enter a noun: "])
    noun3 = input(["Please enter a noun: "])
    ing_verb2 = input(["Please enter a verb ending in -ing: "])
    verb2 = input(["Please enter a verb: "])
    corporation = input(["Please enter the name of a corporation: "])
    verb3 = input(["Finally, please enter a verb: "])

    story_2 ={"Good evening.  I'm " +TV_host+ " , and your're watching The \
    Nightly News on " +channel+ ".  There's been a surge in new cases of "
    + noun1 + "flu.  Some say that we should " +verb1+ " businesses, but is it\
    worth it just to prevent a few people from " +ing_verb1+ "? Meanwhile, members\
    of the " +polit_party+ " Party are proposing a bill that they say will prevent \
    people from loosing their " +plur_noun1+ ".  It may seem like something that's\
    in your best interest, but it's exactly what " +forn_country+ " wants.  First, \
    the "+plur_noun2+ " take to social media and try to convice you that everyone\
    -no matter how " +adjective+ " -is entitled to a decent " +noun2+ ".  Then, \
    they'll infiltrate social movements as part of a covert plot to overthrow the \
    " +noun3+ " and take over the country.  Before you know it, they're " +ing_verb2+
    " down your door to " +verb3+ " you and your family.  More on that message after \
    this message from our sponsor, " +corporation+ ".  Theey make money the \
    old-fashioned way-they" +verb3+ " it."}

    print(story_2)
