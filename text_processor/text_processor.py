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
