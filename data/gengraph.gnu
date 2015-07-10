#!/usr/bin/gnuplot

set terminal pngcairo
set output 'citations.png'

unset key
set title "Citation counts of MLOSS JMLR papers"
set xrange [-1:50]
set logscale y
set style data histogram
set style histogram cluster gap 1
set style fill solid border -1
set boxwidth 0.9
plot './mloss-citations.dat.sort' using 3
