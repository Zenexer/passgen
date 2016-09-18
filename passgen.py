#!/usr/bin/env python3
"""
Copyright (c) 2016, Paul Buonopane and Brandon Currell
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

from sys import stderr, exit
try:
    from sys import argv
    from random import SystemRandom
    from bcrypt import hashpw, gensalt
    from os import path, urandom
except ImportError as err:
    print("Missing a Python module.  Have you run `pip3 install -r requirements.txt` yet?  Details: {0}".format(err), file=stderr)
    exit(1)


# You'll probably want to adjust this to your liking.
def _passchars():
    for i in range(0x000020, 0x00007F): yield chr(i)  # ASCII (Basic Latin): numbers, letters, symbols, space
    for i in range(0x0000A1, 0x0000FF): yield chr(i)  # Latin-1 Supplement: symbols, fractions, accented letters, uncommon letters
    #for i in range(0x0016A0, 0x0016F0): yield chr(i)  # Runic
    #for i in range(0x002190, 0x0021FF): yield chr(i)  # Arrows

    # If you just wanted letters and numbers, for example:
    #for i in range(ord('0'), ord('9')): yield chr(i)  # Numbers
    #for i in range(ord('a'), ord('z')): yield chr(i)  # Lowercase letters
    #for i in range(ord('A'), ord('Z')): yield chr(i)  # Uppercase letters

__urandom_warning = False
def _random(n):
    global __urandom_warning

    if not __urandom_warning:
        try:
            rng = '/dev/random'
            if path.exists(rng):
                with open(rng, 'rb') as f:
                    return f.read(n)
        except Exception as err:
            print("Warning: Using /dev/urandom instead of /dev/random.  Reason: {0}".format(err), file=stderr)
            __urandom_warning = True

    return urandom(n)


class RealSystemRandom(SystemRandom):
    def random(self):
        """Get the next random number in the range [0.0, 1.0)."""
        return (int.from_bytes(_random(7), 'big') >> 3) * RECIP_BPF

    def getrandbits(self, k):
        """getrandbits(k) -> x.  Generates an int with k random bits."""
        if k <= 0:
            raise ValueError('number of bits must be greater than zero')
        if k != int(k):
            raise TypeError('number of bits should be an integer')
        numbytes = (k + 7) // 8                       # bits / 8 and rounded up
        x = int.from_bytes(_random(numbytes), 'big')
        return x >> (numbytes * 8 - k)                # trim excess bits

# Based on code by Brandon Currell: https://gist.github.com/BranicYeti/1264f7f60f66d6a065edb20e37259ddd
class PassGen(object):
    def __init__(self):
        self.chars = [c for c in _passchars()]
        self.random = RealSystemRandom()

    def randchar(self):
        index = self.random.randrange(len(self.chars))  # Ensures even distribution; don't use round()
        return self.chars[index]

    def generate(self, length):
        password = ''
        while len(password) < length:
            c = self.randchar()
            if (len(password) == 0 or len(password) == length - 1) and c == ' ':
                continue
            password += c

        return password


if __name__ == '__main__':
    try:
        length = 64
        if len(argv) >= 2:
            length = int(argv[1])

        gen = PassGen()
        password = gen.generate(length)
        print(password)
    
        # If you want to also output a bcrypt hash:
        #pass_hash = hashpw(password.encode('utf-8'), gensalt(rounds=12))
        #print(pass_hash.decode('ascii'))
    except KeyboardInterrupt:
        print("Interrupted", file=stderr)
