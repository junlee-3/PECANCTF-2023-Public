#!/bin/bash

service postgresql start
# createdb isn't much of a risk, and preventing it means a lot of permission changes
runuser -u postgres -- createuser odoo --createdb

# can't drop db owner to prevent malicious deletion without readding table owner on at least one table
# too much work to figure out which tables
useradd odoo --create-home
# no-database-list and list_db don't seem to work, so we set a password instead
runuser -u odoo -- /odoo/odoo-bin --database odoo --no-database-list --config odoo.conf
