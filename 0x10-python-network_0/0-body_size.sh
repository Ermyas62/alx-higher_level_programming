#!/bin/bash
# the body sizee
curl -sI $1 | grep "Content-Length:" | cut -d' ' -f2
