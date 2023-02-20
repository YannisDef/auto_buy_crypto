#!/bin/bash

test=0
nb_test=0

##CUSTOM
#_END    =   '\x1b[0m'
#_BOLD	=	'\x1b[1m'
#_UNDER	=	'\x1b[4m'
#_REV	=	'\x1b[7m'

#_GREY	=	'\x1b[30m'
#_RED	=	'\x1b[31m'
#_GREEN 	= 	'\x1b[32m'
#_YELLOW	=	'\x1b[33m'
#_BLUE	=	'\x1b[34m'
#_PURPLE	=	'\x1b[35m'
#_CYAN	=	'\x1b[36m'
#_WHITE	=	'\x1b[37m'

function compare_two_output() {
    touch tmp
    touch value

    ./trade $1 ; echo $? > tmp

    echo $2 > value

    if cmp -s tmp value
    then
        echo -e "\x1b[1m\x1b[37m$1 -> \x1b[1m\x1b[1m\x1b[32mOK\x1b[0m"
        let "test += 1"
    else
        echo -e "\x1b[1m\x1b[37m$1 -> \x1b[1m\x1b[1m\x1b[31mKO\x1b[0m"
        diff tmp value
    fi
    let "nb_test += 1"
    echo -e
}

#?   BASIC TESTS
#         POUR RAJOUTER UN TEST
#   {appelle la fonction} {"nom du test"} {"return value expected"}
#    compare_two_output    "BASIC LS"               0


compare_two_output "too many args" 84
compare_two_output "-h"   0

#tableau pour les outputs
#boucle car tous les meme prenoms
#!##############################################################################


#?   GET PERCENTAGE
let "test = test * 100 / nb_test"
echo -e
echo -e "\x1b[1m\x1b[37m\x1b[4mRESULT:\x1b[0m"
percentage=0
perfect=100

while [ $percentage != $perfect ]
do
    if [ $percentage -ge $test ]
    then
        printf "\x1b[1m\x1b[31m|\x1b[0m"
    else
        printf "\x1b[1m\x1b[32m|\x1b[0m"
    fi
    let "percentage += 1"
done

if [ $test -eq $perfect ]
then
    echo -e "\x1b[1m\x1b[32m $test% on $nb_test tests\x1b[0m"
else
    echo -e "\x1b[1m\x1b[31m $test% on $nb_test tests\x1b[0m"
fi
#!##############################################################################

#?   CLEAN
rm tmp
rm value
#!##############################################################################

echo -e