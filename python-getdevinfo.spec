Name:           python3-getdevinfo
Version:        1.0.8
Release:        1%{?dist}
Summary:        A python library that can be used to gather all sorts of information about the storage devices connected to a system
Group:          Applications/System
License:        GPLv3+
URL:            http://www.hamishmb.com/
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3, python3-devel
Requires:       python3, lshw, python3-beautifulsoup4, python3-lxml, coreutils >= 8.21, lvm2, binutils, util-linux

%description
A python library that can be used to gather all sorts of information about the storage devices connected to a system.

%prep
%autosetup -c python3-getdevinfo

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{python3_sitelib}
cp -rv getdevinfo getdevinfo-1.0.8.dist-info %{buildroot}/%{python3_sitelib}
chmod -R a+rx %{buildroot}/%{python3_sitelib}/getdevinfo

%files
/%{python3_sitelib}/getdevinfo
/%{python3_sitelib}/getdevinfo-1.0.8.dist-info

%changelog
* Thu Oct 18 2018 Hamish McIntyre-Bhatty hamishmb@live.co.uk 1.2
- Remove preun section.
* Mon Sep 10 2018 Hamish McIntyre-Bhatty hamishmb@live.co.uk 1.1
- Update to use python3_sitelib macro.
- Add preun section.
* Fri Jan 12 2018 Hamish McIntyre-Bhatty hamishmb@live.co.uk 1.0
- Created initial package.
s
