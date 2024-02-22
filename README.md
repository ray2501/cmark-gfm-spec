# cmark-gfm-spec

openSUSE Tumbleweed cmark-gfm RPM spec

[cmark-gfm](https://github.com/github/cmark) is an extended version of the
C reference implementation of CommonMark, a rationalized version of Markdown
syntax with a spec. This repository adds GitHub Flavored Markdown extensions to
[the upstream implementation](https://github.com/jgm/cmark),
as defined in the [spec](https://github.github.com/gfm/).

A not good thing is newer version cmark-gfm public API depends on `config.h`,
I try to fix it but maybe it is not a good solution.

