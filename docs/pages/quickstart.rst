KumaPot QuickStart
===================
KumaPot is a simple TCP honeypot written in Python 3.8.

Installation
------------

    python -m pip install kumapot

Running
-------

    python -m nanopot

Installing as a debian package
------------------------------

    Get the `.deb` file from the GitHub release page, and run:
        sudo dpkg -i kumapot-1.0.0.deb
    Then enable the service with:
        sudo systemctl enable kumapot

    Config defaults to `/etc/kumapot.example.ini`
    Logs will be available in `/var/log/kumapot.log`

Source Code
-----------

    https://github.com/octacode/KumaPot

Documentation
-------------

    https://kumapot.github.io
