#!/bin/bash
# Run this script to store gmail account data encoded.

echo "Username:"
read username
echo "Password:"
read -s password

echo $username | base64 -o ./src/radixProject/account_data
echo $password | base64 >> ./src/radixProject/account_data
