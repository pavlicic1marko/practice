#!/bin/bash
# number guessing game
number=`shuf -i 1-99 -n1` #random number generator from 1 to 99
trenutni_broj_pokusaja=1 #
maksimalni_broj_pokusaja=5 #max number of guesses
echo tru to guess the number. pick a number from 1 to 99
"sleep 1"
echo imate 5 pokusaja $number
func(){
	echo "enter your number"
}
func
guessing(){
	while [ $trenutni_broj_pokusaja -le $maksimalni_broj_pokusaja ]
	do
		read guess
		if [ $guess -eq $number ]
		then
			echo "tacan broj"
			break
		elif [ $guess -gt $number ]
		then
			echo "vas broj je veci od trazenog"
		else
			echo "vas broj je manji od trazenog"
		fi
		trenutni_broj_pokusaja=` expr $trenutni_broj_pokusaja + 1 `
	done
}
guessing #pozivanje funkcije
echo "kraj igre"

