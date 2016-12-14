#!/bin/sh

# Global variable
DATABASE="analysis/upfamdb.db"
# Create folder
mkdir -p data/pfam28.0
mkdir -p analysis

PFAM28_URL=ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam28.0/Pfam-A.clans.tsv.gz
PFAM28_TARGET="data/pfam28.0/Pfam-A.clans.tsv.gz"
wget ${PFAM28_URL} -O ${PFAM28_TARGET}

# Create sqlite database
cat ./script/pfam.sql | sqlite3 ${DATABASE}
gunzip -c ${PFAM28_TARGET} | sqlite3 -separator $'\t'  ${DATABASE} '.import /dev/stdin pfam'

# TODO: Clean up
