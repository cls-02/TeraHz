[![Documentation Status](https://readthedocs.org/projects/terahz/badge/?version=latest)](https://terahz.readthedocs.io/en/latest/?badge=latest)
# <img alt="TeraHz logo" src="docs/imgs/logo-sq.png" width="200px"> TeraHz

*Za slovensko različico se odpravite na <http://git.sckr-lab.tk/kristjank/TeraHz>*

TeraHz is a low-cost portable spectrometer based on Raspberry Pi and a few
commonly available sensor breakout boards. It's designed to bring low-cost
scientific exploration of the light spectrum to educational institutions that
cannot afford the options available on the current market. It costs less than
200€ with money to spare and uses only free, libre and open-source software
(FLOSS). It is free to use under the ISC license, a spiritual successor to the
classic 3-clause BSD license.

## How to install
Stable releases are available under the releases tab and can be installed either
by flashing a **preinstalled** ready to boot image with a stable version of
TeraHz preinstalled or by flashing a **preconfigured** image of DietPi and
installing TeraHz manually, which is useful if you want to test bleeding edge
releases. For more information, check out the [Build
guide](https://terahz.readthedocs.io/en/latest/build/).

## Docs
TeraHz usually works out of the box. A wireless network named `TeraHz_XXXXXX`
(XXXXXX = the last half of the MAC address) will appear. Password is
`terahertz`. After connection, open a web browser and visit `terahz.site`.
The UI will appear. To fetch data from the sensors, press the 'Get Data' button.
The readings are then plotted and written into the tables below the graph.

More documentation is available at <https://terahz.readthedocs.io>

## Development team
- Kristjan Komloši (cls-02) - Project leader and main programmer
- Jakob Kosec (D3m1j4ck) - Frontend designer
- Juš Dolžan (ANormalPerson) - Math double-checker

<img alt="TeraHz logo" src="http://www.sckr.si/documents/upload/konektor/logo/_SC.gif" width="200px">  
<<<<<<< HEAD
TeraHz has been developed under guidance and financial support of Šolski Center Kranj (Kranj School Centre). Without their support, this project might have never been possible.
=======
TeraHz has been developed under guidance and financial support of Šolski Center Kranj (Kranj School Centre). Without their support, this project might have never been possible. As the project leader, I would like to personally thank prof. Darija Kramarič, who brought my idea to life; and Jože Drenovec, who provided me with everything needed for my experiments.
>>>>>>> 682fe20db291234c1ad2ff8ecb6c142c00220c32
