#
#!/bin/bash

cd /var/lib/odoo15/
mv filestore $1/
mkdir filestore && mv $1 filestore/
chown -R odoo15.odoo15 .
echo "$(ls)"
exit
