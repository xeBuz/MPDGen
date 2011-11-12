# -*- coding: utf-8 *-*
#!/usr/bin/env python

import sys
import time

from daemon import Daemon
from audioscrobbler import AudioScrobblerQuery
from mpd import (MPDClient, CommandError)


class MPDGen(Daemon):

    ' For MPD connection '
    client = MPDClient()
    ' Storage all the artist in memory for optimize querys'
    mpd_library = []
    ' Count of song for append to playlist '
    song_count = 10
    ' Current playin song '
    current_song = ''
    ' Last song played '
    last_song = ''


    def __init__(self):
        """  Initilize the class """
#        Daemon.__init__(self)
        self.mpd_connect(self.client)
        self.load_library(self.client, self.mpd_library)

    def mpd_connect(self, client):
        """ Connect w/MPD Server """
        #ToDo- Tomar Host y Port de un archivo
        # load_conf()
        mpd_host = 'localhost'
        mpd_port = '6600'
        mod_connection = {'host': mpd_host, 'port': mpd_port}
        #ToDo- Try con errores
        client.connect(**mod_connection)

    def load_library(self, client, mpd_library):
        """ Load the full library for """
        temp_library = client.listallinfo()
        for x in range(len(temp_library)):
            for i, j in temp_library[x].iteritems():
                if i == "artist":
                    self.mpd_library.append(j)


    def load_conf():
        #ToDo. HOST, PORT, CANT
        pass

    def get_current_song(self):
        """ Get the current song playing in the server, and save it """        
        self.current_song = self.client.currentsong()

    def get_recommended(self):
        """ Get the similar artist from Last.fm """
        """ Storage in a array and them validate if exists in the server """
        recommended_artists = []
        current_artist = AudioScrobblerQuery(artist=self.current_song['artist'])
        # En base a todos los artistas similares, me fijo cuales tengo en el
        # server MPD, y los almaceno para usarlos despues.
        for artist in current_artist.similar():
            if float(self.client.count("artist", artist.name)['songs']) > 0:
                recommended_artists.append(artist.name)
                if len(recommended_artists) == self.song_count:
                    exit
        ' Return similar artists in the server'
        return recommended_artists



    def get_similar(self, recommended_artists):
        while len(recommended_songs) < COUNT_SONGS:
            artist = random.choice(recommended_artists)
            recommended_songs.append(random.choice(client.search('artist', artist)))
        for i in (len(recommended_songs)):
            
            
    def append_playlist(self, recommended_artists):if len
        recommended_songs.append(random.choice(client.search('artist', artist)))
            
        


    def run(self):
        """ Execute the application """
        self.get_current_song()
        if self.current_song <> self.last_song:
            recommended_artists = self.get_recommended()
            append_playlist(recommended_artists)            




if __name__ == "__main__":
        daemon = MPDGen('/tmp/daemon-example.pid')
        if len(sys.argv) == 2:
                if 'start' == sys.argv[1]:
                        daemon.start()
                elif 'stop' == sys.argv[1]:
                        daemon.stop()
                elif 'restart' == sys.argv[1]:
                        daemon.restart()
                else:
                        print "Unknown command"
                        sys.exit(2)
                sys.exit(0)
        else:
                print "usage: %s start|stop|restart" % sys.argv[0]
                sys.exit(2)
