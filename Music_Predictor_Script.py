# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:15:57 2019

@author: Chaitu Konjeti
"""

#import spotipy
import billboard
#import applemusicpy
import lyricsgenius
#import SpotifyCharts as sCharts
import csv


genius = lyricsgenius.Genius("Xf0XfBJTZon0Sra2rGV56TAXp6jOUaLJVhmHxqbTW5mp-j6S2NVcmHWSLQ29v0dk")



outputFileName = "billboardHot100_Lyrics.csv"
with open(outputFileName, "a+") as outputFile:
    dataWriter = csv.writer(outputFile)
    for year in range(1950, 2020):
        for month in range (1, 13):
            if month in range(1, 10):
                try:
                    billboardChart = billboard.ChartData('hot-100', date = "{}-{:02d}-01").format(year, month)
                except:
                    pass
            if month in range(10, 13):
                try:
                    billboardChart = billboard.ChartData('hot-100', date = "{}-{}-01").format(year, month)
                except:
                    pass
            for i in range(0, 1):
                try:
                    song = billboardChart[i]
                    title = billboardChart[i].title
                    artist = song.artist
                    peakpos = song.peakPos
                    lastpos = song.lastPos
                    numWeeks = song.weeks
                    rank = song.rank
                    isNew = song.isNew
                    lyrics = genius.search_song(title, artist).lyrics
                    row = [title, artist, lyrics, peakpos, lastpos, numWeeks, rank, isNew]
                    dataWriter.writerow(row)
                except:
                    pass
    
    

        
    

    

