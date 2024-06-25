#!/bin/bash

# Start the subscription register command
subscription-manager register --username=mustafakamil --password=Pit5cxcy

# Check if registration was successful
if [ $? -eq 0 ]; then
    echo "Registration successful. Attaching subscription..."
    # Attach the subscription
    subscription-manager attach
    # Check if attachment was successful
    if [ $? -eq 0 ]; then
        echo "Subscription attached successfully."
    else
        echo "Error: Failed to attach subscription."
        exit 1
    fi
else
    echo "Error: Failed to register subscription."
    exit 1
fi
