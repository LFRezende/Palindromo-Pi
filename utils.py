from math import sqrt


def findpal(num, tam):
    """
    Returns whether the word received is a palindrom or not.
    """
    pal = list()
    nome = ""
    found = False
    for k, v in enumerate(num):
        if len(pal) == tam:
            if pal == inversion(pal)[:]:        # If it is equal to its inverse, it is a palindrome.
                found = True
                nome = name(pal)                # Converts the list back to a string
                break
            del pal[0]                          # Deletes the first digit
        pal.append(v)                           # Inserts the next digit, to maintain length

    return found, k - tam, k, nome


def inversion(pal):
    lap = []                        # Setting for the inverted palindrome
    for k in range(1, len(pal) + 1):
        lap.append(pal[-k])
    return lap


def name(pal):
    return "".join(pal)             # Converts list back to a string


def isprime(txt):
    """Using Fermat's Theorem for Prime, where if no prime until the sqrt of n divides N, so N is prime."""
    num = int(txt)      # Converts it to an integer
    for p in range(2, int(sqrt(num)) + 1):      # int used to permit the for loop.
        if (num % p) == 0:
            return False, p                     # Returns the prime that divides txt and states as not a prime.
    return True, 1


