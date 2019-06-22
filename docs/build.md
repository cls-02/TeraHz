# TeraHz build guide
The recommended way of getting TeraHz is the official Raspberry Pi SD card image
provided under the releases tab in the GitHub repository. Installing TeraHz from
source is a time consuming and painful process, even more so if you don't know
what you're doing, and whatever you end up building __will not be officially
supported__ (unless you're a core developer).

With this warning out of the way, let's begin.

## Getting the latest sources
The most reliable way to get working source code is by cloning the official
GitHub repository and checking out the `development-stable` tag. This tag marks
the latest confirmed working commit. Building from the master branch is somewhat
risky, and building from development branches is straight up stupid if you're
not a developer.

Make sure that the repository is cloned into `/home/pi/TeraHz`, as Lighttpd
expects to find frontend files inside this directory.

After cloning and checking out, check the documentation for module dependencies
and the required version of python in the `docs/dependencies.md` file.

## Installing Python
This step depends a lot on the platform you're using. TeraHz was developed with
Raspberry Pi and Raspbian in mind. If you're familiar with Raspbian enough,
you'll know that the latest version of Python available is `3.5`, which is too
obsolete to run TeraHz and the required modules consistently. This leaves us
with compiling Python from source. __This step is guaranteed to be slow,
overnight compiling with something like tmux is recommended.__

### Pre-requirements
Installing python without most C libraries will lead to a rather minimalistic
Python install, missing a lot of important modules. To prevent this, update
the system packages. After that, reboot.

```
sudo apt update
sudo apt full-upgrade
sudo reboot
```

Install the required build tools, libraries and their headers.

```
sudo apt-get install build-essential tk-dev libncurses5-dev libncursesw5-dev \
libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev \
libexpat1-dev liblzma-dev zlib1g-dev
```

### Compiling
Compiling Python from source is, in fact pretty easy, just time-consuming. To combat
that, using tmux to detach and later reattach the session is advised.

Python is packaged in many forms, but you'll be using the most basic
of them all: a gzipped tarball. Download and decompress it, then cd into its
directory.

```
wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz
tar -xzf Python-3.6.8.tgz
cd Python-3.6.8
```

Python's build process is pretty classic, a `.configure` script and a Makefile.
Using the `-j` option with Make can reduce the compile time significantly. Go
with as many threads as you have cores: `-j 4` works great on the Pi 3 B/B+.

```
./configure
make -j4
```

When the compilation ends, install your freshly built version of python.

```
sudo make altinstall
```

"Altinstall" means that the new version of Python will be installed beside the
existing version, and all related commands will use the full naming scheme:
think `python3.6` or `pip3.6` instead of the shorter `python3` or `pip3`.

### Modules
Another painfully slow part is the installation of all the required modules
needed by TeraHz. Luckily, `pip3.6` takes care of the entire installation
process. As before, using tmux is advised.

```
pip3.6 install smbus pyserial flask pandas
```

## Raspi-config
For some law-obeying reason, Raspbian locks down the Wi-Fi interface card until
the Wi-Fi country is set. This means that we will need to set it manually through
the `raspi-config` program. It requires superuser privileges.

```
sudo raspi-config
```

_TODO: add images and setup walkthrough - Wi-Fi country, Partition expand, SMBus
enable, etc._

## Installing packages
In addition to what's already installed, TeraHz requires the following daemons
to run:
  - Lighttpd - Frontend HTTP server
  - Dnsmasq - DNS and DHCP server, used to redirect the `terahz.site` domain
  - Hostapd - Wi-Fi access point

They are available from the Raspbian repository. Install it via `apt`.
  
```
apt install hostapd dnsmasq hostapd
```

## Copying configuration files
To simplify the process of configuring Raspbian to run TeraHz, sample
configuration file are provided
