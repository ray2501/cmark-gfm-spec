%define libname libcmark-gfm0_29_13
Name:           cmark-gfm
Version:        0.29.0
Release:        1
Summary:        CommonMark parsing and rendering library and program in C
License:        BSD-2-Clause AND MIT AND CC-BY-SA-4.0
Group:          Productivity/Text/Utilities
Url:            https://github.com/github/cmark
Source:         %{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.0.2
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRoot:     %{buildroot}

%description
`cmark-gfm` is an extended version of the C reference implementation of
CommonMark, a rationalized version of Markdown syntax with a spec. 

It provides a shared library (`libcmark-gfm`) with functions for parsing
CommonMark documents to an abstract syntax tree (AST), manipulating
the AST, and rendering the document to HTML, groff man, LaTeX,
CommonMark, or an XML representation of the AST.  It also provides a
command-line program (`cmark-gfm`) for parsing and rendering CommonMark
documents.

%package -n %{libname}
Summary:        CmmonMark parsing and rendering library
Group:          System/Libraries

%description -n %{libname}
It provides a shared library (`libcmark-gfm`) with functions for parsing
CommonMark documents to an abstract syntax tree (AST), manipulating
the AST, and rendering the document to HTML, groff man, LaTeX,
CommonMark, or an XML representation of the AST.  It also provides a
command-line program (`cmark-gfm`) for parsing and rendering CommonMark
documents.

%package devel
Summary:        Development files for cmark-gfm library
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}-%{release}

%description devel
This package provides the development files for cmark-gfm.

%prep
%setup -q

%build
%cmake -DCMARK_TESTS=OFF -DCMARK_STATIC=OFF
%make_jobs

%install
%cmake_install DESTDIR=%{buildroot}
cp build/src/config.h %{buildroot}%{_includedir}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%doc COPYING
%doc README.md
%{_bindir}/cmark-gfm
%{_mandir}/man1/cmark-gfm.1%{?ext_man}

%files -n %{libname}
%{_libdir}/libcmark-gfm.so.%{version}.gfm.13
%{_libdir}/libcmark-gfm-extensions.so.%{version}.gfm.13

%files devel
%{_includedir}/cmark-gfm.h
%{_includedir}/cmark-gfm_export.h
%{_includedir}/cmark-gfm_version.h
%{_includedir}/cmark-gfm-extension_api.h
%{_includedir}/cmark-gfm-core-extensions.h
%{_includedir}/config.h
%{_libdir}/libcmark-gfm.so
%{_libdir}/libcmark-gfm-extensions.so
%{_libdir}/pkgconfig/libcmark-gfm.pc
%{_mandir}/man3/cmark-gfm.3%{?ext_man}
%{_libdir}/cmake/cmark-gfm.cmake
%{_libdir}/cmake/cmark-gfm-*.cmake
%{_libdir}/cmake-gfm-extensions

%changelog

