# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 20:15:57 2019

@author: Chaitu Konjeti
@author: Taylor Smith
"""

#import spotipy
import billboard
#import applemusicpy
import lyricsgenius
#import SpotifyCharts as sCharts
import csv
import os
from text import textstatistics as t
import threading as thread

#################################################################

#PATHS:

    #Chaitu: C:/Users/Chaitu Konjeti/SongPopularityPredictionAlgorithm/output
    #        C:/Users/Chaitu Konjeti/SongPopularityPredictionAlgorithm/output/billboardHot100_Lyrics_{}_{}.csv
    
    #Taylor: C:/Users/Taylor Smith/Desktop/Code/SongPopularityPredictionAlgorithm/output
    #        C:/Users/Taylor Smith/Desktop/Code/SongPopularityPredictionAlgorithm/output/billboardHot100_Lyrics_{}_{}.csv

#################################################################

path = "C:/Users/Taylor Smith/Desktop/Code/SongPopularityPredictionAlgorithm/output"
genius = lyricsgenius.Genius("Xf0XfBJTZon0Sra2rGV56TAXp6jOUaLJVhmHxqbTW5mp-j6S2NVcmHWSLQ29v0dk")


sample = ''' Soulja Boy off in this oh
Watch me crank it, watch me roll
Watch me crank dat, Soulja Boy
Then Superman dat oh
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch
Soulja Boy off in this oh
Watch me crank it, watch me roll
Watch me crank dat, Soulja Boy
Then Superman dat oh
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch
Soulja Boy off in this oh
Watch me lean then watch me rock
Super Man dat oh
Yeah watch me crank dat Robocop
Super Fresh, now watch me jock
Jocking on them haterz man
When I do dat Soulja Boy
I lean to the left and crank dat thing
Now you
I'm jocking on you, I'm jockin' on you
And if we get the fightin'
Then I'm cocking on you, then I'm cockin' on you
You catch me at yo local party
Yes I crank it everyday
Haterz get mad cuz
I got me some Bathin' Apes
Soulja Boy off in this oh
Watch me crank it, watch me roll
Watch me crank dat, Soulja Boy
Then Superman dat oh
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch
Soulja Boy off in this oh
Watch me crank it, watch me roll
Watch me crank dat, Soulja Boy
Then Superman dat oh
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch
I'm bouncin' on my toe
Watch me super soak dat oh
I'ma pass it to Arab
And he's gon' crank it up fo' sho'
Haterz wanna be me
Soulja Boy, I'm the man
They be lookin' at my neck
Sayin' it's the Rubberband Man, man
Watch me do it, watch me do it
Dance, dance
Let get to it, let get to it
Nope, you can't do it like me
Doe, so don't do it like me
Folk, I see you tryna do it like me
Man that damn was ugly
Soulja Boy off in this oh
Watch me crank it, watch me roll
Watch me crank dat, Soulja Boy
Then Superman dat oh
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch
Soulja Boy off in this oh
Watch me crank it, watch me roll
Watch me crank dat, Soulja Boy
Then Superman dat oh
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch
I'm too fresh off in this oh
Watch me crank it, watch me roll
Watch me crank that Roosevelt
And super soak that oh
Super soak that oh
Super soak that oh
Super soak that oh
Super soak that oh
I'm too fresh now watch me do
Watch me shuffle, watch me do
Watch me crank that Soulja Boy, now Superman do it
Superman do it
Superman do it
Ahh
Soulja Boy off in this oh
Watch me crank it, watch me roll
Watch me crank dat, Soulja Boy
Then Superman dat oh
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch
Soulja Boy off in this oh
Watch me crank it, watch me roll
Watch me crank dat, Soulja Boy
Then Superman dat oh
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch me you
(Crank dat, Soulja Boy)
Now watch
You, ah you '''
text = t()

#print(text.gunning_fog(sample))


try:  
    os.mkdir(path)
except:  
    pass




"""
    METHOD:
        This method gathers data for songs and organizes said data into a HashMap (Dictionary).
        This method ONLY creates a hash code for each song, then gathers all data into a single list in the HashMap.
        
    PARAMATERS:
        i: The song number in the billboardChart in which we are gathering data
        billboardChart: The specific chart in which we are collecting data (they will vary only by dates)
        songs: The HashMap in which all songs and their data are stored
"""
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
    
    
    

"""
    METHOD:
        This method creates threads for every year specified.
        The thread then calls seperate methods to further thread the program.
        These threads will eventually search for and gather songs and their data.
        
    PARAMETERS:
        startMonth: The month in which data collection will start
        startYear: The year in which data collection will start
        endMonth: The month in which data collection will end
        endYear: The year in which data collection will end
        numSongs: The number of songs to be collected
"""
def getAllSongData(startMonth, startYear, endMonth, endYear, numSongs):
    for year in range(startYear, endYear + 1):
        thread.Thread(None, target=yearlySongData, args=(year, startMonth, endMonth, numSongs)).start()
        
        
        
        
"""
    METHOD:
        This method creates threads for every month specified.
        The thread then calls seperate methods to further thread the program.
        These threads will eventually search for and gather songs and their data.
        This method is used in the getAllSongData thread.
        
    PARAMETERS:
        year: The current year in which the method is taking data (determined in getAllSongData)
        startMonth: The month in which data collection will start
        endMonth: The month in which data collection will end
        numSongs: The number of songs to be collected        
"""
def yearlySongData(year, startMonth, endMonth, numSongs):
    for month in range (startMonth, endMonth + 1):
            thread.Thread(None, target=monthlySongData, args=(year, month, numSongs)).start()
            
            
    
"""
    METHOD:
        This method is called in the yearlySongData method, and collects songs and their data.
        Every call of this method will create a new CSV file and, using writeSongCharacteristics, will
        append their data to the created CSV file.
        CSV files are only written once all data for the month is gathered
        
    PARAMETERS:
        year: The current year in which the method is taking data (determined in getAllSongData)
        month: The current month in which the method is taking data (determined in yearlySongData)
        numSongs: The number of songs to be collected
"""
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
                
            #Accounts for bug where lyrics sometimes include extraneuos information
            for key in songs:
                if (len(songs[key][2]) < 10000):
                    dataWriter.writerow(songs[key])



getAllSongData(5, 2019, 5, 2019, 5)



