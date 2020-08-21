class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d1 = defaultdict(list)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.d1[len(word)].append(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        
        blanks = 0
        for i in word:
            if i=='.':
                blanks += 1

        
        if word in self.d1[len(word)]:
            return True
        elif word not in self.d1[len(word)] and blanks==0:
            return False
        else:
            for w in self.d1[len(word)]:
                match = 0
                for i in range(len(w)):
                    if word[i] == '.':
                        continue
                    if w[i]==word[i]:
                        match += 1
                if match ==len(word)-blanks:
                    return True
        return False
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
