#!/bin/bash

name=$(cat ../docker-compose.yml  | grep container_name | cut -d ":" -f "2" )

echo ""
echo "Stopping containers"
docker stop $name 

echo ""
echo "Removing containers"
docker rm $name 

echo ""
echo "-------------------"

echo ""
echo "containers:"
docker ps -a
echo ""

echo ""
echo "images:"
docker images
