import re
beach = input()

print(len(re.findall(r"sand|water|fish|sun", beach, re.IGNORECASE)))