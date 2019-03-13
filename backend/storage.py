# storage.py - storage backend for TeraHz
# Copyright Kristjan Komloši 2019
# This code is licensed under the 3-clause BSD license


import sqlite3
class jsonStorage:
    def __init__(self, dbFile):
        '''Storage object constructor. Argument is filename'''
        self.db = sqlite3.connect(dbFile)

    def listJSONs(self):
        c = self.db.cursor()
        c.execute('SELECT * FROM storage')
        result = c.fetchall()
        c.close()
        return result

    def storeJSON(self, jsonString, comment):
        c = self.db.cursor()
        c.execute('INSERT INTO storage VALUES (datetime(\'now\', \'localtime\'), ?, ?)', (comment, jsonString))
        c.close()
        self.db.commit()

    def retrieveJSON(self, timestamp):
        '''Retrieves a JSON entry. Takes a timestamp string'''
        c = self.db.cursor()
        c.execute('SELECT * FROM storage WHERE timestamp = ?', (timestamp,))
        result = c.fetchall()
        c.close()
        return result
