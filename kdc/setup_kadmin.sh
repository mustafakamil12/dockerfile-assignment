#!/bin/bash

# Start the kadmin.local command
kadmin.local <<EOF
addprinc root/admin
$KADMIN_PASSWORD
$KADMIN_PASSWORD
EOF
