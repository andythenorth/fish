Generic Makefile system for NewGRFs
-----------------------------------

This version: {{GRF_TITLE}}

Contents:

1 About
2 Installation
3 Usage
4 License
5 Credits



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



-------
3 Usage
-------

The Makefile offers different targets. A brief overview is given here:

all: 
This is the default target, if also no parameter is given to make. It will
simply build the grf file, if it needs building

bundle:
This target will create a directory called "<name>-nightly" and copy the grf
file there and the documentation files, readme.txt, changelog.txt and
license.txt

bundle_zip
This will zip the bundle directory into one zip for distribution

bundle_tar
This will tar the bundle directory into a tar archive for distribution or upload
to bananas

install:
This will create a tar archive (like bundle_tar) and copy it into the INSTALLDIR
as specified in Makefile.local (or the default dir, if that isn't defined).
Don't rely on a good detection of the default installation directory. It's
especially bound to fail on windows machines.

release*:
This target will basically do the same as the bundle* targets with one
difference: They are packed in a uniquely named directory, so that all different
release versions of this can be used in parallel in OpenTTD.

clean:
This phony target will delete all files which this Makefile will create

remake:
It's a shortcut for first cleaning the dir and then making the grf anew.



---------
4 License
---------

This generic NewGRF Makefile was written by Ingo von Borstel (aka planetmaker) and is free to use for anyone under the terms of the GNU Pulic License v2 or higher. See license.txt. 

The source code can be obtained from the #openttdcoop DevZone at http://dev.openttdcoop.org/projects/newgrf-makefile or via mercurial checkout
hg clone http://dev.openttdcoop.org/projects/newgrf-makefile



---------
5 Credits
---------

Author: Ingo von Borstel (aka planetmaker)

Special thanks to #openttdcoop and especially Ammler who provides and works a lot on maintaining the Development Zone where this repository is hosted and who also frequently gives much valuable input. Thanks also to all the NewGRF authors whose NewGRFs can be my playground for this project.
