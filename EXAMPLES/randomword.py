#
import random

class RandomWord():
    def __init__(self):
        with open('../DATA/words.txt') as words_in:
            self._word_list = [w.rstrip() for w in words_in]


    def __call__(self):
        """
        Return one random word when the instance is called

        :return: A random word as a string.
        """
        return random.choice(self._word_list)


    def random_words(self, num_words=1):
        """
        Get list of random words.

        :param num_words: Number of words to return (default 1)
        :return: List of words as strings.
        """
        return random.choices(self._word_list, k=num_words)

if __name__ == '__main__':
    w = RandomWord()
    for _ in range(10):
        print(w())
    
    print()
    print(w.random_words()) 
    print(w.random_words(8))
