from django import template

register = template.Library()

@register.filter(name='Censor')
def Censor(value):
    Banned_List = ['idiot', 'stupid', 'дурак']
    sentence = value.split()
    for i in Banned_List:
        for words in sentence:
            if i in words.lower ():
                pos = sentence.index(words)
                sentence.remove(words)
                sentence.insert(pos, '*' * len(i))
    return " ".join(sentence)