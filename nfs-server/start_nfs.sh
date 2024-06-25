#!/bin/sh
rpcbind 2>&1 | tee /var/log/rpcbind.log
rpc.statd 2>&1 | tee /var/log/rpc.statd.log
exportfs -rv 2>&1 | tee /var/log/exportfs.log
rpc.nfsd 2>&1 | tee /var/log/rpc.nfsd.log
rpc.mountd --foreground 2>&1 | tee /var/log/rpc.mountd.log
