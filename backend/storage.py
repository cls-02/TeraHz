# storage.py - storage backend for TeraHz
# Copyright Kristjan Komloši 2019
# This code is licensed under the 3-clause BSD license

import file
import json
import pandas as pd

class measurementStorage():
    def __init__(self, directory):
        self.storageDirectory = directory

    def storeJSON(self, JSON):
        # JSON sanity check, shouldn't be needed, but just in case...
        if 'metadata' not in JSON or 'timestamp' not in JSON['metadata']:
            raise Exception('Invalid JSON passed to storage backend: no timestamp')

        if 'spectral' not in JSON or [x for x in 'ABCDEFGHIJKLMNOPQR'] not in JSON['spectral']:
            raise Exception('Invalid JSON passed to storage backend: no spectral data')

        if 'uv' not in JSON or ['a', 'b', 'i'] not in JSON['uv']:
            raise Exception('Invalid JSON passed to storage backend: no UVA/B/I data')

        if 'lux' not in JSON:
            raise Exception('Invalid JSON passed to storage backend: no illuminance data')

        filename = JSON['metadata']['timestamp'] + '.thz'
        with file.open()
