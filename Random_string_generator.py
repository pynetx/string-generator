import random
import string
f = open('data', 'a')
for i in range(0, 500000):
    f.write(''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10)) + '\n')
f.close()
