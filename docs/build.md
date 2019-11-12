# TeraHz build guide
In its early development phase, TeraHz was hard and time-consuming to compile and install.
This is not case now, as the more optimized DietPi Linux distribution allows
better performance and simpler configuration than formerly used Raspbian.

## Downloading the complete image
The easiest way to get TeraHz is to download the premade complete image and
write it to an SD card. It already has TeraHz installed and **will work out of
the box** with the correct hardware. The image is designed to run from a 16 GB
micro SD card, class 10 or higher is recommended for snappy performance. The
recommended image writer is Etcher

Please note that while this installation process is the easiest to perform, it
does not guarantee the most recent TeraHz software. Complete images take time to
prepare and despite the developer's best efforts aren't guaranteed to be always
up-to-date.

## Downloading the clean DietPi image and installing TeraHz manually
This process is a bit more involved, but the version of TeraHz installed is
guaranteed to be the latest one available from the repository.

The SD card image used in this case also contains some pre-configuration, but no
TeraHz code is installed. To install TeraHz, you'll need a console access to the
Raspberry Pi, preferably an SSH console over a wired network. DietPi is configured
to get an IP over DHCP. A tool such as arp-scan on linux is very helpful at determining
the device's IP address.

After connecting to the Raspberry Pi with username `root` and password `terahz`,
TeraHz can be installed by cloning the Git repository and running the `etcs/install.sh`
script.

```
git clone https://github.com/cls-02/TeraHz.git
cd TeraHz/etcs
./install.sh
```

When the installation completes, reboot the Raspberry Pi and it will
automatically boot into TeraHz.
