# MixSync
This application can be used to accurately find and sort songs by key and BPM, curated with meticulous verification, and filter them by various attributes for a seamless music-matching experience.

## Changes
- 06.18.24 Initial planning stage, created a prototype using a small database containing anime songs only. Threshold is fixed to ±15 BPM and ±2 keys from the input specified by the user.
- 06.19.24 Added an option to choose whether to look through the database of anime songs or Western songs.
- 06.20.24 Separated the user-defined functions in a separate file. Added a new sorting method that takes the songs with the closest key and BPM to the ones specified by the user at the top.

## Introduction
Have you ever found yourself wondering how you can efficiently determine which song would complement another without making them sound too different from their original versions? One common approach that mashup artists use is to analyze the key and BPM (beats per minute) of the songs. As a mashup artist myself, I prefer to mix songs that share the same key and BPM, or at least are close in these attributes. By "close," I specifically mean that the songs should be no more than 2 keys apart and no more than 15 BPMs apart, although a difference of 5 BPMs is preferable.

However, finding songs that meet these criteria can be quite challenging. You might need to sift through your entire music database—if you even have one—scrolling through numerous irrelevant tracks before stumbling upon a suitable match. If you're not fortunate, you may have to rely on available song key and BPM finders, which often provide inaccurate information. This means you must first verify whether these tools have correctly identified the key and BPM, adding more time and effort to the process. 

The key and BPM (beats per minute) of a song are fundamental elements of its musical composition and structure. The key refers to the tonal center or the pitch around which the song revolves melodically and harmonically. They are typically identified by letters such as C, D, E, etc., followed by major (e.g., C major) or minor (e.g., A minor) to denote the mood and tonality. On the other hand, BPM denotes the tempo or speed at which the song is played, measured in beats per minute. It defines how fast or slow the rhythm of the song progresses, influencing its energy level and feel. Together, the key and BPM of a song provide essential information for musicians, DJs, producers, and listeners alike. They help in understanding the mood, style, and compatibility of songs for mixing, mashups, or creating cohesive playlists. Analyzing and knowing these elements enables greater creativity and precision in music production and performance, ensuring that musical pieces harmonize seamlessly or contrast effectively when desired.

With this application, mashup artists will easily and efficiently find songs that would fit with a certain song by providing accurate information on the keys and BPMs of various songs. The application is designed to efficiently match songs in terms of their key and BPM, solving common issues with existing tools that often provide inaccurate data. It includes a robust system to handle songs with multiple keys or BPMs, ensuring that users can find the best matches even when dealing with complex tracks. The application features a comprehensive database meticulously curated through personal analysis and verification by knowledgeable contributors, minimizing inaccuracies. Users can sort songs by title, key, BPM, artist, origin, type, and year, and filter results by specific song types like Anime or K-Pop. Additionally, the application implements a threshold feature that allows users to search for songs based on the key and BPM threshold that the user will specify as well as the selected song’s BPM and key, respectively. This ensures that mashup artists can maintain a harmonious and cohesive sound in their mixes. The application's functionalities are tailored to enhance the efficiency of music mixing by providing reliable and detailed musical information.

## Objectives of the Study
The application aims to accomplish the following:
-	To create an application that provides accurate information on the keys and BPMs of various songs.
-	To efficiently find songs that would match a certain song in terms of their key and BPM.
-	To implement a robust system to handle songs with multiple keys or BPMs
-	To devise a method for handling BPMs within the specified threshold effectively
-	To verify and validate key and BPM data accuracy to mitigate inaccuracies

## Statement of the Problem
The study attempts to know the efficiency of MixSync as an application to enhance music mixing. Specifically, it seeks to answer the following questions: 
1. How is it different from any other song & key bpm finders available?
2. What specific issues does the application aim to solve regarding key and BPM management?
3. How do you plan to handle songs with multiple keys or BPMs?
Causes data redundancy: Multiple records for songs to differentiate k/b changes.
4. How are you going to handle the BPMs if you have a threshold of 70 BPM to 139 BPM?
Formula: range((SONG_BPM/2) ± 15)
5. What are the possible issues that you see ahead and how do you plan to solve them? 

## Scope and Delimitations
The scope of the application includes the development of a robust database that accurately stores key and BPM (beats per minute) information for a wide range of songs. Unlike existing tools prone to inaccuracies, this database will be meticulously curated through personal analysis and verification by knowledgeable contributors. The application will feature a comprehensive sorting method allowing users to organize songs by title, key, BPM, artist, origin, type, and year, with options for both ascending and descending order. Users will have the flexibility to filter results by specific song types, such as Anime or K-Pop, using checkboxes. Additionally, the application will implement a threshold feature enabling users to search for songs within ±15 BPM of a selected song’s BPM and ±2 keys of its key.
Despite its functionalities, the application has certain limitations. It does not facilitate the actual creation of mashups; rather, it focuses on providing accurate data to assist in the process. Furthermore, it does not claim ownership of the songs stored within its database, which are sourced from publicly available information and contributed by users. Therefore, any legal or copyright issues pertaining to the songs themselves are not the responsibility of the application. These delimitations ensure a clear focus on data accuracy and usability while maintaining ethical and legal standards in music information management. 

## Functionalities
1. Database with Accurate Key and BPM
- Some song key & bpm finders available on the Internet (e.g. TuneBat, SongBPM) provides inaccurate information more specifically with keys. As someone who personally analyzed the songs with the help of other people, 
2. Sorting Method
- Title, Key, BPM, Artist, Origin, Type, Year
- Order: Ascending, Descending
- Checkbox: You have an option to select whether to show a specific/multiple type/s of song only (e.g. Anime, K-Pop, etc.).
3. Threshold
- 
 
## Definition of Terms
-	TITLE. The name of the song.
-	KEY. Refers to the tonal center or the pitch around which the song revolves melodically and harmonically. C, C#, D, D#, E, F, F#, G, G#, A, A#, B.
-	BPM. The number of beats per minute of the song – having the lowest at 70, and the highest being 139.
-	PART. Specifies the part of the song that is being described of the key and BPM such as Intro, Verse, Pre-chorus, Chorus, Post-chorus, Bridge. This will -be used for handling key and BPM changes.
-	ARTIST. The name of the artist.
-	ORIGIN. Specifies if the particular song is being used as a soundtrack for a series, movie, or drama. It includes categories such as Anime Title, Movie Title, Drama Title, and Series Title.
-	TYPE. Specifies the type of song. Anime, J-Pop, K-Pop, Western, OPM.
-	YEAR. Specifies what year the song was released. This will be used by mashup artists who are planning to make year-end mashups.
