# Define the file name
file_name = "LolaTheDoG_words.txt"

# Open the file in write mode
with open(file_name, "w") as file:
    # Loop through all numbers from 0000 to 9999
    for i in range(10000):
        # Format the number to be 4 digits with leading zeros
        number = f"{i:04}"
        # Create the word
        word = f"LolaTheDoG{number}"
        # Write the word to the file followed by a newline
        file.write(word + "\n")

