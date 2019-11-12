# storage.py - storage backend for TeraHz
'''TeraHz storage backend'''
# Copyright Kristjan Komloši 2019
# All code in this file is licensed under the ISC license,
# provided in LICENSE.txt


import sqlite3
class jsonStorage:
    '''Class for simple sqlite3 database of JSON entries'''
    def __init__(self, dbFile):
        '''Storage object constructor. Argument is filename'''
        self.db = sqlite3.connect(dbFile)

    def listJSONs(self):
        '''Returns a list of all existing entries.'''
        c = self.db.cursor()
        c.execute('SELECT * FROM storage')
        result = c.fetchall()
        c.close()
        return result

    def storeJSON(self, jsonString, comment):
        '''Stores a JSON entry along with a timestamp and a comment.'''
        c = self.db.cursor()
        c.execute(('INSERT INTO storage VALUES (datetime'
                   '(\'now\', \'localtime\'), ?, ?)'), (comment, jsonString))
        c.close()
        self.db.commit()

    def retrieveJSON(self, timestamp):
        '''Retrieves a JSON entry. Takes a timestamp string'''
        c = self.db.cursor()
        c.execute('SELECT * FROM storage WHERE timestamp = ?', (timestamp,))
        result = c.fetchall()
        c.close()
        return result
