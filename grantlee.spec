#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD264C7B1D02D6509 (steveire@gmail.com)
#
Name     : grantlee
Version  : 5.1.0
Release  : 2
URL      : http://downloads.grantlee.org/grantlee-5.1.0.tar.gz
Source0  : http://downloads.grantlee.org/grantlee-5.1.0.tar.gz
Source99 : http://downloads.grantlee.org/grantlee-5.1.0.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: grantlee-lib
Requires: grantlee-license
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : doxygen
BuildRequires : qtbase-dev qtbase-extras mesa-dev
BuildRequires : qtscript-dev
BuildRequires : qttools-dev

%description
The Grantlee Libraries
======================
[![OSX/Linux Build Status](https://travis-ci.org/steveire/grantlee.svg?branch=master)](https://travis-ci.org/steveire/grantlee)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/github/steveire/grantlee?branch=master&svg=true)](https://ci.appveyor.com/project/steveire/grantlee/branch/master)

%package dev
Summary: dev components for the grantlee package.
Group: Development
Requires: grantlee-lib
Provides: grantlee-devel

%description dev
dev components for the grantlee package.


%package lib
Summary: lib components for the grantlee package.
Group: Libraries
Requires: grantlee-license

%description lib
lib components for the grantlee package.


%package license
Summary: license components for the grantlee package.
Group: Default

%description license
license components for the grantlee package.


%prep
%setup -q -n grantlee-5.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1535220249
mkdir clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
pushd clr-build ; make test ||: ; popd

%install
export SOURCE_DATE_EPOCH=1535220249
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/grantlee
cp COPYING.LIB %{buildroot}/usr/share/doc/grantlee/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/grantlee/abstractlocalizer.h
/usr/include/grantlee/abstractmarkupbuilder.h
/usr/include/grantlee/bbcodebuilder.h
/usr/include/grantlee/cachingloaderdecorator.h
/usr/include/grantlee/context.h
/usr/include/grantlee/engine.h
/usr/include/grantlee/exception.h
/usr/include/grantlee/filter.h
/usr/include/grantlee/filterexpression.h
/usr/include/grantlee/grantlee_templates_export.h
/usr/include/grantlee/grantlee_textdocument_export.h
/usr/include/grantlee/grantlee_version.h
/usr/include/grantlee/markupdirector.h
/usr/include/grantlee/mediawikimarkupbuilder.h
/usr/include/grantlee/metatype.h
/usr/include/grantlee/node.h
/usr/include/grantlee/outputstream.h
/usr/include/grantlee/parser.h
/usr/include/grantlee/plaintextmarkupbuilder.h
/usr/include/grantlee/qtlocalizer.h
/usr/include/grantlee/rendercontext.h
/usr/include/grantlee/safestring.h
/usr/include/grantlee/taglibraryinterface.h
/usr/include/grantlee/template.h
/usr/include/grantlee/templateloader.h
/usr/include/grantlee/texthtmlbuilder.h
/usr/include/grantlee/token.h
/usr/include/grantlee/typeaccessor.h
/usr/include/grantlee/util.h
/usr/include/grantlee/variable.h
/usr/lib64/cmake/Grantlee5/Grantlee5Config.cmake
/usr/lib64/cmake/Grantlee5/Grantlee5ConfigVersion.cmake
/usr/lib64/cmake/Grantlee5/GrantleeMacros.cmake
/usr/lib64/cmake/Grantlee5/GrantleeTargets-relwithdebinfo.cmake
/usr/lib64/cmake/Grantlee5/GrantleeTargets.cmake
/usr/lib64/libGrantlee_Templates.so
/usr/lib64/libGrantlee_TextDocument.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/grantlee/5.1/grantlee_defaultfilters.so
/usr/lib64/grantlee/5.1/grantlee_defaulttags.so
/usr/lib64/grantlee/5.1/grantlee_i18ntags.so
/usr/lib64/grantlee/5.1/grantlee_loadertags.so
/usr/lib64/libGrantlee_Templates.so.5
/usr/lib64/libGrantlee_Templates.so.5.1.0
/usr/lib64/libGrantlee_TextDocument.so.5
/usr/lib64/libGrantlee_TextDocument.so.5.1.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/grantlee/COPYING.LIB
