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

Usage
=====

``` bash
./passgen.py [length]
```

`length`: Optional length of generated password.  Defaults to 64.

Customization
=============

You can edit the `_passchars` function to adjust the characters that appear in passwords.  The default is ASCII (including space) + visible Latin-1 Supplement.  Regardless of these settings, spaces (U+0020) will not be allowed as the first or last characters in generated passwords.
