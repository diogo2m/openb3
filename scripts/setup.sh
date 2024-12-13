#!/bin/bash

DB_ROOT_PASSWORD="root"
DB_NAME="OpenB3"
SQL_SCRIPT="sql/setup.sql"

if ! command -v mariadb &> /dev/null
then
    echo "MariaDB not found. Installing MariaDB..."
    sudo apt update
    sudo apt install -y mariadb-server
else
    echo "MariaDB is already installed."
fi

echo "Starting MariaDB service..."
sudo systemctl start mariadb
sudo systemctl enable mariadb

echo "Securing MariaDB installation..."
sudo mysql_secure_installation <<EOF

Y
$DB_ROOT_PASSWORD
$DB_ROOT_PASSWORD
Y
Y
Y
Y
EOF

echo "Creating database: $DB_NAME"
mysql -u root -p"$DB_ROOT_PASSWORD" -e "CREATE DATABASE IF NOT EXISTS $DB_NAME;"

echo "Running SQL script: $SQL_SCRIPT"
mysql -u root -p"$DB_ROOT_PASSWORD" $DB_NAME < $SQL_SCRIPT

echo "MariaDB configuration and SQL script execution completed!"
