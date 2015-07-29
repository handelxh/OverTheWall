#!/bin/sh
# git pull
#cp ./360kb/hosts  c:/windows/system32/drivers/etc
if [[ $(uname) == 'Darwin' ]]
then
	echo 'macbook'
	cp ./360kb/hosts /etc/hosts
fi
if [ $(uname) == 'Linux' ]
then
	cp ./360kb/hosts /etc/hosts
	echo 'ubuntu is ok'
fi
if [[ $(uname) == 'MINGW32_NT-6.1' ]] 
then
	cp ./360kb/hosts  c:/windows/system32/drivers/etc
	echo 'windows is ok'

fi
