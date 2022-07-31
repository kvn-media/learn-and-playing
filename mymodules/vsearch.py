##def search4vowels(word):
##    """Return a boolean based on any vowels found."""
##    vowels = set('aeiou')
##    found = vowels.intersection(set(word))
##    return bool(found)
##
##
##def search4vowels(word):
##    """Return any vowels found in a supplied word."""
##    vowels = set('aeiou')
##    found = vowels.intersection(set(word))
##    return found
##
##
##def search4vowels(word):
##    """Return any vowels found in a supplied word."""
##    vowels = set('aeiou')
##    return vowels.intersection(set(word))


def search4vowels(phrase: str) -> set:
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Return a set of the 'letter' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
