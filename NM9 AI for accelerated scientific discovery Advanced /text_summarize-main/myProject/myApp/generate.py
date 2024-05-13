from django.shortcuts import render
import openai

OPENAI_API_KEY= 'Please Add your OpenAPI keys'
openai.api_key = OPENAI_API_KEY


def generate(data):
    text = data
    prompt = """Sumarize following text for University Student.

    text: It’s the word a when it precedes a word that begins with a consonant. It’s the word an when it precedes a word that begins with a vowel. The indefinite article indicates that a noun refers to a general idea rather than a particular thing. For example, you might ask your friend, “Should I bring a gift to the party?” Your friend will understand that you are not asking about a specific type of gift or a specific item. “I am going to bring an apple pie,” your friend tells you. Again, the indefinite article indicates that she is not talking about a specific apple pie. Your friend probably doesn’t even have any pie yet. The indefinite article only appears with singular nouns. Consider the following examples of indefinite articles used in context
    Summary: The indefinite article takes two forms: a and an. It is used to refer to a general idea rather than a specific thing. The indefinite article only appears with singular nouns.
    text: Aegon life iTerm insurance plan helps customers save tax
    Summary: With Aegon Life iTerm Insurance plan, customers can enjoy tax benefits on your premiums paid and save up to â¹46,800^ on taxes. The plan provides life cover up to the age of 100 years. Also, customers have options to insure against Critical Illnesses, Disability and Accidental Death Benefit Rider with a life cover up to the age of 80 years.
    text:There are times when the night sky glows with bands of color. The bands may
    begin as cloud shapes and then spread into a great arc across the entire sky. They
    may fall in folds like a curtain drawn across the heavens. The lights usually grow
    brighter, then suddenly dim. During this time the sky glows with pale yellow, pink,
    green, violet, blue, and red. These lights are called the Aurora Borealis. Some
    people call them the Northern Lights. Scientists have been watching them for
    hundreds of years. They are not quite sure what causes them. In ancient times people were afraid of the Lights. They imagined that they saw fiery dragons in the
    sky. Some even concluded that the heavens were on fire. 
    Summary:The Aurora Borealis, or Northern Lights, are bands of color in the night sky. Ancient
    people thought that these lights were dragon on fire, and even modern scientists
    are not sure what they are.
    text:Called PM Modi 'sir' 10 times to satisfy his ego: Andhra CM
    Summary:Andhra Pradesh CM N Chandrababu Naidu has said, ""When I met then US President Bill Clinton, I addressed him as Mr Clinton, not as 'sir'. (PM Narendra) Modi is my junior in politics...I addressed him as sir 10 times."" ""I did this...to satisfy his ego in the hope that he will do justice to the state,"" he added.
    text: {}
    Summary:
    Tl;dr""".format(text) 
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, temperature=0, max_tokens=200)
    summarization = response
    # split the string
    # words = summarization.split()
    # # remove first word and join the remaning words
    # summary = " ".join(words[1:])
 
    return summarization

