#! /usr/bin/bash

set -eux

# package blnf using 7z.

rm -rf blnf/
rm -f blnf.zip
rm -r blnf.md5
mkdir -p blnf/
cp -r blnf-output/ blnf

find blnf/blnf-output -type f -exec touch -t 200407140001.09 {} +

md5deep -r blnf/blnf-output > blnf/manifest.md5
sha256deep -r blnf/blnf-output > blnf/manifest.sha256

cat blnf/manifest.md5 | wc -l
cat blnf/manifest.sha256 | wc -l

cp RELEASE.md blnf

7z a blnf.zip blnf/

md5sum blnf.zip > blnf.md5
cat blnf.md5
sha256sum blnf.zip > blnf.sha256
cat blnf.sha256
