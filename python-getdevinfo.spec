Name:           python-getdevinfo
Version:        1.1.0
Release:        2
Summary:        A python library that can be used to gather all sorts of information about the storage devices connected to a system
Group:          Applications/System
License:        GPLv3+
URL:            https://www.hamishmb.com/
Source0:        https://www.hamishmb.com/files/Downloads/getdevinfo/1.0.8/Python/getdevinfo-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)
BuildRequires:  lshw
BuildRequires:  lvm2

Requires: python
Requires: lshw
Requires: python3dist(beautifulsoup4)
Requires: python3dist(lxml)	
Requires: coreutils
Requires: lvm2 
Requires: binutils
Requires: util-linux

%description
A python library that can be used to gather all sorts of information about the storage devices connected to a system.

%prep
%setup -qn getdevinfo-%{version}

%build
%py_build

%install
%py_install

#rm -rf $RPM_BUILD_ROOT
#mkdir -p %{buildroot}/%{python_sitelib}
#cp -rv getdevinfo getdevinfo-1.0.8.dist-info %{buildroot}/%{python_sitelib}
#chmod -R a+rx %{buildroot}/%{python_sitelib}/getdevinfo

%files
%{python_sitelib}/getdevinfo
%{python_sitelib}/getdevinfo-%{version}-py*.egg*
#%{python_sitelib}/getdevinfo-1.0.8.dist-info
