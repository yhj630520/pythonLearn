def search4vowels():
    """Display any vowels found in an asked-for word."""
    vowels = set('aeiou')
    word = input('Provide a word to search for vowels: ')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)


def search_for_vowels(word):
    """Display any vowels found in an supplied word."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)


def search_for_vowels_return_bool(word):
    """Return a boolean based on any vowels found."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))
    return bool(found)


def search_for_vowels_return_data(word):
    """Return  data based on any vowels found."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search_for_vowels_by_ann(word: str) -> set:
    """Display any vowels found in an supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(word))


def search_for_vowels_with_phrase(phrase: str) -> set:
    """Display any vowels found in an supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search_for_letters(phrase: str, letter: str) -> set:
    """Restun a set of the 'letters' found in 'phrase'."""
    return set(letter).intersection(set(phrase))


def search_for_vowels_by_default_value(phrase: str, letters: str = 'aeiou') -> set:
    """ 参数指定默认值"""
    return set(letters).intersection(set(phrase))


print(search_for_vowels_by_default_value('asjdlkajsd;i'))
