#!/usr/bin/python3
# Minimal flup configuration for Flask
from flup.server.fcgi import WSGIServer
from app import app

if __name__ == '__main__':
    WSGIServer(app, bindAddress='/var/www/api/terahz.sock').run()
