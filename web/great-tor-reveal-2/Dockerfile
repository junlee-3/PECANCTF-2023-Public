FROM archlinux:latest

RUN pacman --noconfirm -Sy apache tor

COPY httpd.conf /etc/httpd/conf/httpd.conf
COPY index.html /srv/http/index.html

COPY torrc /etc/tor/torrc

COPY run.sh /run.sh
COPY req.sh /req.sh

CMD ["/run.sh"]
EXPOSE 1111
