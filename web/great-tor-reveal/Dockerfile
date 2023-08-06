FROM archlinux:latest

RUN pacman --noconfirm -Sy apache tor

COPY httpd.conf /etc/httpd/conf/httpd.conf
COPY index.html /srv/http/index.html

COPY torrc /etc/tor/torrc

COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD ["/run.sh"]
EXPOSE 1111
