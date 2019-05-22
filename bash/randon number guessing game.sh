#!/bin/bash
# number guessing game
number=`shuf -i 1-99 -n1` #random number generator from 1 to 99
trenutni_broj_pokusaja=1 # number of tries
maksimalni_broj_pokusaja=5 #max number of guesses
echo "pokusajte da pogodite koji smo mi broj izabrali od 1 do 99"
sleep 1
echo imate 5 pokusaja $number
echo "unesite svoj broj"
guessing(){
	while [ $trenutni_broj_pokusaja -le $maksimalni_broj_pokusaja ]
	do

		while [ 1 -eq 1 ] #check user input, if the user enters a number break out of this loop
		do
			read guess
			if ! [[ "$guess" =~ ^[0-9]+$ ]] #is input equal to regular expression(only numerical characters)
				then
					echo "ne smete uneti ni jedan drugi karakter sem arabskih cifri, probajte ponovo"

			else
				break
			fi
		done

		if [ $guess -eq $number ] # check is the quess corect
		then
			echo "uneli ste tacan broj,cestitamo"
			break
		elif [ $guess -gt $number ] #greater than
		then
			echo "vas broj je veci od trazenog"
		else                         # less than
			echo "vas broj je manji od trazenog"
		fi
		trenutni_broj_pokusaja=` expr $trenutni_broj_pokusaja + 1 `
	done
}

guessing  #calling the function

echo "kraj igre"

