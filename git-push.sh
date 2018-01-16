#!/bin/sh

git add .

git checkout

git commit -m "$1"

git push origin master
