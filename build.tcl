#!/usr/bin/tclsh

set arch "x86_64"
set base "cmark-gfm-0.29.0"
set fileurl "https://github.com/github/cmark/archive/0.29.0.gfm.13.tar.gz"

set var [list wget2 $fileurl -O $base.tar.gz]
exec >@stdout 2>@stderr {*}$var

set var2 [list tar xzvf $base.tar.gz]
exec >@stdout 2>@stderr {*}$var2

file rename cmark-gfm-0.29.0.gfm.13 $base

set var2 [list tar czvf ${base}.tar.gz $base]
exec >@stdout 2>@stderr {*}$var2

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb cmark-gfm.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete -force $base
file delete $base.tar.gz
