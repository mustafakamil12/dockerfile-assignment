#!/bin/bash

# Start the kadmin.local command
kinit root/admin <<EOF
$KADMIN_PASSWORD
EOF