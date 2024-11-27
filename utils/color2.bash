#!/bin/bash

# Define the colors
DYEL='\033[38;5;154m'  # HTML Yellow (#DFFF00)
LIME='\033[38;5;118m'  # Lime color  (#7FFF00)
RESET='\033[0m'        # Reset to default

# Display the colors
echo -e "${DYEL}This is DYEL (ANSI 154) - Dynamic Yellow #DFFF00${RESET}"
echo -e "${LIME}This is LIME (ANSI 118) - Lime Green #7FFF00${RESET}"

# Side-by-side comparison
echo -e "Side-by-side comparison:"
echo -e "${DYEL}DYEL${RESET} | ${LIME}LIME${RESET}"

