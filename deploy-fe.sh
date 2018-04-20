#!/bin/bash

git clone -b develop https://github.com/overclock11/conectate-front.git frontend/conectate-front
cd frontend/conectate-front 
(npm i && ng build --output-path ../public)
