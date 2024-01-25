'''
Zain Saeed
Jan 21, 2024
CS 211
'''


"""A bag of letters for finding anagrams.
Associates a cardinality (count) with each character
in the bag.
"""

def normalize(phrase: str) -> list[str]:
    """Normalize word or phrase to the
    sequence of letters we will try to match, discarding
    anything else, such as blanks and apostrophes.
    Return as a list of individual letters.
    """
    result = []
    for i in phrase:
        if i.isalpha():
            result.append(i.lower())
    return result
#print(normalize('  fQwfqwf  352532 ,   x'))

class LetterBag:
    """A bag (also known as a multiset) is
    a map from keys to non-negative integers.
    A LetterBag is a bag of single character
    strings.
    """
    def __init__(self, word=""):
        """Create a LetterBag"""
        self.word = word.strip()
        normal = normalize(self.word)
        self.length = len(normal)  # Counts letters only!
        self.letters = {}
        for letter in normal:
            if letter in self.letters:
                self.letters[letter] += 1
            else:
                self.letters[letter] = 1

    
    def __len__(self):
        return self.length

    def __str__(self):
        return self.word

    def __repr__(self):
        counts = [f"{ch}:{n}" for ch, n in self.letters.items() if n > 0]
        return f'LetterBag({self.word}/[{", ".join(counts)}])'



    def contains(self, other: "LetterBag") -> bool:
        """Determine whether enough of each letter in
        other LetterBag are contained in this LetterBag.
        """
        for other_key, other_value in other.letters.items():
            if other_key in self.letters:
                if self.letters[other_key] < other_value:
                    return False
            else:
                return False
        return True
    
    def copy(self) -> "LetterBag":
        """Make a copy before mutating."""
        copy_ = LetterBag()
        copy_.word = self.word
        copy_.letters = self.letters.copy()  # Copied to avoid aliasing
        copy_.length = self.length
        return copy_
    
    def take(self, other: "LetterBag") -> "LetterBag":
        """Return a LetterBag after removing
        the letters in other.  Raises exception
        if any letters are not present.
        """
        bag = self.copy()
        for other_key, other_value in other.letters.items():
            # Check if a value is in the bag
            if other_key in bag.letters:
                bag.letters[other_key] -= other_value
                assert bag.letters[other_key] >= 0
                # since the other_key is in bag, we want to subtract other_value from bag_value
            else:
                raise ValueError("Letter '{other_key}' is not present in the original bag.")
        bag.length = len(bag) - len(other)
        return bag