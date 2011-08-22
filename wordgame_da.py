
scores = {'a':1, 'b': 3, 'c': 8, 'd': 2, 'e': 1, 'f': 3, 'g': 3,'h': 4,'i': 3,
          'j':4, 'k': 3, 'l': 2, 'm': 4, 'n': 1, 'o': 2, 'p': 4,'r': 1,'s': 2,
          't': 2, 'u': 3, 'v': 4, 'x': 8, 'y': 4, 'z': 9, 'æ': 4, 'ø': 4,'å': 4}
counts = {'a':7, 'b': 4, 'c': 2, 'd': 5, 'e': 9, 'f': 3, 'g': 3,'h': 2,'i': 4,
          'j':2, 'k': 4, 'l': 5, 'm': 3, 'n': 7, 'o': 5, 'p': 2,'r': 7,'s': 6,
          't': 6, 'u': 3, 'v': 3, 'x': 1, 'y': 2, 'z': 1, 'æ': 2, 'ø': 2,'å': 2}
def load_words():
    lines = []
  #file = open("D:\\Dropbox\\development\\Python\\Portable_Python_3.2.0.1\\words-da")
    file = open("/home/tore/Dropbox/development/WordGameHelper/words-da")
    while True:
        line = file.readline()
        line = line.strip()
        if not line:
            break
        if "'" in line:
            continue
        if "é" in line:
            continue
        if int(len(line)) <= 1:
            continue

        if line[0].islower():
            lines.append(line)
        elif line[0].isupper() and line[1].isupper():
            lines.append(line)
        elif line.isupper():
            lines.append(line)
    print("Number of word lines" + str(len(lines)))
    return lines

def print_distribution_info(lines):
    counts = {}
    for word in lines:
        l = len(word)
        if l in counts:
            counts[l] += 1
        else:
            counts[l] = 1
    for k in range(2,35):
        print(str(k) +" :" + str(counts[k]) + " " + str(counts[k]*100/len(lines))[0:4] + "%")

def word_score(word):
    sum = 0
    for letter in word:
        if letter.lower() in scores.keys():
            sum += scores[letter.lower()]
        else:
            sum = -100
    return sum

def group_by_length(lines):
    lengthwords = {}
    for word in lines:
        l = len(word)
        if l in lengthwords:
            lengthwords[l].append(word)
        else:
            lengthwords[l] = []
            lengthwords[l].append(word)
    return lengthwords

#print(lengthwords)
# 4,20
def print_words(length=2,columns=40):
    output_string = ""
    k = length
    curcol = 1
    cols = columns
    lengthwords[k].sort()
    for w in lengthwords[k]:
        if curcol % cols == 0:
            output_string += w + "\n"
        else:
            output_string += w + "\t"
        curcol += 1
    print(output_string)


#print_words(2,17)
#print_words(3,17)
#print_words(4,17)

def print_score_words(word_lists,length=2,columns=40,amount=10):
    scoretuples = []
    output_string = ""
    k = length
    curcol = 1
    cols = columns
    for word in word_lists[k]:
        scoretuples.append((word_score(word),word))
    scoretuples.sort()
    scoretuples.reverse()
    #for w in  scoretuples[0:amount]:
    for w in  scoretuples:
        if curcol % cols == 0:
            output_string += str(w[0]) + ":"+ str(w[1]) + "\n"
        else:
            output_string += str(w[0]) + ":"+ str(w[1]) + "\t"
        curcol += 1
    print(output_string)

def print_score_words2(word_list,length=2,columns=40,amount=10):
    scoretuples = []
    output_string = ""
    curcol = 1
    cols = columns
    pprint()
    for word in word_list:
        scoretuples.append((word_score(word),word))
    scoretuples.sort()
    scoretuples.reverse()
    #for w in  scoretuples[0:amount]:
    for w in  scoretuples:
        if curcol % cols == 0:
            output_string += str(w[0]) + ":"+ str(w[1]) + "\n"
        else:
            output_string += str(w[0]) + ":"+ str(w[1]) + "\t"
        curcol += 1
    print(output_string)


#print_score_words(2,17)
#print_score_words(3,17)
#print_score_words(4,17)
lines = load_words()
#print_distribution_info(lines)
word_lists = group_by_length(lines)

word_length = 7
for i in range(2,word_length + 1):
    print("----------- " + str(i) + "-----------")
    print_score_words(word_lists,i,20,40)

def print_by_letter(lines,letter):
    matching = [s for s in lines if letter in s]
    short = [s for s in matching if len(s) < 8]
    print(short)

def get_word_containing(lines,letter):
    matching = [s for s in lines if letter in s]
    return matching

def print_by_string(letters):
    matching = lines
    for letter in letters:
        matching = [word for word in matching if letter in word]
    matching = [s for s in matching if len(s) < 8]
    print(matching)

def get_list_matching_string(letters):
    matching = lines
    numChars = 10
    for letter in letters:
        matching = [word for word in matching if letter in word]
    matching = [s for s in matching if len(s) < numChars]
    return matching

def get_list_matching_string_and_shorter(letters):
    matching = []
    numChars = 10
    remaingLetters = letters
    while len(remaingLetters) > 0:
        local_matching = lines[:]
        for letter in remaingLetters:
            local_matching = [word for word in local_matching if letter in word]

        remaingLetters = remaingLetters[:-1]
        matching.extend(local_matching)
        matchSet = set(matching)
        matching = list(matchSet)

    matching = [s for s in matching if len(s) < numChars]


    return matching

def pprint(word_list,length=2,columns=40,amount=10):
    output_string = ""
    scoretuples = []
    k = length
    curcol = 1
    cols = columns
    for word in word_list:
        scoretuples.append((word_score(word),word))
    scoretuples.sort()
    scoretuples.reverse()
    for word in scoretuples:
        if curcol % cols == 0:
            output_string += str(word[0]) + ":"+ str(word[1]) + "\n"
        else:
            output_string += str(word[0]) + ":"+ str(word[1]) + "\t"
        curcol += 1
    print(output_string)

#print_by_letter(lines,'z')
#print_by_letter(lines,'c')
#print_by_letter(lines,'x')
print('######')
#mList = get_list_matching_string('katpdl')
mList = get_list_matching_string_and_shorter('aæinnoy')
pprint(mList[:400])

class Player:
  def __init__(num):
    self.number = num
    self.currentLetters = []
    self.totalPoints = 0

class WordFeudGame:
  def __init__(self):
    self.testBoard = Board()
    self.board = Board()
    self.currentPlayer = 1
    self.bagOfLetters = {}


  def changePlayer():
    if self.currentPlayer == 1:
      self.currentPlayer = 2
    else:
      self.currentPlayer = 1

  def getNewTiles(amount = 1):
     return 

class Board:
  def __init__(self):
    self.tiles = []
    self.usedTiles = []

  def checkValidity():
    pass

  def calculatePlacementScore():
    pass

  # output a list of remaining tile to know what to expect.
  def remainingLetterDistribution():
    pass

# algorithm to check validity
#    test the letter sequence against the dictionary.
#     and
#    test each of the orthogonal words created against dictionary (L>1)

# Calculate word score with bonuses
# multiply each letter with its letter multiplier
# add the letter scores and multiply with word multiplier

# algorithm to find highest scoring move
# must be attached to previously played tiles if not the first.
# Must fit board
# can only be formed by the tiles on the line. (7 + additional from board)

# for each line and row append subsets of the strings to make words from dictionary.
# check validity
# get word score and store it as a possible play

# keep the best score 

# algorithm find best move using all available information

# pruning can possibly be done of low scoring words.
