#!/bin/bash

ZIP_FILE="LOLA.zip"
WORDLIST="LolaTheDoG_words.txt"

# Check if the ZIP file exists
if [ ! -f "$ZIP_FILE" ]; then
    echo "Error: $ZIP_FILE not found."
    exit 1
fi

# Check if the wordlist file exists
if [ ! -f "$WORDLIST" ]; then
    echo "Error: $WORDLIST not found."
    exit 1
fi

# Loop through each line in the wordlist file
while IFS= read -r password || [ -n "$password" ]; do
    echo "Trying password: $password"
    # Use 7z to extract with the specified password
    7z x -p"$password" "$ZIP_FILE" -y
    # Check the exit status of 7z
    if [ $? -eq 0 ]; then
        echo "Success! Password found: $password"
        exit 0
    fi
done < "$WORDLIST"


# If we exit the loop, no password was found
echo "Failed to extract $ZIP_FILE with any password from $WORDLIST."
exit 1

