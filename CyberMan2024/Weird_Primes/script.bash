#!/bin/bash

private_key="priv.pem"
output_dir="decrypted_flags"
mkdir -p "$output_dir"

for i in {0..299}; do
    input_file="flag/decryptMe_${i}.txt"
    output_file="${output_dir}/decrypted_${i}.txt"
    
    #echo "Decrypting $input_file"
    openssl pkeyutl -decrypt -keyform PEM -inkey "$private_key" -in "$input_file"
    
    # if [ $? -eq 0 ]; then
    #     echo "Decryption successful for $input_file"
    # else
    #     echo "Error decrypting $input_file"
    # fi
done
