#!/usr/bin/env python3
#
# This is a complex version of lilac.py for building
# a package from AUR.
#
# You can do something before/after building a package,
# including modify the 'pkgver' and 'md5sum' in PKBUILD.
#
# This is especially useful when a AUR package is
# out-of-date and you want to build a new one, or you
# want to build a package directly from sourceforge but
# using PKGBUILD from AUR.
#
# See also:
# [1] ruby-sass/lilac.py
# [2] aufs3-util-lily-git/lilac.py
# [3] octave-general/lilac.py
#

from lilaclib import *

build_prefix = 'extra-x86_64'
# depends = []

def pre_build():
  # obtain base PKGBUILD, e.g.
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    # edit PKGBUILD
    if 'java-runtime' in line:
        print(line.replace('java-runtime','java-environment'))
    elif 'gradle jar' in line:
        print('\tmkdir gradle-cache')
        print('\texport GRADLE_USER_HOME="${srcdir}/${pkgname}/gradle-cache"')
        print(line)
    elif 'changelog=.CHANGELOG' in line:
        print('#'+line)
    else:
        print(line)

def post_build():
  git_add_files('PKGBUILD')
  git_add_files('opsu.sh')
  git_commit()

# do some cleanup here after building the package, regardless of result
# def post_build_always(success):
#   pass

if __name__ == '__main__':
  single_main()
