# TeraHz build guide
The recommended way of getting TeraHz is the official SD card image provided
under the releases tab in the GitHub repository. Installing TeraHz from source
is a time consuming and painful process, even more so if you don't know what
you're doing, and whatever you end up building __will not be officially
supported__ (unless you're a core developer).

With this warning out of the way, let's begin.

## Getting the latest sources
The most reliable way to get working source code is by cloning the official GitHub
repository and checking out the `development-working` tag. This tag marks the latest
confirmed working commit. Building from the master branch is somewhat risky, and
building from development branches is straight up stupid if you're not a developer.

After cloning and checking out, check the documentation for module dependencies
and the required version of python in the `docs/dependencies.md` file.

## Installing Python
This step depends a lot on the platform you're using. TeraHz was developed with
Raspberry Pi and Raspbian in mind. If you're familiar with Raspbian enough,
you'll know that the latest version of Python available is `3.5`, which is too
obsolete to run TeraHz and the required modules consistently.

After messing with Debian arm64 packages in the early development days I determined
that the most reliable way of getting Python on Raspbian is compiling it from source.
This part of the installation will take the largest portion of time, as compiling
anything complex on the Raspberry is painfully slow.

If you're running an OS that provides a recent version of Python, great! You won't
have to waste so much time waiting for the build process to finish.

The Python version TeraHz works best on is `3.6.8`. To install it, download the
gzipped tarball from the official Python website, and decompress it.
