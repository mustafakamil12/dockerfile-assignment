#!/bin/bash

# Start SSSD service
service sssd start

# Start your application
python /app/app.py

# Clean up - remove from Active Directory domain
realm leave test5.com

# Exit
exit 0
