#! /bin/bash

httpd
sleep 1
tor &
sleep 5
echo ============= TOR HOSTNAME ================
cat /var/lib/tor/hidden_service/hostname
echo ===========================================

tail -f /var/log/httpd/access_log
