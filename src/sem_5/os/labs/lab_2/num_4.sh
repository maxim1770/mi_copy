#!/bin/bash

# Пункт 1 +
echo First part

ps -u maxim -o pid=,ppid,time,stime,sz


# Пункт 2 +
echo Second part

# yes > /dev/null &

# jobs

# или CTRL+Z, если процесс не в bg
# kill –SIGTSTP %1

# jobs

# чтобы возобновить выполнение процесса в bg
# bg

# или возобновить выполнение процесса в fg
# fg

# Просмотр процессов
# jobs

# Подробнее тут: https://stackoverflow.com/questions/9900970/bash-send-sigtstp-signal-ctrlz


# Пункт 3 +
echo Third part

# ps -u root -o pid,cmd
