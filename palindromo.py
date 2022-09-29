# Program which reads Pi and gets a "tam"-length palindrome that is prime.
# Imports
from utils import *
from pi import Pi

# Initial settings
l_pal = False  # If it is a palindrome
l_prime = False  # If it is prime
xi = xf = -1  # Initial and Final indexes ("x") for the palindrome.
pal = ""  # Initial setting for the palindrom (a string)
factor = 1  # Divider
count = 0  # Counter in string-slicing
endcount = -1  # Final position of the palindrome in Pi

# Importing a text file with the numbers
arq = "pi_million.txt"  # I grabbed the number in this portal: https://www.piday.org/million/


# Finding the palindrom
num = Pi(arq)  # Importing Pi via the archive "arq"
length = 9  # Length desired for the palindrome
num = num[2:]  # Getting rid of the non-decimal 3 and the point in the text archive.
while count != len(num):
    num = num[count:]  # For next iteration, excludes the already tested string of Pi.
    l_pal, xi, xf, pal = findpal(num, length)  # Analysis of the next palindrome.
    print(pal)
    if l_pal == True:
        l_prime, factor = isprime(pal)
        if (
            l_prime == True
        ):  # If it is prime and a palindrome, we found the requirement -> Break.
            break
    count = xf  # Getting the relative position to the analyzed portion of Pi.
    endcount += count  # Sums the relatives for the absolute position of the Palindrome.

# Final data:
# Initial and Final positions, Final palindrom.
if l_pal and l_prime:
    print(
        f"\n------------\nDesired palindrome:***{pal}***\nVectorial Position: {endcount-length}-{endcount}\n------------"
    )
    print(f"Located on the {endcount - length + 1} th digit of Pi.\n------------")
else:
    print(f"Not found in the first one million digits of Pi.")
