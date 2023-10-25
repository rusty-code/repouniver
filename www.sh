#!/bin/bash

start_game()
{
    echo "УГАДАЙ ЧИСЛО ОТ 1 ДО 100"
    echo "Система загадала число. Отгадай его за 5 попыток"

    # Generate a rundom number
    rnd_num=$RANDOM

    # Bringing a number to range from 1 to 100
    rnd_num=$(( $rnd_num % 100 ))

    echo "(Для проверки прораммы) Загаданное число $rnd_num" # Debug output

    for it in 1 2 3 4 5
    do
        echo -n "Что это за число???: "
        # User input
        read user_input

        if [[ $user_input == $rnd_num ]]
        then
            echo "Победа!!!"
            exit
        else
            echo "Неверно... Осталось попыток $(( 5-$it ))"
        fi
    done
    echo "Поражение"
}

# Start script
start_game