#!/bin/bash

git clone -b develop https://github.com/overclock11/conectate-front.git frontend/conectate-front
cd frontend/conectate-front 
(npm i && ./node_modules/@angular/cli/bin/ng build --output-path ../public)
