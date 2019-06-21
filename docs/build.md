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
and the required version of python.
