from datetime import datetime


class SentenceReadingAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, sentence, question):
        start = datetime.now()
        #Add your code here! Your solve method should receive
	#two strings as input: sentence and question. It should
	#return a string representing the answer to the question.
        pos = {'serena': 'PROPN',
               'andrew': 'PROPN',
               'bobbie': 'PROPN',
               'cason': 'PROPN',
               'david': 'PROPN',
               'farzana': 'PROPN',
               'frank': 'PROPN',
               'hannah': 'PROPN',
               'ida': 'PROPN',
               'irene': 'PROPN',
               'jim': 'PROPN',
               'jose': 'PROPN',
               'keith': 'PROPN',
               'laura': 'PROPN',
               'lucy': 'PROPN',
               'meredith': 'PROPN',
               'nick': 'PROPN',
               'ada': 'PROPN',
               'yeeling': 'PROPN',
               'yan': 'PROPN',
               'the': 'DET',
               'of': 'ADP',
               'to': 'PART',
               'and': 'CCONJ',
               'a': 'DET',
               'in': 'ADP',
               'is': 'AUX',
               'it': 'PRON',
               'you': 'PRON',
               'that': 'PRON',
               'he': 'PRON',
               'was': 'AUX',
               'for': 'ADP',
               'on': 'ADP',
               'are': 'AUX',
               'with': 'ADP',
               'as': 'ADP',
               'I': 'PRON',
               'his': 'PRON',
               'they': 'PRON',
               'be': 'AUX',
               'at': 'ADP',
               'one': 'NUM',
               'have': 'VERB',
               'this': 'PRON',
               'from': 'ADP',
               'or': 'CCONJ',
               'had': 'VERB',
               'by': 'ADP',
               'hot': 'ADJ',
               'but': 'CCONJ',
               'some': 'PRON',
               'what': 'PRON',
               'there': 'ADV',
               'we': 'PRON',
               'can': 'AUX',
               'out': 'ADP',
               'other': 'ADJ',
               'were': 'AUX',
               'all': 'PRON',
               'your': 'PRON',
               'when': 'SCONJ',
               'up': 'ADP',
               'use': 'VERB',
               'word': 'NOUN',
               'how': 'SCONJ',
               'said': 'VERB',
               'an': 'PRON',
               'each': 'PRON',
               'she': 'PRON',
               'which': 'PRON',
               'do': 'VERB',
               'their': 'PRON',
               'time': 'NOUN',
               'if': 'SCONJ',
               'will': 'AUX',
               'way': 'NOUN',
               'about': 'ADP',
               'many': 'ADJ',
               'then': 'ADV',
               'them': 'PRON',
               'would': 'AUX',
               'write': 'VERB',
               'like': 'ADP',
               'so': 'ADV',
               'these': 'PRON',
               'her': 'PRON',
               'long': 'ADV',
               'make': 'VERB',
               'thing': 'NOUN',
               'see': 'VERB',
               'him': 'PRON',
               'two': 'NUM',
               'has': 'VERB',
               'look': 'VERB',
               'more': 'ADJ',
               'day': 'TIME',
               'could': 'AUX',
               'go': 'VERB',
               'come': 'VERB',
               'did': 'VERB',
               'my': 'PRON',
               'sound': 'NOUN',
               'no': 'PRON',
               'most': 'ADJ',
               'number': 'NOUN',
               'who': 'PRON',
               'over': 'ADP',
               'know': 'VERB',
               'water': 'NOUN',
               'than': 'ADP',
               'call': 'VERB',
               'first': 'ADV',
               'people': 'NOUN',
               'may': 'AUX',
               'down': 'ADV',
               'side': 'NOUN',
               'been': 'AUX',
               'now': 'ADV',
               'find': 'VERB',
               'any': 'PRON',
               'new': 'ADJ',
               'work': 'NOUN',
               'part': 'NOUN',
               'take': 'VERB',
               'get': 'VERB',
               'place': 'NOUN',
               'made': 'VERB',
               'live': 'VERB',
               'where': 'SCONJ',
               'after': 'ADP',
               'back': 'ADV',
               'little': 'ADJ',
               'only': 'ADV',
               'round': 'ADV',
               'man': 'NOUN',
               'year': 'NOUN',
               'came': 'VERB',
               'show': 'VERB',
               'every': 'PRON',
               'good': 'ADJ',
               'me': 'PRON',
               'give': 'VERB',
               'our': 'PRON',
               'under': 'ADP',
               'name': 'NOUN',
               'very': 'ADV',
               'through': 'ADP',
               'just': 'ADV',
               'form': 'NOUN',
               'much': 'ADJ',
               'great': 'ADJ',
               'think': 'VERB',
               'say': 'VERB',
               'help': 'VERB',
               'low': 'ADJ',
               'line': 'NOUN',
               'before': 'ADP',
               'turn': 'VERB',
               'cause': 'VERB',
               'same': 'ADJ',
               'mean': 'VERB',
               'differ': 'VERB',
               'move': 'VERB',
               'right': 'ADV',
               'boy': 'INTJ',
               'old': 'ADJ',
               'too': 'ADV',
               'does': 'VERB',
               'tell': 'VERB',
               'sentence': 'NOUN',
               'set': 'VERB',
               'three': 'NUM',
               'want': 'VERB',
               'air': 'NOUN',
               'well': 'INTJ',
               'also': 'ADV',
               'play': 'VERB',
               'small': 'ADJ',
               'end': 'NOUN',
               'put': 'VERB',
               'home': 'NOUN',
               'read': 'VERB',
               'hand': 'NOUN',
               'port': 'NOUN',
               'large': 'ADJ',
               'spell': 'VERB',
               'add': 'VERB',
               'even': 'ADV',
               'land': 'NOUN',
               'here': 'ADV',
               'must': 'AUX',
               'big': 'ADJ',
               'high': 'ADJ',
               'such': 'ADJ',
               'follow': 'VERB',
               'act': 'VERB',
               'why': 'SCONJ',
               'ask': 'VERB',
               'men': 'NOUN',
               'change': 'VERB',
               'went': 'VERB',
               'light': 'ADJ',
               'kind': 'ADV',
               'off': 'ADP',
               'need': 'VERB',
               'house': 'NOUN',
               'picture': 'NOUN',
               'try': 'VERB',
               'us': 'PRON',
               'again': 'ADV',
               'animal': 'NOUN',
               'point': 'NOUN',
               'mother': 'NOUN',
               'world': 'NOUN',
               'near': 'ADV',
               'build': 'VERB',
               'self': 'NOUN',
               'earth': 'NOUN',
               'father': 'NOUN',
               'head': 'NOUN',
               'stand': 'VERB',
               'own': 'ADJ',
               'page': 'NOUN',
               'should': 'AUX',
               'country': 'NOUN',
               'found': 'VERB',
               'answer': 'VERB',
               'school': 'NOUN',
               'grow': 'VERB',
               'study': 'VERB',
               'still': 'ADV',
               'learn': 'VERB',
               'plant': 'NOUN',
               'cover': 'VERB',
               'food': 'NOUN',
               'sun': 'NOUN',
               'four': 'NUM',
               'thought': 'VERB',
               'let': 'VERB',
               'keep': 'VERB',
               'eye': 'NOUN',
               'never': 'ADV',
               'last': 'ADJ',
               'door': 'NOUN',
               'between': 'ADP',
               'city': 'NOUN',
               'tree': 'NOUN',
               'cross': 'ADJ',
               'since': 'SCONJ',
               'hard': 'ADV',
               'start': 'VERB',
               'might': 'AUX',
               'story': 'NOUN',
               'saw': 'VERB',
               'far': 'ADV',
               'sea': 'NOUN',
               'draw': 'VERB',
               'left': 'VERB',
               'late': 'ADV',
               'run': 'VERB',
               "don't": 'PROPN',
               'while': 'SCONJ',
               'press': 'NOUN',
               'close': 'ADV',
               'night': 'TIME',
               'real': 'ADJ',
               'life': 'NOUN',
               'few': 'ADJ',
               'stop': 'VERB',
               'open': 'ADJ',
               'seem': 'VERB',
               'together': 'ADV',
               'next': 'ADJ',
               'white': 'ADJ',
               'children': 'NOUN',
               'begin': 'VERB',
               'got': 'VERB',
               'walk': 'VERB',
               'example': 'NOUN',
               'ease': 'NOUN',
               'paper': 'NOUN',
               'often': 'ADV',
               'always': 'ADV',
               'music': 'NOUN',
               'those': 'PRON',
               'both': 'PRON',
               'mark': 'NOUN',
               'book': 'NOUN',
               'letter': 'NOUN',
               'until': 'ADP',
               'mile': 'NOUN',
               'river': 'NOUN',
               'car': 'NOUN',
               'feet': 'NOUN',
               'care': 'NOUN',
               'second': 'ADV',
               'group': 'NOUN',
               'carry': 'VERB',
               'took': 'VERB',
               'rain': 'NOUN',
               'eat': 'VERB',
               'room': 'NOUN',
               'friend': 'NOUN',
               'began': 'VERB',
               'idea': 'NOUN',
               'fish': 'NOUN',
               'mountain': 'NOUN',
               'north': 'NOUN',
               'once': 'ADV',
               'base': 'NOUN',
               'hear': 'VERB',
               'horse': 'NOUN',
               'cut': 'VERB',
               'sure': 'ADJ',
               'watch': 'VERB',
               'color': 'NOUN',
               'face': 'NOUN',
               'wood': 'NOUN',
               'main': 'ADJ',
               'enough': 'ADV',
               'plain': 'ADV',
               'girl': 'NOUN',
               'usual': 'ADJ',
               'young': 'ADJ',
               'ready': 'ADJ',
               'above': 'ADV',
               'ever': 'ADV',
               'Red': 'PROPN',
               'red': 'ADJ',
               'list': 'NOUN',
               'though': 'SCONJ',
               'feel': 'VERB',
               'talk': 'VERB',
               'bird': 'NOUN',
               'soon': 'TIME',
               'body': 'NOUN',
               'dog': 'NOUN',
               'family': 'NOUN',
               'direct': 'ADJ',
               'pose': 'VERB',
               'leave': 'VERB',
               'song': 'NOUN',
               'measure': 'NOUN',
               'state': 'NOUN',
               'product': 'NOUN',
               'black': 'ADJ',
               'short': 'ADJ',
               'numeral': 'ADJ',
               'class': 'NOUN',
               'wind': 'NOUN',
               'question': 'NOUN',
               'happen': 'VERB',
               'complete': 'ADJ',
               'ship': 'NOUN',
               'area': 'NOUN',
               'half': 'NOUN',
               'rock': 'NOUN',
               'order': 'NOUN',
               'fire': 'NOUN',
               'south': 'NOUN',
               'problem': 'NOUN',
               'piece': 'NOUN',
               'told': 'VERB',
               'knew': 'VERB',
               'pass': 'VERB',
               'farm': 'NOUN',
               'top': 'ADJ',
               'whole': 'ADJ',
               'king': 'NOUN',
               'size': 'NOUN',
               'heard': 'VERB',
               'best': 'ADV',
               'hour': 'NOUN',
               'better': 'ADV',
               'true': 'ADJ',
               'during': 'ADP',
               'hundred': 'NUM',
               'am': 'AUX',
               'remember': 'VERB',
               'step': 'NOUN',
               'early': 'ADV',
               'hold': 'VERB',
               'west': 'NOUN',
               'ground': 'NOUN',
               'interest': 'NOUN',
               'reach': 'VERB',
               'fast': 'ADV',
               'five': 'NUM',
               'sing': 'VERB',
               'listen': 'VERB',
               'six': 'NUM',
               'table': 'NOUN',
               'travel': 'NOUN',
               'less': 'ADJ',
               'morning': 'TIME',
               'ten': 'NUM',
               'simple': 'ADJ',
               'several': 'ADJ',
               'vowel': 'NOUN',
               'toward': 'ADP',
               'war': 'NOUN',
               'lay': 'VERB',
               'against': 'ADP',
               'pattern': 'NOUN',
               'slow': 'ADJ',
               'center': 'NOUN',
               'love': 'NOUN',
               'person': 'NOUN',
               'money': 'NOUN',
               'serve': 'VERB',
               'appear': 'VERB',
               'road': 'NOUN',
               'map': 'VERB',
               'science': 'NOUN',
               'rule': 'NOUN',
               'govern': 'ADJ',
               'pull': 'VERB',
               'cold': 'ADJ',
               'notice': 'NOUN',
               'voice': 'NOUN',
               'fall': 'VERB',
               'power': 'NOUN',
               'town': 'NOUN',
               'fine': 'ADJ',
               'certain': 'ADJ',
               'fly': 'VERB',
               'unit': 'NOUN',
               'lead': 'VERB',
               'cry': 'VERB',
               'dark': 'ADJ',
               'machine': 'NOUN',
               'note': 'NOUN',
               'wait': 'VERB',
               'plan': 'VERB',
               'figure': 'NOUN',
               'star': 'NOUN',
               'box': 'NOUN',
               'noun': 'NOUN',
               'field': 'NOUN',
               'rest': 'NOUN',
               'correct': 'ADJ',
               'able': 'ADJ',
               'pound': 'NOUN',
               'done': 'VERB',
               'beauty': 'NOUN',
               'drive': 'VERB',
               'stood': 'VERB',
               'contain': 'VERB',
               'front': 'NOUN',
               'teach': 'VERB',
               'week': 'NOUN',
               'final': 'ADJ',
               'gave': 'VERB',
               'green': 'ADJ',
               'oh': 'INTJ',
               'quick': 'ADJ',
               'develop': 'VERB',
               'sleep': 'VERB',
               'warm': 'ADJ',
               'free': 'ADJ',
               'minute': 'NOUN',
               'strong': 'ADJ',
               'special': 'ADJ',
               'mind': 'VERB',
               'behind': 'ADV',
               'clear': 'ADJ',
               'tail': 'NOUN',
               'produce': 'VERB',
               'fact': 'NOUN',
               'street': 'NOUN',
               'inch': 'NOUN',
               'lot': 'NOUN',
               'nothing': 'PRON',
               'course': 'NOUN',
               'stay': 'VERB',
               'wheel': 'NOUN',
               'full': 'ADJ',
               'force': 'NOUN',
               'blue': 'ADJ',
               'object': 'NOUN',
               'decide': 'VERB',
               'surface': 'NOUN',
               'deep': 'ADJ',
               'moon': 'NOUN',
               'island': 'NOUN',
               'foot': 'NOUN',
               'yet': 'ADV',
               'busy': 'ADJ',
               'test': 'VERB',
               'record': 'NOUN',
               'boat': 'NOUN',
               'common': 'ADJ',
               'gold': 'NOUN',
               'possible': 'ADJ',
               'plane': 'NOUN',
               'age': 'NOUN',
               'dry': 'ADJ',
               'wonder': 'VERB',
               'laugh': 'VERB',
               'thousand': 'NUM',
               'ago': 'ADV',
               'ran': 'VERB',
               'check': 'VERB',
               'game': 'NOUN',
               'shape': 'NOUN',
               'yes': 'INTJ',
               'cool': 'ADJ',
               'miss': 'VERB',
               'brought': 'VERB',
               'heat': 'NOUN',
               'snow': 'NOUN',
               'bed': 'NOUN',
               'bring': 'VERB',
               'sit': 'VERB',
               'perhaps': 'ADV',
               'fill': 'VERB',
               'east': 'NOUN',
               'weight': 'NOUN',
               'language': 'NOUN',
               'among': 'ADP',
               'adults': 'NOUN',
               'wrote': 'VERB',
               'sings': 'NOUN',
               "dog's": 'PROPN',
               'written': 'VERB'}

        sentence = sentence.split()
        sentence = [s.replace('.', '') for s in sentence]
        question = question.split()
        question = [q.replace('?', '') for q in question]

        if ("What" and "color") in question:
            possible = []
            if question[-1] == "do":
                for word in sentence:
                    if ':' not in word and word not in question and pos[word.lower()] in ['VERB']:
                        possible.append(word)
                print(possible)
                for word in possible:
                    if pos[word.lower()] == 'VERB':
                        print(datetime.now() - start)
                        return word
            for word in sentence:
                if ':' not in word and word not in question and pos[word.lower()] in ['ADJ']:
                    possible.append(word)
            for word in possible:
                if sentence.index(word) - sentence.index(question[-1]) in range(-2, 3):
                    print(datetime.now() - start)
                    return word

        if ("How" and "far") in question:
            possible = []
            for word in sentence:
                if ':' not in word and word not in question and pos[word.lower()] in ['NOUN']:
                    possible.append(word)
            for word in possible:
                if sentence.index(word) - sentence.index(question[-1]) in range(-3, 3):
                    print(datetime.now() - start)
                    return word

        if ("How" and "many") in question:
            possible = []
            for word in sentence:
                if ':' not in word and word not in question and pos[word.lower()] in ['NUM']:
                    possible.append(word)
            for word in possible:
                if pos[word.lower()] in ['NUM']:
                    print(datetime.now() - start)
                    return word

        # Who
        if "Who" in question or ("What" and "name") in question:
            possible = []
            for word in sentence:
                if ':' not in word and word not in question and pos[word.lower()] in ['NOUN', 'PROPN', 'PRON']:
                    possible.append(word)
            for word in possible:
                if pos[word.lower()] in ['NOUN', 'PROPN']:
                    print(datetime.now() - start)
                    return word
            for word in possible:
                if pos[word.lower()] == 'PRON':
                    print(datetime.now() - start)
                    return word

        # What
        if "Where" in question:
            possible = []
            for word in sentence:
                if ':' not in word and word not in question and pos[word.lower()] in ['NOUN']:
                    possible.append(word)
            for word in possible:
                if 'go' in sentence and sentence.index(word) > sentence.index('go'):
                    print(datetime.now() - start)
                    return word
            for word in possible:
                if pos[word.lower()] == 'NOUN':
                    print(datetime.now() - start)
                    return word

        # When
        if "When" in question or 'time' in question:
            for word in sentence:
                if ':' in word:
                    print(datetime.now() - start)
                    return word
            for word in sentence:
                if pos[word.lower()] == 'TIME':
                    print(datetime.now() - start)
                    return word

        # Where
        if "What" in question:
            possible = []
            if question[-1] == "do":
                for word in sentence:
                    if ':' not in word and word not in question and pos[word.lower()] in ['VERB']:
                        possible.append(word)
                print(possible)
                for word in possible:
                    if pos[word.lower()] == 'VERB':
                        print(datetime.now() - start)
                        return word
            for word in sentence:
                if ':' not in word and word not in question and pos[word.lower()] in ['NOUN']:
                    possible.append(word)
            print(possible)
            for word in possible:
                if pos[word.lower()] == 'NOUN':
                    print(datetime.now() - start)
                    return word

        # How
        if "How" in question:
            possible = []
            if 'do' in question:
                for word in sentence:
                    if ':' not in word and word not in question and pos[word.lower()] in ['VERB']:
                        possible.append(word)
                print(possible)
                for word in possible:
                    if pos[word.lower()] == 'VERB':
                        print(datetime.now() - start)
                        return word
            for word in sentence:
                if ':' not in word and word not in question and pos[word.lower()] in ['VERB', 'ADJ', 'ADV']:
                    possible.append(word)
            for word in possible:
                if pos[word.lower()] in ['ADJ', 'ADV']:
                    print(datetime.now() - start)
                    return word
