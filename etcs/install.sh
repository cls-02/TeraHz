# install.sh - install TeraHz onto a Raspbian or DietPi installation
apt -y update
apt -y full-upgrade
apt install -y python3 python3-pip lighttpd dnsmasq hostapd libatlas-base-dev
pip3 install numpy pandas flask smbus2 pyserial
cp -R hostapd/ /etc
cp -R lighttpd/ /etc
cp dnsmasq.conf /etc
cp -R ../frontend /var/www/html
