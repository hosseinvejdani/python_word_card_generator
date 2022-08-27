import random
from itertools import product

# this is python word card generator

def generate_all_combinations(words:list):
   result = product(words, repeat=len(words)) # You can change the repeat more then n length
   result = [list(l) for l in result if len(set(l))==len(words)]
   return result

def generate_word_id(words:list):
   return '-'.join(words)

# words repository
words_repo = ["house",
"picture",
"try",
"us",
"again",
"animal",
"point",
"mother",
"world",
"near",
"build",
"self",
"earth",
"father",
"head",
"stand",
"own",
"page",
"should",
"country",
"found",
"answer",
"school",
"grow",
"study",
"still",
"learn",
"plant",
"cover",
"food",
"sun"]

SIZE = 3

# select SIZE number words randomly
words = random.choices(population=words_repo,k=SIZE)

print(words)

# generate all possible combination with words

words_groups = generate_all_combinations(words) 

print(words_groups)

cards = {}

for words in words_groups:
   cards[generate_word_id(words)] = {"words":words}

print(cards)




