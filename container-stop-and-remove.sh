#!/bin/sh

echo ""
echo "Stopping containers"
docker stop recognizer recognizer_db

echo ""
echo "Removing containers"
docker rm recognizer recognizer_db

echo ""
echo "-------------------"

echo ""
echo "containers:"
docker ps -a
echo ""

echo ""
echo "images:"
docker images
