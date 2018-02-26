#!/bin/bash

curl -d "@testmsg.json" -H "Content-Type: application/json" -X POST http://cbapi-dev.us-east-1.elasticbeanstalk.com/api/holohook
