def palindrom(s):
    s = ''.join(znak.lower() for znak in str(s) if znak.isalnum())
    return s == s[::-1]
print(palindrom("kajak"))
print(palindrom("wrotki"))
print(palindrom("Eva, can I see bees in a cave?"))
print(palindrom(12321))