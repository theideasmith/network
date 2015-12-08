
CC=gcc
analysis: analysis.cpp
	$(CC) analysis.cpp -I/usr/local/include/igraph -L/usr/local/lib -ligraph -lgsl -o analysis

data.csv: analysis
	./analysis > data.csv

data.png: data.csv
	python plot.py
