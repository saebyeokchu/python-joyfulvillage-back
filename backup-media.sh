#!/bin/bash

# Define variables
SOURCE_DIR="/var/lib/docker/volumes/ec2-user_django-media/_data"
BACKUP_DIR="/home/ec2-user/backups"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
ZIP_FILE="$BACKUP_DIR/data_backup_$TIMESTAMP.zip"

# Ensure backup directory exists
mkdir -p $BACKUP_DIR

# Zip the files with root permissions
sudo zip -r $ZIP_FILE $SOURCE_DIR

# Remove old backups (optional: keep only last 7 backups)
ls -t $BACKUP_DIR/*.zip | tail -n +8 | xargs rm -f

echo "Backup completed: $ZIP_FILE"
