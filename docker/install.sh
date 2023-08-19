#!/bin/bash
# ---------------------------------------------------------

# Color ANIS
RED='\033[1;31m';
BLUE='\033[1;34m';
GREEN='\033[1;32m';
YELLOW='\033[1;33m';
CYAN='\033[1;36m';
NC='\033[0m';

# ---------------------------------------------------------

echo -e "${YELLOW}"
echo "$(date +"%T") Install requirements.txt ... " 
echo -e "${NC}"
pip3 install -r docker/requirements.txt