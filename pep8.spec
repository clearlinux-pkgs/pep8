#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pep8
Version  : 1.5.7
Release  : 17
URL      : https://pypi.python.org/packages/source/p/pep8/pep8-1.5.7.tar.gz
Source0  : https://pypi.python.org/packages/source/p/pep8/pep8-1.5.7.tar.gz
Summary  : Python style guide checker
Group    : Development/Tools
License  : MIT
Requires: pep8-bin
Requires: pep8-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
pep8 - Python style guide checker
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

%description python
python components for the pep8 package.


%prep
%setup -q -n pep8-1.5.7

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python2 setup.py test
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pep8

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
