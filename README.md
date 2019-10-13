# N-grams frequencies calculator

A program, enables you to calculate n-grams frequencies for a specified text. 
Computation results are presented in a separate JSON-file for every n.

By default it works with cyrillic symbols, but it's possible to define custom alphabet. 

## Requirements
Python 3.5 or higher version.

Text must be encoded with UTF-8.

## How to use
Launch this command from a terminal (command line):
```bash
# alternatively try python frequency.py -h
python3 frequency.py -h 
```
You will get an output with an options description.

Example of the script usage:
```bash
python3 frequency.py war_and_peace.txt -vp -n 16 -o war_and_peace
```
It will analise war_and_peace.txt file and will calculate n-grams frequencies for all n from 1 to 16. 
Results will be written to the war_and_peace directory, -v enables verbalisation, -p enables pretty printing.

## Goals
The program was written for educational purposes as part of the cryptography course.
