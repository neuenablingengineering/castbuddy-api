#!/bin/bash

curl -i -X POST -H "Content-Type: application/json" \
     --data-binary "{\"deviceid\": 155675, \"tags\": [\"p\"], \"data\": \"[{\\\"t\\\": \\\"20180705043000\\\", \\\"v\\\": [1,2,3,4,5,6,7,8,9,10,11,12,23,14,15,16]}, {\\\"t\\\": \\\"20180705050000\\\", \\\"v\\\": [1,2,3,4,5,6,7,8,9,10,11,12,23,14,15,16]}]\"}" \
     'https://dashboard.hologram.io/api/1/csr/rdm?apikey='
