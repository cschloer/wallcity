#!/bin/bash
AWS_ACCESS_KEY_ID=minioadmin AWS_SECRET_ACCESS_KEY=minioadmin aws s3 cp ./src s3://wallcity/ --recursive --endpoint http://localhost:9000
echo "http://localhost:9000/wallcity/index.html"
