"""Generate markov text from text files."""


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


def make_chains(text_string):
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
    # dictionary of our bigrams
    chains = {}

    # tokenizes by spaces and returns
    word_list = text_string.split()

    i = 0

    # looping until we get to the third to last words in text
    while i < len(word_list) - 2:
        key = (word_list[i], word_list[i+1])
        value = word_list[i+2]

    # checking if key is in chains and appending key if not
    # look into set default method
        if key not in chains: 
            chains[key] = [value]
        else:
            chains[key].append(value)
        i += 1
    
    return chains


def make_text(chains):
    """Returns text from chains."""

    # words is where we accumulate our final string
    words = []

    # chooses a random key
    first_key = choice(chains.keys())

    # creates list of all values from first key
    values = chains[first_key]

    # creates list from tuple
    key_string = list(first_key)

    # adding keys to words using extend because key_string is a list
    words.extend(key_string)

    # choosing a random value from list of values and adding to words
    words.append(choice(values))

    # creating a new key from the last two words of the text string
    new_key = (words[-2], words[-1])

    # adding new words until no new key in chains dictionary
    while new_key in chains:

        values = chains[new_key]
        words.append(choice(values))

        new_key = (words[-2], words[-1])

    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = ""
random_text = make_text(chains)

print random_text
