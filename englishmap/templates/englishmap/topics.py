class topics: 
    def __init__(self, id, name, short, full, links): 
        self.id = id 
        self.name = name
        self.short = short
        self.full = full
        self.links = links
   
# creating list       
list = [
    topics(
        1, 
        'Noun',
        'Dog, apple, cat, house + I, you, he, she, it, we, they',
        "A noun is a word that refers to a thing (book), a person (Betty Crocker), an animal (cat), a place (Omaha), a quality (softness), an idea (justice), or an action (yodeling). It's usually a single word, but not always: cake, shoes, school bus, and time and a half are all nouns.",
        'man.com'
    ), 
    topics(
        2, 
        'Verb',
        'go, eat, dance + be, is, are',
        'Verbs are words that show an action (sing), occurrence (develop), or state of being (exist). Almost every sentence requires a verb. The basic form of a verb is known as its infinitive. The forms call, love, break, and go are all infinitives. Almost all verbs have two other important forms called participles.',
        'manny.com'
    )
    ] 

  
for obj in list:
    print('\n', obj.name, obj.id, obj.short, obj.full, obj.links, sep ='\n' )
    if obj.id == 2:
        fuck = obj
print(fuck.short)




