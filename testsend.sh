#!/bin/bash

curl -d "@testmsg.json" -H "Content-Type: application/json" -X POST http://localhost:5000/api/holohook
