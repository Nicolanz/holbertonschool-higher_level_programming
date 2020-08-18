#!/bin/bash
# Print in bytes the size of a URL
curl -sI $1 | grep Content-Length: | awk '{print $2}';
