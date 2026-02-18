s = str(input())


new = ''.join([x.lower() if x.isupper() else x.upper() for x in s])

if s.isupper() or (s and s[0].islower() and all(c.isupper() for c in s[1:])):
    print(s.swapcase())

else:
    print(s)

