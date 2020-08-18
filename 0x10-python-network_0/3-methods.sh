#!/bin/bash
# display methods available in a server
curl -sI -X OPTIONS $1 | grep Allow: | awk '{print $2, $3, $4}'
