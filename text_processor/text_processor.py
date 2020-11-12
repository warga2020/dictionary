def extract_tokens(in_str: str) -> list:
    """ split text into tokens """
    return in_str.split()


def clean_tokens(tokens_list: list):
    """ remove non-alphabetic characters from the beginning and end of tokens """
    for i, token in enumerate(tokens_list):
        while not token[0].isalpha():
            token = token[1:]
        while not token[-1].isalpha():
            token = token[:-1]
        tokens_list[i] = token


def cutoff_suffixes(tokens_list: list):
    """ suffix - it may be just word's plural form or short form of construction of sentence. """
    for i, token in enumerate(tokens_list):
        tmp_str = token.encode('ascii', errors='replace')
        tokens_list[i] = token[:tmp_str.index('?')] if tmp_str.count('?') else token
