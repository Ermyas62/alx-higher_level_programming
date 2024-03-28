#!/usr/bin/bash
# send JSON data
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
