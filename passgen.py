#!/usr/bin/env python3
# Based on code by Brandon Currell, with minor adjustments: https://gist.github.com/BranicYeti/1264f7f60f66d6a065edb20e37259ddd

import sys
from random import SystemRandom
from bcrypt import hashpw, gensalt


class PassGen(object):
    def __init__(self):
        self.chars = [c for c in ' QqWwEeRrTtYyUuIiOoPpAaSsDdFfGgHhJjKkLlZzXxCcVvBbNnMm1234567890`~!@#$%^&*()-_=+[{]};:\'"\|,<.>/?']
        self.random = SystemRandom()

    def randchar(self):
        index = self.random.randrange(len(self.chars))  # Ensures even distribution; don't use round()
        return self.chars[index]

    def generate(self, length):
        password = ''
        while len(password) < length:
            c = self.randchar()
            if (len(password) == 0 or len(password) == length - 1) and c == ' ':
                continue
            password += self.randchar()

        return password


if __name__ == '__main__':
    length = 64
    if len(sys.argv) >= 2:
        length = int(sys.argv[1])

    gen = PassGen()
    password = gen.generate(length)
    pass_hash = hashpw(password.encode('utf-8'), gensalt(rounds=12))

    print(password)
    print(pass_hash.decode('ascii'))
