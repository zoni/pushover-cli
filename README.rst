pushover-cli
============

A simple command-line interface to send `Pushover`_ notifications.

pushover-cli was written because none of available packages on PyPi fit the author's needs, which were to:

* Work on python versions 2 and 3
* Expose more advanced Pushover options, suchs as priority levels, supplementary URL's and sounds. 


Installation
------------

pushover-cli may be installed from PyPi using::

    pip install pushover-cli
    
Alternatively, to clone the code from GitHub and install from source::

    git clone https://github.com/zoni/pushover-cli.git
    cd pushover-cli
    python setup.py install


Usage
-----

::

    usage: pushover [-h] [--title TITLE] --message MESSAGE --token TOKEN --user
                    USER [--priority PRIORITY] [--retry RETRY] [--expire EXPIRE]
                    [--url URL] [--url-title URL_TITLE] [--sound SOUND]
                    [--device DEVICE]

    Simple pushover client

    optional arguments:
      -h, --help            show this help message and exit
      --title TITLE         your message's title, otherwise your app's name is
                            used
      --message MESSAGE     your message
      --token TOKEN         your application's API token
      --user USER           the user/group key (not e-mail address) of your user
                            (or you)
      --priority PRIORITY   send as -1 to always send as a quiet notification, 1
                            to display as high-priority and bypass the user's
                            quiet hours, or 2 to also require confirmation from
                            the user
      --retry RETRY         how often (in seconds) to repeat the notification to
                            the user in case of an emergency priority
      --expire EXPIRE       how many seconds your notification will continue to be
                            retried for (every retry seconds) in case of an
                            emergency priority
      --url URL             a supplementary URL to show with your message
      --url-title URL_TITLE
                            a title for your supplementary URL, otherwise just the
                            URL is shown
      --sound SOUND         the name of one of the sounds supported by device
                            clients to override the user's default sound choice
      --device DEVICE       your user's device name to send the message directly
                            to that device, rather than all of the user's devices


Changes
-------

1.0.1
~~~~~

* Update author email
* Disable version pinning
* Remove requests workaround

1.0.0
~~~~~

* Initial release


License
-------

The MIT License (MIT)

Copyright (c) 2013 Nick Groenen <nick@groenen.me>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


_`pushover`: https://pushover.net/
