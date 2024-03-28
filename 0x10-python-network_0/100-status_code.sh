#!/bin/bash
# Status of code
curl -so /dev/null -w '%{http_code}' $1
