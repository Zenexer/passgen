<!--
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
-->

Secure password generator
=========================

Simple but cryptographically secure password generator written in Python.

License
=======

This application is released under the [BSD 2-Clause License](https://opensource.org/licenses/BSD-2-Clause).  See the [LICENSE](LICENSE) file for the complete license text.

Requirements
============

* Python 3.x (built for 3.5)
* bcrypt 3.x (built for 3.1.0)

On most systems, you can automatically install the correct requirements using pip:

``` bash
pip3 install -r requirements.txt
```

Usage
=====

``` bash
./passgen.py [length]
```

`length`: Optional length of generated password.  Defaults to 64.

Customization
=============

You can edit the `_passchars` function to adjust the characters that appear in passwords.  The default is ASCII (including space) + visible Latin-1 Supplement.  Regardless of these settings, spaces (U+0020) will not be allowed as the first or last characters in generated passwords.
