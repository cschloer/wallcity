Wall City Static Website

To sync s3 files:
```
# Deploy files to s3
sls client deploy
# Invalidate the cloudfront cache
sls cloudfrontInvalidate
```

To sync s3 files locally:
```
# Run minio on port 9000

# If bucket not created
AWS_ACCESS_KEY_ID=minioadmin AWS_SECRET_ACCESS_KEY=minioadmin aws s3api create-bucket --bucket wallcity --region us-east-1 --endpoint http://localhost:9000
AWS_ACCESS_KEY_ID=minioadmin AWS_SECRET_ACCESS_KEY=minioadmin aws s3api put-bucket-policy --bucket wallcity --policy file://policy.json --endpoint http://localhost:9000
# with policy.json:
##############
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowPublicRead",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::wallcity/*"
            ]
        }
    ]
}
###############

# Sync files
AWS_ACCESS_KEY_ID=minioadmin AWS_SECRET_ACCESS_KEY=minioadmin aws s3 cp ./src s3://wallcity/ --recursive --endpoint http://localhost:9000


```
