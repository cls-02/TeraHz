# storage.py - storage backend for TeraHz
# Copyright Kristjan Komloši 2019
# This code is licensed under the 3-clause BSD license

import file
import json
import pandas as pd
from pathlib import Path

class measurementStorage():
    def __init__(self, directory):
        self.storagePath = Path(directory)
        if not self.storagePath.exists():
            raise Exception('Storage directory does not exist')

    def storeTemp(self, jsonObject):
        with self.storagepath / 'temp.thz' as tempfile:
            json.dump(jsonObject, tempfile)

    def loadTemp(self):
        with self.storagePath / 'temp.thz' as tempfile:
            return json.load(tempfile)

    def tempToFile(self):
        self
