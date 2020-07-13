# install.sh - install TeraHz onto a Raspbian Lite instance
cd `dirname $0`

apt -y update
apt -y full-upgrade
apt install -y python3 python3-pip lighttpd dnsmasq hostapd libatlas-base-dev
pip3 install numpy pandas flask smbus2 pyserial gunicorn

cp -R hostapd/* /etc/hostapd/
chmod +rx /etc/hostapd/edit_ssid.sh
cp dnsmasq.conf /etc/

cp rc.local /etc/
chmod +rx /etc/rc.local
cp interfaces-terahz /etc/network/interfaces.d/

cp -R ../frontend/* /var/www/html/

mkdir -p /usr/local/lib/terahz
cp -R ../backend/* /usr/local/lib/terahz

systemctl unmask dnsmasq hostapd lighttpd
systemctl enable dnsmasq hostapd lighttpd
