"""Generate markov text from text files."""
import sys
input_file = sys.argv[1]

from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    text = ""
    full_text = open(file_path)

    # read method combines all text to one string
    text = text + full_text.read()

    full_text.close()

    return text


def make_chains(text_string, n_gram):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """
    # n_gram = int(raw_input("Enter number of words for your n-gram: "))
    # while n_gram < 0 or n_gram > 10:
    #     print "Not a valid number. Choose a number between 1 - 10"
    #     n_gram = int(raw_input("Enter number of words for your n-gram: "))

    # dictionary of our bigrams
    chains = {}

    # tokenizes by spaces and returns
    word_list = text_string.split()

    i = 0

    # looping until we get to the third to last words in text
    while i < len(word_list) - n_gram:
        # key = (word_list[i], word_list[i+1])
        # Adding n words to the key to make an n-gram
        j = 0
        key_list = []

        while j < n_gram:
            key_list.append(word_list[i+j])
            j = j + 1

        key = tuple(key_list)
        value = word_list[i+n_gram]

    # checking if key is in chains and appending key if not
    # look into set default method
        if key not in chains: 
            chains[key] = [value]
        else:
            chains[key].append(value)
        i += 1

    return chains


def make_text(chains, n_gram):
    """Returns text from chains."""

    # words is where we accumulate our final string
    words = []

    # chooses a random key
    first_key = choice(chains.keys())
    first_letter = first_key[0][0]

        # Look for a tuple with the first word that is capitalized
    while not first_letter.isupper():
        first_key = choice(chains.keys())
        first_letter = first_key[0][0]

    # creates list of all values from first key
    values = chains[first_key]

    # creates list from tuple
    key_string = list(first_key)

    # adding keys to words using extend because key_string is a list
    words.extend(key_string)

    # choosing a random value from list of values and adding to words
    words.append(choice(values))

    # creating a new key from the last n words of the text string

    new_key_list = []
    new_key_list = words[-n_gram:]
    new_key = tuple(new_key_list)

    # Checking for punctuation mark in key
    has_punc = new_key[n_gram-1][-1] == "?"

    # adding new words until no new key in chains dictionary
    while new_key in chains and not has_punc:

        values = chains[new_key]
        words.append(choice(values))

        new_key_list = words[-n_gram:]
        new_key = tuple(new_key_list)

        has_punc = new_key[n_gram-1][-1] == "?"

    return " ".join(words)


n_gram = int(raw_input("Enter number of words for your n-gram: "))
while n_gram < 0 or n_gram > 10:
    print "Not a valid number. Choose a number between 1 - 10"
    n_gram = int(raw_input("Enter number of words for your n-gram: "))


input_path = input_file

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, n_gram)

# Produce random text
random_text = ""
random_text = make_text(chains, n_gram)

print random_text
