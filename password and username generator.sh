#!/bin/bash
#creting random passwords(only alphanumerical characters) of specified character lenght and usernames for the number of users you specify, and writing it down to a file you specify

echo "what will be the base name of the users, by deffault it is guest"
read base_name
echo "how many characters should the password have"
read password_lenght
echo "how many users do you want to create"
read number_of_users
echo "enter the name of the file"
read file_name

for i in $(seq 1 $number_of_users)
do
	echo `strings /dev/urandom | grep -o '[[:alnum:]]' |head -n $password_lenght |tr -d "\n"`",$base_name$i">> `echo $file_name`
done

#for i in {1..2}; do echo `strings /dev/urandom | grep -o '[[:alnum:]]' |head -n 10 |tr -d "\n"` >> `echo $file_name`; done > out.dat
