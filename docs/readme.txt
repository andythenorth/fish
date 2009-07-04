Generic Makefile system for NewGRFs
-----------------------------------

This version: {{GRF_TITLE}}

Contents:

1 About
2 Installation
3 License
4 Credits



-------
1 About
-------

This NewGRF build system aims at NewGRF authors for OpenTTD and TTDPatch who want to employ an easy-to-use system in order to generate their NewGRFS.

Name of this Repo: {{GRF_TITLE}}
GRF_ID:            {{GRF_ID}}
MD5 sum:           {{GRF_MD5}}

Repository version: {{GRF_REVISION}}



--------------
2 Installation
--------------

This Makefile system is easiest to setup if you employ a certain directory structure for your NewGRF project. Clone this project and fill in your NewGRF content. Make sure to adopt Makefile.config to your needs.

Requirements for running this Makefile successfully:
	grfcodec
	renum
	gcc
	md5sum (or md5 on Mac)
	make
If you want to bundle the grf, you'll need additionally
	tar
	zip
	bzip2
Windows only:
On Windows systems this means that you'll need to install MinGW and MSys in order to obtain a posix compatible environment. Then the makefile can be called the very same way as it is on linux and mac systems. MinGW/MSys contain the above mentioned programmes (except renum and grfcodec of course) and can be obtained from http://www.mingw.org/ That site also features an excellent walk-through o how to install it.

If you use for OpenTTD data folder a non-default path or Windows with a non-English localization make sure to copy Makefile.local.sample to Makefile.local and edit the line with
	INSTALLDIR =
accordingly so that it shows the full path to your OpenTTD / TTDP data directory.

---------
3 License
---------

This generic NewGRF Makefile was written by Ingo von Borstel (aka planetmaker) and is free to use for anyone under the terms of the GNU Pulic License v2 or higher. See license.txt. 

The source code can be obtained from the #openttdcoop DevZone at http://dev.openttdcoop.org/projects/newgrf-makefile or via mercurial checkout
hg clone http://dev.openttdcoop.org/projects/newgrf-makefile



---------
4 Credits
---------

Author: Ingo von Borstel (aka planetmaker)

Special thanks to #openttdcoop and especially Ammler who provides and works a lot on maintaining the Development Zone where this repository is hosted and who also frequently gives much valuable input. Thanks also to all the NewGRF authors whose NewGRFs can be my playground for this project.
