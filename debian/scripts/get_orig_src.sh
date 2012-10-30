#!/bin/bash

# The script creates a tar.xz tarball from git-repository of LAMMPS-project
# ./get_orig_src.sh commitID   -   creates a tarball of specified commit
# ./get_orig_src.sh   - creates a tarball of the latest version
# Packages, that needs to be installed to use the script:
# atool, bzr

bzr checkout lp:minieigen
cd minieigen

BZR_REV=$(bzr revno)
VER_DEB=0.3~bzr$BZR_REV
FOLDER_NAME=minieigen-$VER_DEB
TARBALL_NAME=minieigen_$VER_DEB.orig.tar.xz


echo $VER_DEB
echo $FOLDER_NAME
echo $TARBALL_NAME

cd ..
mv minieigen $FOLDER_NAME
rm -rf $FOLDER_NAME/.bzr
apack $TARBALL_NAME $FOLDER_NAME
rm -rf $FOLDER_NAME
