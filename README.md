# Word_Ladder

The doublets game, also known as, word ladder is a word puzzle game invented by Lewis Carroll.

The game starts with two words, the start and the end word and the aim is to find a chain of words that links the start word to the end word. In each step the adjacent words differ by only one character. All the words in the chain should be valid English dictionary words. You can use a graph to represent the transmission between the words. The vertices in the graph  will be the words and edges will be the valid transition from one dictionary word to another dictionary word that differs by one character.

Example1: the start word: milk and the end word: wine

               Chain: milk -> mink -> wink -> wine

Example2: the start word: door and the end word: lock

               Chain: door -> boor -> book -> look -> lock

Example3: the start word: head and the end word: tail

               Chain: head ->held->hell->tell->tall->tail

See details at https://en.wikipedia.org/wiki/Word_ladder

This Python program implements the doublets game using breadth-first-search to traverse on the tree of words. 


We use the file “wordlist.txt” as a valid English list of words. All the words including, start, end and intermediate words should exist in the file.
 
We may get different intermediate words and as long as each word in every step only differs by one character then our chain of words is accepted.
