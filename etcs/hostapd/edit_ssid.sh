#!/bin/bash
# edit_ssid.sh - edits hostapd.conf and sets a MAC address-based SSID
cd `dirname $0`
ssid=`ip link | awk '/wlan0/ {getline; print $2}' | awk -v FS=':' '{printf("TeraHz_%s%s%s\n", $4, $5, $6)}'`
sed "/ssid=.*/s/ssid=.*/ssid=$ssid/" hostapd.conf > newconf
mv newconf hostapd.conf
