#!/bin/bash
# run.sh - run the backend server
sudo gunicorn app:app -b 0.0.0.0:5000 &
disown
