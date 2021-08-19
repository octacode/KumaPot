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

    Get the `.deb` file from the GitHub release page, or build the package with:
         dpkg-deb --build ./deb kumapot-1.0.0.deb
    Install the package with:
        sudo dpkg -i kumapot-1.0.0.deb
    Then enable the service with:
        sudo systemctl enable kumapot

    Config defaults to `/etc/kumapot.ini`
    Logs will be available in `/var/log/kumapot.log`

Debian Package
-----------------


Then install with

    dpkg -i kumapot-1.0.0.deb

Source Code
-----------

    https://github.com/octacode/KumaPot

Documentation
-------------

    https://kumapot.github.io
