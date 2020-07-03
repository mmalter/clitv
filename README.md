# clitv
Watch stuff using your cli

## Compatibility
Tested on Debian. Should work on BSDs.

## Dependencies
Depends on urwid and docopt.
You probably also want youtube-dl and mplayer.

## Installation
With superuser privileges :

    python3 setup.py install

## Configuration
You probably want to review the configuration in /etc.

In particular, you need a Youtube API key to watch Youtube. You can get one for free at https://console.developers.google.com/.

## Get started
    clitv --interactive
