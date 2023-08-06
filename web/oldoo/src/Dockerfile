FROM python:2

RUN apt-get update && apt-get install -y \
  libldap2-dev \
  libpq-dev \
  libsasl2-dev \
  postgresql \
  postgresql-client \
  node-less \
&& apt-get clean && rm -rf /var/lib/apt/lists/*

RUN git config --global core.compression 0 \
&& git clone --filter=tree:0 --no-checkout https://github.com/odoo/odoo

WORKDIR /odoo
RUN git checkout 16714a7e71da91382bb111fad32282a65205dffd \
&& sed -ie 's/psycopg2==2.6.2/psycopg2==2.7.5/g' requirements.txt \
&& pip install --no-cache-dir -r requirements.txt

COPY ./user_flag/ /odoo
COPY ./bonus_flag/ /var/lib/bonus

COPY odoo.conf entrypoint.sh ./
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "/odoo/entrypoint.sh" ]

EXPOSE 8069
