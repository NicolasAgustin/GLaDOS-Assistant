#!/bin/bash

curl -L --retry 30 --get --fail --data-urlencode "text=${1}" -o $2 "https://glados.c-net.org/generate"


