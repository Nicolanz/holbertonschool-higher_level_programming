#!/bin/bash
# display methods available in a server
curl -sI -X OPTIONS $1 | grep Allow | sed 's/Allow: //'
