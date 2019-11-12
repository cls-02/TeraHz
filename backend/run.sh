#!/bin/bash
# run.sh - run the backend server
cd `dirname $0`
sudo gunicorn app:app -b 0.0.0.0:5000 &
