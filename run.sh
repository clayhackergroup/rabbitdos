#!/bin/bash

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
RESET='\033[0m'

# Banner
clear
echo -e "${CYAN}=========================================="
echo -e "${YELLOW}        RRRRR    AAAAA  BBBBB   III  TTTTT"
echo -e "        R    R  A     A B    B   I     T"
echo -e "        RRRRR   AAAAAAA BBBBB    I     T"
echo -e "        R   R   A     A B    B   I     T"
echo -e "        R    R  A     A BBBBB   III    T"
echo -e "${GREEN}     Rabbit DDoS Tool by Clay Group"
echo -e "${CYAN}   Follow me on Instagram: @h4cker.in"
echo -e "${RESET}=========================================="

# Tool Information
echo -e "${GREEN}[*] Tool Name:${RESET} Rabbit DDoS Tool"
echo -e "${GREEN}[*] Creator:${RESET} Clay Group"
echo -e "${GREEN}[*] Instagram:${RESET} @h4cker.in"
echo -e "${GREEN}[*] Purpose:${RESET} Stress testing your own server to check its resilience under high traffic."

# How the Tool Works
echo -e "\n${CYAN}How This Tool Works:${RESET}"
echo -e "${YELLOW}1.${RESET} This tool sends multiple requests to the specified server URL."
echo -e "${YELLOW}2.${RESET} You can specify the number of threads (simultaneous requests)."
echo -e "${YELLOW}3.${RESET} The tool will simulate high traffic to test your server's response.\n"

# Running the Python Script
echo -e "${GREEN}[+] Starting the tool...${RESET}"
python3 run.py

# End Message
echo -e "${GREEN}[+] Tool execution completed.${RESET}"
