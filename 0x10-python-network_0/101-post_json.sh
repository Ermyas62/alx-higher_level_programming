#!/usr/bin/bash
# send JSON data
curl -s -d "@$2" -X POST -H 'Content-Type: application/json' $1
