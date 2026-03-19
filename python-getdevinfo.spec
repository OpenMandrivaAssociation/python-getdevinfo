%define module getdevinfo

Name:		python-getdevinfo
Version:	2.0.1
Release:	1
Summary:	A device information gatherer for Linux
Group:		Applications/System
License:	GPL-3.0-or-later
URL:		https://www.hamishmb.com/
Source0:	https://www.hamishmb.com/files/downloads/%{module}/%{version}/Python/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	lshw
BuildRequires:	lvm2
BuildRequires:	util-linux
Requires: lshw
Requires: python%{pyver}dist(beautifulsoup4)
Requires: python%{pyver}dist(lxml)
Requires: coreutils
Requires: lvm2 
Requires: binutils
Requires: util-linux

%description
A device information gatherer for Linux.

Working on Linux, this script makes use of lshw, lvdisplay and blkid to
get a comprehensive amount of disk information.

This information is available in a structured dictionary for ease of use.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%files
%doc README.md
%license LICENSE
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}*.*-info
