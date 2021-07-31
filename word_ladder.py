import collections
import copy

class WordLadderSolve:             #class to generate the word ladder and solve the problem
    def __init__(self, start):
        self.ladder = [[start]]    #the word from which we are going to start the wordLadder

    def AddWord(self, word):       #We use this to append the possible adjacent words
        for item in self.ladder:
            item.append(word)      #append the word to the item of the class

    def LastWord(self):            #We use this because we need to secure that
        return self.ladder[0][-1]  #the last word is the same is all lists in self.ladder

    def FinalLadder(self):          #This will return the final complete ladder
        return self.ladder

    def MergeLadders(self, other):   #We use this to merge two ladders
        self.ladder += other.ladder


def PossibleAdjacents(word, dict):  # The arguments are the given word and the dictionary
  for i in range (len(word)):
      for j in range(ord('a'), ord('z') + 1):                     # we will have only words with lower
          new_word = "".join((word[:i], chr(j), word[i + 1:]))    #case letters, as the file also has
          if new_word in dict and new_word != word:               #only words with lower case letters
              yield new_word


def BFS(start, end, dictionary):  #The arguments are the starting word, the destination word and the given dictionary.
    start = start.lower()         #as we stated above we want lowercase words
    end = end.lower()

    if start == end:
        return "The starting word and the destination word are the same."
    if len(start) != len(end):
        return "The starting word and the destination word do no have the same length."

    wordList = set(dictionary)
    if start not in wordList:
        return "The starting word is not a valid word in the dictionary."
    if end not in wordList:
        return "The destination word is not a valid word in the dictionary."
    explored = {start}
    # That queue contains items that are lists of the WordLaddersSolve class
    queue = collections.deque([WordLadderSolve(start)])
    path = None                            # this will contain the path of WordLadder
    while queue:                           # while the queue is not empty
        #We are going to return all of the shortest paths. Therefore we ned to repeat
        #the same process for every level (number of queue items)
        num_level = len(queue)
        explored_level = {}  # explored words in this level
        for i in range(num_level):  # go through all in this range.
            queue_element = queue.popleft()
            for node in PossibleAdjacents(queue_element.LastWord(), wordList):
                if node in explored:                        # if it has been explored, continue with the next
                    continue
                new_ladder = copy.deepcopy(queue_element)   #copy the element to the new_ladder
                new_ladder.AddWord(node)                    #add it to the new_ladder
                if node == end:
                    if path:                                #if that path is not None merge the ladders
                        path.MergeLadders(new_ladder)
                    else:
                        path = new_ladder                   #else put the path equal to the new_ladder
                elif node in explored_level:                # check if the word has been explored
                    explored_level[node].MergeLadders(new_ladder)      #merge the ladders
                else:
                    explored_level[node] = new_ladder
                    queue.append(new_ladder)
        if path:                                                       #if the path is not None
            break
        explored |= explored_level.keys()                              #union of explored with explored_level.keys
    if path:
        return path.FinalLadder()

    else:
        return "There is not any path to go from the starting word to the destination word."



if __name__ == '__main__':
    wordsfile = open('wordlist.txt', 'r')
    WordsDictionary = [word for word in wordsfile.read().splitlines()]

    #Now lets try our code with different examples
    print(BFS("milk", "wine", WordsDictionary))
    print()
    print(BFS("door", "lock", WordsDictionary))
    print()
    print(BFS("head", "tail", WordsDictionary))
    print()
    print(BFS("cat", "dog", WordsDictionary))
    print()

    #Examples of errors:
    print(BFS("joke", "happiness", WordsDictionary))            #The words are not of the same length.
    print()
    print(BFS("asseverating", "longitudinal", WordsDictionary)) #There is no path that connects these words.
    print()
    print(BFS("hrgaar", "turtle", WordsDictionary))             #The starting word is not a valid word from the dictionary.
    print()
    print(BFS("magazine", "magazine", WordsDictionary))         #The start and end words are the same.
    print()
    #Time to ask the user for input of start word and end word:
    print("Lets play the Word Ladders Game!")
    start = input("Please give the start word: ")
    end = input("Please give the destination word: ")
    print("We can reach the end word as follows:")
    print(BFS(start, end, WordsDictionary))

