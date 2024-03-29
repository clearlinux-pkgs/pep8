#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pep8
Version  : 1.7.0
Release  : 65
URL      : https://files.pythonhosted.org/packages/3e/b5/1f717b85fbf5d43d81e3c603a7a2f64c9f1dabc69a1e7745bd394cc06404/pep8-1.7.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/3e/b5/1f717b85fbf5d43d81e3c603a7a2f64c9f1dabc69a1e7745bd394cc06404/pep8-1.7.0.tar.gz
Summary  : Python style guide checker
Group    : Development/Tools
License  : MIT
Requires: pep8-bin = %{version}-%{release}
Requires: pep8-python = %{version}-%{release}
Requires: pep8-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=================================
        
        pep8 is a tool to check your Python code against some of the style
        conventions in `PEP 8`_.

%package bin
Summary: bin components for the pep8 package.
Group: Binaries

%description bin
bin components for the pep8 package.


%package python
Summary: python components for the pep8 package.
Group: Default
Requires: pep8-python3 = %{version}-%{release}

%description python
python components for the pep8 package.


%package python3
Summary: python3 components for the pep8 package.
Group: Default
Requires: python3-core
Provides: pypi(pep8)

%description python3
python3 components for the pep8 package.


%prep
%setup -q -n pep8-1.7.0
cd %{_builddir}/pep8-1.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603398283
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pep8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
