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

#################################################################
#Create hashset that updates peakpos, number of weeks in hot-100
#################################################################


genius = lyricsgenius.Genius("Xf0XfBJTZon0Sra2rGV56TAXp6jOUaLJVhmHxqbTW5mp-j6S2NVcmHWSLQ29v0dk")


def getAllSongData(startMonth, startYear, endMonth, endYear, numSongs):
    for year in range(startYear, endYear + 1):
        for month in range (startMonth, endMonth + 1):
            outputFileName = "billboardHot100_Lyrics_{}_{}.csv".format(year, month)
            day = 0
            while (day <= 28):            
                with open(outputFileName, "a+") as outputFile:
                    dataWriter = csv.writer(outputFile)
                    if month in range(1, 10):
                        try:
                            billboardChart = billboard.ChartData('hot-100', date = "{}-{:02d}-{}".format(year, month, day))
                            for i in range(0, numSongs):
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
                        except:
                            pass
                    elif month in range(10, 13):
                        try:
                            billboardChart = billboard.ChartData('hot-100', date = "{}-{}-01".format(year, month))
                            for i in range(0, numSongs):
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
                        except:
                            pass
                day += 7
                

getAllSongData(1, 2009, 3, 2010, 1)