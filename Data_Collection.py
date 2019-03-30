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
import os
import textstat
import threading as thread

#################################################################

#################################################################
path = "C:/Users/Taylor Smith/Desktop/Code/SongPopularityPredictionAlgorithm/output"
genius = lyricsgenius.Genius("Xf0XfBJTZon0Sra2rGV56TAXp6jOUaLJVhmHxqbTW5mp-j6S2NVcmHWSLQ29v0dk")
try:  
    os.mkdir(path)
except:  
    pass

def writeSongCharacteristics(i, billboardChart, songs):
    key = str(billboardChart[i].title + billboardChart[i].artist)
    
    if key not in songs:
        song = billboardChart[i]
        title = billboardChart[i].title
        artist = song.artist
        peakpos = song.peakPos
        lastpos = song.lastPos
        numWeeks = song.weeks
        currentPos = song.rank
        isNew = song.isNew
        lyrics = genius.search_song(title, artist).lyrics
        row = [title, artist, lyrics, peakpos, lastpos, numWeeks, currentPos, isNew]
        songs[key] = row
        
    if key in songs:
        if billboardChart[i].peakPos != songs.get(key)[3]:
            newRow = songs.get(key)
            newRow[3] = billboardChart[i].peakPos
            songs[key] = newRow
        if billboardChart[i].weeks != songs.get(key)[5]:
            newRow = songs.get(key)
            newRow[5] = billboardChart[i].weeks
            songs[key] = newRow
            

def getAllSongData(startMonth, startYear, endMonth, endYear, numSongs):
    for year in range(startYear, endYear + 1):
        thread.Thread(None, target=yearlySongData, args=(year, startMonth, endMonth, numSongs)).start()
        

def yearlySongData(year, startMonth, endMonth, numSongs):
    for month in range (startMonth, endMonth + 1):
            thread.Thread(None, target=monthlySongData, args=(year, month, numSongs)).start()
    

def monthlySongData(year, month, numSongs):
        outputFileName = "C:/Users/Taylor Smith/Desktop/Code/SongPopularityPredictionAlgorithm/output/billboardHot100_Lyrics_{}_{}.csv".format(year, month)
        
        with open(outputFileName, 'a+', newline='', encoding='utf-8') as outputFile:
            songs = {}
            day = 1
            dataWriter = csv.writer(outputFile)
            
            while (day <= 31):
                if month in range(1, 10):
                    try:
                        billboardChart = billboard.ChartData('hot-100', date = "{}-{:02d}-{}".format(year, month, day))
                        for i in range(0, numSongs):
                            try:
                                writeSongCharacteristics(i, billboardChart, songs)
                            except:
                                pass
                    except:
                        pass
                    
                elif month in range(10, 13):
                    try:
                        billboardChart = billboard.ChartData('hot-100', date = "{}-{}-{}".format(year, month, day))
                        for i in range(0, numSongs):
                            try:
                                writeSongCharacteristics(i, billboardChart, songs)
                            except:
                                pass
                    except:
                        pass
                day += 5
                
            for key in songs:
                if (len(songs[key][2]) < 10000):
                    dataWriter.writerow(songs[key])



getAllSongData(1, 2017, 6, 2018, 1)








