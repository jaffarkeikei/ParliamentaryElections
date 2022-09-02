# Parliamentary Elections


## Problem Specifications

This project consists of a pair of classes that read and analyse election data. They are intended to process data from Canada, but also to work for other parliamentary democracies.


## Terminology

Parliamentary democracy is a democratic form of government in which citizens elect people to represent them, and the prime minister is determined based on the number of representatives elected by the various political parties.
The legislature or parliament of a country, state, or province is the group of elected representatives. They have the authority to make decisions and pass laws.
Each representative is called a member of parliament. They are said to have a seat in parliament.
The territory is divided into electoral districts or ridings. Each is a geographical area that elects one member of parliament.
A riding is identified by its name, such as Brampton Centre.
Between elections, new ridings may be added and/or old ones deleted.
(In addition, the border associated with a riding can change, but since our program only knows a riding’s name, and not the geographic area with which it is associated, such changes have no relevance to this assignment.)
A jurisdiction is a country, state, or province.
An election occurs on one specific date.
A polling station is a location where citizens vote. Each polling station reports its results, which are combined and tabulated to determine who won a seat in each riding.
Canada’s electoral system is referred to as a “first-past-the-post” system. This means that in each riding, the candidate with the highest number of votes wins the seat for that riding.
The party with the most seats over all ridings wins the election.


## Election data files

_The code is designed to be able to load election data from any data files that follows these rules_:

The file is in csv format, which means that each line represents a row of a table, and the table cells on that line are separated by commas.
Each row has the same number of table cells (and hence the same number of commas).
An empty cell is represented by two commas with nothing between them, not even a blank. (A blank is not nothing! It is a very short string.)
The file begins with a header line that contains column names rather than data.
The data that your program needs is in these columns (counting from column 0):
column 1: the name of a riding
column 13: the name of a party
column 17: a number of votes earned by that party in that riding.
Additional votes for that party in that riding could be recorded elsewhere in the same file or in another file.
Each file could contain results from more than one polling station, and each polling station could have results split across multiple files. The program can be used to read data from a series of files.


## The program

_The code consists of two classes_:
Election and Jurisdiction.

An instance of class Election records data about a single election.
An instance of class Jurisdiction records data about any number of past elections in a particular jurisdiction. It does so by containing within itself any number of instances of Election.
You will notice that party names are not defined by constants. This is because there is no fixed number of parties or party names. The program discovers party names as it reads data file(s).

Also, there are methods that have a parameter whose type is TextIO.
