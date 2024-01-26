#!/bin/bash
aws s3 cp ../src/static/assets/workouts.json s3://wallcity/static/assets/workouts.json --profile tischtennis
aws s3 cp ../src/workouts.html s3://wallcity/workouts.html --profile tischtennis
cd ..
sls cloudfrontInvalidate
