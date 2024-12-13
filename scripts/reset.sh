#!/bin/bash

DB_ROOT_PASSWORD="root"
DB_NAME="OpenB3"
SQL_SCRIPT="sql/reset.sql"

mysql -u $DB_ROOT_PASSWORD -p $DB_NAME < $SQL_SCRIPT
