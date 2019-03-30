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


songNumber = 3
startYear = 1958
endYear = 1959
startMonth = 6
endMonth = 10



for year in range(startYear, endYear):
    for month in range (startMonth, endMonth):
        outputFileName = "billboardHot100_Lyrics_{}_{}.csv".format(year, month)
        day = 0
        while (day <= 28):            
            with open(outputFileName, "a+") as outputFile:
                dataWriter = csv.writer(outputFile)
                if month in range(1, 10):
                    try:
                        billboardChart = billboard.ChartData('hot-100', date = "{}-{:02d}-{}".format(year, month, day))
                        for i in range(0, songNumber):
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
                        for i in range(0, songNumber):
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