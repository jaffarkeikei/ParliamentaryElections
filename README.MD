# Parliamentary Elections

Welcome to the repository for **Parliamentary Elections** - a project centered around processing and analyzing election data from parliamentary systems.

## Table of Contents

- [Problem Specifications](#problem-specifications)
- [Terminology](#terminology)
- [Election Data Files](#election-data-files)
- [The Program](#the-program)

## Problem Specifications

This repository contains a pair of classes designed to read and analyze election data. The primary aim is to process data from Canada's parliamentary system, while maintaining flexibility to accommodate similar systems in other countries.

## Terminology

To provide context for the project, here are some key terms:

- **Parliamentary Democracy**: A form of government where citizens elect representatives, influencing the prime minister's selection based on representatives' numbers.

- **Legislature/Parliament**: The elected representatives responsible for decision-making and passing laws.

- **Member of Parliament**: Elected representative holding a parliamentary seat.

- **Electoral District/Riding**: A geographically defined area electing one member of parliament.

- **Jurisdiction**: Refers to a country, state, or province.

- **Election**: The process of citizens voting for representatives on a specific date.

- **Polling Station**: Voting location where citizens cast their votes; results contribute to determining riding winners.

- **First-Past-The-Post System**: Winning candidate in a riding is the one with the highest votes.

## Election Data Files

The code is designed to load election data from CSV files following these criteria:

- CSV Format: Each line represents a table row, cells separated by commas.
- Consistent Columns: All rows possess the same number of cells (and commas).
- Empty Cell: Indicated by two consecutive commas.
- Header Line: The file begins with column names (not data).
- Relevant Columns: Data extraction focuses on these columns (0-indexed):
  - Column 1: Riding name
  - Column 13: Party name
  - Column 17: Votes earned by a party in a riding
  - Additional votes might be distributed across files.

## The Program

This repository contains two essential classes: `Election` and `Jurisdiction`.

- `Election`: Records data about individual elections.
- `Jurisdiction`: Manages data for multiple past elections within a specific jurisdiction. It aggregates instances of `Election`.

One notable feature is the dynamic discovery of party names, allowing the program to adapt to the available data without predefined constants.

Certain methods are tailored to handle file input/output through a parameter of type `TextIO`.

If you have any questions or feedback, please don't hesitate to get in touch!

Thank you for exploring the Parliamentary Elections repository!

