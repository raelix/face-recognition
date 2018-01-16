#!/bin/sh

test -z $1 && echo "Commit description required." 1>&2 && exit 1

git add ../

git checkout

git commit -m "$1"

git push origin master
