Problem specifications
In this warmup assignment, you will complete a pair of classes that read and analyse election data. They are intended to process data from Canada, but also to work for other parliamentary democracies.

Terminology
Before we begin, let’s define some terminology you’ll be working with.

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

Election data files
The code is designed to be able to load election data from any data files that follows these rules:

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

You do not need to “clean” (i.e., fix flaws in) the data when reading it from a file. The only thing you should do with each string you find delimited by commas in a csv file is remove the one pair of double-quotes that surround the string. All the cells in the csv files have double-quotes and we don’t consider them to be part of the data. (If you open in Excel you don’t see them.)

Sample data
We are providing some sample data that comes from Elections Canada (Links to an external site.). It follows the format defined above, but is larger than any fake dataset you are likely to create for testing purposes, so it will give your code a workout. Your program must handle any data file in the format we defined, including these.

Note that each of these sample data files contains polling station results from only one riding. But as noted above, your program must not assume this will always be the case.

The program
The code consists of two classes: Election and Jurisdiction.

An instance of class Election records data about a single election.
An instance of class Jurisdiction records data about any number of past elections in a particular jurisdiction. It does so by containing within itself any number of instances of Election.
You will notice that party names are not defined by constants. This is because there is no fixed number of parties or party names. The program discovers party names as it reads data file(s).

You will see methods that have a parameter whose type is TextIO. For example:

def read_results(self, input_stream: TextIO) -> None:
TextIO is just a type for what you get when you open a file. For example, if client code does f = open('blah'), then f could be passed to the parameter input_stream, and inside the method we could do all the things you are used to doing with files, like for line in instream input_stream.

